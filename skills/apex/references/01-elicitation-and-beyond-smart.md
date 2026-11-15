# 01. Dual-Mode Elicitation Engineering & The Pros/Cons Decision Matrix

## 1. Why Bare "3-Option Multiple Choice" Fails the User

When an AI presents 3 bare options (`Option A`, `Option B`, `Option C`) without asking the user personal open questions and without analyzing the **Pros, Cons, and Best-Fit** of each option, two critical failures occur:
1. **No Space for Personal Desires ("Không có phần hỏi riêng người dùng"):** When options A/B/C are merged directly into the question, the user's own secret ideas, personal workflow preferences, and unique domain insights (*outside* AI's 3 options) are never excavated.
2. **Blind Choice Paralysis ("Không có Ưu/Nhược điểm nên không biết chọn gì"):** Listing 3 brief titles or 1-sentence descriptions leaves the user guessing which option actually matches their personal goals, budget, and operating habits.

---

## 2. When to Use the 2-Section Format (and When Not To)

The 2-section format solves two real problems: personal open questions so the user's own ideas surface, and pros/cons/best-fit so options are never chosen blindly. Applied mechanically, though, it hurts. The worst case is showing it *again* after the user has already said "just pick and continue".

Use it only when all three hold:
1. There is a **genuine fork**: 2–3 viable paths that differ in ways only the user can weigh (cost vs. speed, manual vs. automated, scope).
2. The user has **not delegated** the decision ("cứ chọn phương án bạn thấy hợp nhất", "you decide", "làm luôn").
3. You have **already led with value**: Turn 1 opens with 2–4 concrete domain findings, and the questions and table come after them.

Otherwise, recommend one path in a sentence, say what would change your mind, and keep going. When the user delegates, convert their answers into decisions and build in the same reply.

Always keep **one open question** for the user's own idea, even when you skip the table. That is where knowledge the model does not have comes from.

```
[Turn 1]  2–4 concrete findings for this user's domain  →  recommended direction (+ draft if cheap)
          →  ≤ 3 questions that change the build (one of them open)  →  options table ONLY if a real fork exists
[Turn 2+] user delegated?  → decide in one line, build slice 1 (the biggest flow) now
          user chose/mixed? → acknowledge how their own idea changed the plan, then build
```

### Options template (only for a genuine fork; write it in the user's language)

```markdown
**One question for you first:** <one open question, answerable in a line, that invites the user's own idea>

| Option | How it works | Pros | Cons / trade-offs | Best if you want… |
| :--- | :--- | :--- | :--- | :--- |
| A | … | … | … | … |
| B | … | … | … | … |
| C (only if a real third path exists) | … | … | … | … |

**My recommendation:** <A, B or C>, because <a reason tied to what this user said>. I would choose differently if <condition>.
You can also mix: tell me which parts of each you want.
```

Rules for the table:
- At most 3 options. Mixing is an invitation in one line, not a fourth row.
- Do not mark an option as recommended inside the table. The recommendation is a separate line that follows from this user's answers.
- Every option has a real cost; state it. Never write "zero risk", "100%" or similar promises.

---

## 3. The 2-Pass Discovery Loop (Pass 1: Value + Questions $\rightarrow$ Pass 2: Decide & Build)

* **Pass 1:** Lead with findings. Then ask the personal questions, plus the options table if a genuine fork exists (see §2).
* **Pass 2:** Once the user replies:
  * Say briefly how their own ideas changed the plan.
  * Resolve the remaining edge cases **yourself** with sensible defaults and list them as assumptions they can override. Do not open another question round unless an edge case is truly blocking and only the user can answer it.
  * Start building slice 1, the flow carrying most of their volume or pain.

---

## 4. The Johari Window Protocol (Quadrant-4 Unknown-Unknowns)

Map project knowledge into 4 quadrants. Quadrant 4 is where this skill adds the most, so give it real effort:
1. **Quadrant 1 (Known Knowns):** What the user stated.
2. **Quadrant 2 (Known Unknowns):** What the user asked AI to solve.
3. **Quadrant 3 (Hidden Personal Context — User knows, AI doesn't know yet):** The user's private business secrets, personal preferences, local market habits, or novel ideas outside AI's training average. *(Extracted via **Section 1: Dedicated Personal Open Questions**!)*
4. **Quadrant 4 (Unknown Unknowns — User doesn't know, AI Council injects):**
   * Industry landmines, legal/compliance traps, unit-economics killers, schema corruption risks, and a few beyond-expectation additions that are cheap to build and to maintain (say what each costs and why it matters to this user).

---

## 5. Upgrading SMART to SMART-ER at Gate 4

When you write acceptance criteria, in whatever order the work happens, make each one **SMART-ER**:
* **S**pecific (Exact input, processing logic, output format, and explicit *Non-Goals*)
* **M**easurable (Quantifiable numeric threshold)
* **A**chievable (Realistic for the operator's budget and Bus Factor)
* **R**elevant (Directly drives core JTBD & protects unit margins)
* **T**ime-bound (Mapped to Vertical Slices 1..4)
* **E**valuated (backed by a test, a check in the target app, a worked example, or a written walk-through for non-software work)
* **R**esilient 12M (12-month durability: Tier-B config isolation + immutable historical snapshots)
