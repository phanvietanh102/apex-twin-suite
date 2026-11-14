# Eval v2 (short): pre-registration

Written **before** any run. Do not edit after results arrive.

- **Date:** 2026-11-14
- **Condition under test:** skill v4.0 (uncommitted working tree), compared with no skill. Model: Claude Opus 5.5 in Claude Code.
- **Scenario sampling:** `random.sample` over the 12-scenario pool in `ANALYSIS-AND-UPGRADE-PLAN.md` §5, with seed `1794640140`.
  - Drawn: #11 homestay with 6 rooms on several OTAs ("works, make it better"; VI); #6 small bakery in Germany, ordering and allergen compliance (EN); #2 agricultural co-operative, purchasing and profit sharing (VI).
  - All three are existing-workspace scenarios, so all three use `product-workspace-reviewer-apex`. Greenfield is not covered by this draw.
- **Scenario authoring:** an independent agent writes each scenario's fixture, Turn-1 and Turn-2 messages, and a hidden checklist of 15–25 items. It does not read the skill and has no contact with the runners or graders.
- **Format:** 2 turns per scenario. Turn 2 delegates the decision ("cứ làm" / "go ahead").
- **Grading:** one blind A/B grader per scenario, with A/B positions shuffled. Six criteria scored 1–10, plus checklist recall (✓ = 1, ◐ = 0.5) and friction metrics (words per reply, setup steps, required installs).

## Pass criteria (decided in advance)

| # | Criterion | Pass if |
| :--- | :--- | :--- |
| P1 | Completeness | Mean hidden-checklist recall of v4.0 ≥ no-skill + 10 percentage points |
| P2 | Friction did not regress | Mean "low friction" score of v4.0 ≥ 6.3 (the v3.8 run-2 mean, 19/3) |
| P3 | Overall | v4.0 total ≥ no-skill total in at least 2 of 3 scenarios |
| P4 | No correctness regression | Mean correctness of v4.0 ≥ no-skill mean − 1 |

**Interpretation rule:** a difference under 7 points per scenario total is within grader noise (observed ±7) and must not be described as a win or loss on its own.
