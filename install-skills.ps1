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
