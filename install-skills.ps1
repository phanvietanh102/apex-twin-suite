#Requires -Version 5.1
<#
.SYNOPSIS
    APEX Twin Suite - local installer (Windows).
    Copies both skills and the slash commands into every supported host on this
    machine. Each target is replaced cleanly, so files removed upstream do not
    linger. Prefer installing from the GitHub link (see README) for auto-updates.
    Targets:
      - Workspace copies (.agents/skills and .claude/skills, both git-ignored)
      - Claude Code / Claude Desktop  (~/.claude/skills, ~/.claude/commands)
      - Codex                         (~/.codex/skills)
      - VS Code user prompts          (%APPDATA%\Code\User\prompts)
      - Antigravity                   (~/.gemini/config/skills and plugins)
      - Upload archives for the claude.ai chat (./dist, git-ignored)
#>

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Skills = @("idea-to-product-apex", "product-workspace-reviewer-apex")

# Replace a target skill folder with a clean copy (no Python caches).
function Install-Skill {
    param([string]$Source, [string]$Destination)
    if (Test-Path $Destination) { Remove-Item $Destination -Recurse -Force }
    New-Item -ItemType Directory -Force -Path $Destination | Out-Null
    Copy-Item -Path "$Source\*" -Destination $Destination -Recurse -Force
    Get-ChildItem -Path $Destination -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue |
        Remove-Item -Recurse -Force
}

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  APEX TWIN SUITE - LOCAL INSTALLER" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

$DistDir = Join-Path $RepoRoot "dist"
New-Item -ItemType Directory -Force -Path $DistDir | Out-Null
$AgyPlugin = Join-Path $HOME ".gemini\config\plugins\idea-to-product-apex"

foreach ($SkillName in $Skills) {
    $SkillSource = Join-Path $RepoRoot "skills\$SkillName"

    # Workspace-local copies for hosts that read project skills
    Install-Skill $SkillSource (Join-Path $RepoRoot ".agents\skills\$SkillName")
    Install-Skill $SkillSource (Join-Path $RepoRoot ".claude\skills\$SkillName")

    # Global: Claude Code / Claude Desktop, Codex, Antigravity
    Install-Skill $SkillSource (Join-Path $HOME ".claude\skills\$SkillName")
    Install-Skill $SkillSource (Join-Path $HOME ".codex\skills\$SkillName")
    Install-Skill $SkillSource (Join-Path $HOME ".gemini\config\skills\$SkillName")
    Install-Skill $SkillSource (Join-Path $AgyPlugin "skills\$SkillName")

    # VS Code user prompt
    if ($env:APPDATA) {
        $VsCodePromptsDir = Join-Path $env:APPDATA "Code\User\prompts"
        New-Item -ItemType Directory -Force -Path $VsCodePromptsDir | Out-Null
        Copy-Item -Path (Join-Path $SkillSource "SKILL.md") -Destination (Join-Path $VsCodePromptsDir "$SkillName.prompt.md") -Force
    }

    # Upload archive for the claude.ai chat, built from the clean global copy
    $ZipPath = Join-Path $DistDir "$SkillName-claude-desktop.zip"
    if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }
    Compress-Archive -Path (Join-Path $HOME ".claude\skills\$SkillName") -DestinationPath $ZipPath -Force

    Write-Host "[OK] Installed skill: $SkillName" -ForegroundColor Green
}

# Slash commands for Claude Code (/apex, /idea-to-product, /apex-lean,
# /apex-review, /review-product, /apex-improve). They only point at the skills,
# so the skills stay the single source of behaviour.
$ClaudeCommandsDir = Join-Path $HOME ".claude\commands"
New-Item -ItemType Directory -Force -Path $ClaudeCommandsDir | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "commands\*.md") -Destination $ClaudeCommandsDir -Force
Write-Host "[OK] Installed slash commands -> $ClaudeCommandsDir" -ForegroundColor Green

# Antigravity plugin manifest and logo
New-Item -ItemType Directory -Force -Path (Join-Path $AgyPlugin "assets") | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "plugin.json") -Destination (Join-Path $AgyPlugin "plugin.json") -Force
Copy-Item -Path (Join-Path $RepoRoot "assets\logo.svg") -Destination (Join-Path $AgyPlugin "assets\logo.svg") -Force

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  DONE. Restart your host (Claude Code, Codex, Antigravity) to load it." -ForegroundColor Green
Write-Host "  Upload archives for the claude.ai chat are in: $DistDir" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan
