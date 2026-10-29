#!/usr/bin/env python3
"""
OpenAlex Source Map Builder

Matches every journal in JOURNALS (dispatch_journal_agents.py) to its OpenAlex source and
stores the result in tools/openalex_sources.json, keyed by slug:

  "strategic-management-journal": {
    "journal":      "Strategic Management Journal",     # registry name
    "source_id":    "S102949365",                        # null if unmatched
    "display_name": "Strategic Management Journal",     # OpenAlex name
    "issn_l":       "0143-2095",
    "method":       "issn" | "name" | "manual",
    "confirmed":    true,
    "note":         "...",                               # why it needs review, if it does
    "candidates":   [...]                                # alternatives, for review
  }

Matching:
  1. ISSN. ISSNs are taken from the registry URL, the journal's skill file, and (optionally)
     an ISSN CSV. A single ISSN match is confirmed automatically, unless OpenAlex's name for
     the source clearly differs from the registry name (skill-file ISSNs were written by
     agents and can be wrong). ISSNs that point to different sources are left unmatched.
  2. Name. Otherwise the registry name is searched among OpenAlex journals. An exact match
     (ignoring case, punctuation, "&"/"and" and a leading "The") is stored unconfirmed;
     anything else is left unmatched with the top candidates listed.

Reviewing: to accept matches, run --confirm with their slugs (or set "confirmed": true by
hand). To fix or fill in a match, set "source_id" (and "display_name"), "method": "manual"
and "confirmed": true.

Re-running skips journals already in the map, so a run stopped by OpenAlex's daily budget
continues where it left off. --refresh re-resolves the unconfirmed ones (e.g. after adding
--issn-csv); manual and confirmed entries are never changed.

Requires OPENALEX_MAILTO and/or OPENALEX_API_KEY in the environment (see
dispatch_journal_agents.py). Without a key, OpenAlex's daily budget is small.

Usage:
  python build_openalex_sources.py
  python build_openalex_sources.py --field STRAT
  python build_openalex_sources.py --slug strategic-management-journal
  python build_openalex_sources.py --issn-csv tools/abs_ajg_2024_full_list.csv --refresh
  python build_openalex_sources.py --confirm mis-quarterly nature
"""

import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from dispatch_journal_agents import (
    TOOLS_DIR, REPO_ROOT, FIELD_FOLDERS, JOURNALS, OPENALEX_MAILTO, OPENALEX_API_KEY,
)


# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────

SOURCES_MAP   = TOOLS_DIR / "openalex_sources.json"
API_URL       = "https://api.openalex.org/sources"
SELECT        = "id,display_name,issn_l,issn,type,homepage_url,host_organization_name,works_count"
REQUEST_PAUSE = 0.2        # seconds between requests
MAX_ATTEMPTS  = 5          # per request, on burst 429s / 5xx / network errors
TIMEOUT       = 30         # seconds per request
N_CANDIDATES  = 3          # alternatives stored for review

ISSN_RE = re.compile(r"\b(\d{4})-?(\d{3}[\dXx])\b")


# ─────────────────────────────────────────────
# NORMALISATION
# ─────────────────────────────────────────────

def valid_issn(issn):
    """ISSN check digit (mod 11), so stray 8-digit numbers in URLs are not queried."""
    digits = issn.replace("-", "").upper()
    total = sum(int(d) * w for d, w in zip(digits[:7], range(8, 1, -1)))
    check = (11 - total % 11) % 11
    return digits[7] == ("X" if check == 10 else str(check))


def norm_issn(text):
    """First valid ISSN in text, as NNNN-NNNC."""
    for a, b in ISSN_RE.findall(text):
        issn = f"{a}-{b.upper()}"
        if valid_issn(issn):
            return issn
    return None


def norm_name(name):
    """HTML entities decoded (OpenAlex has "&amp"), lower-case, "&" -> "and", no punctuation
    or leading "the", single spaces."""
    name = html.unescape(name).lower().replace("&", " and ")
    name = re.sub(r"[^a-z0-9 ]+", " ", name)
    name = re.sub(r"^\s*the\s+", "", name)
    return " ".join(name.split())


def names_agree(a, b):
    """Equal, or one name contained in the other as whole words ("Journal of Finance" does
    not agree with "Journal of Financial Economics")."""
    a, b = f" {norm_name(a)} ", f" {norm_name(b)} "
    return a in b or b in a


# ─────────────────────────────────────────────
# ISSN SOURCES
# ─────────────────────────────────────────────

def skill_path(field, slug):
    folder = FIELD_FOLDERS.get(field, field.lower().replace("&", "and").replace(" ", "-"))
    return REPO_ROOT / "skills" / folder / f"{slug}_SKILL.md"


def issns_from_skill(path):
    """ISSNs on any line of the skill that mentions ISSN."""
    if not path.exists():
        return []
    found = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if "issn" in line.lower():
            found += [i for i in (f"{a}-{b.upper()}" for a, b in ISSN_RE.findall(line))
                      if valid_issn(i)]
    return found


def load_issn_csv(path):
    """
    Return {normalised journal name: [ISSNs]} from a CSV with a title column (header
    containing "title", "journal" or "name") and one or more columns whose header contains
    "issn".
    """
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        issn_cols  = [h for h in headers if "issn" in h.lower()]
        title_cols = [h for word in ("title", "journal", "name") for h in headers
                      if h not in issn_cols and word in h.lower()]
        if not issn_cols or not title_cols:
            sys.exit(f"ERROR: {path}: need a title column and an ISSN column; "
                     f"headers are {headers}")
        print(f"  [ISSN CSV] title column '{title_cols[0]}', ISSN columns {issn_cols}")
        table = {}
        for row in reader:
            issns = [i for i in (norm_issn(row[c] or "") for c in issn_cols) if i]
            if issns:
                table.setdefault(norm_name(row[title_cols[0]] or ""), []).extend(issns)
    return table


def collect_issns(name, url, field, slug, csv_table):
    issns = []
    if norm_issn(url):
        issns.append(norm_issn(url))
    issns += issns_from_skill(skill_path(field, slug))
    issns += csv_table.get(norm_name(name), [])
    return list(dict.fromkeys(issns))      # dedupe, keep order


# ─────────────────────────────────────────────
# OPENALEX
# ─────────────────────────────────────────────

class OpenAlexStop(Exception):
    """OpenAlex cannot be used for now: daily budget spent, request refused, or unreachable."""


budget = {"remaining_usd": None}    # last X-RateLimit-Remaining-USD seen


def note_budget(headers):
    try:
        budget["remaining_usd"] = float(headers.get("X-RateLimit-Remaining-USD"))
    except (TypeError, ValueError):
        pass


def budget_spent(exc):
    """A 429 caused by the daily budget rather than a burst; retrying won't help today."""
    if budget["remaining_usd"] is not None and budget["remaining_usd"] <= 0:
        return True
    try:
        body = exc.read().decode("utf-8", errors="replace").lower()
    except Exception:
        body = ""
    return any(word in body for word in ("budget", "daily", "credit", "usd"))


def openalex_get(params):
    """
    GET /sources with params; returns the results list. Retries bursts (honouring
    Retry-After), 5xx and network errors. Raises OpenAlexStop when the daily budget is
    spent, a request is refused, or retries run out.
    """
    params = {**params, "select": SELECT}
    if OPENALEX_MAILTO:
        params["mailto"] = OPENALEX_MAILTO
    if OPENALEX_API_KEY:
        params["api_key"] = OPENALEX_API_KEY
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    agent = f"academic_writing_skills (mailto:{OPENALEX_MAILTO})" if OPENALEX_MAILTO \
        else "academic_writing_skills"

    for attempt in range(1, MAX_ATTEMPTS + 1):
        time.sleep(REQUEST_PAUSE)
        wait = 2 ** attempt
        try:
            req = urllib.request.Request(url, headers={"User-Agent": agent})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                note_budget(resp.headers)
                return json.load(resp)["results"]
        except urllib.error.HTTPError as exc:
            note_budget(exc.headers)
            if exc.code == 429 and budget_spent(exc):
                raise OpenAlexStop("OpenAlex's daily budget is used up (HTTP 429). Set "
                                   "OPENALEX_API_KEY for a larger budget, or wait for the reset.")
            if exc.code != 429 and exc.code < 500:
                raise OpenAlexStop(f"OpenAlex refused the request (HTTP {exc.code}); "
                                   f"check OPENALEX_MAILTO / OPENALEX_API_KEY.")
            error = exc
            if (exc.headers.get("Retry-After") or "").isdigit():
                wait = min(int(exc.headers["Retry-After"]), 60)
        except (urllib.error.URLError, TimeoutError) as exc:
            error = exc
        print(f"    OpenAlex: {error}; retrying in {wait}s ({attempt}/{MAX_ATTEMPTS})")
        time.sleep(wait)
    raise OpenAlexStop(f"OpenAlex still failing after {MAX_ATTEMPTS} attempts ({error}). "
                       f"Repeated 429s usually mean the daily budget is used up.")


def short_id(openalex_id):
    return openalex_id.rsplit("/", 1)[-1]


def describe(source):
    return {
        "source_id":    short_id(source["id"]),
        "display_name": source.get("display_name"),
        "issn_l":       source.get("issn_l"),
        "publisher":    source.get("host_organization_name"),
        "homepage_url": source.get("homepage_url"),
        "works_count":  source.get("works_count"),
    }


# ─────────────────────────────────────────────
# MATCHING
# ─────────────────────────────────────────────

def match_journal(name, issns, fetch):
    """
    Decide one journal's entry. fetch(params) returns OpenAlex /sources results, so this is
    testable without the network.
    """
    entry = {"journal": name, "source_id": None, "display_name": None, "issn_l": None,
             "method": None, "confirmed": False, "issns_tried": issns}

    by_id = {}
    if issns:                       # one request for all ISSNs ("|" is OpenAlex's OR)
        for source in fetch({"filter": "issn:" + "|".join(issns)}):
            by_id.setdefault(short_id(source["id"]), source)

    if len(by_id) == 1:
        source = next(iter(by_id.values()))
        entry.update({k: v for k, v in describe(source).items()
                      if k in ("source_id", "display_name", "issn_l")})
        entry["method"] = "issn"
        entry["confirmed"] = names_agree(name, source.get("display_name") or "")
        if not entry["confirmed"]:
            entry["note"] = "ISSN match, but OpenAlex's name differs from the registry name"
        return entry
    if len(by_id) > 1:
        entry["note"] = "ISSNs point to different OpenAlex sources"
        entry["candidates"] = [describe(s) for s in by_id.values()]
        return entry

    results = fetch({"search": name, "filter": "type:journal", "per_page": 10})
    exact = [s for s in results if norm_name(s.get("display_name") or "") == norm_name(name)]
    if len(exact) == 1:
        entry.update({k: v for k, v in describe(exact[0]).items()
                      if k in ("source_id", "display_name", "issn_l")})
        entry["method"] = "name"
        entry["note"] = "name match: confirm by hand"
        entry["candidates"] = [describe(s) for s in results
                               if s is not exact[0]][:N_CANDIDATES]
        return entry

    entry["note"] = ("several OpenAlex journals share this name" if exact
                     else "no ISSN and no exact name match")
    entry["candidates"] = [describe(s) for s in (exact or results)][:N_CANDIDATES]
    return entry


def keep_existing(entry):
    return bool(entry) and (entry.get("method") == "manual" or entry.get("confirmed") is True)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def load_map(path=None):
    path = path or SOURCES_MAP
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def save_map(sources, path=None):
    path = path or SOURCES_MAP
    path.write_text(json.dumps(dict(sorted(sources.items())), indent=2, ensure_ascii=False)
                    + "\n", encoding="utf-8")


def summarize(sources, slugs):
    rows = [sources[s] for s in slugs if s in sources]
    count = lambda pred: sum(1 for e in rows if pred(e))
    lines = [
        f"Journals: {len(rows)}",
        f"  confirmed by ISSN:   {count(lambda e: e['method'] == 'issn' and e['confirmed'])}",
        f"  manual / confirmed:  {count(lambda e: e['method'] in ('manual', 'name') and e['confirmed'])}",
        f"  ISSN, name differs:  {count(lambda e: e['method'] == 'issn' and not e['confirmed'])}",
        f"  name match, to check: {count(lambda e: e['method'] == 'name' and not e['confirmed'])}",
        f"  unmatched:           {count(lambda e: not e['source_id'])}",
    ]
    review = [(s, sources[s]) for s in slugs if s in sources and not sources[s]["confirmed"]]
    if review:
        lines += ["", "To review:"]
        for slug, e in review:
            got = f"{e['display_name']} ({e['source_id']})" if e["source_id"] else "-"
            lines.append(f"  {slug}: registry '{e['journal']}' -> {got}; {e.get('note', '')}")
    return "\n".join(lines)


def confirm(slugs):
    """Mark reviewed matches as confirmed. Refuses slugs that are missing or have no match."""
    sources = load_map()
    bad = [s for s in slugs if not (sources.get(s) or {}).get("source_id")]
    if bad:
        sys.exit(f"ERROR: nothing written; not in the map or unmatched: {', '.join(bad)}")
    for slug in slugs:
        e = sources[slug]
        e["confirmed"] = True
        e.pop("note", None)
        print(f"  confirmed {slug}: {e['display_name']} ({e['source_id']})")
    save_map(sources)


def main():
    parser = argparse.ArgumentParser(description="Match registry journals to OpenAlex sources.")
    parser.add_argument("--field",    type=str, default=None)
    parser.add_argument("--slug",     type=str, default=None)
    parser.add_argument("--issn-csv", type=Path, default=None,
                        help="CSV with journal titles and ISSNs, e.g. the ABS AJG list")
    parser.add_argument("--refresh",  action="store_true",
                        help="re-resolve journals already in the map (except manual/confirmed)")
    parser.add_argument("--confirm",  nargs="+", metavar="SLUG",
                        help="mark these slugs' matches as confirmed after review (no requests)")
    args = parser.parse_args()

    if args.confirm:
        confirm(args.confirm)
        return

    if not (OPENALEX_MAILTO or OPENALEX_API_KEY):
        sys.exit("ERROR: set OPENALEX_MAILTO (and OPENALEX_API_KEY if OpenAlex requires one) "
                 "in the environment first.")

    journals = [j for j in JOURNALS
                if (not args.field or j[3] == args.field) and (not args.slug or j[4] == args.slug)]
    if not journals:
        sys.exit("No journals matched.")
    csv_table = load_issn_csv(args.issn_csv) if args.issn_csv else {}

    sources = load_map()
    resolved = kept = 0
    stopped = None
    try:
        for name, url, rating, field, slug in journals:
            existing = sources.get(slug)
            if keep_existing(existing) or (existing and not args.refresh):
                kept += 1
                continue
            issns = collect_issns(name, url, field, slug, csv_table)
            sources[slug] = match_journal(name, issns, openalex_get)
            resolved += 1
            e = sources[slug]
            status = ("ok" if e["confirmed"] else "REVIEW") if e["source_id"] else "UNMATCHED"
            print(f"  {slug:<48} {e['method'] or '-':<6} {status}")
    except OpenAlexStop as exc:
        stopped = exc
    finally:
        save_map(sources)

    print(f"\n{resolved} resolved, {kept} kept unchanged; map: {SOURCES_MAP}\n")
    print(summarize(sources, [j[4] for j in journals]))
    if budget["remaining_usd"] is not None:
        print(f"\nOpenAlex budget remaining today: ${budget['remaining_usd']:.4f}")
    if stopped:
        sys.exit(f"\nSTOPPED: {stopped}\nProgress is saved. Run the same command again to "
                 f"continue; journals already in the map are skipped.")


if __name__ == "__main__":
    main()
