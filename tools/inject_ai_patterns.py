#!/usr/bin/env python3
"""
AI-Writing Patterns Injector

Writes the canonical "Avoiding AI-Writing Patterns" block (tools/ai_patterns_fragment.md)
into every *_SKILL.md under skills/, between versioned markers:

  ## Avoiding AI-Writing Patterns

  <!-- academic-humanizer:start vX.Y.Z -->
  ...fragment body...
  <!-- academic-humanizer:end -->

  ---

  ## Sources

If the markers are present, the text from the start marker to the end marker is replaced.
Otherwise the section from the heading up to the next "## " heading (or end of file) is
replaced. Text outside the section is left byte-identical; encoding (UTF-8, with or
without BOM) and line endings (LF or CRLF) are kept. Idempotent: a second run changes
nothing.

If any file has zero sections or more than one, nothing is written and the script exits 1.
With --add-missing, a file with no section gets one before "## Sources" instead
(dispatch_journal_agents.py does this for every skill it generates).

Usage:
  python inject_ai_patterns.py                      # all skills under skills/
  python inject_ai_patterns.py --dry-run            # report only, write nothing
  python inject_ai_patterns.py path/to/x_SKILL.md   # specific files only
  python inject_ai_patterns.py --add-missing path/to/new_SKILL.md
"""

import argparse
import sys
from pathlib import Path


# ─────────────────────────────────────────────
# PATHS AND MARKERS
# ─────────────────────────────────────────────

TOOLS_DIR  = Path(__file__).parent          # .../tools/
REPO_ROOT  = TOOLS_DIR.parent               # .../
SKILLS_DIR = REPO_ROOT / "skills"
FRAGMENT   = TOOLS_DIR / "ai_patterns_fragment.md"

HEADING      = "## Avoiding AI-Writing Patterns"
START_PREFIX = "<!-- academic-humanizer:start"
END_MARKER   = "<!-- academic-humanizer:end -->"
SEPARATOR    = "---"
BOM          = "﻿"


class InjectError(Exception):
    pass


# ─────────────────────────────────────────────
# PARSING
# ─────────────────────────────────────────────

def load_fragment(path=FRAGMENT):
    """Return the fragment as a list of lines without line endings, markers included."""
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip("\n").split("\n")
    if not lines[0].startswith(START_PREFIX) or lines[-1] != END_MARKER:
        raise InjectError(f"{path}: must start with '{START_PREFIX} vX.Y.Z -->' "
                          f"and end with '{END_MARKER}'")
    if any(l.startswith(START_PREFIX) or l == END_MARKER for l in lines[1:-1]):
        raise InjectError(f"{path}: markers may appear only on the first and last lines")
    return lines


def split_section(lines):
    """
    Split a skill (list of lines without endings) around the AI-patterns section.

    Returns (head, middle, tail): head ends with the heading line, tail starts at the next
    "## " heading (or is empty at end of file), middle is everything in between.
    Raises InjectError unless there is exactly one section and the markers are well formed.
    """
    headings = [i for i, l in enumerate(lines) if l.rstrip() == HEADING]
    if len(headings) != 1:
        raise InjectError(f"expected 1 '{HEADING}' section, found {len(headings)}")
    h = headings[0]

    starts = [i for i, l in enumerate(lines) if l.startswith(START_PREFIX)]
    ends   = [i for i, l in enumerate(lines) if l.rstrip() == END_MARKER]

    if not starts and not ends:
        t = h + 1
        while t < len(lines) and not lines[t].startswith("## "):
            t += 1
        return lines[:h + 1], lines[h + 1:t], lines[t:]

    if len(starts) != 1 or len(ends) != 1:
        raise InjectError(f"expected 1 start and 1 end marker, "
                          f"found {len(starts)} and {len(ends)}")
    s, e = starts[0], ends[0]
    if not h < s < e:
        raise InjectError("markers are out of order or outside the section")
    if any(l.startswith("## ") for l in lines[h + 1:s]):
        raise InjectError("start marker is not inside the section")

    # After the end marker: optional blank lines, an optional separator, blank lines.
    t = e + 1
    while t < len(lines) and lines[t].strip() == "":
        t += 1
    if t < len(lines) and lines[t].strip() == SEPARATOR:
        t += 1
        while t < len(lines) and lines[t].strip() == "":
            t += 1
    if t < len(lines) and not lines[t].startswith("## "):
        raise InjectError("unexpected text between the end marker and the next heading")
    return lines[:h + 1], lines[h + 1:t], lines[t:]


def build_middle(fragment, at_eof):
    middle = [""] + fragment + ["", SEPARATOR]
    return middle if at_eof else middle + [""]


# ─────────────────────────────────────────────
# INJECTION
# ─────────────────────────────────────────────

def inject_text(text, fragment):
    """Return text with the AI-patterns section replaced by the fragment."""
    bom = text.startswith(BOM)
    if bom:
        text = text[1:]
    newline = "\r\n" if "\r\n" in text else "\n"
    final_newline = text.endswith("\n")
    lines = text.replace("\r\n", "\n").split("\n")
    if final_newline:
        lines.pop()

    head, _, tail = split_section(lines)
    lines = head + build_middle(fragment, at_eof=not tail) + tail

    # A file whose section ends it now ends with the separator, so it needs a final newline.
    out = newline.join(lines) + (newline if final_newline or not tail else "")
    return (BOM if bom else "") + out


def add_section_text(text, fragment):
    """
    Like inject_text, but a skill with no section gets one: inserted before the "## Sources"
    heading (or appended at the end), preceded by a "---" separator. Used for newly
    generated skills, which are written without the section.
    """
    if any(l.rstrip() == HEADING for l in text.splitlines()):
        return inject_text(text, fragment)

    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.replace("\r\n", "\n").rstrip("\n").split("\n")
    sources = next((i for i, l in enumerate(lines) if l.startswith("## Sources")), len(lines))
    head, tail = lines[:sources], lines[sources:]
    while head and head[-1].strip() == "":
        head.pop()
    if head and head[-1].strip() != SEPARATOR:
        head += ["", SEPARATOR]
    lines = head + ["", HEADING] + build_middle(fragment, at_eof=not tail) + tail
    return newline.join(lines) + newline


def find_skills(skills_dir=SKILLS_DIR):
    return sorted(skills_dir.rglob("*_SKILL.md"))


def inject_files(paths, fragment, dry_run=False, add_missing=False):
    """Inject into every path. Writes nothing unless every file parses. Returns changed paths."""
    inject = add_section_text if add_missing else inject_text
    updates, errors = [], []
    for path in paths:
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
            new = inject(text, fragment)
        except (InjectError, UnicodeDecodeError) as exc:
            errors.append(f"{path}: {exc}")
            continue
        if new != text:
            updates.append((path, new.encode("utf-8")))

    if errors:
        raise InjectError("\n".join(errors))
    if not dry_run:
        for path, data in updates:
            path.write_bytes(data)
    return [path for path, _ in updates]


def main():
    parser = argparse.ArgumentParser(
        description="Inject the canonical AI-patterns block into skill files.")
    parser.add_argument("paths", nargs="*", type=Path,
                        help="skill files to process (default: every *_SKILL.md under skills/)")
    parser.add_argument("--fragment", type=Path, default=FRAGMENT)
    parser.add_argument("--dry-run",  action="store_true", help="report changes, write nothing")
    parser.add_argument("--add-missing", action="store_true",
                        help="add the section to skills that have none, instead of failing")
    args = parser.parse_args()

    paths = args.paths or find_skills()
    try:
        fragment = load_fragment(args.fragment)
        changed = inject_files(paths, fragment, dry_run=args.dry_run,
                               add_missing=args.add_missing)
    except InjectError as exc:
        print(f"ERROR: nothing written.\n{exc}", file=sys.stderr)
        sys.exit(1)

    verb = "would change" if args.dry_run else "changed"
    print(f"{len(paths)} files: {len(changed)} {verb}, {len(paths) - len(changed)} unchanged")


if __name__ == "__main__":
    main()
