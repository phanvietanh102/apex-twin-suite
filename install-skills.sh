#!/usr/bin/env bash
# ==============================================================================
# APEX Twin Suite — local installer (macOS / Linux / WSL / Git Bash)
# Copies both skills and the slash commands into every supported host on this
# machine. Each target is replaced cleanly, so files removed upstream do not
# linger. Prefer installing from the GitHub link (see README) for auto-updates.
# ==============================================================================

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS=("idea-to-product-apex" "product-workspace-reviewer-apex")
AGY_PLUGIN="$HOME/.gemini/config/plugins/idea-to-product-apex"

# Replace a target skill folder with a clean copy (no Python caches).
install_skill() {
    local src="$1" dest="$2"
    rm -rf "$dest"
    mkdir -p "$dest"
    cp -R "$src/." "$dest/"
    find "$dest" -type d -name "__pycache__" -prune -exec rm -rf {} +
}

echo "======================================================================"
echo "  APEX TWIN SUITE - LOCAL INSTALLER"
echo "======================================================================"

for SKILL in "${SKILLS[@]}"; do
    SRC="$REPO_ROOT/skills/$SKILL"

    # Workspace-local copies (git-ignored) for hosts that read project skills
    install_skill "$SRC" "$REPO_ROOT/.agents/skills/$SKILL"
    install_skill "$SRC" "$REPO_ROOT/.claude/skills/$SKILL"

    # Global: Claude Code / Claude Desktop, Codex, Antigravity
    install_skill "$SRC" "$HOME/.claude/skills/$SKILL"
    install_skill "$SRC" "$HOME/.codex/skills/$SKILL"
    install_skill "$SRC" "$HOME/.gemini/config/skills/$SKILL"
    install_skill "$SRC" "$AGY_PLUGIN/skills/$SKILL"

    echo "[OK] Installed skill: $SKILL"
done

# Slash commands for Claude Code (/apex, /idea-to-product, /apex-lean,
# /apex-review, /review-product, /apex-improve)
mkdir -p "$HOME/.claude/commands"
cp "$REPO_ROOT"/commands/*.md "$HOME/.claude/commands/"
echo "[OK] Installed slash commands -> ~/.claude/commands"

# Antigravity plugin manifest and logo
mkdir -p "$AGY_PLUGIN/assets"
cp "$REPO_ROOT/plugin.json" "$AGY_PLUGIN/plugin.json"
cp "$REPO_ROOT/assets/logo.svg" "$AGY_PLUGIN/assets/logo.svg"

echo "======================================================================"
echo "  DONE. Restart your host (Claude Code, Codex, Antigravity) to load it."
echo "======================================================================"
