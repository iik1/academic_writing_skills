#!/usr/bin/env python3
"""
AI-Writing Patterns Self-Check

Run after inject_ai_patterns.py. Asserts, for every *_SKILL.md under skills/:
  - exactly one start marker and one end marker, in order
  - the block between them (markers included) equals tools/ai_patterns_fragment.md
  - the text outside the section equals the text outside the section at the baseline commit,
    and the section itself is exactly heading, blank, block, blank, "---"
  - the frontmatter parses and its name is unchanged from the baseline (skills whose
    frontmatter was already missing or nameless at the baseline are listed as warnings)
  - the skill count matches the baseline, with no file added, missing or skipped
  - a second injector run would change nothing

Line endings and a BOM are ignored when comparing against the baseline.

Usage:
  python check_ai_patterns.py
  python check_ai_patterns.py --baseline <commit>
"""

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

from inject_ai_patterns import (
    REPO_ROOT, SKILLS_DIR, FRAGMENT, START_PREFIX, END_MARKER, BOM,
    InjectError, load_fragment, split_section, build_middle, find_skills, inject_files,
)

# Baseline commit from issue #2: the 21-rule rollout merged with the origin/main cleanup.
BASELINE = "f3580953abb0fc47d284d95b87c6e9b1032d121b"


def git(*args, stdin=None):
    return subprocess.run(["git", "-C", str(REPO_ROOT), *args], input=stdin,
                          capture_output=True, check=True).stdout


def read_baseline(ref):
    """Return {repo-relative path: text} for every *_SKILL.md under skills/ at ref."""
    names = [n for n in git("ls-tree", "-r", "--name-only", ref, "--", "skills")
             .decode("utf-8").splitlines() if n.endswith("_SKILL.md")]
    out = git("cat-file", "--batch", stdin="".join(f"{ref}:{n}\n" for n in names).encode())
    texts, pos = {}, 0
    for name in names:
        header_end = out.index(b"\n", pos)
        size = int(out[pos:header_end].split()[2])
        texts[name] = out[header_end + 1:header_end + 1 + size].decode("utf-8")
        pos = header_end + 1 + size + 1
    return texts


def to_lines(text):
    text = text[1:] if text.startswith(BOM) else text
    return text.replace("\r\n", "\n").split("\n")


def frontmatter_name(text):
    """Return (name, None), or (None, problem) if the frontmatter is missing or has no name."""
    lines = to_lines(text)
    if lines[0] != "---" or "---" not in lines[1:]:
        return None, "no frontmatter"
    end = lines.index("---", 1)
    try:
        meta = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError:
        return None, "frontmatter does not parse"
    if not isinstance(meta, dict) or not meta.get("name"):
        return None, "frontmatter has no name"
    return meta["name"], None


def check_file(text, base_text, fragment):
    lines = to_lines(text)
    starts = [i for i, l in enumerate(lines) if l.startswith(START_PREFIX)]
    ends   = [i for i, l in enumerate(lines) if l == END_MARKER]
    assert len(starts) == 1 and len(ends) == 1, \
        f"{len(starts)} start and {len(ends)} end markers"
    assert starts[0] < ends[0], "end marker before start marker"
    assert lines[starts[0]:ends[0] + 1] == fragment, "block differs from the fragment"

    head, middle, tail = split_section(lines)
    base_head, _, base_tail = split_section(to_lines(base_text))
    assert head == base_head, "text before the section differs from the baseline"
    assert tail == base_tail, "text after the section differs from the baseline"
    # Strip the final "" left by a trailing newline so EOF sections compare cleanly.
    if not tail and middle and middle[-1] == "":
        middle = middle[:-1]
    assert middle == build_middle(fragment, at_eof=not tail), "section is not in canonical shape"

    name, problem = frontmatter_name(text)
    base_name, base_problem = frontmatter_name(base_text)
    assert (name, problem) == (base_name, base_problem), \
        f"frontmatter changed: {base_name or base_problem!r} -> {name or problem!r}"
    return base_problem


def main():
    parser = argparse.ArgumentParser(description="Verify the AI-patterns rollout.")
    parser.add_argument("--baseline", default=BASELINE, help="commit to compare against")
    args = parser.parse_args()

    fragment = load_fragment()
    baseline = read_baseline(args.baseline)
    paths = find_skills()
    current = {p.relative_to(REPO_ROOT).as_posix(): p for p in paths}
    failures = []

    for name in sorted(set(baseline) - set(current)):
        failures.append(f"{name}: in baseline but missing now")
    for name in sorted(set(current) - set(baseline)):
        failures.append(f"{name}: not in baseline")

    checked, warnings = 0, []
    for name in sorted(set(current) & set(baseline)):
        try:
            problem = check_file(current[name].read_bytes().decode("utf-8"),
                                 baseline[name], fragment)
            checked += 1
            if problem:
                warnings.append(f"{name}: {problem} (already so at baseline)")
        except (AssertionError, InjectError, UnicodeDecodeError) as exc:
            failures.append(f"{name}: {exc}")

    try:
        rerun = inject_files(paths, fragment, dry_run=True)
        if rerun:
            failures.append(f"a second injector run would change {len(rerun)} files")
    except InjectError as exc:
        failures.append(f"injector re-run failed:\n{exc}")

    print(f"baseline {args.baseline[:7]}: {len(baseline)} skills; "
          f"now {len(current)}; {checked} passed")
    if warnings:
        print(f"WARNING: {len(warnings)} skills have frontmatter problems not caused by the injector")
        for w in warnings:
            print(f"  {w}")
    if failures:
        print(f"FAIL: {len(failures)} problems", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
