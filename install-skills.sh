#!/usr/bin/env bash
# ==============================================================================
# APEX Twin Engine Suite (v3.5) — Cross-Platform Installer (macOS / Linux / WSL)
# Installs BOTH symmetric skills:
#   1. idea-to-product-apex (Greenfield A-to-Z Idea-to-Product Engine)
#   2. product-workspace-reviewer-apex (Brownfield Product/App/Workspace Reviewer)
# ==============================================================================

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS=("idea-to-product-apex" "product-workspace-reviewer-apex")

echo "======================================================================"
echo "  APEX TWIN ENGINE SUITE (v3.5) - MACOS / LINUX / WSL INSTALLER"
echo "======================================================================"

mkdir -p "$REPO_ROOT/dist"
mkdir -p "$HOME/.claude/skills"
mkdir -p "$HOME/.gemini/config/skills"
mkdir -p "$HOME/.gemini/config/plugins/idea-to-product-apex/skills"
mkdir -p "$HOME/.gemini/config/plugins/idea-to-product-apex/assets"

for SKILL in "${SKILLS[@]}"; do
    SRC="$REPO_ROOT/skills/$SKILL"

    # 1. Workspace local skills
    mkdir -p "$REPO_ROOT/.agents/skills/$SKILL"
    cp -R "$SRC/"* "$REPO_ROOT/.agents/skills/$SKILL/"
    mkdir -p "$REPO_ROOT/.claude/skills/$SKILL"
    cp -R "$SRC/"* "$REPO_ROOT/.claude/skills/$SKILL/"

    # 2. Global Claude Code / Claude Desktop skills
    mkdir -p "$HOME/.claude/skills/$SKILL"
    cp -R "$SRC/"* "$HOME/.claude/skills/$SKILL/"

    # 3. Global Antigravity skills & plugin
    mkdir -p "$HOME/.gemini/config/skills/$SKILL"
    cp -R "$SRC/"* "$HOME/.gemini/config/skills/$SKILL/"
    mkdir -p "$HOME/.gemini/config/plugins/idea-to-product-apex/skills/$SKILL"
    cp -R "$SRC/"* "$HOME/.gemini/config/plugins/idea-to-product-apex/skills/$SKILL/"

    echo "[OK] Installed Twin Skill: $SKILL"
done

if [ -f "$REPO_ROOT/plugin.json" ]; then
    cp "$REPO_ROOT/plugin.json" "$HOME/.gemini/config/plugins/idea-to-product-apex/plugin.json"
fi

echo "======================================================================"
echo "  INSTALLATION COMPLETE! READY FOR CLAUDE & ANTIGRAVITY."
echo "======================================================================"
