#!/usr/bin/env bash
#
# install-hooks.sh — point this clone at the hooks/ directory in the repository.
#
# Hooks normally live in .git/hooks/, which is NOT pushed to GitHub. Setting
# core.hooksPath makes git read them from a tracked folder instead, so the hooks
# travel with the repository and every clone gets them after running this once.
#
# Usage (from the repository root):
#   ./hooks/install-hooks.sh
#
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

hooks_dir="hooks"

if [[ ! -d "$hooks_dir" ]]; then
  echo "No $hooks_dir/ directory found at $repo_root" >&2
  exit 1
fi

chmod +x "$hooks_dir"/pre-commit 2>/dev/null || true
git config core.hooksPath "$hooks_dir"

echo "Hooks installed."
echo "  core.hooksPath = $(git config core.hooksPath)"
echo "  active hooks   : $(ls "$hooks_dir" | grep -v install-hooks.sh | tr '\n' ' ')"
echo
echo "Current limits:"
echo "  PDFs  : $(( $(git config --int hooks.maxPdfSize 2>/dev/null || echo $((8*1024*1024))) / 1024 / 1024 )) MB"
echo "  other : $(( $(git config --int hooks.maxFileSize 2>/dev/null || echo $((5*1024*1024))) / 1024 / 1024 )) MB"
echo
echo "Change them with:  git config hooks.maxPdfSize \$((12*1024*1024))"
echo "Disable hooks with: git config --unset core.hooksPath"
