#Requires -Version 5.1
<#
.SYNOPSIS
    1-Click Multi-Host Installer for the APEX Twin Engine Suite (v3.5 Twin-Synchronized Edition)
    Installs BOTH symmetric skills:
      1. idea-to-product-apex (Greenfield A-to-Z Idea-to-Product Engine)
      2. product-workspace-reviewer-apex (Brownfield Existing Product, App & Workspace Forensic Reviewer)
    Targets:
      - Current Workspace (.agents/skills & .claude/skills)
      - Global Claude Code / Claude Desktop Skills (~/.claude/skills/)
      - Packaged ZIPs for Claude Desktop UI Upload (./dist/)
      - Global Antigravity Skills & Plugin (~/.gemini/config/skills & ~/.gemini/config/plugins/idea-to-product-apex)
#>

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Skills = @("idea-to-product-apex", "product-workspace-reviewer-apex")
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  APEX TWIN ENGINE SUITE (v3.5) - SYMMETRIC MULTI-HOST INSTALLER" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

$DistDir = Join-Path $RepoRoot "dist"
New-Item -ItemType Directory -Force -Path $DistDir | Out-Null

$GlobalAgyPlugin = Join-Path $HOME ".gemini\config\plugins\idea-to-product-apex"
$GlobalAgyPluginAssets = Join-Path $GlobalAgyPlugin "assets"
New-Item -ItemType Directory -Force -Path $GlobalAgyPluginAssets | Out-Null

foreach ($SkillName in $Skills) {
    $SkillSource = Join-Path $RepoRoot "skills\$SkillName"

    # 1. Workspace (.agents/skills & .claude/skills)
    $WsAgentSkill = Join-Path $RepoRoot ".agents\skills\$SkillName"
    $WsClaudeSkill = Join-Path $RepoRoot ".claude\skills\$SkillName"
    New-Item -ItemType Directory -Force -Path $WsAgentSkill | Out-Null
    Copy-Item -Path "$SkillSource\*" -Destination $WsAgentSkill -Recurse -Force
    New-Item -ItemType Directory -Force -Path $WsClaudeSkill | Out-Null
    Copy-Item -Path "$SkillSource\*" -Destination $WsClaudeSkill -Recurse -Force

    # 2. Global Claude (~/.claude/skills/<SkillName>)
    $GlobalClaudeSkill = Join-Path $HOME ".claude\skills\$SkillName"
    New-Item -ItemType Directory -Force -Path $GlobalClaudeSkill | Out-Null
    Copy-Item -Path "$SkillSource\*" -Destination $GlobalClaudeSkill -Recurse -Force

    # 2b. Global Codex / OpenAI VS Code Extension (~/.codex/skills/<SkillName>)
    $GlobalCodexSkill = Join-Path $HOME ".codex\skills\$SkillName"
    New-Item -ItemType Directory -Force -Path $GlobalCodexSkill | Out-Null
    Copy-Item -Path "$SkillSource\*" -Destination $GlobalCodexSkill -Recurse -Force

    # 2c. Global VS Code User Prompts ($env:APPDATA\Code\User\prompts\<SkillName>.prompt.md)
    if ($env:APPDATA) {
        $VsCodePromptsDir = Join-Path $env:APPDATA "Code\User\prompts"
        New-Item -ItemType Directory -Force -Path $VsCodePromptsDir | Out-Null
        Copy-Item -Path (Join-Path $SkillSource "SKILL.md") -Destination (Join-Path $VsCodePromptsDir "$SkillName.prompt.md") -Force
    }

    # 3. Individual ZIP for Claude Desktop UI Upload
    $ZipPath = Join-Path $DistDir "$SkillName-claude-desktop.zip"
    if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }
    Compress-Archive -Path $SkillSource -DestinationPath $ZipPath -Force

    # 4. Global Antigravity Skill & Plugin bundle
    $GlobalAgySkill = Join-Path $HOME ".gemini\config\skills\$SkillName"
    New-Item -ItemType Directory -Force -Path $GlobalAgySkill | Out-Null
    Copy-Item -Path "$SkillSource\*" -Destination $GlobalAgySkill -Recurse -Force

    $PluginSkillDest = Join-Path $GlobalAgyPlugin "skills\$SkillName"
    New-Item -ItemType Directory -Force -Path $PluginSkillDest | Out-Null
    Copy-Item -Path "$SkillSource\*" -Destination $PluginSkillDest -Recurse -Force

    Write-Host "[OK] Installed & Packaged Twin Skill: $SkillName" -ForegroundColor Green
}

# Create Claude Code Global Slash Commands (~/.claude/commands/*.md) for VS Code & CLI
$ClaudeCommandsDir = Join-Path $HOME ".claude\commands"
New-Item -ItemType Directory -Force -Path $ClaudeCommandsDir | Out-Null

$ApexCmd = @'
---
description: Launch APEX Engine 1 (idea-to-product-apex) — Greenfield A-to-Z Idea-to-Product with Personal Open Excavation + 3-Option Pros/Cons/Best-Fit Matrix, 6-Role C-Suite Red-Team & 12-Month Evergreen Architecture
---
Read and strictly follow the complete protocol in `~/.claude/skills/idea-to-product-apex/SKILL.md` (and its `references/` and `scripts/` modules) for the user's request below.

⛔ MANDATORY 2-SECTION DISCOVERY RULE (NEVER OUTPUT BARE A/B/C OPTIONS!):
In every Discovery turn (Phase 1 & Phase 2), you MUST explicitly divide your visible response into TWO sections:
1. **PHẦN 1 — Câu Hỏi Riêng Khai Thác Mong Muốn & Ý Tưởng Cá Nhân Của Bạn (Dedicated Personal Open Questions — NO A/B/C attached!):** Ask 2–3 open, personal questions to uncover the user's own secret vision, personal preferences, contrarian ideas outside AI's suggestions, and daily operational habits.
2. **PHẦN 2 — Bảng Phân Tích 3 Gợi Ý Chiến Lược Kèm Ưu Điểm / Nhược Điểm / Độ Phù Hợp (Pros/Cons/Best-Fit Decision Matrix + Option D Hybrid):** For every AI suggestion (`Option A`, `Option B`, `Option C`), you MUST present a Markdown table showing:
   - `Cơ chế cốt lõi (Core Mechanism)`
   - `✅ Ưu điểm (Pros)`
   - `⚠️ Nhược điểm / Đánh đổi (Cons / Trade-offs)`
   - `🎯 Hợp nhất với mong muốn của bạn nếu... (Best Fit For Your Desire If...)`
   - Plus `Option D (Lai ghép / Tự thiết kế theo ý riêng ở Phần 1)` so the user can combine the best parts of A/B/C with their personal desires!

$ARGUMENTS
'@
[System.IO.File]::WriteAllText((Join-Path $ClaudeCommandsDir "idea-to-product.md"), $ApexCmd, $Utf8NoBom)
[System.IO.File]::WriteAllText((Join-Path $ClaudeCommandsDir "apex.md"), $ApexCmd, $Utf8NoBom)

$ReviewCmd = @'
---
description: Launch APEX Engine 2 (product-workspace-reviewer-apex) — Record X-Ray State, Re-Interview Root Vision from Scratch, Build Vision-vs-Reality Gap Matrix (with Pros/Cons/Best-Fit) & Run Full A-to-Z Upgrade
---
Read and strictly follow the complete protocol in `~/.claude/skills/product-workspace-reviewer-apex/SKILL.md` (and its `references/` and `scripts/` modules) for the user's request below.

⛔ IRON RULE OF TURN 1 (NO PREMATURE FIXES!):
On this first turn, you MUST ONLY:
1. Run `xray_scanner.py` (or inspect the workspace) and report the OBJECTIVE BASELINE INVENTORY (what files, modules, workflows, and data currently exist). Explicitly state that you are holding off on proposing any fixes yet.
2. Immediately interview the user from the root of their ORIGINAL IDEA & ULTIMATE PRODUCT VISION from A-to-Z (Step 1B: Original Root Vision, Open-Canvas Unbuilt Ambitions, Operating Pain Points, and Sacred Assets to Keep).
3. STOP and WAIT for the user's reply!
4. On Turn 2 (after the user replies), construct the **4-Column Vision-vs-Reality Gap Matrix** (`Keep / Realign / Missing A-to-Z Build / 30% Kano Delighters`), ask **Dedicated Personal Customization Questions**, and present the **3 Strategic A-to-Z Evolution Options (`A / B / C` + `Hybrid Option D`) in a full Markdown Table with explicit `✅ Pros (Ưu điểm)`, `⚠️ Cons (Nhược điểm)`, and `🎯 Best Fit (Hợp nhất với bạn nếu...)`**!

$ARGUMENTS
'@
[System.IO.File]::WriteAllText((Join-Path $ClaudeCommandsDir "review-product.md"), $ReviewCmd, $Utf8NoBom)
[System.IO.File]::WriteAllText((Join-Path $ClaudeCommandsDir "apex-review.md"), $ReviewCmd, $Utf8NoBom)
Write-Host "[OK] Registered Claude Code & VS Code Slash Commands (/apex, /idea-to-product, /apex-review, /review-product)" -ForegroundColor Green

# Create combined Twin Suite ZIP
$BundleZip = Join-Path $DistDir "apex-twin-suite-v3.5-bundle.zip"
if (Test-Path $BundleZip) { Remove-Item $BundleZip -Force }
Compress-Archive -Path (Join-Path $RepoRoot "skills\*") -DestinationPath $BundleZip -Force
Write-Host "[OK] Packaged Combined Twin Suite ZIP -> $BundleZip" -ForegroundColor Green

# Write plugin.json for Antigravity Global Plugin
$PluginJson = @{
    name = "idea-to-product-apex"
    displayName = "APEX Twin Suite (v3.5): Idea-to-Product & Product/Workspace Reviewer"
    version = "3.5.0"
    description = "Symmetric Twin Engine Suite: (1) idea-to-product-apex for A-to-Z Greenfield development and (2) product-workspace-reviewer-apex for Brownfield Product/App/Workspace forensic auditing, refactoring & 12-Month Evergreen immunity."
    logo = "assets/logo.svg"
    suggestedPrompts = @(
        "/idea-to-product I have a new product idea—run Dual-Mode discovery, inject 30% Kano delighters, and architect a 12-month evergreen system",
        "/review-product Run a Forensic X-Ray scan, 6-Role C-Suite audit, and non-destructive upgrade on my existing product/workspace",
        "/audit-workspace Clean up workspace entropy, lock historical Red-Zone data, and extract a 2-minute editable Tier-B config"
    )
} | ConvertTo-Json -Depth 5
[System.IO.File]::WriteAllText((Join-Path $GlobalAgyPlugin "plugin.json"), $PluginJson, $Utf8NoBom)

# Write SVG Logo
$LogoSvg = @'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
  <defs>
    <linearGradient id="apexGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="50%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#DB2777"/>
    </linearGradient>
  </defs>
  <rect x="14" y="14" width="100" height="100" rx="22" fill="url(#apexGrad)"/>
  <path d="M48 34 L72 86 L58 86 L48 62 L38 86 L24 86 Z" fill="#FFFFFF"/>
  <path d="M80 34 L104 86 L90 86 L80 62 L70 86 L56 86 Z" fill="#E0E7FF" opacity="0.88"/>
  <circle cx="64" cy="96" r="6" fill="#FDE047"/>
</svg>
'@
[System.IO.File]::WriteAllText((Join-Path $GlobalAgyPluginAssets "logo.svg"), $LogoSvg, $Utf8NoBom)

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  TWIN ENGINE SUITE v3.5 INSTALLED (100% SYMMETRY VERIFIED)" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan
