# 07. Completeness Lenses (a DO-CONFIRM sweep for any field)

## Why this exists

Strong models rarely lack intelligence. They lack **thoroughness that survives to the end**. In testing, a strong model asked the user about a critical requirement and then silently dropped it from the build. Another polished a minor flow while the flow carrying most of the user's volume was missing. Neither was a knowledge gap; both were coverage gaps.

These lenses are **not steps**. Think and work however you judge best. Then, before you present a plan or hand anything over, sweep your draft through each lens, the way a pilot runs a checklist after doing the work, not instead of it. The lenses are field-agnostic: they apply equally to a SaaS product, a family clinic, a wedding, a farm co-operative, a school club, a law office, a factory line, a personal budget or a research project.

**When to sweep:**
- lightly, after the first plan;
- fully, before every handover;
- again, after any large change of direction.

**What to record:** the context profile's answers, a one-line `N/A` reason for each rule it switches off, and the lenses that produced a finding. Every finding becomes a row in `TRACE.md` (see 08) with a decided status. A finding that is only mentioned in chat and never tracked counts as dropped.

---

## Step 0: tailor before you sweep (context profile)

Not every rule fits every context. Forcing all of them on everyone is just another rigid frame: it costs time, lengthens replies, and drags in irrelevant work. Applicability depends on **features of the context, not the industry label**:
- a personal finance plan *does* have counterparties (bank fees, early-repayment penalties);
- a large factory's internal training calendar does *not* need a counterparty audit.

Answer these questions in a few seconds, internally. Record them under `context_profile` in the STATE file (`_apex/STATE.json` in LEAN mode):

| # | Profile question | Yes / partly / no |
| :--- | :--- | :--- |
| a | Does money change hands with other parties (customers, suppliers, banks, platforms, members)? | |
| b | Is there personal or sensitive data about anyone other than the user? | |
| c | Is the activity regulated, or does it involve employees, licences, public claims or safety? | |
| d | Do people other than the user operate it or depend on it? | |
| e | Does someone control money or data on behalf of others (members, clients, employees)? | |
| f | Does it replace or correct a process or records that already exist? | |
| g | Is it meant to run for months or more, as opposed to a one-off (an event, a single document)? | |
| h | Is there an established profession or trade with standard practices for this work? | |
| i | Stakes: what is the worst realistic outcome if something is missed? (low / medium / high) | |

**Activation table:** a rule applies when its condition holds. Otherwise mark it `N/A` with a one-line reason. A rule must never be silently skipped, and never be forced.

| Rule | Applies when | Typical N/A |
| :--- | :--- | :--- |
| Lens 3, counterparty audit + own protection | (a) | A study plan with no fees or contracts |
| Lens 4, rules & obligations | Always a quick check; in depth when (c) | Rarely fully N/A |
| Lens 5, data minimisation & retention | (b) | The user's own private notes |
| Lens 6, plausibility checks | Existing data (f), or numeric assumptions in a plan | Nothing numeric yet. Apply it to the assumptions instead |
| Lens 7, governance & conflicts of interest | (e) | A solo personal project |
| Lens 8, people & operations | (d) | Solo and self-operated |
| Second-order: past periods | (f) and a fix corrects something already done | Greenfield |
| Second-order: cost & price | The fix changes cost, and the user sells or budgets | Non-commercial, no budget |
| Second-order: people to inform | (d) | Solo |
| Second-order: the system's own failure; switchover plan | (d) or (g), and an automation or a replaced process (f) | A one-off document |
| Standard instruments of the field (09) | (h) | Genuinely novel activity |
| Change scenarios (08 §4) | Count by (g) and (i); see 08 | A one-off past its date |

**Depth follows stakes (i).** At high stakes, an applicable lens gets real work and proof. At low stakes, one sentence is enough. The profile also tells you what to *leave out* of the reply: a shorter answer that covers what matters beats a longer one that covers everything.

---

## The 12 lenses

| # | Lens | Ask yourself | Examples across fields |
| :--- | :--- | :--- | :--- |
| 1 | **Purpose & stakeholders** | Whose outcome is this? Who pays, who operates, who is affected, who can veto? | School app: students, parents, teachers, principal, ministry. Wedding: couple, both families, vendors, venue. |
| 2 | **Every flow, ranked by weight** | List every flow, channel, actor and device. Rank them by volume, money and risk. Is the heaviest one complete *first*? | 70% of orders via one marketplace; 80% of clinic visits are re-visits; most farm revenue in one harvest month. |
| 3 | **Money** | In and out, timing, debts, deposits, refunds, rounding, currency, taxes, fees, margins. Who absorbs the cost of an error? **Audit the counterparties too:** check every penalty, fee, deduction or invoice others claim from the user against the contract and any legal cap. Also check the user's own protection: their terms with customers, liability caps, insurance. | Unpaid balance hidden in an archive; float rounding on money; a client penalty far above the contract rate and the statutory cap; a SaaS with no liability cap in its terms. |
| 4 | **Rules & obligations** | Which laws, regulations, standards, licences, platform terms, contracts, insurance or accessibility duties apply *in this jurisdiction*, and what changed recently or is coming? | Invoicing/tax rules for the business type; health-data privacy; building permits; food-safety certification; ad disclosure. Date-stamp each and tag certainty. |
| 5 | **Information & records** | What must be recorded, kept unchanged, backed up, deleted or kept private? What is the single source of truth? **Minimise:** every artifact *you* create carries only the personal data it needs. Sensitive identifiers (ID numbers, bank details, health data) are masked or left in a restricted source, never copied into shared files or new channels. Give them a retention and deletion rule. Preserving history is not a reason to spread it. | Issued quotes must not change when prices change; guest ID photos deleted after the legal retention period; a payroll sheet shared with team leads that shows no ID or bank numbers. |
| 6 | **Failure, edge cases & plausibility** | Wrong input, duplicates, missing data, offline, a dependency failing, the key person absent, peak load: how is each detected, contained and recovered? **Sanity-check the data against itself and against field norms:** impossible dates, statuses that contradict their dates, volumes or yields beyond physical norms, stock that cannot exist, claims the user's own data contradicts. Anomalies are where errors and fraud hide. | "Checked out" on a future booking; a yield 2× the regional norm; selling more than the recorded stock; an ad claiming "20% cheaper" that the price list disproves. |
| 7 | **Misuse, safety & governance** | Fraud, abuse, injection, wrong access, physical safety, reputational harm, and conflicts of interest of whoever controls money or data. | Fake bookings; spreadsheet formula injection; payment-diversion emails; the chairman approving his own profit share; a staff member seeing salaries. |
| 8 | **People & operations** | The daily routine and its time budget, the skills needed, training, handover when someone leaves. | A part-time packer; a volunteer team that rotates each semester; an owner who has 15 minutes a day. |
| 9 | **Time & change (12 months)** | What will change: prices, rules, volume, season, team, tools, vendors, the user's goals? Turn each into a scenario you can test or rehearse (see 08). | A material price spike (and how practitioners hedge it); a new sales channel; a tax rate ending; a new mandate such as e-invoicing; enrolment doubling; a vendor shutting down; cash running short before harvest or high season (financing). |
| 10 | **Adoption & friction** | How many setup steps? Which devices? What does the user already use? What does day-1 success look like? | Prefer the user's existing spreadsheet or phone over a new install; offer a one-click launcher. |
| 11 | **Measurement** | How will the user know it works and is improving? Record a baseline plus 1–3 metrics. | Minutes per quote; error rate per month; cash collected within 7 days; visitor-to-click rate. |
| 12 | **Field expertise** | What would a 15-year practitioner of *this* field notice in five minutes that a newcomer would miss? (Build this from the domain brief, 09.) | Material wastage norms in construction; lot/expiry tracking for perishables or cosmetics; seasonality in tourism. |

---

## Second-order sweep (after you have decided the fixes)

A fix often has consequences that are easy to leave unfinished. For each significant change, ask the questions that the context profile activates:

- **Past periods:** if this corrects an error, which past records, payments or customers were affected, and what is the remedy? Example: refund last months' over-deducted contributions, not just fix next month.
- **Cost and price:** who bears the new cost of doing it right, and does a price, quote or budget need to change? Example: compliance raises labour cost by X/month, so the next client quote must include it.
- **People:** who is affected, and who must be told before the change? How should they be told (meeting, message, in their language)? Have a ready-to-send message for each.
- **The system's own failure:**
  - What if the account that owns it leaves?
  - What if an automation silently stops? Add an alarm that fires when nothing happens.
  - Are permissions too broad, e.g. anyone can delete?
  - Has the switchover been rehearsed? Run in parallel (shadow mode) or do a drill ("the key person is off sick this week") before cutting over.

## Closing a finding

A finding is closed by a **fix or a ready-to-use replacement**, not by a warning. "This ad claim is risky" is half the job. "Replace it with this compliant offer" closes it. "This penalty is too high" is half the job. "Here is the contract clause and the statutory cap, and a message to dispute it" closes it.

## How a sweep should feel

- **Fast.** Most lenses take one thought. Spend time only where something turns up.
- **Specific.** "Consider security" is not a finding. "The packer's link exposes revenue totals" is.
- **Weighted.** Fix what carries the most volume, money or risk first (lens 2). Do not gold-plate a minor flow.
- **Honest.** If a lens needs facts you cannot verify (lens 4 especially), record it as a need to verify, with who can confirm it.
