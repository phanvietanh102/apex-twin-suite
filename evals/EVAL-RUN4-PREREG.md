# Eval Run 4: pre-registration

Written **before** any run. Do not edit after results arrive.

- **Date:** 2026-11-14
- **Condition under test:** skill v4.1, which is v4.0 plus the three run-3 fixes:
  - no silent deferral of High rows;
  - native-first delivery, verified in the target app;
  - no clutter (everything under `_apex/`);
  - plus a next-12–24-months section in the domain brief.

  It is compared with no skill, on Claude Opus 5.5 in Claude Code.
- **Scenario sampling:** fresh, never-used scenarios from the pool in `ANALYSIS-AND-UPGRADE-PLAN.md` §5. Seed `1794643981`. Two drawn from the greenfield/new subset and one from the existing-workspace subset.
  - **Drawn:**
    - #5 indie B2B SaaS (EN, greenfield) → `idea-to-product-apex`;
    - #12 small UK law office, matter and deadline management (EN, greenfield) → `idea-to-product-apex`;
    - #9 garment workshop with 40 workers, outsourced orders (VI, existing workspace) → `product-workspace-reviewer-apex`.
- **Scenario authoring:** an independent agent writes the Turn-1/Turn-2 messages, a fixture (for #9 only) and a hidden checklist of 15–25 items per scenario. It does not read the skill.
- **Format:** 2 turns. Turn 2 delegates the decision.
- **Grading:** one blind A/B grader per scenario, with shuffled positions. The same six 1–10 criteria, checklist recall, and friction metrics as run 3.

## Pass criteria (decided in advance)

| # | Criterion | Pass if |
| :--- | :--- | :--- |
| P1 | Completeness | Mean hidden-checklist recall of v4.1 ≥ no skill + 10 percentage points |
| P2 | Friction did not regress | Mean "low friction" score of v4.1 ≥ 6.3 |
| P3 | Overall | v4.1 total ≥ no-skill total in at least 2 of 3 scenarios |
| P4 | No correctness regression | Mean correctness of v4.1 ≥ no-skill mean − 1 |
| P5 | Native-first held | v4.1 deliverables contain zero spreadsheet error values when recalculated, and v4.1 never requires a runtime the user does not already have (a technical user who already runs it is exempt) |
| P6 | No silent deferral | The grader finds zero High-weight items (law, safety, money at risk, irreversible data, root vision, #1 pain) that v4.1 deferred with only a "check later" line and no user agreement |

**Interpretation rule:** a per-scenario difference under 7 points is within grader noise and must not be described as a win or loss on its own. **Run 3 is the baseline for judging whether the fixes helped.** In run 3, v4.0 scored 140 vs. 139, recall 85.2% vs. 82.9%, and friction 6.33.
