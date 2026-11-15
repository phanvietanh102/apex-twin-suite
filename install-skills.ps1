#Requires -Version 5.1
<#
.SYNOPSIS
    APEX Twin Suite - local installer (Windows).
    Installs the two skills, `apex` and `apex-review`, into every supported host
    on this machine. Each target is replaced cleanly, and the names used before
    v4.5 are removed so the old and new skills never run side by side.
    Prefer installing from the GitHub link (see README) for auto-updates.
    Targets:
      - Workspace copies (.agents/skills and .claude/skills, both git-ignored)
      - Claude Code / Claude Desktop  (~/.claude/skills)
      - Codex                         (~/.codex/skills)
      - VS Code user prompts          (%APPDATA%\Code\User\prompts)
      - Antigravity                   (~/.gemini/config/skills and plugins)
      - Upload archives for the claude.ai chat (./dist, git-ignored)
#>

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Skills = @("apex", "apex-review")
$OldSkills = @("idea-to-product-apex", "product-workspace-reviewer-apex")   # names before v4.5
$OldCommands = @("apex", "apex-review", "idea-to-product", "review-product", "apex-lean", "apex-improve")
$SkillRoots = @(
    (Join-Path $RepoRoot ".agents\skills"),
    (Join-Path $RepoRoot ".claude\skills"),
    (Join-Path $HOME ".claude\skills"),
    (Join-Path $HOME ".codex\skills"),
    (Join-Path $HOME ".gemini\config\skills"),
    (Join-Path $HOME ".gemini\config\plugins\apex-twin-suite\skills")
)

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

foreach ($Root in $SkillRoots) {
    foreach ($Old in $OldSkills) {
        $OldPath = Join-Path $Root $Old
        if (Test-Path $OldPath) {
            Remove-Item $OldPath -Recurse -Force
            Write-Host "[CLEAN] Removed old skill name: $OldPath" -ForegroundColor Yellow
        }
    }
    foreach ($SkillName in $Skills) {
        Install-Skill (Join-Path $RepoRoot "skills\$SkillName") (Join-Path $Root $SkillName)
    }
}
Write-Host "[OK] Installed skills: $($Skills -join ', ')" -ForegroundColor Green

# The skills are invoked directly as /apex and /apex-review. Remove the command
# files earlier versions installed, but only those that point at the old skill names.
foreach ($Cmd in $OldCommands) {
    $File = Join-Path $HOME ".claude\commands\$Cmd.md"
    if ((Test-Path $File) -and (Select-String -Path $File -Pattern "idea-to-product-apex|product-workspace-reviewer-apex" -Quiet)) {
        Remove-Item $File -Force
        Write-Host "[CLEAN] Removed old command file: $File" -ForegroundColor Yellow
    }
}

# VS Code user prompts
if ($env:APPDATA) {
    $VsCodePromptsDir = Join-Path $env:APPDATA "Code\User\prompts"
    New-Item -ItemType Directory -Force -Path $VsCodePromptsDir | Out-Null
    foreach ($Old in $OldSkills) {
        $OldPrompt = Join-Path $VsCodePromptsDir "$Old.prompt.md"
        if (Test-Path $OldPrompt) { Remove-Item $OldPrompt -Force }
    }
    foreach ($SkillName in $Skills) {
        Copy-Item -Path (Join-Path $RepoRoot "skills\$SkillName\SKILL.md") -Destination (Join-Path $VsCodePromptsDir "$SkillName.prompt.md") -Force
    }
}

# Upload archives for the claude.ai chat, built from the clean global copies
$DistDir = Join-Path $RepoRoot "dist"
New-Item -ItemType Directory -Force -Path $DistDir | Out-Null
foreach ($SkillName in $Skills) {
    $ZipPath = Join-Path $DistDir "$SkillName-claude-desktop.zip"
    if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }
    Compress-Archive -Path (Join-Path $HOME ".claude\skills\$SkillName") -DestinationPath $ZipPath -Force
}

# Antigravity plugin manifest and logo; drop the plugin folder used before v4.5.
$OldAgyPlugin = Join-Path $HOME ".gemini\config\plugins\idea-to-product-apex"
if (Test-Path $OldAgyPlugin) { Remove-Item $OldAgyPlugin -Recurse -Force }
$AgyPlugin = Join-Path $HOME ".gemini\config\plugins\apex-twin-suite"
New-Item -ItemType Directory -Force -Path (Join-Path $AgyPlugin "assets") | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "plugin.json") -Destination (Join-Path $AgyPlugin "plugin.json") -Force
Copy-Item -Path (Join-Path $RepoRoot "assets\logo.svg") -Destination (Join-Path $AgyPlugin "assets\logo.svg") -Force

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  DONE. Restart your host, then use /apex and /apex-review." -ForegroundColor Green
Write-Host "  Upload archives for the claude.ai chat are in: $DistDir" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan
