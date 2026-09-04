#!/usr/bin/env bash
set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Configuration des garde-fous Git..."
cd "$ROOT_DIR"

# 1. Configurer les hooks Git du dépôt
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit

# 2. Configurer les hooks Claude Code si présents
if [ -f ".claude/hooks/block-dangerous-git.sh" ]; then
  chmod +x .claude/hooks/block-dangerous-git.sh
fi

echo "✅ Garde-fous Git activés (.githooks/pre-commit et .claude/hooks/)."
