# CLAUDE.md

# Part 1: Price optimization

Keep this file under 200 lines. It is sent on every turn.
Task-specific procedures belong in `.claude/skills/`.

## Commands

```bash
./claude/scripts/install.sh      # once per clone: git hooks + jq check
./claude/scripts/cost-audit.sh   # what this repo adds to every request
./claude/scripts/test-hooks.sh   # smoke-test the Claude Code hooks
```

## Conventions

- Keep every non-doc file under 5,000 tokens (~20 KB). A pre-commit hook enforces this; `docs/` is exempt via `.token-budget-ignore`.
- Prefer CLIs (`gh`, `aws`, `supabase`, `netlify`) over MCP servers.

## Workflows (loaded on demand as skills)

- Creating a new Q&A file: use the `interview-qa` skill.
- Validating or fixing an existing Q&A file: use the `interview-qa-review` skill.
- Reviewing a pull request: use the `pr-review` skill.
- Ending or pausing a long task: use the `handoff` skill.
- Shrinking this file under 200 lines: use the `compress-claude-md` skill.
- Finding where agents search too long or trust stale docs: use the `retro` skill.

## Cost rules for agents

- Use Explore/Plan subagents for searching and planning (they run on Haiku).
- Run tests, lint, and builds through the `test-runner` subagent when the
  output may be long.
- Grep before you Read. Read only the line ranges you need (offset/limit);
  a hook blocks full reads of files over ~10,000 tokens (most files in `docs/`).
- Do not paste whole files or full command output into the conversation.
- Test/lint/build output is filtered to errors automatically; append `# raw`
  to a command only if the filtered output is not enough.
- Keep replies short: no restating the plan, no summaries of unchanged code.
- Never edit lockfiles or generated code by hand.

# Part 2: Other best practices

## Project Overview

Interview questions and answers for full stack web developers. Each file in `docs/<area>/<category>/<topic>.md` covers one topic, split into easy, moderate and advanced questions. [README.md](README.md) is the index of all topics.

## Rules

- Whenever any content in this repo is added or updated, update the `_Last updated: <Month> <Day>, <Year>_` line at the top of [README.md](README.md) to the current date (for example, `_Last updated: October 29, 2026_`).
- Whenever any questions and answers markdown file (for example, [docs/front-end/other/web-vitals.md](docs/front-end/other/web-vitals.md)) is added or updated in any way, it must have the same `_Last updated: <Month> <Day>, <Year>_` line at the beginning, set to the current date. Put it right after the `#` title, separated by blank lines, the same as in [README.md](README.md). If the file does not have the line yet, add it.

## Commands

```bash
npm run prettier   # format everything (also runs automatically on Stop)
```

## Specs

This project uses spec-driven development for larger changes. The rules live in the
`implement-spec` skill (`.claude/skills/implement-spec/`); use it for any spec
or backlog work.

- Only start spec-track work for an Approved spec in `specs/active/` or a quick-track item
  in `specs/backlog.md`.
- Keep the spec and `specs/progress.md` in sync with what you actually build.

## Subagents

Project agents live in `.claude/agents/`. Delegate when the process is large but the result is small; do targeted or context-dependent work inline.

- `oss-researcher`: before implementing an unfamiliar feature (see Workflow).
- `code-reviewer`: after finishing a change, before committing.
- `test-runner`: to run tests/lint/format checks without flooding context.

## Workflow

- For unfamiliar features, don't write from scratch. First search GitHub for open-source implementations, compare approaches, then pick one and start. Summarize which approach you chose and why before implementing.
- Explore before editing: read the relevant files and existing patterns first. Reuse existing helpers instead of adding near-duplicates.
- For anything touching more than a few files, write a short plan (or use plan mode) and get agreement before coding.
- Never claim something works without running it. If you couldn't verify, say so explicitly.
- Fix root causes, not symptoms. Don't silence errors or skip checks to make them pass.
- Keep diffs focused on the task. No drive-by refactors, renames, or reformatting of untouched content — note them as follow-ups instead.
- Ask before: adding dependencies, changing CI, deleting files, or any git push / force operation.
- When stuck after two failed attempts at the same approach, stop, explain what you tried, and propose alternatives rather than looping.
- Commit in logical units with Conventional Commit messages; never commit secrets or generated artifacts.
- When a correction from the user is likely to recur, propose adding it to this file so it sticks.
- Keep `CLAUDE.md` split into two parts: Part 1 price optimization, Part 2 other best practices. Put new content in the matching part.
