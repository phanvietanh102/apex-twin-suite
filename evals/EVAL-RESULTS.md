# Eval Results

## Run 4 (2026-11-14): v4.1 (run-3 fixes) vs. no skill on 3 fresh random scenarios, including greenfield

**Method:**
- Pre-registered in [EVAL-RUN4-PREREG.md](EVAL-RUN4-PREREG.md).
- Seed `1794643981` drew three never-used scenarios:
  - #5 indie B2B SaaS (EN, greenfield);
  - #12 small English law firm (EN, greenfield);
  - #9 Vietnamese garment workshop (VI, existing workspace).
- An independent author wrote the hidden checklists (23 / 23 / 21 weighted items) without reading the skill.
- Graders were blind. They recalculated the workbooks in desktop Excel and ran the code and tests.

| Scenario | v4.1 | No skill | Δ | Recall v4.1 | Recall no skill | Low friction v4.1 / no skill |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| t1 B2B SaaS (EN, greenfield) | **49** | 44 | +5 (noise) | **91.3%** | 82.6% | 7 / 7 |
| t2 Law firm, England (EN, greenfield) | **49** | 39 | **+10 (win)** | **93.5%** | 67.4% | 6 / 7 |
| t3 Garment workshop (VI, workspace) | **49** | 47 | +2 (noise) | 90.5% | **95.2%** | 6 / 6 |
| **Total / mean** | **147** | **130** | **+17** | **91.75%** | **81.75%** | 6.33 / 6.67 |

### Pre-registered criteria

| # | Criterion | Result |
| :--- | :--- | :--- |
| P1 | Recall ≥ no skill + 10 pp | ✅ **Pass, razor-thin**: +10.0 pp. Driven by t2 (+26 pp); t3 was −4.8 pp |
| P2 | Low-friction mean ≥ 6.3 | ✅ Pass, borderline (6.33) |
| P3 | v4.1 total ≥ no skill in at least 2 of 3 | ✅ Pass, 3/3 (one beyond noise) |
| P4 | Correctness mean ≥ no skill − 1 | ✅ Pass (8.33 vs. 7.67) |
| P5 | Native-first: no spreadsheet errors, no foreign runtime | ✅ Pass. Both v4.1 workbooks recalculated with 0 error values in desktop Excel. No Python for the non-coders. Microsoft 365 / Excel 2007+ functions only |
| P6 | No silent deferral of High items | ✅ Pass. 0 / 0 / 0 (graders checked) |

**Compared with run 3 (v4.0):** the total moved from 140 vs. 139 to **147 vs. 130**, and mean recall from +2.3 pp to **+10.0 pp**. The three fixes did what they targeted:
- the co-op-style failure (Python plus `#NAME?`) did not recur;
- no High item was deferred;
- the law firm got AML/CDD, conflicts, undertakings and the wills register that the plain model skipped.

### Still weak

- **Cost went up:** ~889k tokens for v4.1 vs. ~466k for no skill (**1.9×**). v4.1 runs took 33–44 min; no-skill runs took 7–27 min.
- **Friction is flat at about 6.3:** long replies, and in t1 about 5.6k words of side documents.
- **t3 slips:**
  - worker ID-card and bank numbers were left in the shared payroll file (a lens-7 privacy miss that the plain model avoided);
  - the backup went to the same PC;
  - the `.bat` launcher fails on Windows 7;
  - one silent omission (refunding social-insurance contributions withheld before October).
- **Statistics:** n = 1 per scenario. Only t2 clears the ±7 noise band on its own.

---

## Run 3 (2026-11-14): v4.0 vs. no skill on 3 random, previously unseen scenarios

**Method:** pre-registered in [EVAL-V2-PREREG.md](EVAL-V2-PREREG.md).
- **Scenarios:** seed `1794640140` drew #11 homestay in Đà Lạt (VI), #6 bakery in Freiburg (EN) and #2 coffee co-operative in Đắk Lắk (VI). All three are existing workspaces, so all three used the reviewer skill. **No greenfield case was drawn.**
- **Answer keys:** an independent author wrote the fixtures and hidden checklists (22 / 24 / 24 items) without reading the skill.
- **Format:** 2 turns, with the user delegating in turn 2.
- **Grading:** blind A/B graders. Graders recalculated the workbooks in real Excel and ran the code.

| Scenario | v4.0 | No skill | Δ | Recall v4.0 | Recall no skill | Low friction v4.0 / no skill |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| s1 Homestay (VI) | **51** | 48 | +3 (noise) | **93%** | 86% | 7 / 7 |
| s2 Bakery, Germany (EN) | **48** | 42 | +6 (noise) | **83%** | 81% | 7 / 5 |
| s3 Coffee co-op (VI) | 41 | **49** | **−8 (loss)** | 79% | **81%** | 5 / 7 |
| **Total / mean** | **140** | **139** | +1 | **85.2%** | **82.9%** | 6.33 / 6.33 |

**Cost:** v4.0 used ~770k tokens vs. ~502k for no skill (**1.5×**).

### Pre-registered criteria

| # | Criterion | Result |
| :--- | :--- | :--- |
| P1 | Recall ≥ no skill + 10 pp | ❌ **FAIL** (+2.3 pp) |
| P2 | Low-friction mean ≥ 6.3 | ✅ Pass, borderline (6.33) |
| P3 | v4.0 total ≥ no skill in at least 2 of 3 | ✅ Pass (s1, s2), but both wins are within noise |
| P4 | Correctness mean ≥ no skill − 1 | ✅ Pass (8.0 vs. 7.67) |

**Honest verdict:** on unseen existing-workspace scenarios, **v4.0 ≈ no skill** in quality, at 1.5× the cost. The completeness goal (P1) was **not** demonstrated.

### Where v4.0 was better (lenses working)
- Legal precision with sources and hedging: guest registration law, catering VAT split.
- An overbooking playbook with a message script.
- Access control: the cleaner does not see revenue.
- Effective-date pricing for Tết.
- A closed-day pickup check.
- Measurement baseline and `IMPROVEMENT-LOG`.
- Prepayment consent and cancellation terms.

### Where v4.0 lost (data-driven causes)
1. **Deferral loophole.** `TRACE.md` made "DEFERRED: check later" look legitimate. High-weight items (Stollen labelling, traceability, the live shared order book that *is* the owner's vision, data retention) got a one-line deferral instead of substance.
2. **Code over the user's own tool.** "Proof = tests" pushed it toward Python engines. In s3 the co-op's Excel-only accountant got Python + openpyxl + a `.bat`, and the summary sheet showed `#NAME?` in real Excel. In s2 the system depended on one laptop and a 970-line Python tool. The rule "deliver on what the user already has" existed but was outweighed.
3. **Footprint.** It left two jargon process files (~3,000 words) in the co-op's folder, against the LEAN rule.
4. **Both sides missed** forward-looking finance and field items (price risk, cheaper working capital, e-invoicing 2027/28). Lens 12 is not yet pulling these out.

### Next optimizations (from this data)
- **No silent deferral of high-weight items.** Legal, safety, money, the root vision and the top pain must be `DONE` in a minimal form now, or `DEFERRED` only with the user's agreement.
- **Native-first and verified in the target app.** Build inside the user's tool (Excel/Sheets formulas, the existing platform). Verify by recalculating in that app; zero `#NAME?`/`#REF!`. Code only if the user's environment already runs it and someone can maintain it. Tests serve the deliverable; they are not a reason to write code.
- **Zero process clutter.** Keep `TRACE.md` and ledgers in the chat or a single `_apex/` folder. User-facing files go in the user's language.
- **Next eval:** a fresh draw that **includes greenfield cases**. Today's 3 scenarios are no longer unseen.

---

## Run 2 (2026-11-14): after the v3.8 prompt rewrite

**What changed between runs:**
- Wow-first Turn 1.
- When the user delegates, the skill decides and builds.
- The biggest flow is built first.
- Machinery is kept backstage.
- `LEAN` is the default mode; the critic subagent runs only in `DEEP`, once, with no sleep-polling.
- The reviewer's Turn 1 gives read-only findings first (`xray_scanner.py --scan-only`), and its description was narrowed.

**Method:**
- Only the with-skill side was re-run.
- It was graded blind against the **unchanged run-1 without-skill outputs**, with A/B positions shuffled.
- Same prompts, fixture and rubric as run 1.

| Case | With skill (v3.8) | Without skill (run-1 output, regraded) | Winner |
| :--- | :---: | :---: | :--- |
| 1. Cosmetics shop order app | **47** | 44 | With |
| 2. Construction quote workspace review | **52** | 45 | With |
| 3. Affiliate review website plan | **49** | 42 | With |
| **Total** | **148** | **131** | With (+13%) |

**With-skill score, run 1 → run 2:** 120 → **148** (+28). In every case the skill went from losing or tying to winning.

**Highlights graded in run 2:**
- **Case 1 (with skill):** before being asked, it raised the e-invoice duty and the end of lump-sum tax, Shopee's tax withholding, and cosmetics lot/expiry tracking. It kept lot/expiry in the build, imports Shopee and GHTK files from a phone, and exports an item list for an e-invoice provider. Tests: 18/18 logic and 13/13 Apps Script against a mock sheet.
- **Case 2 (with skill):** found 9/9 planted issues and quantified the VAT exposure (~21.4M on one quote). It matched the v2 result to the đồng, made a verified backup, set the archive read-only, and passed 10/10 tests with real PDF export.
- **Case 3 (with skill):** covered 9/9 checklist items, with no math errors. It found an original, cheap angle (measure each appliance's effect on the EVN electricity bill), gave a funnel net of cancellations, tax and commission caps, and shipped a toolchain passing 22/22 tests.

**Remaining weaknesses:**
- **Friction for beginners:** case 3 required installing Python, and replies are still long. Low-friction scores were 7 / 7 / 5.
- **Small slips:** post titles dated a year early; file paths pointing to the wrong folder.

**Cost (both turns, with skill):**

| Case | Run 1 | Run 2 |
| :--- | :--- | :--- |
| 1 | ~371k tokens | ~224k tokens |
| 2 | ~253k tokens | ~134k tokens |
| 3 | ~111k tokens | ~149k tokens |
| **Total** | **~735k** | **~507k (−31%)** |

Without skill, run 1 used ~371k in total, so the skill still costs about 1.4×.

**Caveats:**
- **Grader variance is large.** The same without-skill outputs scored 145 in run 1 and 131 in run 2 (±7 per case). The direction is consistent (3/3 wins), but margins of ~3–7 points per case are near the noise floor.
- n = 1 per case.
- Only Opus 5.5 was tested; the Gemini Argon run is still pending.

---

# Run 1 (2026-11-13)

**Setup:**
- Model: Claude Opus 5.5 in Claude Code, using the gate scripts after the `[[FILL]]` fix.
- Cases: 3 from [EVAL-PROMPTS.md](EVAL-PROMPTS.md). Each case ran with and without the skill, for 2 turns.
- Grading: one blind A/B grader per case. Graders ran the produced code and tests.
- Full transcripts and grades were saved in the session scratchpad (not committed).

## Scores (6 criteria × 10 = 60)

| Case | With skill | Without skill | Winner |
| :--- | :---: | :---: | :--- |
| 1. Cosmetics shop order app (greenfield) | 42 | **49** | Without |
| 2. Construction quote workspace review (brownfield) | 45 | **47** | ~Tie |
| 3. Affiliate review website plan (greenfield) | 33 | **49** | Without |
| **Total** | **120** | **145** | Without (+21%) |

### Per-criterion (sum over 3 cases, max 30)

| Criterion | With skill | Without skill |
| :--- | :---: | :---: |
| Insight beyond the user's knowledge | 23 | 22 |
| Correctness | 22 | 24 |
| Fit to the user's constraints | 21 | 27 |
| Progress (working artifacts) | 20 | 25 |
| Low friction | 14 | 24 |
| Overall wow | 20 | 23 |

### Cost (both turns, per agent)

| Case | With skill | Without skill |
| :--- | :--- | :--- |
| 1 | ~371k tokens, ~35 min (spawned its own critic subagent, slept waiting for re-scores) | ~178k tokens |
| 2 | ~253k tokens, ~21 min | ~114k tokens, ~7 min |
| 3 | ~111k tokens, ~6 min | ~79k tokens, ~4 min |

## What the skill did well

- **Case 2:** found the single most valuable insight of the whole run: the rough-construction (`phần thô`) formula may underprice every quote by about half. It also produced 22 tests, a PDF with a 30/40/30 payment schedule and a steel price-rise clause, and re-quoting with a difference table.
- **Case 1:** deeper engineering: lot/expiry tracking on bills with frozen prices, repeat no-show customers, safe re-paste of GHTK statements, and a packer view that hides money. Its turn-1 insights were rated excellent.
- **Case 3:** sharper blind spots: AI Overviews, keyword cannibalisation, link rot, and a month-6 stop-loss rule.

So the skill's **content** (blind-spot hunting, delighters, verification, Red-Zone protection) adds real value.

## What cost the skill the win

1. **It ignored delegation.** The user said "cứ chọn phương án bạn thấy hợp nhất và làm tiếp" ("just pick what fits best and keep going"). The skill still produced another options table or question round (cases 2 and 3), which pushed real progress to a third turn.
2. **Jargon and self-scoring reached the user.** "Gate PASS 100/100", Tier A/B/C, C-Suite scores, and 7 English docs left in a 3-person shop's workspace.
3. **It lost focus on the user's biggest need.** Case 1 left Shopee orders, 70% of the volume, out of the app while polishing the 30% inbox flow.
4. **Cost:** 1.4×–2.1× the tokens and up to 3× the time, without a matching quality gain.

## Recommended changes (then re-run this pack)

1. **Respect delegation:** when the user says "you decide", pick an option, state one line of why, and proceed.
2. **Wow-first Turn 1:** give 2–3 concrete findings plus a draft, then at most 3 questions.
3. **Keep the machinery internal:** gates, scores and tiers stay internal and never appear in user-facing text. Ledger docs go in the user's language, or are optional in LEAN mode.
4. **Cover the biggest volume first:** state which flow carries most of the user's volume and make it slice 1.
5. **Critic subagent only in DEEP mode,** with no sleep-polling loops.
6. **Invest in domain knowledge packs** (VN tax and e-invoice rules, platform fees, construction norms). This is where the skill can beat a strong bare model.

## Caveats

- n = 1 run per case, with one grader per case.
- Graders could guess which side had the skill from its writing style.
- Only Claude Opus 5.5 was tested. Run the same pack on Gemini Argon in Antigravity before generalising.
