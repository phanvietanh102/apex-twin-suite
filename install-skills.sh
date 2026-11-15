#!/usr/bin/env bash
# ==============================================================================
# APEX Twin Suite — local installer (macOS / Linux / WSL / Git Bash)
# Installs the two skills, `apex` and `apex-review`, into every supported host
# on this machine. Each target is replaced cleanly, and the names used before
# v4.5 are removed so the old and new skills never run side by side.
# Prefer installing from the GitHub link (see README) for auto-updates.
# ==============================================================================

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS=("apex" "apex-review")
OLD_SKILLS=("idea-to-product-apex" "product-workspace-reviewer-apex")   # names before v4.5
OLD_COMMANDS=("apex" "apex-review" "idea-to-product" "review-product" "apex-lean" "apex-improve")
SKILL_ROOTS=(
    "$REPO_ROOT/.agents/skills"        # workspace-local copies (git-ignored)
    "$REPO_ROOT/.claude/skills"
    "$HOME/.claude/skills"             # Claude Code / Claude Desktop
    "$HOME/.codex/skills"              # Codex
    "$HOME/.gemini/config/skills"      # Antigravity
    "$HOME/.gemini/config/plugins/apex-twin-suite/skills"
)

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

for ROOT in "${SKILL_ROOTS[@]}"; do
    for OLD in "${OLD_SKILLS[@]}"; do
        if [ -d "$ROOT/$OLD" ]; then
            rm -rf "$ROOT/$OLD"
            echo "[CLEAN] Removed old skill name: $ROOT/$OLD"
        fi
    done
    for SKILL in "${SKILLS[@]}"; do
        install_skill "$REPO_ROOT/skills/$SKILL" "$ROOT/$SKILL"
    done
done
echo "[OK] Installed skills: ${SKILLS[*]}"

# The skills are invoked directly as /apex and /apex-review. Remove the command
# files earlier versions installed, but only those that point at the old skill names.
for CMD in "${OLD_COMMANDS[@]}"; do
    FILE="$HOME/.claude/commands/$CMD.md"
    if [ -f "$FILE" ] && grep -q -e "idea-to-product-apex" -e "product-workspace-reviewer-apex" "$FILE"; then
        rm -f "$FILE"
        echo "[CLEAN] Removed old command file: $FILE"
    fi
done

# Antigravity plugin manifest and logo; drop the plugin folder used before v4.5.
AGY_PLUGIN="$HOME/.gemini/config/plugins/apex-twin-suite"
rm -rf "$HOME/.gemini/config/plugins/idea-to-product-apex"
mkdir -p "$AGY_PLUGIN/assets"
cp "$REPO_ROOT/plugin.json" "$AGY_PLUGIN/plugin.json"
cp "$REPO_ROOT/assets/logo.svg" "$AGY_PLUGIN/assets/logo.svg"

echo "======================================================================"
echo "  DONE. Restart your host, then use /apex and /apex-review."
echo "======================================================================"
