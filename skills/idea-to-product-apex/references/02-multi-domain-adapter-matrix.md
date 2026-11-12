# 02. Universal Multi-Domain Adapter Matrix (Ma Trận Thích Ứng Đa Lĩnh Vực)

Most existing AI skills (`obra/superpowers`, `BMAD-METHOD`, `spec-kit`) are hardcoded for **Software Engineering only**. When a user brings an idea in Construction, Real Estate, SEO/Content Marketing, E-Commerce, Agency Operations, or Finance, software-only skills force awkward tech jargon or fail completely.

The **APEX Engine** dynamically adapts its vocabulary, blind-spot radar, Kano delighters, deliverables, and 12-month durability guardrails across **7 Core Domain Archetypes** (plus hybrid combinations).

---

## Domain Detection & Routing Table

Identify which primary domain (and secondary domain, if hybrid) matches the user's idea:

| Domain ID | Domain Archetype | Typical Ideas / Use Cases | Primary Output Form |
| :--- | :--- | :--- | :--- |
| **`DOM-01`** | **Software, SaaS & AI Agents** | Web/Mobile apps, internal tools, AI bots, Chrome extensions, workflow automations, APIs. | Production codebase, database schema, CI/CD, deployment & runbook. |
| **`DOM-02`** | **Construction, Architecture & Real Estate** | Cost estimation tools, project tracking, portfolio/lead-gen sites, inspection SOPs, property valuation/CRM. | Interactive calculators/portals, quotation engines, field checklists, visual showcase systems. |
| **`DOM-03`** | **Content, SEO, AIO (GEO) & Media** | Programmatic SEO, AI Overview optimization, multi-channel content factories, brand authority systems. | Content architecture, entity knowledge graphs, automated publishing pipelines, quality rubrics. |
| **`DOM-04`** | **E-Commerce, Retail & Supply Chain** | D2C stores, catalog/pricing engines, inventory/order tools, conversion funnels, loyalty/retention systems. | Storefront/funnel systems, unit-economics calculators, SKU/inventory trackers, CRM flows. |
| **`DOM-05`** | **B2B Services, Agency & Operations SOP** | Client onboarding, proposal/invoice generators, internal company OS, KPI dashboards, HR/training systems. | Operational playbooks, automated document/invoice generators, dashboards, SOP templates. |
| **`DOM-06`** | **FinTech, EdTech, Legal & Healthcare** | Personal/business finance trackers, LMS/courses, compliance checkers, booking/patient intake systems. | High-trust verified systems, audit logs, deterministic calculation engines, privacy guardrails. |
| **`DOM-07`** | **Hardware, IoT & Physical-Digital Hybrid** | Smart devices, manufacturing QA, QR/NFC physical touchpoints, kiosk/POS systems, field telemetry. | Edge-cloud specs, offline-first protocols, hardware BOM/tolerance matrices, fleet runbooks. |

---

## Deep-Dive Domain Playbooks

### 1. `DOM-01`: Software, SaaS & AI Automation
* **Common User Blind Spots (Quadrant 4):**
  * Hardcoding LLM prompts, model names, or third-party APIs directly into business logic (breaks when APIs deprecate in 3–6 months).
  * Ignoring authentication/authorization boundaries, rate limiting, and token/infra cost ceilings.
  * Building complex microservices when a modular monolith with SQLite/PostgreSQL is 10x easier to maintain for 1 year.
* **Signature 30% Kano Delighters:**
  * Built-in **Admin Config & Health Dashboard** (change prompts, pricing, or rules without touching code).
  * **1-Click Export / Backup & Restore** (JSON/CSV/SQLite snapshot) so data is never trapped.
  * **Dry-Run / Simulation Mode** to preview actions before committing changes.
* **12-Month Evergreen Guardrails:**
  * Strictly use the **Adapter Pattern** for all external APIs/LLMs.
  * Pin all dependency versions (`package-lock.json` / `requirements.txt`) and avoid bleeding-edge alpha libraries.
  * Separate configuration/rules (`config.yaml` / `.env` / DB settings table) from core application code.

---

### 2. `DOM-02`: Construction, Architecture & Real Estate (Xây dựng, Kiến trúc & Bất động sản)
* **Common User Blind Spots (Quadrant 4):**
  * **Material & Labor Price Drift:** A construction quote generator or sales tool with hardcoded prices becomes useless in 60 days when steel/cement/finishing prices fluctuate.
  * **Trust Deficit in High-Ticket Decisions:** Customers buying a house or signing a construction contract don't convert from generic text—they need **Visual Proof (Before/After, 3D/AR, actual site photos, stage-by-stage inspection checklists, legal/Feng Shui calculators, transparent bill-of-quantities)**.
  * **Speed-to-Lead Decay:** If a lead asks for a quote or property info and waits $>15$ minutes, conversion drops by $80\%$.
* **Signature 30% Kano Delighters:**
  * **Interactive Instant Preliminary Estimator & PDF Proposal Generator:** Customer selects area, floors, style, and package $\rightarrow$ immediately receives a branded, itemized budget breakdown + timeline chart.
  * **Visual Progress / Legal Milestone Tracker:** Interactive timeline showing exact legal steps or construction inspection gates (Móng $\rightarrow$ Thân $\rightarrow$ Mái $\rightarrow$ Hoàn thiện) with photo evidence slots.
  * **Smart Comparison & Feng Shui / Cashflow Assistant:** Built-in loan amortization calculator, rental yield estimator, or orientation/Feng Shui quick-check.
* **12-Month Evergreen Guardrails:**
  * **Externalized Price & Material Matrix:** All unit prices (đơn giá nhân công, vật tư thô, hoàn thiện, lãi suất ngân hàng) live in an editable Google Sheet / JSON / Admin table so non-technical staff can update prices in 2 minutes.

---

### 3. `DOM-03`: Content, SEO, AIO (AI Overviews / GEO) & Digital Media
* **Common User Blind Spots (Quadrant 4):**
  * Writing generic AI articles that Google/Search engines penalize as "scaled thin content" within 3 months.
  * Optimizing only for legacy keywords while ignoring **AIO / GEO (Generative Engine Optimization)**: structured Schema.org JSON-LD, Entity-Attribute-Value (E-A-V) density, original data tables, and first-hand E-E-A-T proof (real photos, case studies, author credentials).
  * Lack of **Content Decay & Cannibalization Tracking** (multiple articles competing for the same intent).
* **Signature 30% Kano Delighters:**
  * **Multi-Channel Atomizer:** 1 core deep-research pillar automatically outputs: (1) SEO/AIO Pillar Article with Schema JSON-LD, (2) Comparison Table & FAQ block, (3) Facebook/LinkedIn/Zalo social posts, and (4) Short-video script.
  * **Automated E-E-A-T & AIO Citation Scorer:** A checklist/script that scores every draft for entity completeness, citation readiness, and zero-fluff density before publishing.
* **12-Month Evergreen Guardrails:**
  * Build around **Evergreen Topical Clusters & Hub-and-Spoke Architecture** rather than ephemeral algorithm hacks.
  * Isolate year-sensitive data (prices, "top 10 in 2026", statistics) into modular data blocks for 1-click annual refresh.

---

### 4. `DOM-04`: E-Commerce, Retail, D2C & Billing/Invoicing
* **Common User Blind Spots (Quadrant 4):**
  * Focusing on storefront aesthetics while ignoring **Unit Economics** (CAC, AOV, Gross Margin, Return Rate, Cash Conversion Cycle).
  * Manual order/invoice errors (wrong SKU pricing, missing discount tiers, inconsistent customer history, unformatted PDF/Excel invoices).
  * Zero post-purchase retention loop (losing 100% of customers after the first transaction).
* **Signature 30% Kano Delighters:**
  * **Smart Bundle & Margin Guardrail Engine:** Automatically suggests cross-sells/bundles while warning the operator if a discount pushes net margin below the safety floor.
  * **Dual-Format Instant Invoice & Reconciliation System:** Generates pixel-perfect PDF + Excel invoices with automatic version tracking, customer debt/payment ledger, and 1-click Zalo/Email summary.
  * **Automated Re-Order / VIP Care Trigger:** Flags customers due for replenishment or follow-up based on purchase cycle.
* **12-Month Evergreen Guardrails:**
  * Immutable transaction logs (never overwrite historical invoices when product catalog prices change in the future!).
  * Versioned templates and tax/fee configuration tables.

---

### 5. `DOM-05`: B2B Services, Agency, Consulting & Internal Operations OS
* **Common User Blind Spots (Quadrant 4):**
  * **Bus Factor = 1:** The workflow only works when the founder operates it manually because tacit knowledge isn't codified into decision trees and templates.
  * Scope creep and unstandardized deliverables eating up profit margins.
* **Signature 30% Kano Delighters:**
  * **Self-Serve Client Intake & Diagnostic Scorecard:** Prospects answer 7 structured questions and immediately receive an automated "Health/Readiness Audit Report" (builds instant authority before the sales call).
  * **SOP Runbook with Embedded Quality Checklists:** Every operational task includes a "Definition of Done" verifier.
* **12-Month Evergreen Guardrails:**
  * Modular SOP design where tools can change (e.g., swapping Notion/Sheets/CRM) without changing the underlying data contract and workflow gates.

---

### 6. `DOM-06`: Regulated & High-Trust Domains (FinTech, EdTech, Legal, Healthcare)
* **Common User Blind Spots (Quadrant 4):**
  * Using probabilistic LLMs to do financial math, tax calculations, or medical/legal rule evaluation (LLMs hallucinate arithmetic!).
  * Missing audit trails (who changed what number and when) and PII/privacy protection.
* **Signature 30% Kano Delighters:**
  * **Hybrid Deterministic + AI Architecture:** 100% of math/rules run in deterministic code/formulas (with unit tests), while AI is used strictly for natural language explanation, intake parsing, and personalized coaching.
  * **Explainable Citation Trail:** Every output shows the exact formula, rule, or source document behind the conclusion.
* **12-Month Evergreen Guardrails:**
  * Rule/regulation versioning (effective-date tables so old records use old rules and new records use new rules).

---

### 7. `DOM-07`: Hardware, IoT & Physical-Digital Hybrid Systems
* **Common User Blind Spots (Quadrant 4):**
  * Assuming 100% Wi-Fi/Internet connectivity (systems freeze when network drops).
  * No remote diagnostics or physical calibration fallback.
* **Signature 30% Kano Delighters:**
  * **Offline-First Local Queue + QR Quick-Diagnostic:** Works offline and syncs later; scanning a QR code on the physical asset opens instant status/maintenance logs.
* **12-Month Evergreen Guardrails:**
  * Backward-compatible payload schemas and hardware abstraction layers.
