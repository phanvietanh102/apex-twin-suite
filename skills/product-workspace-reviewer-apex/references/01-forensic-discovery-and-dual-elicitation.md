# 01. Forensic X-Ray Discovery & Dual-Mode Pain Excavation

## 1. Why Reviewing an Existing Product/Workspace Is Fundamentally Harder Than Building From Scratch

When a user brings an existing app, website, Excel/invoice workflow, SEO content folder, or project workspace they have been using for months or years, two fatal traps await naive AI agents:
1. **The "Arrogant Rewrite" Trap:** Naive AI looks at an old workspace or codebase, calls it messy, and rewrites it from scratch—accidentally destroying unwritten business rules, historical customer records, SEO rankings, or muscle-memory habits the owner relies on daily!
2. **The "Cosmetic Praise" Trap:** Naive AI skims 3 files, gives a generic list of 5 textbook tips, and misses the **silent financial, operational, and structural leaks** killing the system from the inside.

---

## 2. Step 1: Automated Non-Destructive X-Ray Scan

Before asking the user a single question, run `scripts/xray_scanner.py` (or inspect the workspace structure) to gather objective forensic facts:
1. **Asset & File Topology:** Total files, directory depth, file formats (code, spreadsheets, PDFs, images, markdown, configs).
2. **Entropy & Version Chaos Index:** Detect duplicated or manually versioned files (e.g., `quote-v1.xlsx`, `quote-v2-final.xlsx`, `copy of ...`, `.bak`, `old/`) which prove that the user is suffering from **manual versioning pain**.
3. **Blast-Radius Zoning (Green / Yellow / Red Zones):**
   * 🟢 **Green Zones (Safe to Modernize Immediately):** UI polish, new export templates, documentation, isolated helper scripts, static asset organization.
   * 🟡 **Yellow Zones (Test-Protected Refactoring):** Core workflow scripts, search/filter logic, SEO/AIO schema templates, folder restructuring.
   * 🔴 **Red Zones (Live Business Data / Financial / Historical Ledger):** Historical invoices/orders, customer databases, payment/billing formulas, live production URLs, authentication keys. *(Rule: Never mutate Red Zones without a verified backup snapshot and Strangler-Fig wrapper!)*

---

## 3. Step 2: The 3-Layer "Dual-Mode Hybrid Elicitation" for Existing Systems

Once the X-Ray scan completes, interview the user (max 3–4 questions per turn) combining **Open Pain/Habit Excavation + Brutal Diagnostic Grilling + A/B/C/D Modernization Paths**:

### Layer 1: Open Excavation of "Sacred Habits" & "Secret Ambitions"
* Ask what **MUST NOT CHANGE** (*"Which parts of your current tool or workspace work so well—or are so ingrained in your daily muscle memory—that they must not be disrupted?"*).
* Ask for the user's **Own Upgrade Vision** (*"While operating this system day-to-day, what upgrade or automation have you wished for that hasn't been built yet?"*).

### Layer 2: Brutal Diagnostic Stress-Test
* Point directly to concrete evidence found in the X-Ray scan:
  * *"During the X-Ray scan, I detected [X manually versioned v1/v2 files / Y hardcoded price parameters / Z manual copy-paste steps]. How many minutes per week does this cost you, and has it ever caused a calculation or versioning mistake?"*

### Layer 3: AI Benchmark Modernization Paths (Options A/B/C + Wildcard D)
Always provide 3 calibrated modernization options plus Option D so the user controls the exact blast radius:
* **Option A (Surgical Polish & Hygiene — 100% Non-Disruptive):** Clean directory structure, patch silent bugs, extract a Tier-B config table, and automate backups.
* **Option B (Recommended — Evolutionary 3-Tier Upgrade + 30% Kano Delighters):** Preserve 100% of historical Red-Zone data, decouple core logic from config, add 3 high-ROI Kano delight features, and guarantee 12 months of zero-rewrite operation.
* **Option C (10x System Transformation via Strangler Fig):** Build a next-generation automation layer wrapping existing data for a zero-downtime transition.
* **Option D (Your Custom / Hybrid Upgrade Path):** Full priority given to the operator's proprietary workflow vision!

---

## 4. Mapping the "4 Silent Leaks" (The Brownfield Equivalent of Johari Quadrant 4)

Just as `idea-to-product-apex` injects 4 Unknown-Unknown industry blind spots, `product-workspace-reviewer-apex` MUST uncover **4 Silent Leaks** that the operator has grown accustomed to:

1. **Leak 1 — Cognitive & Time Bleed:**
   Manual copy-pasting between files, repetitive formatting, or hunting for files across chaotic directories.
2. **Leak 2 — Unit Economics & Revenue Bleed:**
   Slow lead response times, outdated unit prices in quotes/invoices, unmonetized follow-ups, or excessive API/hosting waste.
3. **Leak 3 — Structural & Volatility Rot:**
   Hardcoded prices, tax rates, prompts, or file paths that require manual editing in multiple places whenever market conditions shift.
4. **Leak 4 — Catastrophic Fragility:**
   Lack of immutable historical snapshots (editing a template overwrites old customer records), zero automated validation on input errors, or single-device lock-in without 1-click export.
