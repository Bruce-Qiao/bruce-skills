#!/usr/bin/env bash
# Install all skills listed in skills.txt into ~/.claude/skills/
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="$HOME/.claude/skills"
LIST="$SCRIPT_DIR/skills.txt"

if [[ ! -f "$LIST" ]]; then
  echo "ERROR: $LIST not found." >&2
  exit 1
fi

mkdir -p "$TARGET"

installed=0
skipped=0
while IFS= read -r skill || [[ -n "$skill" ]]; do
  skill="${skill%%#*}"
  skill="$(echo "$skill" | xargs)"
  [[ -z "$skill" ]] && continue

  src="$SCRIPT_DIR/$skill"
  if [[ ! -d "$src" ]]; then
    echo "WARN: '$skill' listed in skills.txt but directory not found, skipping." >&2
    skipped=$((skipped + 1))
    continue
  fi

  echo "Installing $skill -> $TARGET/$skill"
  rm -rf "$TARGET/$skill"
  cp -r "$src" "$TARGET/$skill"
  installed=$((installed + 1))
done < "$LIST"

echo
echo "Done. Installed: $installed, skipped: $skipped."
echo "Restart Claude Code to load the new skills."
