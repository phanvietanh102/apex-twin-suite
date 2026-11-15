# 01. Forensic X-Ray Recording, Root-Vision Elicitation & Vision-vs-Reality Gap Matrix

## 1. The Fatal Flaw of Traditional "Code/Workspace Reviewers" (`Sửa Ngọn Quên Gốc`)

When a user brings an existing app, website, Excel/invoice workflow, SEO content folder, or project workspace they have been using, three fatal traps await naive AI agents:
1. **The "Premature Patching" Trap (`Sửa Ngọn Quên Gốc`):** Naive AI scans the existing folder and immediately proposes patches/refactoring for the files it sees—never realizing that the existing workspace may cover only part of the owner's original idea, or have been built in the wrong direction.
2. **The "Arrogant Rewrite" Trap:** Naive AI deletes or overwrites working files, accidentally destroying historical customer records (`Red Zone`) or sacred muscle-memory habits.
3. **The "Cosmetic Praise" Trap:** Naive AI skims 3 files, gives 5 generic textbook tips, and fails to run a true A-to-Z `idea-to-product` evolution.

To defeat all three traps, `apex-review` separates **Turn 1 (read-only: evidence-backed findings + root-vision questions)** from **Turn 2+ (gap matrix, then build)**.

---

## 2. Turn 1: Findings First, Then Root-Vision Questions (Read-Only)

A Turn 1 containing only an inventory plus an interview feels like homework to a busy owner. Findings come first: they prove the review is worth reading. File changes still wait until the owner has said what is sacred.

### Step 1A: Read the Workspace and Report Findings
1. Run `scripts/xray_scanner.py --dir <target> --name <name> --scan-only` for the inventory: file counts, duplicate/version files, and zones. It writes nothing. Then **open the actual files**: run what is safe to run, recompute the numbers, and read the records.
2. Report **3–6 findings ranked by money and data risk**, each with evidence (file:line, the computed number, the affected record) and what it costs the owner. Typical findings: an under- or over-pricing formula, money in float, the same price kept in several places, an unpaid balance hidden in an archive, duplicate outputs, missing validity dates or payment terms.
3. Mark the zones in plain words:
   * **Safe to change:** docs, static assets.
   * **Change only with tests:** logic, scripts, templates.
   * **Never touch:** historical invoices, customer data, credentials. These are read-only and get snapshot protection.
4. Proposing *what* to fix is fine. **Do not edit, move or create files in the workspace on Turn 1**, unless the owner's first message already says what must stay untouched and tells you to decide and proceed (see SKILL.md).

### Step 1B: Root-Vision Questions (≤ 3, after the findings)
1. **Original vision:** *"Setting aside what is built now: what did you originally want this to do, from start to finish?"*
2. **Pain and gaps:** *"Where does it break down or waste your time, and what did you want that it never did?"*
3. **Sacred assets:** *"Which files, data or habits must stay exactly as they are?"*

Drop or merge any question the workspace already answers. Then stop and wait for the reply (same exception as above).

---

## 3. Turn 2 (After the Owner Replies): The 4-Column Vision-vs-Reality Gap Matrix & A-to-Z Expansion

Show the matrix to the owner in short, plain language. The bucket labels below are internal names.

Once the user shares their **Original Root Vision**, cross-examine **Root Vision** against **Current Workspace Reality** in a short **4-column gap matrix**. Leave a bucket empty when nothing belongs in it:

| Gap Bucket | Definition | Action in A-to-Z Pipeline |
| :--- | :--- | :--- |
| **1. 🟢 Met & Healthy (`KEEP & PROTECT`)** | Parts of the current workspace that already fulfill the user's Root Vision accurately and reliably. | Lock & preserve 100%; wrap cleanly into the upgraded architecture. |
| **2. 🟡 Built Wrong / Drifted (`REALIGN & REFACTOR`)** | Existing files/code that attempted to solve a requirement from the Root Vision, but built it poorly, hardcoded it, or drifted from the user's true intent. | Split into **15-Min Quick-Win Patches** and **Surgical 3-Tier Refactors** with regression parity tests. |
| **3. 🔵 Unbuilt Core Vision (`MISSING A-TO-Z BUILD`)** | Core features, workflows, or desires from the user's Root Vision that the current workspace **never built at all**! | Execute full **Greenfield A-to-Z Idea-to-Product Engineering** to build these missing pillars from scratch! |
| **4. 🚀 Beyond expectation (`KANO DELIGHTERS + SILENT LEAKS`)** | High-value capabilities and silent-leak remedies the owner did not know to ask for, drawn from the domain brief. | Add the few that are cheap to build and to maintain and clearly matter to this owner. |

### The 4 Silent Leaks (Injected into Bucket 4)
1. **Leak 1 — Cognitive & Time Bleed:** Manual copy-pasting, repetitive steps, or hunting across `v1/v2` files.
2. **Leak 2 — Unit Economics & Revenue Bleed:** Slow quote/response turnaround, unguarded margin drops, or wasted API/hosting cost.
3. **Leak 3 — Structural & Volatility Rot:** Hardcoded prices, tax rates, rules, or prompts scattered inside logic files instead of a 2-Minute Editable Tier-B Config.
4. **Leak 4 — Catastrophic Fragility:** Risk of overwriting historical Red-Zone records, zero input validation, or lack of 1-click export/backup.

### Selecting the Evolution Path (Only When the Choice Is Genuinely the Owner's)
**If the owner delegated** ("cứ chọn phương án bạn thấy hợp nhất và làm tiếp", "you decide", "làm luôn"), skip the table. Pick the path in one line, list your assumptions, and start building slice 1 (verified backup and Red-Zone lock), then their biggest pain.

Otherwise, after the gap matrix, ask one question and show the options. Write both in the owner's language.

**One question first:** "Looking at this list, is there anything of your own you want to add, drop or put first?"

The paths usually differ in scope. Describe each for *this* workspace, with its real cost:

| Path | What it covers | Pros | Cons / trade-offs | Best if you want… |
| :--- | :--- | :--- | :--- | :--- |
| A. Clean up and stabilise | Keep what works, fix what was built wrong, put volatile values in one place, protect history | Fastest; least change for the operators | The parts of the vision that were never built stay unbuilt | A stable version of today's system, soon |
| B. Complete the vision | Everything in A, plus build what was never built and a few beyond-expectation additions | Reaches what the owner originally wanted | Takes longer; more for the operators to learn | The system you set out to build |
| C. Larger rebuild around the old data | A new structure that wraps the existing records | Most headroom for growth | Most change, most testing, highest risk of disruption | To scale well beyond today's size |

Then add a separate line: **"My recommendation: <A, B or C>, because <a reason from the owner's own answers>."** Do not mark a path as recommended inside the table, and never promise "zero risk" or "100%". The owner may also mix paths; one sentence inviting that is enough.

Once a path is chosen or delegated, continue with the outcomes listed in SKILL.md.
