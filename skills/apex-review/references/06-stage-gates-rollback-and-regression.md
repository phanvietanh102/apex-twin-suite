# 06. Gates, Rollback and Parity While Upgrading

Load this when you start changing the owner's files (any mode). SKILL.md and references 07–09 take precedence over anything here.

## 1. Reading a large workspace

- Run `scripts/xray_scanner.py --dir <target> --name <name> --scan-only` first. It maps files, duplicates and zones in seconds and writes nothing.
- Then read the files that matter for the heaviest flows in full. Do not pull hundreds of files into context blindly.
- Which references to load, and the three rigor modes (`LEAN`, `STANDARD`, `DEEP`), are defined once in SKILL.md.

## 2. What the gate script checks, and what stays your judgement

`review_gate_audit.py --dir <target> --gate <1..6> --scan-target <files or folders you built or changed>` checks structure and evidence. It cannot judge quality; that part is yours.

| Gate | The script checks | You must judge |
| :--- | :--- | :--- |
| 1–2 | Ledger documents exist, have real content and no `[[FILL]]` markers (STANDARD/DEEP). `TRACE.md` rows are valid whenever the file exists | The findings have evidence. The owner's sacred items and root vision are captured in their words |
| 3 | A critique score ≥ 85 is recorded (scorecard line or `upgraded_health_score` in STATE). Ledger modes only | The critique was honest and its flaws were actually fixed. The script only reads the number |
| 4 | Architecture and roadmap documents are complete | The plan protects history, extracts volatile values, and has a rollback path |
| 5 | At least one proven slice (slice 1 = verified backup). `TRACE.md` valid: `DONE` has evidence, no High row deferred without `agreed:`. No stubs in the scanned files | Parity tests pass. The deliverable works in the operators' real tool |
| 6 | Every slice proven, no `OPEN` rows, the required change scenarios passed | The handover is usable by the people who operate it |

In `LEAN` mode there are no ledger documents. The script then checks `_apex/TRACE.md`, the stub scan and, at Gate 6, the change scenarios in `_apex/STATE.json` (create both with `xray_scanner.py --lean`).

Report results to the owner as plain outcomes, never as gate numbers.

## 3. Safety steps before changing any existing file

1. **Backup first.** Take a verified backup (or confirm a clean Git tree) of everything you will touch, so any change can be reversed in one step. Tell the owner where the backup is.
2. **Parity check.** Capture 3–5 real past cases with their exact outputs. Run the same inputs through the upgraded version. Deterministic numbers must match, unless a correction is intended; then state the old value, the new value and why.
3. **Reference integrity.** After renaming or moving anything, scan scripts, links, formulas and config references for broken paths.
4. **Stub and hygiene scan.** Run the gate script with `--scan-target` on the files you built or changed, to confirm you left no unfinished stubs, and check that you created no new duplicate files. Stubs that were already in the owner's code are findings to report; do not edit code outside the agreed scope to clear them.
