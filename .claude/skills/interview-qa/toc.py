#!/usr/bin/env python3
"""Rebuild and verify the table of contents of an interview Q&A file.

Usage:
  python3 .claude/skills/interview-qa/toc.py <file.md>           # rebuild TOC, then verify
  python3 .claude/skills/interview-qa/toc.py --check <file.md>   # verify only
  add --per-section N to force N questions per section (default: read N from
  the "# Easy Questions (1-N)" header, else 150; 50 gives 1-50/51-100/101-150)

Rebuild replaces everything between "## Table of Contents" and the first
"# Easy Questions (1-N)" header. It is safe to run repeatedly.
Exits 1 and lists problems if verification fails.
"""
import re
import sys

SECTIONS = []
TOTAL = 0


def configure(n):
    """Set the three sections to n questions each (150 gives 1-150/151-300/301-450)."""
    global SECTIONS, TOTAL
    SECTIONS = [
        (f"{label} Questions ({i * n + 1}-{(i + 1) * n})", i * n + 1, (i + 1) * n)
        for i, label in enumerate(["Easy", "Moderate", "Advanced"])
    ]
    TOTAL = 3 * n


def detect_per_section(path):
    m = re.search(r"^# Easy Questions \(1-(\d+)\)\s*$", open(path, encoding="utf-8").read(), re.M)
    return int(m.group(1)) if m else 150

# Words that make text read as AI-generated. Checked as whole words in prose,
# ignoring code blocks, `inline code` and "quoted strings".
AI_WORDS = re.compile(
    r"\b(delve[sd]?|delving|crucial(ly)?|leverag(e|es|ed|ing)|seamless(ly)?|"
    r"comprehensive(ly)?|furthermore|moreover|in essence|game[- ]chang\w*|"
    r"plethora|tapestry|underscore[sd]? the importance)\b|—",
    re.I,
)


def slug(heading):
    """GitHub heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def outside_fences(lines):
    """Yield (index, line) for lines not inside fenced code blocks."""
    fence = None
    for i, line in enumerate(lines):
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if m:
            mark = m.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield i, line


def questions(lines):
    out = []
    for _, line in outside_fences(lines):
        m = re.match(r"^## (\d+): (.+?)\s*$", line)
        if m:
            out.append((int(m.group(1)), f"{m.group(1)}: {m.group(2)}"))
    return out


def body_start(lines):
    for i, line in outside_fences(lines):
        if line.strip() == f"# {SECTIONS[0][0]}":
            return i
    sys.exit(f"error: '# {SECTIONS[0][0]}' header not found")


def rebuild(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    try:
        toc = lines.index("## Table of Contents")
    except ValueError:
        sys.exit("error: '## Table of Contents' heading not found")
    start = body_start(lines)
    qs = questions(lines[start:])
    new = ["## Table of Contents", ""]
    new += [f"- [{name}](#{slug(name)})" for name, _, _ in SECTIONS]
    for name, lo, hi in SECTIONS:
        new += ["", f"### {name}", ""]
        new += [f"- [{h}](#{slug(h)})" for n, h in qs if lo <= n <= hi]
    new += ["", "---", ""]
    lines = lines[:toc] + new + lines[start:]
    open(path, "w", encoding="utf-8").write("\n".join(lines))


def check(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    problems = []

    if text.count("```") % 2:
        problems.append("odd number of ``` fences (unclosed code block)")
    if not re.search(r"^_Last updated: \w+ \d{1,2}, \d{4}_$", "\n".join(lines[:5]), re.M):
        problems.append("missing '_Last updated: <Month> <Day>, <Year>_' line after the title")

    start = body_start(lines)
    qs = questions(lines[start:])
    nums = [n for n, _ in qs]
    if nums != list(range(1, TOTAL + 1)):
        seen, dups = set(), set()
        for n in nums:
            (dups if n in seen else seen).add(n)
        missing = sorted(set(range(1, TOTAL + 1)) - seen)
        out_of_order = any(b < a for a, b in zip(nums, nums[1:]))
        problems.append(
            f"questions: {len(nums)} found; missing {missing[:20]}; "
            f"duplicates {sorted(dups)[:20]}; out of order: {out_of_order}"
        )

    headers = [l[2:].strip() for _, l in outside_fences(lines[start:]) if l.startswith("# ")]
    if headers != [name for name, _, _ in SECTIONS]:
        problems.append(f"section headers are {headers}")
    section_of = {}
    current = None
    for _, l in outside_fences(lines[start:]):
        if l.startswith("# "):
            current = l[2:].strip()
        m = re.match(r"^## (\d+): ", l)
        if m:
            section_of[int(m.group(1))] = current
    for name, lo, hi in SECTIONS:
        wrong = [n for n in range(lo, hi + 1) if n in section_of and section_of[n] != name]
        if wrong:
            problems.append(f"questions {wrong[:10]} are not under '# {name}'")

    anchors = {slug(h) for _, h in qs} | {slug(name) for name, _, _ in SECTIONS}
    # Greedy link text: headings may contain [brackets], e.g. "[hidden]" or "[]".
    toc_links = re.findall(r"^- \[.*\]\(#([^)]+)\)$", "\n".join(lines[:start]), re.M)
    q_links = [a for a in toc_links if re.match(r"\d+-", a)]
    if len(q_links) != TOTAL:
        problems.append(f"TOC has {len(q_links)} question links, expected {TOTAL}")
    broken = [a for a in toc_links if a not in anchors]
    if broken:
        problems.append(f"TOC links with no matching heading: {broken[:10]}")
    if any("`" in h for _, h in qs):
        problems.append("question headings contain backticks")
    if any("**" in h for _, h in qs):
        problems.append("question headings contain ** (Prettier turns __x__ into bold; write *args as 'args')")

    fancy = []
    for i, l in outside_fences(lines):
        prose = re.sub(r'`[^`]*`|"[^"]*"', "", l)
        fancy += [f"{i + 1}: {m.group(0)}" for m in AI_WORDS.finditer(prose)]
    if fancy:
        problems.append(f"AI-sounding words (rewrite in plain words): {fancy[:15]}")

    if problems:
        print(f"FAIL {path}")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"OK {path}: {TOTAL} questions, TOC and anchors match")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    only_check = "--check" in args
    per_section = None
    if "--per-section" in args:
        i = args.index("--per-section")
        try:
            per_section = int(args[i + 1])
        except (IndexError, ValueError):
            sys.exit(__doc__)
        del args[i : i + 2]
    files = [a for a in args if a != "--check"]
    if len(files) != 1:
        sys.exit(__doc__)
    configure(per_section or detect_per_section(files[0]))
    if not only_check:
        rebuild(files[0])
    sys.exit(check(files[0]))
