#!/usr/bin/env python3
"""
OpenAlex Source Map Check

Validates tools/openalex_sources.json against JOURNALS (dispatch_journal_agents.py):
  - every registry slug has an entry                        (missing -> exit 1)
  - confirmed entries have a source ID                       (otherwise -> exit 1)
  - lists unmatched entries, unconfirmed entries, duplicate source IDs, and map entries
    for slugs no longer in the registry

Usage:
  python check_openalex_sources.py
"""

import sys
from collections import defaultdict

from build_openalex_sources import SOURCES_MAP, load_map
from dispatch_journal_agents import JOURNALS


def main():
    if not SOURCES_MAP.exists():
        sys.exit(f"ERROR: {SOURCES_MAP.name} not found; run build_openalex_sources.py first.")
    sources = load_map()
    registry = {j[4]: j[0] for j in JOURNALS}

    missing      = [s for s in registry if s not in sources]
    extra        = [s for s in sources if s not in registry]
    broken       = [s for s, e in sources.items() if e.get("confirmed") and not e.get("source_id")]
    unmatched    = [s for s in registry if s in sources and not sources[s].get("source_id")]
    unconfirmed  = [s for s in registry if s in sources and sources[s].get("source_id")
                    and not sources[s].get("confirmed")]
    by_source = defaultdict(list)
    for s in registry:
        if s in sources and sources[s].get("source_id"):
            by_source[sources[s]["source_id"]].append(s)
    duplicates = {sid: slugs for sid, slugs in by_source.items() if len(slugs) > 1}

    confirmed = len(registry) - len(missing) - len(unmatched) - len(unconfirmed)
    print(f"Registry: {len(registry)} journals; map: {len(sources)} entries")
    print(f"  confirmed: {confirmed}   unconfirmed: {len(unconfirmed)}   "
          f"unmatched: {len(unmatched)}   missing: {len(missing)}")

    def section(title, items):
        if items:
            print(f"\n{title} ({len(items)}):")
            for item in items:
                print(f"  {item}")

    section("Missing from the map", missing)
    section("Confirmed but no source_id", broken)
    section("Unmatched", [f"{s}: {sources[s].get('note', '')}" for s in unmatched])
    section("Unconfirmed", [f"{s}: registry '{registry[s]}' -> "
                            f"'{sources[s].get('display_name')}' ({sources[s]['source_id']})"
                            for s in unconfirmed])
    section("Duplicate source IDs", [f"{sid}: {', '.join(slugs)}"
                                     for sid, slugs in duplicates.items()])
    section("Not in the registry", extra)

    if missing or broken:
        sys.exit(1)


if __name__ == "__main__":
    main()
