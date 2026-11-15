# 06. Gates and Verification While Building

Load this when you start building (any mode). SKILL.md and references 07–09 take precedence over anything here. Which references to load, and the three rigor modes (`LEAN`, `STANDARD`, `DEEP`), are defined once in SKILL.md.

## 1. Keep process smaller than the product

A plan is a means; the working result is what the user came for. Do not let process text crowd out the build: load a reference only when you need it, and once building starts, work from the spec and `TRACE.md`. Every build step should leave complete, working files, with no placeholders.

## 2. What the gate script checks, and what stays your judgement

`fitness_audit.py --dir <target> --gate <1..6> --scan-code <dir>` checks structure and evidence. It cannot judge quality; that part is yours.

| Gate | The script checks | You must judge |
| :--- | :--- | :--- |
| 1–2 | Blueprint documents exist, have real content and no `[[FILL]]` markers (STANDARD/DEEP). `TRACE.md` rows are valid whenever the file exists | The goal, constraints and the user's own ideas are captured. Field-specific traps from the domain brief are addressed |
| 3 | A critique score ≥ 85 is recorded (scorecard line or `c_suite_audit_score` in STATE). Ledger modes only | The critique was honest and its flaws were actually fixed. The script only reads the number |
| 4 | Architecture and roadmap documents are complete | Volatile values live in one editable place and history is protected from later edits |
| 5 | At least one proven slice. `TRACE.md` valid: `DONE` has evidence, no High row deferred without `agreed:`. No stubs in the scanned files | The tests really pass. The deliverable works where the daily operators will use it |
| 6 | Every slice proven, no `OPEN` rows, the required change scenarios passed | The handover is usable: setup, daily routine, backup, what to change and how |

In `LEAN` mode there are no blueprint documents. The script then checks `_apex/TRACE.md`, the stub scan and, at Gate 6, the change scenarios in `_apex/STATE.json` (create both with `init_project.py --lean`).

When the user has delegated the decisions, do not stop at a gate to ask for confirmation; record your assumptions and continue. Report results as plain outcomes, never as gate numbers.

## 3. Verifying each slice

Saying "it is finished" is not verification. Before marking a slice `done`:

1. **Stub scan.** Run the gate script with `--scan-code`. It flags `TODO`/`FIXME` comments and `raise NotImplementedError`. Also check by reading that there is no fake data, no button without a handler, and no secret or business number hard-coded in core logic. A faithful mock used only in tests is fine; say so.
2. **Tests that could fail.** Cover:
   - the normal path with exact expected output;
   - boundaries: zero, negative, empty, very large, non-ASCII input;
   - a config-change test: change a price or rule, confirm new results use it and previously saved records are unchanged.
3. **A real run.** Execute the command or open the result as the operator would:
   - scripts and services: run them and read the output and generated files;
   - web or UI: load it, check for runtime errors, check phone width;
   - spreadsheets and documents: recalculate in the target app with zero error values; check formatting.
4. **Record the proof** in `TRACE.md` (and in `STATE.json` slices for STANDARD/DEEP): the command and its result, not a claim.

## 4. When the user changes scope mid-build

Classify the change before touching the core:
- **A value or rule:** change the config only.
- **A new capability:** add it as a separate module or schedule it as a later slice.
- **Something that conflicts with a core decision** (for example, it would let history be edited or make costs uncapped): tell the user what it breaks and offer a safe alternative.

Add a `TRACE.md` row for it either way.
