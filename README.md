<div align="center">

<img src="./assets/logo.svg" alt="APEX Twin Suite Logo" width="110" height="110" />

# 🚀 APEX Twin Engine Suite (`v3.5`)
### **From Raw Idea to 12-Month Evergreen Product — And Forensic Brownfield Evolution**
*The Multi-Domain C-Suite AI Harness for Claude Desktop, Claude Code & Google Antigravity*

[![Version](https://img.shields.io/badge/version-3.5.0--twin-6366F1?style=for-the-badge)](./CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge)](./LICENSE)
[![Hosts](https://img.shields.io/badge/Hosts-Claude_Desktop_%7C_Claude_Code_%7C_Antigravity-8B5CF6?style=for-the-badge)](#🛠️-1-click-installation--setup)
[![Domains](https://img.shields.io/badge/Domains-7_Industries_(SaaS_•_Construction_•_SEO_•_E--Com_•_Ops)-EC4899?style=for-the-badge)](#🌐-7-universal-domain-adapters)
[![Evergreen](https://img.shields.io/badge/Guarantee-12--Month_Zero--Rewrite-F59E0B?style=for-the-badge)](#🏛️-the-6-core-innovations)

[**📖 Architecture Whitepaper**](./DEEPSEARCH-ARCHITECTURE-WHITEPAPER.md) • [**💼 Executive Pitch Deck**](./EXECUTIVE-PITCH-DECK.md) • [**📊 vs. Superpowers / BMAD / Spec-Kit**](#-head-to-head-comparison) • [**⚡ 1-Click Install**](#🛠️-1-click-installation--setup)

</div>

---

## 💡 Why APEX Twin Suite Exists

**90% of AI-built projects collapse within 30 to 60 days**—not because foundation models lack coding or writing ability, but because of **4 Systemic AI Failure Modes**:

1. **The Prompt Ceiling & Sycophancy Trap:** By default, LLMs obey user prompts uncritically (*Premature Convergence*). When a user is not a domain veteran, the output is permanently capped by the user's own blind spots instead of incorporating top-1% industry standards.
2. **The Anchoring vs. Ambiguity Dilemma:** Existing discovery skills either ask vague open-ended questions (paralyzing beginners who *"have an idea but don't know where to start"*) or force 3 narrow multiple-choice options (suppressing a founder's contrarian secret via *Anchoring Bias*).
3. **Software-Only Myopia:** Popular frameworks (`obra/superpowers`, `BMAD-METHOD`, `github/spec-kit`) are 95% hardcoded for software engineering repositories. They fail when applied to **Construction, Real Estate, SEO/AIO (Generative Engine Optimization), E-Commerce, Invoicing, or Enterprise Operations**.
4. **Month-2 Architectural Rot & Context Bloat:** Hardcoded prices, tax rates, business rules, and prompts get tangled inside core logic; historical customer records get overwritten during updates; and heavy process prompts dilute the LLM's output token budget during implementation.

---

## ✨ The Solution: Two 100%-Symmetric Twin Engines

**APEX Twin Suite (`v3.5`)** provides two equal-caliber, cross-synchronized engines—one for **Greenfield creation (`0 -> 1 -> 12M`)** and one for **Brownfield forensic evolution (`1 -> 10x -> 12M`)**:

| Engine | Skill Package & Triggers | Core Mission |
| :--- | :--- | :--- |
| **🟢 Engine 1: Greenfield (A-to-Z Build)** | **[`idea-to-product-apex`](./skills/idea-to-product-apex/SKILL.md)**<br>`/idea-to-product` • `/apex` • `/apex-lean` | Takes a raw 1-sentence seed idea $\rightarrow$ runs **Dual-Mode Hybrid Elicitation** $\rightarrow$ injects **Johari Unknown-Unknowns & +30% Kano Delighters** $\rightarrow$ passes a **6-Role C-Suite Red-Team** $\rightarrow$ builds a **3-Tier, 12-Month Evergreen Product**. |
| **🔵 Engine 2: Brownfield (Forensic Review)** | **[`product-workspace-reviewer-apex`](./skills/product-workspace-reviewer-apex/SKILL.md)**<br>`/review-product` • `/apex-review` • `/audit-workspace` | Scans an **existing Product, App, or chaotic Workspace** via [`xray_scanner.py`](./skills/product-workspace-reviewer-apex/scripts/xray_scanner.py) $\rightarrow$ maps **Green/Yellow/Red Blast-Radius Zones** $\rightarrow$ plugs **4 Silent Leaks** $\rightarrow$ upgrades via non-destructive **Strangler-Fig** with **100% Behavioral Parity**. |

> **Multilingual Native Execution:** While the codebase, specifications, and skill instructions are written in clean English for optimal LLM token efficiency, the engines automatically converse and generate user-facing deliverables in **whatever language the user speaks** (English, Vietnamese, Japanese, Spanish, etc.).

---

## 🏛️ The 6 Core Innovations

### 1. Dual-Mode Hybrid Elicitation (Eliminating Anchoring Bias)
Every discovery turn combines **three cognitive layers**:
* **Layer A — Open Contrarian Excavation:** Extracts the founder's unique insight, unfair advantage, or contrarian idea *outside* the LLM's statistical average.
* **Layer B — Brutal Socratic Stress-Testing:** Challenges edge cases, operational bottlenecks, and failure modes (inspired by `/grill-me` and `superpowers`).
* **Layer C — AI Benchmark Matrix (Options A/B/C + Wildcard D):** Provides 3 battle-tested industry options as a safety net for beginners, plus **Option D (Custom/Hybrid Vision)**.

### 2. Johari Quadrant-4 Blind Spots & +30% Kano Delight Injection
Before locking scope, the engine maps at least **4 Industry Unknown-Unknowns** (regulatory traps, unit-economics killers, schema drift) and injects **20–30% asymmetric Kano Delighters**—features that require $<20\%$ marginal build effort while multiplying perceived value by $10\times$.

### 3. 6-Role C-Suite Council with Subagent Isolation & Deduction Scoring
Proposals and existing workspaces are audited by a **6-Persona Executive Council**:
* **CPO (Product & Cognitive Walkthrough)** • **CTO (Systems & Blast-Radius Architect)** • **VP of Domain Strategy** • **CFO (FinOps & Unit Economics)** • **CRO/COO (Risk, Security & Bus-Factor-1 Ops)** • **Devil's Advocate Customer**.
* **Anti-Sycophancy Enforcement:** Requires frontier high-reasoning models (`Claude Opus/Sonnet Thinking`, `Gemini Pro/Argon High`), delegates critique to an **isolated Subagent Critic** when supported, mandates quantitative deliverables (FMEA tables, Unit Economics formulas), and applies **Adversarial Deduction Scoring** (must uncover $\ge 3$ concrete flaws in Pass 1).

### 4. Shift-Left Stage Gates (`Gate 1..6`) & Executable Anti-Stub Verification
Never wait until Step 6 to discover an error made in Step 2:
* Automated Python auditors ([`fitness_audit.py`](./skills/idea-to-product-apex/scripts/fitness_audit.py) and [`review_gate_audit.py`](./skills/product-workspace-reviewer-apex/scripts/review_gate_audit.py)) enforce `--gate 1` through `--gate 6` after every phase.
* During implementation (Phase 5), `--scan-code` / `--scan-target` scans all source files to **block unfinished `TODO`s, `FIXME`s, `NotImplementedError`s, and fake mock arrays**, enforcing real unit tests and **Behavioral Parity Regression Tests**.

### 5. Zero-Bloat Phase-Isolated Context Loading (95% Build Token Budget)
To prevent complex process instructions from degrading code/deliverable quality (*Transformer Attention Dilution*):
* The agent loads **only** the reference module for the current active phase (`01`..`06`).
* During Phase 5 (Implementation/Refactoring), philosophical discovery docs are dropped from context so **95% of token capacity goes directly into complete, production-grade output**.
* Supports **3 Adaptive Rigor Modes**: `LEAN` (1 compact spec file + immediate build), `STANDARD`, and `DEEP-ENTERPRISE`.

### 6. The 12-Month Evergreen Guarantee (3-Tier Decoupling & 5-Zone Hygiene)
Every product and upgraded workspace is engineered to run for **at least 365 days without structural rewrites**:
* **Tier A (Immutable Core Logic)** is strictly separated from **Tier B (2-Minute Editable Configs/Prices/Rules/Prompts)** and **Tier C (UI/Export Adapters)**.
* **Red-Zone Snapshot Isolation:** Historical invoices, quotes, and customer records are saved as immutable snapshots—updating next month's prices never corrupts past records.
* **5-Zone Workspace Taxonomy:** Standardizes directories into `00-CONFIG-AND-TEMPLATES`, `01-ACTIVE-OPERATIONS`, `02-CORE-SYSTEM-AND-TOOLS`, `03-IMMUTABLE-ARCHIVE`, and `04-EXPORTS-AND-DELIVERABLES`, paired with a **Day 1 $\rightarrow$ Day 30 $\rightarrow$ Day 90 $\rightarrow$ Day 180 $\rightarrow$ Day 365** operational playbook.

---

## 📊 Head-to-Head Comparison

| Enterprise & Engineering Criterion | `obra/superpowers` | `BMAD-METHOD` | `github/spec-kit` | 🏆 **APEX Twin Suite `v3.5`** |
| :--- | :---: | :---: | :---: | :---: |
| **Multi-Domain Adaptability (Beyond Software)** | ❌ Software Only | ❌ Software Agile | ❌ Software Specs | ✅ **7 Core Industries (`DOM-01`..`07`)** |
| **Dual-Mode Elicitation (Open Probe + A/B/C/D)** | ⚠️ Open Only | ⚠️ Rigid Forms | ❌ Manual Spec | ✅ **Open Probe + Grill-Me + A/B/C/D** |
| **Proactive Unknown-Unknowns & +30% Delight** | ❌ | ❌ | ❌ | ✅ **Johari Q4 + 30% Kano Delighters** |
| **6-Role C-Suite Council + Subagent Critic** | ⚠️ Code Review Only | ⚠️ Sequential Handoff | ❌ | ✅ **6 C-Suite Roles + Deduction Score** |
| **Shift-Left Stage Gates (`Gate 1..6`) & Anti-Stub** | ⚠️ TDD Only | ❌ | ❌ | ✅ **Python Gate & Anti-Stub Scanner** |
| **Zero-Bloat Context Isolation (95% Build Budget)** | ✅ Lightweight | ❌ Heavy Context Bloat | ✅ Lightweight | ✅ **Phase-Isolated + `LEAN` Mode** |
| **Symmetric Brownfield Workspace/App Reviewer** | ❌ | ⚠️ Partial | ❌ | ✅ **Full `xray_scanner.py` + Red-Zone Lock** |
| **12-Month Zero-Rewrite Architecture Guarantee** | ❌ | ❌ | ❌ | ✅ **3-Tier Config + Snapshot Isolation** |

---

## 🌐 7 Universal Domain Adapters

Both Twin Engines dynamically load specialized ontologies, blind-spot radars, KPIs, and verification gates across 7 domains:

* **`DOM-01` — Software, SaaS & AI Agents:** Modular monoliths, provider-agnostic LLM/API adapters, zero-stub TDD, live admin config panels.
* **`DOM-02` — Construction, Architecture & Real Estate:** Externalized material/labor price matrices (editable in 2 mins), instant BOQ/quote PDF generators, site photo taxonomy (`<ProjectCode>_<Client>`), stage-gate inspection checklists.
* **`DOM-03` — Content, SEO, AIO (GEO) & Digital Media:** Generative Engine Optimization (Entity-Attribute-Value tables, JSON-LD Schema.org), topical cluster hubs, E-E-A-T citation scorers, multi-channel content atomizers.
* **`DOM-04` — E-Commerce, Retail & Billing/Invoicing:** Dual-format pixel-perfect **PDF + Excel** invoice engines, immutable historical ledgers, customer price memory, real-time margin floor guards.
* **`DOM-05` — B2B Services, Agency & Internal Operations SOP:** Bus-Factor-1 elimination, 5-Zone Workspace hygiene, self-serve client diagnostic scorecards.
* **`DOM-06` — FinTech, EdTech, Legal & Healthcare:** Hybrid Deterministic Math + AI Explanation, immutable audit trails, effective-date rule versioning.
* **`DOM-07` — Hardware, IoT & Physical-Digital Hybrid:** Offline-first local queues, QR quick-diagnostics, backward-compatible payload schemas.

---

## 🛠️ 1-Click Installation & Setup

### Option A: Automated Cross-Platform Installer (Windows / macOS / Linux)

**Windows (PowerShell):**
```powershell
git clone https://github.com/phanvietanh102/apex-twin-suite.git
cd apex-twin-suite
powershell -ExecutionPolicy Bypass -File .\install-skills.ps1
```

**macOS / Linux / WSL (Bash):**
```bash
git clone https://github.com/phanvietanh102/apex-twin-suite.git
cd apex-twin-suite
chmod +x ./install-skills.sh && ./install-skills.sh
```
*Automatically installs both `idea-to-product-apex` and `product-workspace-reviewer-apex` into:*
* **Claude Code / Local Skills:** `~/.claude/skills/`
* **Google Antigravity Skills & Global Plugin:** `~/.gemini/config/skills/` & `~/.gemini/config/plugins/idea-to-product-apex/`
* **Workspace Local Skills:** `./.agents/skills/` & `./.claude/skills/`

### Option B: Direct ZIP Upload to Claude Desktop App UI
Download from [**GitHub Releases (`v3.5.0`)**](https://github.com/phanvietanh102/apex-twin-suite/releases/tag/v3.5.0) or `./dist/`, then in **Claude Desktop** go to **Settings $\rightarrow$ Capabilities / Skills $\rightarrow$ Upload a skill**:
* [`dist/idea-to-product-apex-claude-desktop.zip`](./dist/idea-to-product-apex-claude-desktop.zip) *(Greenfield A-to-Z Engine)*
* [`dist/product-workspace-reviewer-apex-claude-desktop.zip`](./dist/product-workspace-reviewer-apex-claude-desktop.zip) *(Brownfield Forensic Reviewer Engine)*

---

## ⚡ Slash Commands & CLI Tools

### 🟢 Engine 1: Greenfield A-to-Z Development (`idea-to-product-apex`)
* **`/idea-to-product [your idea]`** or **`/apex [your idea]`**: Full 6-Phase pipeline starting with Dual-Mode Discovery.
* **`/apex-lean [your idea]`**: Fast-track Zero-Bloat mode (1 compact spec + immediate verified build).
* **`/apex-redteam`**: Convene the 6-Role C-Suite Council to stress-test your concept.
* **CLI Blueprint Scaffolder & Shift-Left Gate Auditor:**
  ```bash
  python ./skills/idea-to-product-apex/scripts/init_project.py --dir "./my-project" --name "My Project" --domain "DOM-01"
  python ./skills/idea-to-product-apex/scripts/fitness_audit.py --dir "./my-project" --gate 6 --scan-code "./my-project"
  ```

### 🔵 Engine 2: Brownfield Product, App & Workspace Review (`product-workspace-reviewer-apex`)
* **`/review-product [path or description]`** or **`/apex-review`**:
  1. **Turn 1A (Silent X-Ray Snapshot):** Scans and records the objective baseline inventory (`xray_scanner.py`) with **zero premature fix proposals**.
  2. **Turn 1B (Root-Vision A-to-Z Interview):** Re-interviews the user from the root of their **Original Idea & Ultimate Product Vision** from scratch.
  3. **Turn 2 (4-Column Vision-vs-Reality Gap Matrix):** Cross-examines Root Vision vs. Current Workspace across **Keep & Protect (Green)**, **Realign & Refactor (Yellow)**, **Missing A-to-Z Build (Blue)**, and **+30% Kano Delighters (Rocket)**.
  4. **Turns 3–6 (Full A-to-Z Evolution):** Runs the complete `idea-to-product-apex` C-Suite Red-Team, 12M Evergreen 3-Tier Architecture, A-to-Z Build + Surgical Refactor, and Parity Verification!
* **`/audit-workspace`**: Clean up a chaotic folder (`v1`, `v2`, `final_copy`), quarantine Red-Zone historical records, and reorganize into the 5-Zone Taxonomy without breaking links.
* **CLI Forensic X-Ray Scanner & Review Gate Auditor:**
  ```bash
  python ./skills/product-workspace-reviewer-apex/scripts/xray_scanner.py --dir "./existing-workspace" --name "Existing System" --domain "DOM-04"
  python ./skills/product-workspace-reviewer-apex/scripts/review_gate_audit.py --dir "./existing-workspace" --gate 6 --scan-target "./existing-workspace"
  ```

---

## 📂 Repository Structure

```text
apex-twin-suite/
├── README.md                                   # Flagship English Documentation & Quickstart
├── DEEPSEARCH-ARCHITECTURE-WHITEPAPER.md       # DeepSearch Research & C-Suite Red-Team Whitepaper (EN)
├── EXECUTIVE-PITCH-DECK.md                     # Executive & Client Presentation Deck (EN)
├── CHANGELOG.md                                # Version History (v1.0 -> v3.5 Twin-Synchronized)
├── LICENSE                                     # MIT Open-Source License
├── plugin.json                                 # Antigravity / Claude Plugin Manifest
├── install-skills.ps1                          # 1-Click Windows PowerShell Installer
├── install-skills.sh                           # 1-Click macOS / Linux Bash Installer
├── dist/                                       # Ready-to-Upload ZIP Packages for Claude Desktop & Releases
└── skills/
    ├── idea-to-product-apex/                   # ENGINE 1: Greenfield A-to-Z Development (6 Refs + 2 Scripts)
    └── product-workspace-reviewer-apex/        # ENGINE 2: Brownfield Forensic Review & Upgrade (6 Refs + 2 Scripts)
```

---

## ⭐ Star & Share

If **APEX Twin Engine Suite** helped you turn an ambiguous idea into a resilient system—or rescued an existing codebase/workspace from operational debt—please give this repository a **⭐ Star** on GitHub!
