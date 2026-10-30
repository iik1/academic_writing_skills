#!/usr/bin/env python3
"""
Article Candidate List Builder

For each journal, draws a fixed list of recent research articles from OpenAlex for the
Phase 2 spot-check and saves it to reports/<slug>_articles.json. The journal must have a
confirmed entry in tools/openalex_sources.json (build_openalex_sources.py).

Pool:      OpenAlex works of type "article" from the journal's source, for each year from
           three full years ago to the current year: up to SAMPLE_PER_YEAR per year, drawn
           with OpenAlex's sample + seed (seed derived from slug and year), so the same
           journal and window always ask for the same sample. If that gives fewer than
           N_CANDIDATES usable articles (review journals such as Annual Reviews), works of
           type "review" are added the same way.
Filtering: front matter OpenAlex sometimes types as articles ("Issue Information",
           "Editorial Board", errata, ...) and works without DOI or landing page are dropped.
Ranking:   open access with a full-text link, then other open access, then the rest. Within
           each group picks rotate across years (newest first), then across issues; ties
           within an issue are ordered by a hash of slug and DOI. No randomness: the same
           OpenAlex responses always give the same list.

An existing list is kept unless --refresh is given, so a journal's sample stays fixed.

Requires OPENALEX_MAILTO and/or OPENALEX_API_KEY in the environment.

Usage:
  python build_article_lists.py --slug strategic-management-journal
  python build_article_lists.py --field STRAT
  python build_article_lists.py                    # every journal in the registry
  python build_article_lists.py --field STRAT --refresh
  python build_article_lists.py --refresh --slug annual-review-sociology review-of-finance
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import date, datetime, timezone

import openalex_client
from build_openalex_sources import load_map, short_id
from dispatch_journal_agents import REPO_ROOT, JOURNALS
from openalex_client import OpenAlexStop, budget


# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────

REPORTS_DIR     = REPO_ROOT / "reports"
N_CANDIDATES    = 25       # articles per journal list
FULL_YEARS      = 3        # full years before the current one
SAMPLE_PER_YEAR = 200      # OpenAlex's maximum page size
SELECT = ("id,doi,title,type,publication_year,publication_date,biblio,"
          "open_access,best_oa_location,primary_location")

# Front matter OpenAlex sometimes types as "article". Whole-title phrases (optionally with
# volume/issue info) and prefixes only front matter uses, so that real titles such as
# "Editorial independence and CEO pay" or "Correction for measurement error" are kept.
FRONT_MATTER_TITLE = re.compile(
    r"^\W*(issue information|editorial board|editorial|masthead|front matter|back matter|"
    r"table of contents|contents|cover|cover image|index|author index|subject index|"
    r"book reviews?|call for papers|in this issue|reviewers?|list of reviewers|"
    r"introduction|preface|foreword|announcements?|in memoriam|obituary)"
    r"(\W+(vol(ume)?|issue|no|number|[0-9]).*|\W*)$", re.I)
FRONT_MATTER_PREFIX = re.compile(
    r"^\W*(erratum|errata|corrigendum|correction to\b|correction:|retraction\b|retracted:|"
    r"expression of concern|editorial:|editors?'?s?'? (note|notes|introduction|comments?|"
    r"page|report|letter)\b|from the editors?\b|book review:|introduction to\b|"
    r"special issue\b|announcements?:|announcement ?editors|preface:|foreword:|"
    r"(thanks|acknowledg\w*) (to|of) (our |the )?reviewers|reviewers (of|for) (volume|\d))",
    re.I)


def is_front_matter(title):
    title = title.replace("’", "'").replace("‘", "'")    # curly apostrophes
    return bool(FRONT_MATTER_TITLE.match(title) or FRONT_MATTER_PREFIX.match(title))


def articles_path(slug):
    return REPORTS_DIR / f"{slug}_articles.json"


def window(today=None):
    year = (today or date.today()).year
    return year - FULL_YEARS, year


def seed_for(slug, year):
    return int(hashlib.sha1(f"{slug}:{year}".encode()).hexdigest(), 16) % 10**9


# ─────────────────────────────────────────────
# SELECTION (pure: no network)
# ─────────────────────────────────────────────

def candidate(work):
    """Flatten one OpenAlex work into a candidate entry, or None if it is not usable."""
    if work.get("type") not in (None, "article", "review"):
        return None
    title = (work.get("title") or "").strip()
    if not title or is_front_matter(title):
        return None
    doi = (work.get("doi") or "").replace("https://doi.org/", "") or None
    oa = work.get("open_access") or {}
    best = work.get("best_oa_location") or {}
    primary = work.get("primary_location") or {}
    landing = (best.get("landing_page_url") or primary.get("landing_page_url")
               or (f"https://doi.org/{doi}" if doi else None))
    if not (doi or landing):
        return None
    biblio = work.get("biblio") or {}
    return {
        "doi":          doi,
        "openalex_id":  short_id(work["id"]) if work.get("id") else None,
        "title":        title,
        "year":         work.get("publication_year"),
        "volume":       biblio.get("volume"),
        "issue":        biblio.get("issue"),
        "is_oa":        bool(oa.get("is_oa")),
        "oa_status":    oa.get("oa_status"),
        "fulltext_url": best.get("pdf_url") if oa.get("is_oa") else None,
        "landing_url":  landing,
    }


def interleave(lists):
    """Round-robin over lists: first of each, then second of each, ..."""
    out, i = [], 0
    while any(i < len(l) for l in lists):
        out += [l[i] for l in lists if i < len(l)]
        i += 1
    return out


def spread(cands, slug):
    """Order candidates to rotate across years (newest first), then across issues."""
    by_year = {}
    for c in cands:
        issue_key = (str(c["volume"] or ""), str(c["issue"] or "")) \
            if (c["volume"] or c["issue"]) else ("", "online-first")
        by_year.setdefault(c["year"] or 0, {}).setdefault(issue_key, []).append(c)
    tie = lambda c: hashlib.sha1(f"{slug}:{c['doi'] or c['landing_url']}".encode()).hexdigest()
    years = []
    for year in sorted(by_year, reverse=True):
        issues = [sorted(arts, key=tie) for _, arts in sorted(by_year[year].items())]
        years.append(interleave(issues))
    return interleave(years)


def select(works, slug, n=N_CANDIDATES):
    """Pick n candidates from OpenAlex works. Pure and deterministic."""
    seen, cands = set(), []
    for work in works:
        c = candidate(work)
        key = c and (c["doi"] or c["landing_url"])
        if c and key not in seen:
            seen.add(key)
            cands.append(c)
    groups = [[c for c in cands if c["is_oa"] and c["fulltext_url"]],
              [c for c in cands if c["is_oa"] and not c["fulltext_url"]],
              [c for c in cands if not c["is_oa"]]]
    picked = [c for g in groups for c in spread(g, slug)][:n]
    pool = {"usable": len(cands), "open_access": sum(c["is_oa"] for c in cands),
            "with_fulltext_link": len(groups[0])}
    return [{"rank": i + 1, **c} for i, c in enumerate(picked)], pool


# ─────────────────────────────────────────────
# FETCH AND SAVE
# ─────────────────────────────────────────────

def works_filter(source_id, year, work_type="article"):
    return f"primary_location.source.id:{source_id},publication_year:{year},type:{work_type}"


def fetch_works(slug, source_id, years, fetch, work_type="article"):
    """One sampled request per year. fetch(path, params) returns the results list."""
    works = []
    for year in years:
        works += fetch("works", {"filter": works_filter(source_id, year, work_type),
                                 "sample": SAMPLE_PER_YEAR, "seed": seed_for(slug, year),
                                 "per_page": SAMPLE_PER_YEAR, "select": SELECT})
    return works


def build_list(slug, journal, entry, fetch, today=None, n=N_CANDIDATES):
    """Return the list document for one journal, or (None, reason) if there is none."""
    if not entry or not entry.get("source_id"):
        return None, "no OpenAlex match in openalex_sources.json"
    if not entry.get("confirmed"):
        return None, "OpenAlex match not confirmed in openalex_sources.json"
    first, last = window(today)
    years = list(range(first, last + 1))
    works = fetch_works(slug, entry["source_id"], years, fetch)
    candidates, pool = select(works, slug, n)
    work_types = ["article"]
    if len(candidates) < n:     # review journals (e.g. Annual Reviews): add review articles
        works += fetch_works(slug, entry["source_id"], years, fetch, "review")
        candidates, pool = select(works, slug, n)
        work_types.append("review")
    if not candidates:
        return None, f"no research articles in OpenAlex for {first}-{last}"
    return {
        "slug":         slug,
        "journal":      journal,
        "source_id":    entry["source_id"],
        "display_name": entry.get("display_name"),
        "generated":    datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "window":       {"from_year": first, "to_year": last},
        "query": {
            "endpoint":        "https://api.openalex.org/works",
            "filters":         [works_filter(entry["source_id"], "<year>", t) for t in work_types],
            "sample_per_year": SAMPLE_PER_YEAR,
            "seeds":           {str(y): seed_for(slug, y) for y in years},
        },
        "pool":         {"works_returned": len(works), **pool},
        "candidates":   candidates,
    }, None


def main():
    parser = argparse.ArgumentParser(description="Build article candidate lists from OpenAlex.")
    parser.add_argument("--field",   type=str, default=None)
    parser.add_argument("--slug",    type=str, nargs="+", default=None)
    parser.add_argument("--n",       type=int, default=N_CANDIDATES)
    parser.add_argument("--refresh", action="store_true", help="rebuild existing lists")
    args = parser.parse_args()

    journals = [j for j in JOURNALS
                if (not args.field or j[3] == args.field) and (not args.slug or j[4] in args.slug)]
    if not journals:
        sys.exit("No journals matched.")
    openalex_client.require_credentials()
    sources = load_map()
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    built = kept = skipped = 0
    stopped = None
    try:
        for name, url, rating, field, slug in journals:
            path = articles_path(slug)
            if path.exists() and not args.refresh:
                kept += 1
                continue
            doc, reason = build_list(slug, name, sources.get(slug), openalex_client.get, n=args.n)
            if doc is None:
                skipped += 1
                print(f"  {slug:<48} NO LIST: {reason}")
                continue
            path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            built += 1
            p = doc["pool"]
            print(f"  {slug:<48} {len(doc['candidates']):>2} candidates "
                  f"({sum(c['fulltext_url'] is not None for c in doc['candidates'])} with full-text link; "
                  f"pool {p['usable']}, {p['open_access']} OA)")
    except OpenAlexStop as exc:
        stopped = exc

    print(f"\n{built} built, {kept} kept (already saved), {skipped} without a list")
    if budget["remaining_usd"] is not None:
        print(f"OpenAlex budget remaining today: ${budget['remaining_usd']:.4f}")
    if stopped:
        sys.exit(f"\nSTOPPED: {stopped}\nRun the same command again to continue; "
                 f"saved lists are kept.")


if __name__ == "__main__":
    main()
