# 09. Domain Discovery Protocol (works for any field, country or context)

## Why this exists

No static playbook can cover every industry, country, niche and personal situation a user may bring. A model's general knowledge is broad but thin at the edges: local law, current rates and fees, practitioner norms, seasonality. Those edges are exactly where users get hurt, and exactly where they would say "wow, I didn't know that."

So instead of looking up a fixed playbook, **build a short domain brief for this user's exact context** before committing to a plan. Then use it to drive Turn-1 findings, lens 12, and the change scenarios.

The 7 archetypes in `02-*` are worked examples of what a good brief contains. They are **not a boundary**. The same protocol applies to agriculture, a dental clinic, a tutoring centre, a festival, logistics, a nonprofit, a law firm, a hotel, a personal investment plan, a PhD project, a public-sector service, or a hybrid none of these names cover.

---

## The brief (about one page; internal unless showing it helps the user)

1. **Context identity:**
   - field and sub-niche;
   - **jurisdiction** (country, region, city);
   - scale (solo / team / organisation; volumes);
   - business, public or personal;
   - the user's language and literacy with tools.
2. **Value chain & actors:** who supplies, who decides, who pays, who uses, who regulates.
3. **Money model & norms:** how value and money flow, plus typical unit economics, prices, margins, fees and benchmarks. Give ranges and sources, not single precise numbers.
4. **Rules:** the regulators, laws, standards, licences and platform policies that apply. For each:
   - the identifier (law or decree number, standard name) and its effective date;
   - a certainty tag (`known` / `likely` / `verify`);
   - anything that **changed in the last 1–2 years or is scheduled to change**.
5. **The practitioner's checklist:** 5–10 things an experienced person in this field always checks. Prompt yourself: *"What would a 15-year veteran notice in five minutes that a newcomer would miss?"*
   - **Standard instruments first.** For each core process, ask *"what instrument does this field already use for exactly this step?"* before inventing a custom one. Examples: bundle tickets for piece-rate work in garment factories; a key-dates register with a second-person check in law firms; a channel manager or iCal sync for multi-OTA lodging; an allergen matrix tied to recipe versions in food.
   - Custom solutions that ignore the field's standard instrument lose to it. Adopt the standard and improve on it.
6. **Typical failure modes & seasonality:** how projects like this usually fail, and when the field's peaks and troughs occur.
7. **The next 12–24 months:** strong models under-cover what is coming. In eval run 3, both the skill and the plain model missed price risk, cheaper financing and upcoming mandates. Cover:
   - **scheduled changes:** new mandates (e-invoicing, reporting, licensing, labelling), rates that expire or change, platform policy shifts;
   - **money over time:** price volatility of the key inputs and outputs and how practitioners hedge it (contracts, timing, buffers); working-capital and financing options typical for this field (supplier credit, preferential or cooperative loans, prepayments, deposits);
   - **growth path:** what the user's stated long-term goal requires that is not in place yet (a certification, a licence, a data history, a reputation asset), so that today's design does not block it.
8. **Tools the field already uses:** the software, forms, marketplaces and associations people already rely on. Integrating with what exists usually beats replacing it.
9. **Unknowns to verify:** a list, each with *how* to verify it (ask the user, an official source, an accountant or lawyer, the platform's help centre).

---

## Sources, in order of trust

1. The **user's own files and words** for local reality. Users know their market; ask one open question that invites what you could not know.
2. **Official or regulator sources and primary documents,** if a web or search tool is available. Record the date.
3. Your own knowledge, tagged by certainty.
4. Reputable practitioner sources (industry associations, established guides).

## Honesty rules

- Never invent a law number, rate or date. If you are unsure, describe the rule in general terms and mark it `verify`, naming who can confirm it.
- Prefer "as of <date>, X; check whether it has changed" over a confident absolute.
- When a rule has a threshold (revenue, headcount, size), say which side the user appears to be on **and why**, rather than asserting it.

## How the brief feeds the work

- **Turn 1:** 2–4 of the most valuable, specific brief items become the opening findings.
- **Lens 12:** the practitioner's checklist becomes the field-expertise lens.
- **Change scenarios:** items from rules (scheduled changes), money over time (price volatility, financing) and seasonality become 12-month tests.
- **`TRACE.md`:** anything in the brief that creates work becomes a row.
