---
name: interview-qa-review
description: Validate and correct an existing interview questions and answers markdown file for a specific technology (e.g. angular.md, react.md). Checks factual accuracy, up-to-date APIs, code correctness, structure, numbering, duplicates, and difficulty placement, then fixes the problems in place. Use whenever the user asks to validate, review, fact-check, verify, fix, correct, or update the questions and answers of a technology, e.g. "validate angular.md" or "review and correct the DynamoDB questions".
---

# Interview Q&A Validation and Correction

Audit one existing interview Q&A file against the current state of its technology, fix every problem found, and report what changed.

## Step 1: Locate the file and decide the mode

- Find the file the user named (e.g. `docs/front-end/frameworks/angular.md`). If the name is ambiguous or matches several files, list the candidates and ask which one.
- If the file doesn't exist, stop and tell the user. Suggest the `interview-qa` skill to create it.
- Default mode is **fix**: apply corrections directly to the file.
- If the user says "just review", "report only", or "don't change anything", use **report-only** mode: make no edits and produce the report from Step 8 instead.
- Do not modify any file other than the one requested, except where Step 7 requires a README fix.

## Step 2: Establish the current state of the technology

Do not rely on memory alone.

- Use web search or official documentation to find the latest stable version and its current APIs, features, deprecations, removals, and recommended practices.
- Compare against the version the file's intro claims to target. If the intro names an older version, the whole file needs a currency check against the newer one.
- Build a short internal list of "things that changed": deprecated APIs, removed APIs, renamed features, new recommended replacements. Use it throughout the audit.

## Step 3: Audit the structure

Check the file against the standard structure and record every deviation:

1. `# <Technology> Interview Questions and Answers` as the H1 title.
2. An intro paragraph stating the question count, the difficulty split, and the targeted version.
3. `## Table of Contents` linking to the three sections:
   - `[Easy Questions (1-150)](#easy-questions-1-150)`
   - `[Moderate Questions (151-300)](#moderate-questions-151-300)`
   - `[Advanced Questions (301-450)](#advanced-questions-301-450)`
4. Three `###` sections in this order: Easy (1-150), Moderate (151-300), Advanced (301-450).
5. Questions use the format `**N: Question text?**` followed by the answer.
6. Numbering runs continuously from 1 to 450 with no gaps, duplicates, or restarts.
7. Exactly 150 questions per section, and each number falls in its section's range.
8. All code fences are opened and closed, with a correct language tag.
9. Every table of contents link matches an actual header anchor.

If the file legitimately differs from this standard (for example, an older file with a different count), do not force it into the standard. Report the difference and ask the user before restructuring.

## Step 4: Audit the content

Review every question and answer in order, in batches of about 50 so nothing is skimmed. For each one, check:

- **Factual accuracy:** the answer is technically correct and not misleading.
- **Currency:** it uses current APIs and recommended practice. Flag anything deprecated, removed, or superseded. Legacy material may stay only if candidates still meet it in real projects, and it must be labeled as legacy.
- **Code correctness:** snippets have valid syntax, correct imports, correct method signatures, and actually demonstrate the point being made.
- **Completeness:** the answer fully addresses the question. Flag answers that are vague, circular, or missing the key point interviewers expect.
- **Clarity:** the question is phrased the way a real interviewer would ask it, and it isn't ambiguous.
- **Duplicates:** no question repeats or nearly repeats another question anywhere in the file.
- **Difficulty placement:** the question sits in the right section. Basic definitions don't belong in Advanced, and internals or architecture questions don't belong in Easy.
- **Coverage:** note major feature areas of the technology that no question covers.

Do not invent APIs or behavior while correcting. If you can't confirm something from documentation, mark it as uncertain in the report instead of guessing.

## Step 5: Validate the code

- Where tools are available, check snippets mechanically instead of by eye. For example, compile TypeScript with `tsc`, syntax-check JavaScript with `node --check`, parse JSON and YAML, and run small self-contained snippets.
- Do not install heavy dependencies or run snippets that need external services, credentials, or network access. Review those by reading against the documentation.
- Treat a snippet that fails to run as a bug to fix, unless it is deliberately incomplete (a fragment) and the answer says so.

## Step 6: Apply the corrections

In fix mode:

- Make the smallest edit that fixes each problem. Do not rewrite answers that are already correct, and do not change style or tone for its own sake.
- **Never renumber.** Every question keeps its number. When a duplicate or invalid question must go, replace it in place with a new, distinct question of the same difficulty on an uncovered topic, using the same number.
- When a question is in the wrong difficulty section, swap it with a question of the right level, or replace it, so each section still holds exactly 150 and numbering stays continuous.
- Update the intro paragraph if the targeted version changed.
- Fix broken table of contents links and unclosed code fences.
- Edit in batches and re-read each batch after editing to confirm the markdown is still valid.

## Step 7: Check README.md

- Confirm the technology is listed in `README.md` exactly once and that its link points to the real file path.
- If the entry is missing, duplicated, or has a wrong path, fix it by following the README's existing format. Change nothing else in the README.

## Step 8: Final verification and report

After editing, re-verify the structure checks from Step 3 (450 questions, 150 per section, numbering 1-450, working table of contents links, closed code fences).

Then report to the user:

1. **Summary:** the file, the version it now targets, and totals for questions reviewed, corrected, and replaced.
2. **Corrections by category:** counts for factual errors, outdated APIs, broken code, duplicates replaced, difficulty moves, and structural fixes.
3. **Notable changes:** the most significant fixes, each with the question number and a one-line description (for example, "Q212: replaced the deprecated `X` with `Y`").
4. **Uncertain items:** anything that could not be confirmed and was left unchanged or flagged.
5. **Coverage gaps:** major topics the file doesn't cover, with an offer to add questions for them.

In report-only mode, give the same report, but describe each issue and the fix you would make instead of describing a change already applied.
