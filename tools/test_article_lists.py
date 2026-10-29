#!/usr/bin/env python3
"""
Offline test for build_article_lists.py, against stored OpenAlex responses in
tools/fixtures/openalex_works_sample.json (four years, two issues per year, open access mixed,
plus front matter, a non-article, a duplicate, an online-first article and an unusable record).

Usage:
  python test_article_lists.py
"""

import json
import random
from datetime import date
from pathlib import Path

import build_article_lists as bal

FIXTURE = Path(__file__).parent / "fixtures" / "openalex_works_sample.json"
SLUG    = "strategic-management-journal"
TODAY   = date(2026, 10, 29)


def fixture_fetch(responses, calls):
    def fetch(path, params):
        calls.append((path, params))
        year = params["filter"].split("publication_year:")[1].split(",")[0]
        return responses.get(year, {"results": []})["results"]
    return fetch


def main():
    responses = json.loads(FIXTURE.read_text(encoding="utf-8"))
    works = [w for r in responses.values() for w in r["results"]]

    # Front-matter filter: drops front matter, keeps look-alike research titles.
    for title in ["Issue Information", "Editorial Board, Volume 47", "Editorial", "Erratum",
                  "Correction to: Dynamic capabilities", "Retraction: X", "Editorial: Special issue",
                  "Introduction to the special issue on stakeholders", "Thanks to our reviewers",
                  "Book Reviews", "Index"]:
        assert bal.is_front_matter(title), title
    for title in ["Editorial independence and CEO pay", "Correction for measurement error",
                  "Index funds and corporate governance", "Covering the costs of entry",
                  "Contentious politics and firms", "Retractions and reputation"]:
        assert not bal.is_front_matter(title), title

    cands, pool = bal.select(works, SLUG, n=1000)
    titles = [c["title"] for c in cands]
    assert not any(bal.is_front_matter(t) for t in titles)
    assert "A comment on replication" not in titles, "non-article type kept"
    assert "No identifiers at all" not in titles, "unusable record kept"
    assert len({c["doi"] for c in cands}) == len(cands), "duplicate kept"
    assert sum(t.startswith("Editorial independence") for t in titles) == 4
    assert sum(t.startswith("Online-first") for t in titles) == 4
    assert pool["usable"] == len(cands) == 4 * 16   # 12 regular + 1 online-first + 3 look-alikes

    # Ranking: OA with full-text link, then other OA, then the rest.
    rank = lambda c: 0 if c["is_oa"] and c["fulltext_url"] else (1 if c["is_oa"] else 2)
    ranks = [rank(c) for c in cands]
    assert ranks == sorted(ranks), "groups out of order"
    assert pool["with_fulltext_link"] == ranks.count(0) and pool["open_access"] == ranks.count(0) + ranks.count(1)

    # Spread: within the full-text group the first picks rotate across all four years,
    # newest first, and the first two picks of a year come from different issues.
    top = [c for c in cands if rank(c) == 0]
    assert [c["year"] for c in top[:4]] == [2026, 2025, 2024, 2023], [c["year"] for c in top[:4]]
    for year in (2026, 2024):
        first_two = [c for c in top if c["year"] == year][:2]
        assert len({(c["volume"], c["issue"]) for c in first_two}) == 2, year

    # Determinism: same responses in any order give the same list; n is respected.
    picked, _ = bal.select(works, SLUG)
    for seed in range(5):
        shuffled = works[:]
        random.Random(seed).shuffle(shuffled)
        assert bal.select(shuffled, SLUG)[0] == picked
    assert len(picked) == bal.N_CANDIDATES and [c["rank"] for c in picked] == list(range(1, 26))
    assert bal.select(works, "another-journal")[0] != picked, "slug should vary tie order"

    # build_list: one sampled request per year of the window, with a stable seed.
    calls = []
    entry = {"source_id": "S102949365", "display_name": "Strategic Management Journal", "confirmed": True}
    doc, reason = bal.build_list(SLUG, "Strategic Management Journal", entry,
                                 fixture_fetch(responses, calls), today=TODAY)
    assert reason is None and doc["window"] == {"from_year": 2023, "to_year": 2026}
    assert [p["filter"] for _, p in calls] == [bal.works_filter("S102949365", y) for y in range(2023, 2027)]
    assert all(path == "works" and p["sample"] == bal.SAMPLE_PER_YEAR and p["seed"] == bal.seed_for(SLUG, int(y))
               for (path, p), y in zip(calls, doc["query"]["seeds"]))
    assert doc["candidates"] == picked and doc["pool"]["works_returned"] == len(works)
    again, _ = bal.build_list(SLUG, "Strategic Management Journal", entry,
                              fixture_fetch(responses, []), today=TODAY)
    assert again["candidates"] == doc["candidates"] and again["query"] == doc["query"]

    # No list, no error: unmatched, unconfirmed, or no recent articles.
    none = lambda path, params: []
    assert bal.build_list(SLUG, "x", None, none, today=TODAY) == (None, "no OpenAlex match in openalex_sources.json")
    assert bal.build_list(SLUG, "x", {**entry, "confirmed": False}, none, today=TODAY)[1].startswith("OpenAlex match not confirmed")
    assert bal.build_list(SLUG, "x", entry, none, today=TODAY)[1] == "no research articles in OpenAlex for 2023-2026"

    print(f"OK: {len(cands)} usable of {len(works)} works; list of {len(picked)}, "
          f"{sum(rank(c) == 0 for c in picked)} with full-text link")


if __name__ == "__main__":
    main()
