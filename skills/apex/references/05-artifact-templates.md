# 05. The Project Ledger: What the Scaffolder Creates and How to Fill It

Load this only in `STANDARD` or `DEEP` mode. The scaffolder (`scripts/init_project.py`) is the source of truth for the templates; this file explains their purpose. SKILL.md and references 07–09 take precedence over anything here.

## What gets created

| Mode | Command | Creates |
| :--- | :--- | :--- |
| `LEAN` | `init_project.py --dir <target> --name <name> --lean` | `_apex/TRACE.md`, `_apex/STATE.json` |
| `STANDARD` / `DEEP` | `init_project.py --dir <target> --name <name>` | `docs/apex-blueprint/` with `TRACE.md`, `STATE.json` and the six documents below |

Every decision in the templates is a `[[FILL: hint]]` marker. Replace each with content drawn from the user's answers or from real evidence. Nothing is pre-decided or pre-scored. Write the documents in the user's language; the gates check structure, not English keywords.

The ledger exists so that a later session, or the user months from now, can see what was decided and why without re-deriving it.

## The six documents

| File | Purpose |
| :--- | :--- |
| `00-PROJECT-CONSTITUTION.md` | Who it is for, the job to be done, the user's own ideas, hard constraints, what is deliberately out of scope, and the design rules that must hold |
| `01-DISCOVERY-AND-PRFAQ.md` | The decisions taken in discovery, field-specific traps from the domain brief, a short "press release" of the finished result, and the hardest questions with honest answers |
| `02-KANO-SPEC-AND-DELIGHT.md` | Must-haves, multipliers and beyond-expectation additions, with a measurable target and a proof for each |
| `03-ARCHITECTURE-AND-SOPS.md` | Where volatile values live, how history is protected, the key decisions and their reasons, and the operators' routine |
| `04-12M-EVERGREEN-ROADMAP.md` | The build slices (heaviest flow first) and what to expect at 1 week, 1, 3, 6 and 12 months |
| `05-FITNESS-FUNCTIONS-AND-RUNBOOK.md` | The critique log and scorecard (see 03), the checks that keep the system healthy, and the re-review prompt |

## `STATE.json` fields that the gates read

- `slices[]`: each with `status` (`pending` / `done`) and a `verification_proof` when done.
- `c_suite_audit_score`: the critique total. It starts at 0 and is set only by a real critique.
- `change_scenarios[]`, `change_scenarios_required`, `change_scenarios_waiver`: see 08 §4.
- `context_profile`: the answers from 07 Step 0.
