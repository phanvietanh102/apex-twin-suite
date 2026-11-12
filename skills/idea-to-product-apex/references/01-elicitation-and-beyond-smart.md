# 01. Dual-Mode Elicitation Engineering & Beyond SMART

## 1. Why Pure "SMART" OR Pure "3-Option Multiple Choice" Alone Both Fail

### A. The Limitation of Using SMART Too Early
* **Where SMART succeeds:** Stage 4–5 execution tracking (turning known features into testable metrics).
* **Where SMART fails (Stage 1–2):** Forcing SMART on Day 1 locks the project inside the tiny box of what the user already knows, missing industry blind spots (*Unknown-Unknowns*) and asymmetric delight features.

### B. The Limitation of Pure "3-Option AI Suggestions" (Anchoring Bias)
* If AI *only* gives 3 pre-baked options (A/B/C), two dangerous failures happen:
  1. **Suppressing the Founder's Secret:** The user might have a brilliant, contrarian, or insider idea (*outside* AI's prediction box). Seeing A/B/C immediately anchors their thinking to AI's statistical average and kills their unique edge!
  2. **Shallow Compliance:** The user lazily picks "Option A" without being challenged on the hard operational realities of their business.

---

## 2. The APEX v3.5 Upgrade: The 3-Layer "Dual-Mode Hybrid Elicitation" Protocol

To get the best of both worlds (the relentless depth of `/grill-me` & `obra/superpowers` **AND** the supportive guidance of AI recommendations when the user is stuck), Phase 1 & Phase 2 MUST combine **Open Contrarian Excavation + Brutal Stress-Testing + AI Benchmark Options**:

```
[Layer 1: Open Contrarian Excavation] -> Uncover the user's unique insight & proprietary secret
                 +
[Layer 2: Brutal Socratic Stress-Test] -> Challenge blind spots, contradictions & edge cases
                 +
[Layer 3: AI Benchmark Options (A/B/C + Wildcard D)] -> Industry benchmarks for parts not yet decided
```

### How to Format Every Discovery Turn (3–4 Questions Max per Turn):

For each question in Phase 1, structure it in **Dual-Mode** (translated naturally into the user's language):
1. **Part 1 — Open & Contrarian Probe:**
   Explicitly ask for the user's own vision, wild ideas, or secret weapon *before* biasing them, and ask a sharp stress-test question (*"What makes your approach fundamentally different from existing solutions? If a customer abandons this in the first 30 seconds, what is the real reason?"*).
2. **Part 2 — AI Benchmark Options (Options A/B/C + Wildcard Option D):**
   Provide 2–3 battle-tested industry options **strictly as a springboard/fallback** if the user hasn't decided yet, plus **Option D (Your Own Custom / Hybrid Vision)**.

#### Canonical Dual-Mode Question Template:
```markdown
### 🔍 Deep Discovery & Industry Benchmark Alignment (Round 1)

> **Rule of Thumb:** If you already have your own unique angle or contrarian idea (outside the options below), **prioritize sharing your own vision first** — the best products come from insights outside AI's statistical average! Options A/B/C serve as industry-standard reference paths if you want a recommendation.

1. **[Open & Contrarian Probe #1 - Core Value & Unfair Advantage]:**
   Based on your real-world intuition or domain experience, what is the single most expensive pain point or unique capability you want in this product that competitors miss?
   * *Industry-Standard Reference Paths:*
     - **Option A (Recommended for rapid automation & speed-to-value):** [...]
     - **Option B (High-ticket B2B / Expert depth):** [...]
     - **Option C (Organic acquisition / Self-serve funnel):** [...]
     - **Option D (Your custom / contrarian vision outside A/B/C):** Describe freely!

2. **[Brutal Operational Stress-Test #2 - Daily Reality & Failure Points]:**
   Suppose this system goes live tomorrow: Who operates it daily, and what friction will cause them to make mistakes or abandon it after 2 weeks?
   * *System Council Reference Designs:*
     - **Option A (Zero-Touch / 1-Click Automation):** [...]
     - **Option B (Co-Pilot / Human-in-the-loop review):** [...]
     - **Option D (Your specific operational workflow):** [...]
```

---

## 3. The 2-Pass Discovery Loop (Pass 1: Divergent Excavation $\rightarrow$ Pass 2: Convergent Grill-Me)

Never lock requirements after a single superficial exchange if ambiguities remain:
* **Pass 1 (Divergent Discovery):** Uncover the user's unique vision, core JTBD, target domain (`DOM-01`..`DOM-07`), and resource constraints using the Dual-Mode template above.
* **Pass 2 (Convergent "Grill-Me" Stress-Test):** Once the user replies (especially if they share a custom/novel idea outside A/B/C!), switch to **High-Intensity Socratic Grilling**:
  * Probe every edge case of the user's unique idea: *"Your custom idea [X] has strong potential, but we must stress-test 3 survival questions so it doesn't break in production: (1) Where does input data come from when offline or malformed? (2) What is the marginal cost/time per run? (3) How do we handle exception [Y]?"*

---

## 4. The Johari Window Protocol (Quadrant-4 Unknown-Unknowns)

Map project knowledge into 4 quadrants and **dedicate 50% of advisory energy to Quadrant 4**:
1. **Quadrant 1 (Known Knowns):** What the user stated.
2. **Quadrant 2 (Known Unknowns):** What the user asked AI to solve.
3. **Quadrant 3 (Hidden Context — User knows, AI doesn't know yet):** The user's private business secrets, local market habits, or novel ideas outside AI's training average. *(Extracted via Layer 1 Open Contrarian Questions!)*
4. **Quadrant 4 (Unknown Unknowns — User doesn't know, AI Council injects):**
   * Industry landmines, legal/compliance traps, unit-economics killers, schema corruption risks, and **30% Kano Asymmetric Delighters**.

---

## 5. Upgrading SMART to SMART-ER at Gate 4

Only after Discovery (Gate 1), Kano Delight (Gate 2), and C-Suite Red-Team (Gate 3) are complete, lock every specification into **SMART-ER**:
* **S**pecific (Exact input, processing logic, output format, and explicit *Non-Goals*)
* **M**easurable (Quantifiable numeric threshold)
* **A**chievable (Realistic for the operator's budget and Bus Factor)
* **R**elevant (Directly drives core JTBD & protects unit margins)
* **T**ime-bound (Mapped to Vertical Slices 1..4)
* **E**valuated (Backed by an automated verification script or test command at that exact step)
* **R**esilient 12M (12-month durability: Tier-B config isolation + immutable historical snapshots)
