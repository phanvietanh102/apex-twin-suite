# 04. The 12-Month Evergreen Architecture Framework (1-Year Zero-Rewrite Guarantee)

## 1. Why 90% of AI-Built Products & Plans Break Within 30–90 Days

When users build products or plans with standard AI prompts, the output looks impressive on Day 1 ("Demo-Driven Development"), but collapses by Month 2 or Month 3 due to **6 Systemic Decay Forces**:

1. **Volatility Coupling:** Prices, tax rates, supplier lists, prompt templates, API endpoints, or SEO rules are hardcoded inside source code or static documents. When reality changes in Month 2, the user cannot update it without calling a developer to rewrite the system.
2. **Dependency & API Rot:** Relying on unstable third-party packages, unpinned dependencies, or a single AI model version that gets deprecated.
3. **Historical State Corruption:** Updating a product price or business rule accidentally alters past invoices, quotes, or reports because state wasn't versioned or snapshot-isolated.
4. **Context Amnesia Across Time:** Three months later, when the user wants to tweak a small feature, the AI has zero memory of why the system was built that way, and its new edit breaks three existing features.
5. **Silent Operational Drift:** A webhook, scraper, formula, or integration fails silently; the owner only discovers it weeks later when customers complain.
6. **Cognitive Overload on the Owner:** The system requires 15 manual steps every day. After 3 weeks of excitement, human discipline fades and the system is abandoned.

---

## 2. The 6 Architectural Laws for a 1-Year Zero-Rewrite System

To guarantee that a product or execution plan works reliably for **at least 12 months without needing core upgrades**, every APEX design enforces these 6 engineering laws:

### Law 1: Strict 3-Tier Separation (Immutable Core — Editable Config — Presentation Adapters)
Every system (whether software, spreadsheet engine, content factory, or business workflow) must be partitioned into:
* **Tier A — The Immutable Core Engine (12+ Months Stable):**
  * Pure calculation engines, state machines, accounting/ledger rules, data validation schemas, and file/export pipelines.
  * *Rule:* Zero business numbers, zero seasonal text, and zero vendor-specific hardcoded strings allowed here.
* **Tier B — The Externalized Configuration & Rule Layer (Editable in 2 Minutes):**
  * Pricing matrices, product catalogs, prompt templates, AI model names, tax/commission percentages, brand colors/logos, contact info, and domain rules.
  * *Rule:* Stored in human-readable, easily editable files (`config.json`, `settings.yaml`, `.env`, CSV/Excel tables, or an Admin UI panel) with **automatic schema validation** (if the user types text where a number belongs, the system warns clearly instead of crashing).
* **Tier C — The Adapter & Presentation Layer:**
  * UI views, PDF/Excel/Web templates, notification channels, and LLM/API wrappers.
  * *Rule:* Swapping an LLM provider or changing a PDF layout never touches Tier A.

### Law 2: Historical Immutability & Snapshot Isolation
* Whenever an output is generated (an invoice, a construction estimate, a contract, a published report, an order), save a **self-contained immutable snapshot** (including the exact unit prices and rules active at that timestamp).
* Future edits to the price catalog (Tier B) must **only** affect new transactions from that day forward, never corrupting historical records.

### Law 3: Local-First / Boring-Tech Durability
* When choosing technologies or workflows for a 12-month horizon, prioritize **Boring, Battle-Tested, Low-Maintenance Stacks** over hype:
  * Prefer standard HTML/CSS/JS, TypeScript, Python standard library, SQLite/PostgreSQL, static/serverless deployments, or self-contained offline-capable tools over fragile 50-microservice chains.
  * Every external dependency must justify its existence. If a 20-line pure function can replace a heavy external library, write the 20-line function.
  * Always include **1-Click Local Backup & Export** (JSON/CSV/XLSX/ZIP) so the user owns 100% of their data even if cloud services change pricing.

### Law 4: Automated Architectural Fitness Functions
A system stays healthy for 1 year only if it can **self-verify**. Embed lightweight Fitness Functions into the project:
* **Data/Input Integrity Check:** Validates all config files and user inputs against min/max bounds and required fields before execution.
* **Unit Economics & Cost Ceiling Guard:** Hard cap on API calls, token usage, or discount thresholds (e.g., blocks or warns if margin $< X\%$ or daily API spend $> \$Y$).
* **Regression Smoke Test (`verify` script):** A single command or checklist that tests the core end-to-end flow in $<10$ seconds to prove nothing is broken.

### Law 5: Graceful Degradation & The "5-Minute Manual Fallback"
* Ask: *"What happens if the internet is slow, the AI API is down, or a third-party service changes policy?"*
* Every automated step must have a **Graceful Fallback**:
  * If AI API fails $\rightarrow$ fall back to deterministic rule/template mode so business operations never halt.
  * Provide a **5-Minute Manual SOP** in the Runbook for critical path operations.

### Law 6: Day-1 Blast-Radius Zoning & 5-Zone Workspace Hygiene
To maintain 100% parity with `product-workspace-reviewer-apex` and guarantee the workspace never degrades into `v1_final_copy` chaos over 12 months:
* **Blast-Radius Zoning from Day 1:**
  * 🟢 **Green Zone:** UI themes, static templates, docs (safe for rapid iteration).
  * 🟡 **Yellow Zone:** Core calculation/workflow engine (protected by unit tests).
  * 🔴 **Red Zone:** Historical customer records, issued invoices, database ledgers, credentials (100% immutable snapshots).
* **5-Zone Directory Taxonomy:** Structure business/project workspaces into `00-CONFIG-AND-TEMPLATES`, `01-ACTIVE-OPERATIONS`, `02-CORE-SYSTEM-AND-TOOLS`, `03-IMMUTABLE-ARCHIVE`, and `04-EXPORTS-AND-DELIVERABLES`.

---

## 3. The 4-Horizon Longevity Stress-Test Matrix (Day 1 $\rightarrow$ Day 365)

Every roadmap generated in `04-12M-EVERGREEN-ROADMAP.md` must explicitly plan for these 5 time horizons so the user just follows the plan without needing to re-architect:

| Time Horizon | Focus & System State | Built-in Mechanism Designed on Day 1 | User Action Required |
| :--- | :--- | :--- | :--- |
| **Horizon 1: Day 1–7 (Launch & Immediate Value)** | Core MVP + Top Kano Delighters live; zero-friction onboarding. | Vertical slices verified end-to-end; initial config populated with real defaults. | Use the product immediately; validate with first real cases. |
| **Horizon 2: Day 30 (Habit & Calibration)** | First month of real data reveals edge cases and price/rule adjustments. | Externalized Config Layer (`config.json` / Admin sheet) allows tweaking parameters without code changes. | Spend 10 mins adjusting config numbers based on Month 1 reality. |
| **Horizon 3: Day 90 (Scale & Automation Lock)** | Data volume grows $5\times$–$10\times$; repetitive patterns emerge. | Built-in filtering, pagination, archiving, and template presets prevent UI/system slowdown. | Run Quarterly 15-Min Archive/Backup routine. |
| **Horizon 4: Day 180 (Mid-Year Market Shift)** | Competitors copy basic features; market prices or external APIs shift. | Phase-2 Dormant Delighters (pre-designed in Blueprint) can be toggled on; Adapter layer swaps APIs in 5 mins. | Toggle pre-built growth/delight modules in roadmap. |
| **Horizon 5: Day 365 (1-Year Evergreen Milestone)** | Full year of historical data, seasonal cycles, and annual audit. | Immutable snapshots + 1-Click Annual Summary/Export + Schema Versioning ready for Year 2. | Export annual data archive; system continues into Year 2 seamlessly. |
