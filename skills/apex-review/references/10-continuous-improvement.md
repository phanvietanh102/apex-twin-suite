# 10. Continuous Improvement Mode ("it already works — make it better every day")

## When to use it

The owner says the system already works ("đang chạy ổn", "it's fine, but…"), or asks how to keep improving it, or the review finds no urgent breakage. Many of the highest-value upgrades hide in workflows their owners believe are already as good as they can be. They are not broken; they quietly cost minutes, money or risk every day, and the owner does not know a better way exists.

The aim is not a one-off fix. It is to leave the owner with a **measured baseline, a ranked list of improvements, and a habit of measuring and improving**, sized to their time.

---

## The loop

1. **Baseline (measure before changing anything).** Pick 2–4 metrics that matter to *this* owner. Measure them from the workspace's own data where possible; otherwise ask for a quick estimate and mark it as such. Good candidates:
   - minutes per unit of work (per quote, order, report, lesson, patient intake);
   - error or rework rate (wrong prices, duplicate orders, missing fields);
   - money leakage (unpaid balances, underpricing, unused subscriptions, fees);
   - lead time (request → delivered);
   - risk exposure (unprotected records, a single person who knows how something works).
2. **Find improvements with the completeness lenses** (07), weighted toward lens 2 (heaviest flow), 3 (money), 6 (failures) and 11 (measurement). Add the practitioner's checklist from the domain brief (09). Ask: *what do the best operators in this field do that this workspace does not?*
3. **Rank by ROI:** estimated gain per month ÷ effort to build and to maintain. Show the top 3–5 to the owner as a short table: gain, effort, risk, recommendation. Low-effort, high-gain items go first, even if unglamorous.
4. **Implement the top items as slices,** each with a before/after measurement on the same metric, a parity check, and a `TRACE.md` row.
5. **Instrument:** where cheap, make the workspace measure itself, e.g. a log row per job, a monthly summary, a reminder when a metric drifts. The owner should never need to count by hand again.
6. **Hand over the habit:**
   - **`IMPROVEMENT-LOG.md`**, in the owner's language: date, change, metric before → after, notes.
   - **A re-review prompt** the owner can paste every 1–3 months, e.g. "Đọc IMPROVEMENT-LOG.md và số liệu 3 tháng qua; so với baseline; đề xuất 3 cải tiến tiếp theo theo ROI."
   - **The next 2–3 candidate improvements** already identified, so the next session starts warm.

---

## Guardrails

- Never trade protected history, or a habit the owner called sacred, for an efficiency gain without their explicit agreement.
- Do not over-engineer. A 5-minute daily saving that needs a 2-hour weekly upkeep is a loss.
- Report gains in the owner's terms (time, money, fewer mistakes), with the measurement behind them.
