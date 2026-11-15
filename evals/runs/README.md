# Eval runs 3 and 4: raw evidence

Everything here is synthetic. The businesses, people, phone numbers, ID numbers and bank details in the fixtures were invented by the scenario author for testing; none refers to a real person or organisation.

Each scenario folder contains:

| File | What it is |
| :--- | :--- |
| `scenario.md` | The two user messages (Turn 1 and Turn 2) |
| `checklist.md` | The hidden, weighted answer key, written before either assistant ran |
| `fixture/` | The messy workspace the user pointed at (existing-workspace scenarios only) |
| `A/turn1.md`, `A/turn2.md`, `B/…` | The two assistants' replies, as the blind grader saw them |
| `grade.md` | The blind grader's report: scores, per-item recall, evidence |

`MAPPING.txt` in each run says which side had the skill. Graders did not see it.

Not included: the files each assistant built (`work/` folders, up to 12 MB per side) and the graders' temporary copies. Local machine paths were replaced with `<scratch>`, `<repo>` and `<home>`.

These scenarios are now public, so they no longer count as unseen. Draw fresh ones for the next eval.
