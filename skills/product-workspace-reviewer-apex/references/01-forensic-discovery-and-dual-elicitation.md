# 01. Forensic X-Ray Recording, Root-Vision Elicitation & Vision-vs-Reality Gap Matrix

## 1. The Fatal Flaw of Traditional "Code/Workspace Reviewers" (`Sửa Ngọn Quên Gốc`)

When a user brings an existing app, website, Excel/invoice workflow, SEO content folder, or project workspace they have been using, three fatal traps await naive AI agents:
1. **The "Premature Patching" Trap (`Sửa Ngọn Quên Gốc`):** Naive AI scans the existing folder and immediately proposes patches/refactoring for the files it sees—never realizing that the existing workspace only implemented 30–40% of the user's **Original Root Idea**, or built it in the wrong direction because the previous AI didn't know how to elicit requirements!
2. **The "Arrogant Rewrite" Trap:** Naive AI deletes or overwrites working files, accidentally destroying historical customer records (`Red Zone`) or sacred muscle-memory habits.
3. **The "Cosmetic Praise" Trap:** Naive AI skims 3 files, gives 5 generic textbook tips, and fails to run a true A-to-Z `idea-to-product` evolution.

To defeat all three traps, `product-workspace-reviewer-apex` strictly separates **Phase 1 (Turn 1: Objective X-Ray Recording + Root-Vision Interview ONLY)** from **Phase 2 (Turn 2: Vision-vs-Reality Gap Matrix + Full A-to-Z Evolution Blueprint)**.

---

## 2. Phase 1 (Turn 1): Silent/Factual X-Ray Recording + Root-Vision Interview (NO FIXES ALLOWED!)

### Step 1A: Objective Non-Destructive X-Ray Recording
Run `scripts/xray_scanner.py` (or inspect the workspace structure) and output ONLY the **Objective Baseline Telemetry**:
1. **Asset & Module Inventory:** Total files, directory depth, existing modules/scripts/templates, and what workflows are currently present.
2. **Entropy & Version Chaos Index:** Any duplicated or manually versioned files (`v1`, `v2`, `final_copy`, `.bak`).
3. **Blast-Radius Zoning (Green / Yellow / Red Zones):**
   * 🟢 **Green Zones:** Docs, static UI/assets, export templates.
   * 🟡 **Yellow Zones:** Existing logic/scripts/templates that can be refactored under test protection.
   * 🔴 **Red Zones:** Historical invoices/orders, customer databases, live credentials (100% read-only snapshot protection).

> **⛔ IRON GATE 1A:** Right after showing this factual inventory, explicitly tell the user:
> *"I have recorded the current state of your workspace above. I am **not** proposing any fixes yet—first, I want to interview you from the root of your original idea so we can compare what you truly wanted from A-to-Z against what this workspace currently does."*

### Step 1B: Root-Vision A-to-Z Elicitation Interview (From Scratch)
Ask the user **3 to 4 open, root-level questions** (mirroring `idea-to-product-apex`) before designing any solution:
1. **Q1 — Original Root Vision & Ultimate North Star:**
   *"Temporarily set aside the limitations of the current files in this workspace: when you first started this project, what was the complete, ideal product or outcome you wanted it to achieve from A to Z?"*
2. **Q2 — Open-Canvas Unbuilt Ambitions & Outside-the-Box Ideas:**
   *"What features, workflows, or secret ideas did you originally want (or recently think of) that the current workspace completely missed, left half-finished, or built the wrong way?"*
3. **Q3 — Real-World Friction & Disappointments:**
   *"When operating the current workspace in real life, what frustrates you the most or wastes the most time compared to your initial expectation?"*
4. **Q4 — Sacred Assets & Habits to Preserve:**
   *"Which specific data, files, or working parts in the current workspace are already serving you well and must be preserved 100%?"*

> **🛑 HARD STOP AT THE END OF TURN 1:** Stop immediately after asking Q1–Q4 and wait for the user's response! Never output repair options or code edits on Turn 1.

---

## 3. Phase 2 (Turn 2 — After User Replies): The 4-Column Vision-vs-Reality Gap Matrix & A-to-Z Expansion

Once the user shares their **Original Root Vision**, cross-examine **Root Vision** against **Current Workspace Reality** in a mandatory **4-Column Gap Matrix**:

| Gap Bucket | Definition | Action in A-to-Z Pipeline |
| :--- | :--- | :--- |
| **1. 🟢 Met & Healthy (`KEEP & PROTECT`)** | Parts of the current workspace that already fulfill the user's Root Vision accurately and reliably. | Lock & preserve 100%; wrap cleanly into the upgraded architecture. |
| **2. 🟡 Built Wrong / Drifted (`REALIGN & REFACTOR`)** | Existing files/code that attempted to solve a requirement from the Root Vision, but built it poorly, hardcoded it, or drifted from the user's true intent. | Split into **15-Min Quick-Win Patches** and **Surgical 3-Tier Refactors** with regression parity tests. |
| **3. 🔵 Unbuilt Core Vision (`MISSING A-TO-Z BUILD`)** | Core features, workflows, or desires from the user's Root Vision that the current workspace **never built at all**! | Execute full **Greenfield A-to-Z Idea-to-Product Engineering** to build these missing pillars from scratch! |
| **4. 🚀 30% Beyond-Expectation Expansion (`KANO DELIGHTERS + 4 SILENT LEAKS`)** | High-ROI industry capabilities (`DOM-01..07`) and 4 Johari Silent Leak remedies that the user didn't even know to ask for. | Inject 20–30% asymmetric delight features that elevate the product far beyond the user's original expectation. |

### The 4 Silent Leaks (Injected into Bucket 4)
1. **Leak 1 — Cognitive & Time Bleed:** Manual copy-pasting, repetitive steps, or hunting across `v1/v2` files.
2. **Leak 2 — Unit Economics & Revenue Bleed:** Slow quote/response turnaround, unguarded margin drops, or wasted API/hosting cost.
3. **Leak 3 — Structural & Volatility Rot:** Hardcoded prices, tax rates, rules, or prompts scattered inside logic files instead of a 2-Minute Editable Tier-B Config.
4. **Leak 4 — Catastrophic Fragility:** Risk of overwriting historical Red-Zone records, zero input validation, or lack of 1-click export/backup.

### Selecting the Strategic A-to-Z Evolution Archetype (End of Phase 2)
After presenting the **4-Column Vision-vs-Reality Gap Matrix**, offer **3 Strategic A-to-Z Product Evolution Paths + Option D**:
* **Option A (Surgical Realignment & Hygiene):** Keep Bucket 1, fix Bucket 2 (`REALIGN`), extract Tier-B Config, and lock Red-Zone history.
* **Option B (Recommended — Full Root-Vision A-to-Z Completion + 30% Kano Delighters):** Keep Bucket 1, refactor Bucket 2, **build 100% of Bucket 3 (`MISSING A-TO-Z BUILD`)**, and **inject Bucket 4 (`30% KANO DELIGHTERS`)** under a 12-Month Evergreen 3-Tier architecture.
* **Option C (10x Next-Gen Platform Transformation via Strangler-Fig):** Build a complete next-generation A-to-Z system around the existing data asset with zero-downtime cutover.
* **Option D (Your Custom / Hybrid A-to-Z Vision):** Prioritize the user's custom synthesis.

Once the user confirms the Vision-vs-Reality Gap Matrix, proceed seamlessly through **Phase 3 (6-Role C-Suite Red-Team Council)** $\rightarrow$ **Phase 4 (Unified A-to-Z Evergreen Architecture)** $\rightarrow$ **Phase 5 (Full A-to-Z Build of Missing Features + Surgical Refactoring of Existing Assets)** $\rightarrow$ **Phase 6 (Before/After Vision-Fulfillment Delta & 365-Day Handover)**.
