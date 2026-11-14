# 07. Completeness Lenses (a DO-CONFIRM sweep for any field)

## Why this exists

Strong models rarely lack intelligence. They lack **thoroughness that survives to the end**. In evals, a strong model asked the user about a critical requirement and then silently dropped it from the build. Another polished a minor flow while the flow carrying most of the user's volume was missing. Neither was a knowledge gap; both were coverage gaps.

These lenses are **not steps**. Think and work however you judge best. Then, before you present a plan or hand anything over, sweep your draft through each lens, the way a pilot runs a checklist after doing the work, not instead of it. The lenses are field-agnostic: they apply equally to a SaaS product, a family clinic, a wedding, a farm co-operative, a school club, a law office, a factory line, a personal budget or a research project.

**When to sweep:**
- lightly, after the first plan;
- fully, before every handover;
- again, after any large change of direction.

**What to record:** only the lenses that produced a finding. Every finding becomes a row in `TRACE.md` (see 08) with a decided status. A finding that is only mentioned in chat and never tracked counts as dropped.

---

## The 12 lenses

| # | Lens | Ask yourself | Examples across fields |
| :--- | :--- | :--- | :--- |
| 1 | **Purpose & stakeholders** | Whose outcome is this? Who pays, who operates, who is affected, who can veto? | School app: students, parents, teachers, principal, ministry. Wedding: couple, both families, vendors, venue. |
| 2 | **Every flow, ranked by weight** | List every flow, channel, actor and device. Rank them by volume, money and risk. Is the heaviest one complete *first*? | 70% of orders via one marketplace; 80% of clinic visits are re-visits; most farm revenue in one harvest month. |
| 3 | **Money** | In and out, timing, debts, deposits, refunds, rounding, currency, taxes, fees, margins. Who absorbs the cost of an error? | Unpaid balance hidden in an archive; float rounding on money; platform fee changes; deposit forfeiture rules for an event. |
| 4 | **Rules & obligations** | Which laws, regulations, standards, licences, platform terms, contracts, insurance or accessibility duties apply *in this jurisdiction*, and what changed recently or is coming? | Invoicing/tax rules for the business type; health-data privacy; building permits; food-safety certification; ad disclosure. Date-stamp each and tag certainty. |
| 5 | **Information & records** | What must be recorded, kept unchanged, backed up, deleted or kept private? What is the single source of truth? | Issued quotes must not change when prices change; patient records retention; student grades history. |
| 6 | **Failure & edge cases** | Wrong input, duplicates, missing data, offline, a dependency failing, the key person absent, peak load. For each: how is it detected, contained and recovered? | Duplicate orders from chat; supplier no-show on event day; internet down at a clinic counter. |
| 7 | **Misuse & safety** | Fraud, abuse, injection, wrong access, physical safety, reputational harm. | Fake bookings; spreadsheet formula injection; unsafe DIY renovation step; a staff member seeing salaries. |
| 8 | **People & operations** | The daily routine and its time budget, the skills needed, training, handover when someone leaves. | A part-time packer; a volunteer team that rotates each semester; an owner who has 15 minutes a day. |
| 9 | **Time & change (12 months)** | What will change: prices, rules, volume, season, team, tools, vendors, the user's goals? Turn each into a scenario you can test or rehearse (see 08). | A material price spike (and how practitioners hedge it); a new sales channel; a tax rate ending; a new mandate such as e-invoicing; enrolment doubling; a vendor shutting down; cash running short before harvest or high season (financing). |
| 10 | **Adoption & friction** | How many setup steps? Which devices? What does the user already use? What does day-1 success look like? | Prefer the user's existing spreadsheet or phone over a new install; offer a one-click launcher. |
| 11 | **Measurement** | How will the user know it works and is improving? Record a baseline plus 1–3 metrics. | Minutes per quote; error rate per month; cash collected within 7 days; visitor-to-click rate. |
| 12 | **Field expertise** | What would a 15-year practitioner of *this* field notice in five minutes that a newcomer would miss? (Build this from the domain brief, 09.) | Material wastage norms in construction; lot/expiry tracking for perishables or cosmetics; seasonality in tourism. |

---

## How a sweep should feel

- **Fast.** Most lenses take one thought. Spend time only where something turns up.
- **Specific.** "Consider security" is not a finding. "The packer's link exposes revenue totals" is.
- **Weighted.** Fix what carries the most volume, money or risk first (lens 2). Do not gold-plate a minor flow.
- **Honest.** If a lens needs facts you cannot verify (lens 4 especially), record it as a need to verify, with who can confirm it.
