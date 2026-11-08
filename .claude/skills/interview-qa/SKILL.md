---
name: interview-qa
description: Create a markdown file of 450 interview questions and answers (150 easy, 150 moderate, 150 advanced) for a specific technology, framework, language, or tool. Use whenever the user asks to add, create, or generate interview questions and answers for a technology, e.g. "add interview questions and answers for DynamoDB".
---

# Interview Questions and Answers Generator

Create one markdown file containing 450 interview questions and answers for the requested technology: 150 easy, 150 moderate, 150 advanced.

## Step 1: Pick the file location and name

- Place the file in the folder that best matches the technology's category. All category folders live inside `docs/`. Category folders: `docs/front-end/`, `docs/back-end/`, `docs/ai-engineering/`, `docs/optimization/`, `docs/mix/`. Use `docs/mix/` only if nothing else fits. Create a new category folder only if the user asks, and always inside `docs/`.
- The folder structure must mirror the `README.md` categorization. Every `####` subcategory in the README has a matching kebab-case subfolder under its `###` category folder, for example `#### Cloud` under `### Back End` maps to `docs/back-end/cloud/`, and `#### Libs` under `### Front End` maps to `docs/front-end/libs/`. Current subfolders:
  - `docs/back-end/`: `cloud/`, `languages/`, `frameworks/`, `libs/`, `other/`
  - `docs/front-end/`: `languages/`, `frameworks/`, `libs/`, `other/`
  - `docs/ai-engineering/`: `apis/`, `agents/`, `frameworks/`, `rag/`, `tools/`, `other/`
- If a category has subcategories, put the file in the matching subfolder, never directly in the category folder. Use `other/` only if no other subcategory fits.
- If the README gets a new subcategory (or a category gets subcategories for the first time), create the matching subfolder, move the files listed under it there, and update their README links so the folders and the README stay in sync.
- Name the file in lowercase kebab-case: `dynamodb.md`, `react-unit-testing.md`, `redux-toolkit.md`.
- Before writing, check whether the file already exists. If it does, ask the user whether to overwrite it or stop.
- Steps 3-4 fully define the file format, so don't read whole files to learn it. To match tone, read only the first questions of one existing file (for example `grep -n -A12 '^## 1:' docs/front-end/frameworks/angular.md | head -40`). To find where the README entry goes, `grep` the README for the target `###`/`####` section instead of reading the whole file.

## Step 2: Verify the current state of the technology

Do not rely on memory alone.

- Use web search or the official documentation to find the latest stable version and its current APIs, features, and best practices.
- If this takes more than a few searches or page fetches, delegate it to a `general-purpose` subagent and have it return a compact fact sheet (current version, SDK/package names, current APIs with exact names, what is deprecated or removed, source URLs) instead of fetching dozens of pages into the main conversation. When a docs site redirects to another domain, fetch the target domain directly from then on.
- Note what is deprecated or removed. Teach the modern approach first. Mention legacy approaches only where candidates will still meet them in real projects, and label them as legacy.
- Do not invent APIs, flags, or method names. If unsure that something exists, check it or leave it out.

## Step 3: File structure

The file must follow this exact structure:

1. `# <Technology> Interview Questions and Answers` as the H1 title, then a blank line and `_Last updated: <Month> <Day>, <Year>_` with the current date.
2. A short intro paragraph (2-4 sentences) stating the question count, the difficulty split, and which version of the technology the answers target.
3. `## Table of Contents` that lists every question, not just the sections:
   - First, links to the three sections:
     - `- [Easy Questions (1-150)](#easy-questions-1-150)`
     - `- [Moderate Questions (151-300)](#moderate-questions-151-300)`
     - `- [Advanced Questions (301-450)](#advanced-questions-301-450)`
   - Then a `###` subheading per section (`### Easy Questions (1-150)` and so on), each followed by a bullet list linking to every question in that section, for example `- [1: What is Angular?](#1-what-is-angular)`. The link text is the question heading exactly as written.
   - Then a `---` line to separate the table of contents from the questions.
4. Three main sections, in this order, each with a `#` header:
   - `# Easy Questions (1-150)`
   - `# Moderate Questions (151-300)`
   - `# Advanced Questions (301-450)`

`docs/front-end/frameworks/angular.md` is the reference for this layout.

## Step 4: Question format

Number questions continuously from 1 to 450 across the whole file. Do not restart numbering per section. Each question is a `##` heading, so it gets an anchor the table of contents can link to:

```
## 1: What is <concept>?

Answer text.

## 2: How do you <task>?

Answer text, with a code example if useful.
```

Table of contents anchors follow GitHub's heading slug rules: lowercase, drop every character that isn't a letter, number, underscore, hyphen or space, then turn each space into a hyphen. For example, `## 12: How does Object.groupBy work?` becomes `#12-how-does-objectgroupby-work`. Keep question headings free of backticks and markdown formatting so the link text and anchors stay clean.

## Step 5: Content rules

- **Easy (1-150):** fundamentals, core concepts, terminology, basic syntax, and common everyday usage.
- **Moderate (151-300):** practical usage, common patterns, configuration, integration with other tools, debugging, and trade-offs.
- **Advanced (301-450):** internals, architecture, performance tuning, scalability, security, edge cases, design decisions, and scenario-based questions.
- Add a code example wherever it helps the answer, in fenced code blocks with the correct language tag. Code must be correct, runnable, and use current APIs.
- Keep answers concise but complete: 2-6 sentences for conceptual answers, plus code where needed.
- No duplicate or near-duplicate questions. Each question must cover a distinct topic.
- Cover the technology broadly: every major feature area should appear at least once.
- Phrase questions the way real interviewers ask them.

## Step 6: Writing process

450 Q&As is too large for a single write. Work in batches:

1. Create the file with the title, intro, and the section links of the table of contents.
2. Append the questions in batches of about 25-50, in numerical order, so the numbering stays continuous. Write each batch with the Write tool to a part file in the scratchpad (`part1.md`, `part2.md`, ...) and join them with `cat`. Don't put large content in `cat <<'EOF'` heredocs: this machine's bash 3.2 refuses or breaks on big heredocs containing backticks.
3. Once all 450 questions are written, run `python3 .claude/skills/interview-qa/toc.py <file>`. It rebuilds the full table of contents (section links, per-section question links, `---`) and then verifies the file. Don't write your own TOC script.
4. The same run verifies the file: `_Last updated_` line, exactly 450 questions numbered 1-450 with no gaps or duplicates, each in the right section, 450 question links in the TOC, every link pointing to an existing heading anchor, no backticks in headings, and all code blocks closed. Fix anything it reports and re-run until it prints `OK`. Use `--check` to verify without rebuilding.
5. Report the file path and a one-line summary when done.

## Step 7: Register the technology in README.md

`README.md` lists every technology covered by this repo. After the Q&A file is complete, add the new technology to that list.

- Follow the existing format exactly: same bullet or table style, same link style, same capitalization pattern, same grouping.
- If the README groups technologies by category (front-end, back-end, and so on) and subcategory (Cloud, Languages, Frameworks, Libs, Other), add the entry under the category and subcategory that match the folder and subfolder the file was placed in. If a matching group doesn't exist, create one in the same style as the others and create the matching subfolder.
- Keep the existing ordering convention. If the list is alphabetical, insert the entry alphabetically. If it is not sorted, append it at the end of its group.
- The link must point to the new file's relative path, for example `docs/back-end/other/dynamodb.md`.
- Do not add a duplicate. If the technology is already listed, update that entry's link instead of adding a second one.
- Do not change any other part of the README, except the `_Last updated_` line: set it to the current date by pattern, not by its expected old value, because other sessions may have changed it already: `sed -i '' "s/^_Last updated: .*_$/_Last updated: $(date '+%B %-d, %Y')_/" README.md`.

## Step 8: Final check and report

- Confirm the README entry exists, appears exactly once, and its link path matches the actual file path.
- Report back with the Q&A file path, the README line that was added or changed, and a one-line summary.
