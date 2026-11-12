# 02. Universal 7-Domain Forensic Audit & Modernization Matrix

Just like its Greenfield twin, `product-workspace-reviewer-apex` adapts its forensic lenses, leak detectors, workspace hygiene rules, and 30% Kano upgrades across all **7 Core Domain Archetypes** (`DOM-01` through `DOM-07`).

---

## Domain Routing & Forensic Signature Table

| Domain ID | Domain Archetype | Typical Existing Assets Brought for Review | Primary Forensic Focus |
| :--- | :--- | :--- | :--- |
| **`DOM-01`** | **Software, SaaS & AI Apps** | Existing web/mobile codebases, scripts, bots, extensions, API backends. | Technical debt, hardcoded configs/prompts, N+1 queries, missing tests, UI friction. |
| **`DOM-02`** | **Construction, Architecture & Real Estate** | Project photo folders, quotation sheets, portfolio websites, property listings. | Chaotic site photo folders, hardcoded material prices, slow quote generation, weak visual trust proof. |
| **`DOM-03`** | **Content, SEO, AIO (GEO) & Media** | Existing websites/blogs, content workflow folders, prompt libraries, SEO sheets. | Content decay, keyword cannibalization, missing Schema.org/AIO entity markup, manual publishing bottlenecks. |
| **`DOM-04`** | **E-Commerce, Retail & Billing/Invoices** | Excel/PDF invoice folders (`v1`, `v2`), product catalogs, order trackers, storefronts. | Manual invoice versioning chaos, overwritten historical prices, margin calculation errors, zero retention tracking. |
| **`DOM-05`** | **B2B Services, Agency & Operations Workspaces** | Client folders, SOP docs, proposal templates, internal tracking sheets. | Bus-Factor-1 bottlenecks, inconsistent naming conventions, slow client onboarding, scope creep leaks. |
| **`DOM-06`** | **FinTech, EdTech, Legal & Healthcare** | Financial calculators, course portals, compliance checklists, intake forms. | Unverified formula math, missing audit logs, privacy exposure, outdated regulatory rules. |
| **`DOM-07`** | **Hardware, IoT & Physical-Digital Hybrid** | Device configs, field maintenance logs, QR asset trackers, local scripts. | Offline failure points, firmware/config version drift, manual field logging errors. |

---

## Deep-Dive Forensic Playbooks by Domain

### 1. `DOM-01`: Existing Software, SaaS & AI Applications
* **Top 4 Silent Leaks to Hunt:**
  1. **Spaghetti Coupling:** Business rules, API keys, and LLM prompts hardcoded inside UI components or route handlers.
  2. **Dark/Dead Code & Dependency Rot:** Unused packages, duplicated helper functions, and unpinned versions waiting to break.
  3. **Zero Regression Safety Net:** No automated smoke test to verify core workflows after an edit.
  4. **UX Onboarding Drop-off:** Too many clicks/inputs before the user sees results.
* **30% Kano Modernization Upgrades:**
  * Extract all hardcoded constants/prompts into a validated `config.json` / Admin panel (Tier-B extraction).
  * Add an automated 10-second smoke & edge-case test suite.
  * Add 1-click data export/backup and live inline validation.

---

### 2. `DOM-02`: Existing Construction, Architecture & Real Estate Workspaces/Sites
* **Top 4 Silent Leaks to Hunt:**
  1. **Media & Project Folder Entropy:** Hundreds of unorganized site photos (`IMG_1234.jpg`), mixed project codes, and scattered design versions without a standardized taxonomy.
  2. **Stale Estimation Sheets:** Material and labor prices buried inside complex formulas where changing one cell breaks the sheet.
  3. **Weak Conversion Architecture on Web/Portals:** Portfolio pages showing raw photos without structured project metadata (area, budget tier, timeline, before/after story, instant quote CTA).
  4. **Manual Quote Delay:** Taking hours to assemble a PDF quote instead of 60 seconds.
* **30% Kano Modernization Upgrades:**
  * **Automated Project & Media Taxonomy Organizer:** Standardize folder hierarchy (`<ProjectCode>_<Client>_<Year>/<01-Design|02-SitePhotos|03-Quotes|04-Handover>`) with automatic manifest indexing.
  * **Live Configurable Estimator + 1-Click Branded PDF Quote:** Separate material unit prices into a clean Tier-B table and generate instant client-ready proposals.

---

### 3. `DOM-03`: Existing Content, SEO, AIO (GEO) Websites & Workflows
* **Top 4 Silent Leaks to Hunt:**
  1. **AIO / Generative Search Blindness:** Pages written as walls of text without Entity-Attribute-Value (E-A-V) tables, FAQ blocks, or valid `JSON-LD` Schema markup—causing AI engines (ChatGPT, Gemini, Google AI Overviews) to ignore them.
  2. **Cannibalization & Orphan Pages:** Multiple posts targeting overlapping intents without a Hub-and-Spoke internal linking structure.
  3. **Prompt/Workflow Fragmentation:** Scattered prompts in text files producing inconsistent brand tone and generic AI fluff.
  4. **Technical Core Web Vitals & Health Leaks:** Broken links, unoptimized images, missing meta/canonical tags.
* **30% Kano Modernization Upgrades:**
  * **AIO Citation & Schema Injector:** Upgrade top pillar pages with structured comparison tables, TL;DR answer boxes, and automated JSON-LD schema.
  * **Automated Content Quality & E-E-A-T Scorer:** A verification script that checks entity density, heading structure, and real-proof slots before publishing.

---

### 4. `DOM-04`: Existing E-Commerce, Retail & Invoice/Billing Workspaces
* **Top 4 Silent Leaks to Hunt:**
  1. **The `v1 / v2 / final` File Duplication Trap:** Manual invoice files (`Invoice_ClientA_v1.xlsx`, `Invoice_ClientA_v2.pdf`) scattered across folders without a central immutable ledger.
  2. **Formula & Rounding Fragility:** Manual edits overwriting `SUM` or discount formulas, or PDF exports cutting off columns/signatures.
  3. **Zero Customer History & Debt Tracking:** Having to open 20 old spreadsheets to check what price a repeat customer was charged last month.
  4. **Margin Blindness:** Issuing discounts without seeing real-time net profit impact.
* **30% Kano Modernization Upgrades:**
  * **Unified Invoice & Ledger Engine:** 1 master data/config table + 1-click dual export (pixel-perfect **PDF + Excel** simultaneously) with automatic version numbering and immutable historical log.
  * **Instant Customer Price Memory & Margin Guard:** Automatically recalls the customer's last price tier and warns if margin drops below threshold.

---

### 5. `DOM-05`: Existing B2B Services, Agency & Operations Workspaces
* **Top 4 Silent Leaks to Hunt:**
  1. **Tacit Knowledge Lock-in (Bus Factor = 1):** Only the owner knows which file is the latest template or how to run the weekly report.
  2. **Workspace Clutter:** Mixing active projects, archived clients, scratch files, and templates in the same root directory.
* **30% Kano Modernization Upgrades:**
  * **Clean 5-Zone Workspace Architecture:** (`00-CONFIG-AND-TEMPLATES`, `01-ACTIVE-OPERATIONS`, `02-CORE-SYSTEM-AND-TOOLS`, `03-IMMUTABLE-ARCHIVE`, `04-EXPORTS-AND-DELIVERABLES`) + 1-Page Operator Dashboard.

---

### 6. `DOM-06` & `DOM-07`: Regulated Systems (FinTech/EdTech/Health) & IoT/Hardware
* **Top 4 Silent Leaks to Hunt:**
  1. Unverified calculation logic or AI hallucination risks in deterministic fields.
  2. Missing audit trail (who modified what and when) or lack of offline fallback when connectivity drops.
* **30% Kano Modernization Upgrades:**
  * Deterministic math verification test suite + immutable audit log + offline-first local cache.
