# 05. The Review Ledger: What the Scaffolder Creates and How to Fill It

Load this only in `STANDARD` or `DEEP` mode, after the owner has answered the Turn-1 questions. The scaffolder (`scripts/xray_scanner.py`) is the source of truth for the templates; this file explains their purpose. SKILL.md and references 07–09 take precedence over anything here.

## What gets created

| Mode | Command | Creates |
| :--- | :--- | :--- |
| `LEAN` | `xray_scanner.py --dir <target> --name <name> --lean` | `_apex/TRACE.md`, `_apex/STATE.json` |
| `STANDARD` / `DEEP` | `xray_scanner.py --dir <target> --name <name>` | `docs/apex-review/` with `TRACE.md`, `REVIEW-STATE.json` and the six documents below |

Every judgement in the templates is a `[[FILL: hint]]` marker. Replace each with content drawn from the owner's answers or from file evidence. The scaffold records only measured facts (file counts, zones, duplicates); it never pre-selects an option or a score. Write the documents in the owner's language; the gates check structure, not English keywords.

## The six documents

| File | Purpose |
| :--- | :--- |
| `00-PRESERVATION-CONSTITUTION.md` | What must not break: the owner's sacred habits and assets, the zones (safe to change / change only with tests / never touch), and the non-breaking rules |
| `01-FORENSIC-XRAY-AND-LEAKS.md` | Measured inventory, the owner's root vision in their words, the gap matrix (keep / built wrong / never built / beyond expectation), and silent leaks with file evidence |
| `02-KANO-UPGRADE-SPEC.md` | The fixes, multipliers and beyond-expectation additions chosen for this owner, with a measurable target and a parity proof for each |
| `03-STRANGLER-ARCHITECTURE-AND-HYGIENE.md` | How volatile values move into one editable place, the decisions taken and why, and the operators' routine after the upgrade |
| `04-ZERO-DOWNTIME-MIGRATION-ROADMAP.md` | The slices (slice 1 is always the verified backup and history lock) and the 12-month roadmap |
| `05-DIAGNOSTIC-SCORECARD-AND-ROLLBACK.md` | The before/after critique scorecard (see 03), the checks that keep it healthy, and the rollback steps |

## `REVIEW-STATE.json` fields that the gates read

- `slices[]`: each with `status` (`pending` / `done`) and a `verification_proof` when done.
- `upgraded_health_score`: the critique's "after" total, set only by a real critique.
- `change_scenarios[]`, `change_scenarios_required`, `change_scenarios_waiver`: see 08 §4.
- `context_profile`: the answers from 07 Step 0.

`baseline_health_score` and `upgraded_health_score` both start as `null`. The scaffolder never invents a score.
