<div align="center">

<img src="./assets/logo.svg" alt="APEX Twin Suite Logo" width="110" height="110" />

# 🚀 APEX Twin Engine Suite (`v3.7`)
### **Stop Letting AI Build the Wrong Thing Fast — Or Patch Your Workspace Blindly**
*The Multi-Domain C-Suite AI Harness for Claude Code, VS Code, Cursor, Codex & Google Antigravity*

[![Version](https://img.shields.io/badge/version-3.7.0--twin-6366F1?style=for-the-badge)](./CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge)](./LICENSE)
[![Hosts](https://img.shields.io/badge/Auto--Sync-Claude_Code_%7C_VS_Code_%7C_Cursor_%7C_Codex_%7C_Antigravity-8B5CF6?style=for-the-badge)](#⚡-10-second-install-via-github-link-auto-updates)
[![Domains](https://img.shields.io/badge/Domains-7_Industries_(SaaS_•_Construction_•_SEO_•_E--Com_•_Ops)-EC4899?style=for-the-badge)](#🌐-7-universal-domain-adapters-what-you-dont-know-to-ask-ai)
[![Evergreen](https://img.shields.io/badge/Guarantee-12--Month_Zero--Rewrite-F59E0B?style=for-the-badge)](#🏛️-the-6-architectural-pillars)

[**⚡ 10-Second GitHub Link Install**](#⚡-10-second-install-via-github-link-auto-updates) • [**🔍 Live Experience Preview**](#-see-the-psychological--engineering-difference-in-30-seconds) • [**📊 vs. Superpowers / BMAD / Spec-Kit**](#-head-to-head-comparison) • [**📖 Whitepaper**](./DEEPSEARCH-ARCHITECTURE-WHITEPAPER.md) • [**💼 Executive Pitch Deck**](./EXECUTIVE-PITCH-DECK.md)

> ⭐ **Pro-Tip (Save Yourself Weeks of Rewrites):** Click **Star** in the top-right corner now so you always have both the **Greenfield Builder (`/idea-to-product`)** and the **Root-Vision Workspace Reviewer (`/review-product`)** bookmarked for your next project.

</div>

---

## 🛑 Have You Experienced These 3 Painful AI Moments?

If you have used Claude, Cursor, ChatGPT, or Gemini to build a project or clean up an existing workspace over the last few months, you have likely hit **three silent walls**:

1. **The "Yes-Man" Trap (Premature Convergence):**
   You share an idea. The AI says *"Great idea!"* and immediately generates 1,000 lines of code or text—without challenging your blind spots. Three days later, you realize the architecture is a dead end, prices/rules are hardcoded everywhere, and `// TODO` stubs are hiding in critical paths.
2. **The "3-Option Prison" (Choice Paralysis Without Trade-Offs):**
   Even when a skill asks questions, it traps you inside 3 bare multiple-choice options (`Option A / B / C`)—**never asking for your personal secret vision outside those 3 options**, and **never explaining the Pros, Cons, or Best-Fit of each option**. You are forced to guess blindly.
3. **The "Premature Patching" Wrecking Ball (`Sửa Ngọn Quên Gốc`):**
   When you point an AI at an **existing workspace or half-built app**, it immediately proposes code patches for whatever files happen to be in the folder on Turn 1—never stopping to ask: *"Wait, what was your **Original Root Vision** from A to Z, and what did this workspace fail to build in the first place?"*

---

## 🔄 Cognitive Contrast: Standard AI vs. Your AI on `APEX Twin Suite`

| Moment in Your Workflow | ❌ Standard AI / Typical Skills | ✅ **APEX Twin Engine Suite (`v3.7`)** |
| :--- | :--- | :--- |
| **When You Pitch a New Idea** | Guesses requirements or locks you into 3 bare options (`A/B/C`) with zero trade-off analysis. | **2-Section Personal + Pros/Cons Discovery:**<br>1️⃣ Asks **Personal Open Questions** first to capture *your* unique vision.<br>2️⃣ Presents a **3-Option Decision Matrix** with explicit **`✅ Pros`**, **`⚠️ Cons`**, and **`🎯 Best Fit If You Want...`** + **Option D (Hybrid)**. |
| **When You Audit an Existing Workspace** | Immediately proposes superficial fixes on Turn 1 without knowing your original goal. | **Turn-1 Hard Stop Gate:**<br>1️⃣ Records an objective X-Ray (`xray_scanner.py`) with **zero premature fixes**.<br>2️⃣ Re-interviews your **Original Root Vision** from scratch.<br>3️⃣ Builds a **4-Column Vision-vs-Reality Gap Matrix** (`Keep` \| `Realign` \| `Missing A-to-Z Build` \| `+30% Kano Delighters`) and runs a full A-to-Z upgrade! |
| **Domain Knowledge Ceiling** | Limited to what *you* already know to ask for; software-centric. | Proactively injects **$\ge 4$ Johari Unknown-Unknowns** + **30% Asymmetric Kano Delighters** across **7 Industries** (SaaS, Construction/BOQ, SEO/AIO, E-Com/Invoicing, B2B Ops, FinTech, IoT). |
| **Quality & Anti-Sycophancy** | Same AI thread praises its own plan; leaves `TODO` stubs in Step 5. | **6-Role C-Suite Red-Team Council** (via isolated Critic Subagent + Deduction Scoring from 100) + **4 Python CLI Gate Auditors** that mechanically block `TODO`/`FIXME` stubs at every step. |
| **Month-6 Survival** | Changing a price, tax rate, or prompt breaks historical records or requires a rewrite. | **12-Month Evergreen 3-Tier Architecture:** Tier-B **2-Minute Editable Config** + **Red-Zone Historical Snapshot Isolation** (changing Month-6 prices never alters Month-1 invoices). |

---

## ⚡ 10-Second Install via GitHub Link (Auto-Updates!)

Because this repository includes native multi-host plugin manifests ([`.claude-plugin/`](./.claude-plugin/marketplace.json), [`.antigravity-plugin/`](./.antigravity-plugin/plugin.json), [`.cursor-plugin/`](./.cursor-plugin/plugin.json), and [`.codex-plugin/`](./.codex-plugin/plugin.json)), **you never need to manually copy files or upload `.zip` archives in your IDE.**

### 1. Direct GitHub Auto-Sync in Claude Code & VS Code (Recommended)
Run these two commands inside **Claude Code** (CLI or VS Code Extension):
```text
/plugin marketplace add phanvietanh102/apex-twin-suite
/plugin install apex-twin-suite@apex-twin-suite
```
*Done! Whenever `phanvietanh102/apex-twin-suite` is updated on GitHub, your environment syncs the latest version automatically.*

### 2. One-Command Multi-Host Installer (Claude + VS Code + Codex + Antigravity)
**Windows (PowerShell):**
```powershell
git clone https://github.com/phanvietanh102/apex-twin-suite.git
cd apex-twin-suite
powershell -ExecutionPolicy Bypass -File .\install-skills.ps1
```
**macOS / Linux / WSL:**
```bash
git clone https://github.com/phanvietanh102/apex-twin-suite.git
cd apex-twin-suite
chmod +x ./install-skills.sh && ./install-skills.sh
```

> **Note for `claude.ai` Web Browser Users Only:** If you use the web chat interface at `claude.ai` (which only accepts `.zip` uploads under *Settings $\rightarrow$ Capabilities $\rightarrow$ Skills*), grab the pre-built archives from [**GitHub Releases**](https://github.com/phanvietanh102/apex-twin-suite/releases/tag/v3.5.0).

---

## 🔍 See the Psychological & Engineering Difference in 30 Seconds

### 🟢 Engine 1: `idea-to-product-apex` (Greenfield A-to-Z Builder)
Trigger with `/idea-to-product [your idea]` or `/apex [your idea]`. Instead of rushing into half-baked code or trapping you in blind choices, the engine always opens with **Two Mandatory Discovery Sections**:

```markdown
### 💬 SECTION 1: Dedicated Personal Open Questions (Your Unique Vision First)
1. Core Desire & Signature Edge: Based on your personal intuition or domain experience, what is the ideal outcome you want this product to achieve? Is there a unique feature or secret workflow you have in mind that competitors miss?
2. Daily Operating Reality (Socratic Check): Who will operate this daily, how many minutes per day should it take at most, and what friction would cause you or your users to abandon it after 2 weeks?

### 🧭 SECTION 2: AI 3-Option Decision Matrix (With Explicit Pros, Cons & Best-Fit)
| Option | Core Mechanism | ✅ Pros | ⚠️ Cons / Trade-offs | 🎯 Best Fit For You If... |
| :--- | :--- | :--- | :--- | :--- |
| **Option A (Recommended)** | 3-Tier Automated Pipeline + 2-Min Config | • Eliminates 80% manual work<br>• 12-Month zero-rewrite | • Takes 1 extra slice to set up config schema | You want **fast time-to-value, high automation, and 12-month durability**. |
| **Option B (Lean Sprint)** | Single-file lightweight core | • Ships in 1 session<br>• Zero learning curve | • Manual steps remain at higher volume | You want **absolute simplicity today** and accept minor manual steps. |
| **Option C (10x Enterprise)** | Multi-agent autonomous suite | • Maximum scale & audit logs | • Higher setup & token overhead | You are building a **high-volume multi-user system from Day 1**. |
| **Option D (Your Hybrid)** | Custom mix of Section 1 + A/B/C | • 100% tailored to your personal taste | • Requires 1 Socratic alignment pass | You want **your own idea in Section 1 + the best parts of A & C**. |
```

### 🔵 Engine 2: `product-workspace-reviewer-apex` (Root-Vision Brownfield Reviewer)
Trigger with `/review-product` or `/apex-review` inside any existing repo or folder. It enforces a **Strict 4-Stage Root-Anchored Protocol**:
1. **Turn 1A — Silent/Factual X-Ray Recording (`xray_scanner.py`):** Inventories files, detects `v1/v2/final` entropy, and maps **Green / Yellow / Red Blast-Radius Zones**—while **strictly locking out premature repair proposals**.
2. **Turn 1B — Root-Vision Interview from Scratch:** Asks what your **Original Root Idea & Ultimate North Star** was when you started the project, and stops to wait for your answer.
3. **Turn 2 — The 4-Column Vision-vs-Reality Gap Matrix + Pros/Cons Table:**
   Cross-examines your **Root Vision** against **Current Workspace Reality**:
   * 🟢 **Column 1 (`KEEP & PROTECT`):** Existing assets & Red-Zone historical data that already fulfill your Root Vision.
   * 🟡 **Column 2 (`REALIGN & REFACTOR`):** Existing files that drifted from your intent or hardcoded volatile parameters (*15-Min Quick-Win Patches + Surgical Refactors*).
   * 🔵 **Column 3 (`MISSING A-TO-Z BUILD`):** Core desires from your Root Vision that the old workspace **never built at all**—queued for full Greenfield A-to-Z construction!
   * 🚀 **Column 4 (`+30% KANO DELIGHTERS & 4 SILENT LEAKS`):** High-leverage industry features injected by the C-Suite Council.
4. **Turns 3–6 — Full A-to-Z Idea-to-Product Execution:** Convenes the **6-Role C-Suite Red-Team**, architects the **12-Month Evergreen 3-Tier system**, builds missing features, refactors legacy modules, and verifies 100% behavioral parity via `review_gate_audit.py`.

---

## 🏛️ The 6 Architectural Pillars

1. **Dual-Mode Personal + Pros/Cons Elicitation:** Excavates the founder's proprietary insight first, then provides a full `Pros / Cons / Best-Fit` trade-off matrix for every architectural decision.
2. **Johari Quadrant-4 Blind Spots & +30% Kano Delight Quota:** Uncovers $\ge 4$ domain-specific Unknown-Unknowns and injects 20–30% asymmetric delight features ($<20\%$ effort, $10\times$ perceived value).
3. **6-Role C-Suite Council with Isolated Subagent Critic:** Audits every plan through **CPO, CTO, VP Domain, CFO, CRO/COO, and Skeptical Customer** personas using **Adversarial Deduction Scoring** (starts at 100, must uncover $\ge 3$ concrete flaws in Pass 1).
4. **Shift-Left Stage Gates (`Gate 1..6`) & Python Anti-Stub Scanners:** [`fitness_audit.py`](./skills/idea-to-product-apex/scripts/fitness_audit.py) and [`review_gate_audit.py`](./skills/product-workspace-reviewer-apex/scripts/review_gate_audit.py) verify every step immediately and scan code to block `TODO`, `FIXME`, `NotImplementedError`, and fake mock stubs—plus **1 Normal + 2 Chaos/Sabotage Simulations** for non-code workflows.
5. **Zero-Bloat Phase-Isolated Context Loading (95% Build Token Budget):** Loads only the active phase's reference module and drops philosophical prose during Phase 5 so **95% of token capacity goes into complete, production-ready output**.
6. **12-Month Evergreen Guarantee, Hot-Swap Pivot & Upgrade Triggers:** Separates **Tier A (Immutable Core)**, **Tier B (2-Minute Editable Config)**, and **Tier C (Adapters)**, enforces **5-Zone Workspace Hygiene**, and defines quantitative scale thresholds.

---

## 📊 Head-to-Head Comparison

| Enterprise & Behavioral Criterion | `obra/superpowers` | `BMAD-METHOD` | `github/spec-kit` | `aegis-harness` | 🏆 **APEX Twin Suite `v3.7`** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Personal Open Probe + Pros/Cons/Best-Fit Table** | ⚠️ Open Only | ❌ Rigid Forms | ❌ Manual Spec | ⚠️ Bare A/B/C | ✅ **2-Section Personal + Pros/Cons Matrix** |
| **Root-Vision Re-Anchored Brownfield Reviewer** | ❌ | ⚠️ Partial | ❌ | ⚠️ 27-Line File | ✅ **Turn-1 Stop + 4-Column A-to-Z Gap Matrix** |
| **Executable Python Verification & X-Ray Scripts** | ❌ | ❌ | ❌ | ❌ (0 Scripts) | ✅ **4 Python CLI Engines (`xray` + `gates`)** |
| **Multi-Domain Playbooks (Beyond Software)** | ❌ Software Only | ❌ Software Only | ❌ Software Only | ❌ Slogan Only | ✅ **7 Deep Industry Playbooks (`DOM-01`..`07`)** |
| **6-Role C-Suite Council + Isolated Subagent Critic** | ⚠️ Code Review | ⚠️ Sequential | ❌ | ⚠️ 1-Thread | ✅ **6 C-Suite Roles + Subagent Deduction** |
| **12-Month Zero-Rewrite & Red-Zone Snapshot Lock** | ❌ | ❌ | ❌ | ⚠️ 3 Bullet Points | ✅ **3-Tier Config + Snapshot Isolation** |

---

## 🌐 7 Universal Domain Adapters (*What You Don't Know to Ask AI*)

Both Twin Engines automatically load specialized ontologies, hidden risk radars, KPIs, and verification gates across 7 industries:

* **`DOM-01` — Software, SaaS & AI Agents:** Modular monoliths, provider-agnostic LLM/API adapters, zero-stub TDD, live admin config panels.
* **`DOM-02` — Construction, Architecture & Real Estate:** Externalized material/labor price matrices (editable in 2 mins when steel/cement prices fluctuate), instant BOQ/quote PDF generators, site photo taxonomy (`<ProjectCode>_<Client>`), stage-gate inspection checklists.
* **`DOM-03` — Content, SEO, AIO (GEO) & Digital Media:** Generative Engine Optimization (Entity-Attribute-Value tables, JSON-LD Schema.org), topical cluster hubs, E-E-A-T citation scorers, multi-channel content atomizers.
* **`DOM-04` — E-Commerce, Retail & Billing/Invoicing:** Dual-format pixel-perfect **PDF + Excel** invoice engines, immutable historical ledgers, customer price memory, real-time margin floor guards.
* **`DOM-05` — B2B Services, Agency & Internal Operations SOP:** Bus-Factor-1 elimination, 5-Zone Workspace hygiene, self-serve client diagnostic scorecards.
* **`DOM-06` — FinTech, EdTech, Legal & Healthcare:** Hybrid Deterministic Math + AI Explanation, immutable audit trails, effective-date rule versioning.
* **`DOM-07` — Hardware, IoT & Physical-Digital Hybrid:** Offline-first local queues, QR quick-diagnostics, backward-compatible payload schemas.

---

## ⭐ Support & Bookmark This Repository

If **APEX Twin Engine Suite** helps you turn raw ideas into durable products—or rescues an existing workspace from architectural rot—please **give this repository a ⭐ Star on GitHub** and share it with a teammate!

<div align="center">
  <b>Built for Builders, Founders, and Domain Operators Worldwide 🌍 | MIT License</b>
</div>
