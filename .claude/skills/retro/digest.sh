#!/usr/bin/env bash
# Compress the last N Claude Code sessions for this repo into a short digest.
# Usage: digest.sh [N=10] [project_dir]
# Prints, per session: first prompt, user messages, and a numbered tool-call
# timeline with errors marked, so a retro never has to read raw transcripts.
set -euo pipefail

n="${1:-10}"
repo="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
dir="${2:-$HOME/.claude/projects/$(printf '%s' "$repo" | sed 's|[^A-Za-z0-9]|-|g')}"
current="${CLAUDE_CODE_SESSION_ID:-${CLAUDE_SESSION_ID:-}}"

[ -d "$dir" ] || { echo "No transcripts at $dir" >&2; exit 1; }

ls -t "$dir"/*.jsonl | grep -v "${current:-^$}" | head -n "$n" | while read -r f; do
  echo "=== session $(basename "$f" .jsonl) ($(date -r "$f" '+%Y-%m-%d %H:%M'))"
  jq -r --arg repo "$repo/" '
    def short: tostring | gsub("\n"; " ") | gsub("cd \($repo[:-1]); "; "")
      | gsub($repo; "") | gsub("/private/tmp/claude-[0-9]+/[^ ]*/scratchpad/"; "SP/") | .[0:160];
    select(.isSidechain != true) |
    if .type == "user" and (.message.content | type) == "string" then
      "USER: " + (.message.content | short)
    elif .type == "user" then
      .message.content[]? |
      if .type == "text" then "USER: " + (.text | short)
      elif .type == "tool_result" and .is_error == true then
        "  !! error: " + ((.content | if type == "array" then map(.text? // "") | join(" ") else . end) | short)
      else empty end
    elif .type == "assistant" then
      .message.content[]? | select(.type == "tool_use") |
      "  " + .name + " " + (
        .input.file_path // .input.pattern // .input.command //
        .input.query // .input.skill // .input.description // .input | short)
    else empty end
  ' "$f" | grep -v '^USER: <' | awk '
    # Collapse runs of scratchpad Write/Edit calls (batched drafts) into one line.
    /^  (Write|Edit) SP\// { if (!run) first = i + 1; run++; i++; next }
    run { printf "%3d  [%d Write/Edit calls to scratchpad, #%d-#%d]\n", first, run, first, i; run = 0 }
    /^  [A-Za-z]/ { printf "%3d%s\n", ++i, $0; next }
    { print }
    END { if (run) printf "%3d  [%d Write/Edit calls to scratchpad, #%d-#%d]\n", first, run, first, i }'
  echo
done
