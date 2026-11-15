I picked the approach, built the core of the product, and an independent reviewer then found 10 flaws in it, which I fixed. Here's where it stands:

- **Positioning:** *patient reminders for clinics that run on Google Calendar.* Google Calendar doesn't remind patients, while Dentrix and similar systems already do. Signing up is just "connect your calendar", which fits your no-sales-calls rule.
- **Built:** the reminder engine in TypeScript (`clinic-reminders/`). **38 tests pass** and `npm run demo` processes a Porto-style calendar from start to finish.
- **Not built yet:** the Postgres storage, Google sign-in, the real AWS SMS/email connections, the dashboard and sign-up. Each has a week in the plan.
- **Plan:** `LAUNCH-PLAN.md` is now a 2-page run sheet. It has weekly tasks up to 28 Feb, the exact legal and business steps within your €1,000, and pricing.
- **Your next 7 days:** about 4 h of business setup that takes weeks to come back (list below), plus the Postgres storage.

## How the engine handles your four fears

**1. Health data.** You are a "processor" in the EU and a "business associate" in the US. In practice that means two documents, both available free from the regulators:
- **EU:** the EU's official template for data-processing agreements (Decision 2021/915).
- **US:** HHS's sample BAA provisions.

Spend about €400 on one hour with a US health-privacy lawyer, who reviews the BAA and the SMS wording together. The AWS BAA is self-serve and free.

In the code:
- Messages contain only clinic, date, time and a link, never a name or treatment.
- Each region uses its own SMS/email accounts and link domain.
- The confirm token is never stored in a usable form.
- The engine will **not** text a number it isn't sure about. The reviewer found real cases: an insurance ID read as a phone number, two numbers in one event, a physio's email taken for the patient's, and two patients with the same name. All are now tested.

**2. The SMS bill.** There are seven separate limits:
- a monthly cap for each clinic;
- at most 1 SMS per patient per day and 3 per week;
- a global ceiling of 400 SMS a day (about €18);
- a list of countries you allow texting to (Canadian and Caribbean "+1" numbers no longer count as US);
- a daily limit on test sends;
- sign-up refuses a clinic name long enough to make every SMS cost double;
- Portuguese accents are swapped for plain letters.

On that last one: ã, õ, á and lowercase ç push an SMS into a costlier format with **2–3× the cost**. In the tests, a Portuguese reminder went from 2 segments to 1.

**3. Being woken at 3am.** Nothing is ever sent between 20:00 and 09:00, and reminders go out the day before at 10:00. So a crash at 3am is caught up after breakfast, and that is tested. Anything that can't go out in time lands on the **front-desk call list**. You get alerts by email, during the day only.

**4. Building something nobody pays for.**
- Porto goes live on **6 Dec**, with their no-show rate from the 4 weeks before recorded so the improvement can be shown.
- Paid from month 2 at the founding price.
- The honest maths for your €5k goal: at about €75 per clinic per month, you need **65–90 clinics**, roughly 7 new ones a month from March. Getting clinics is the real risk, so the plan includes a distribution track.

## Decisions I made (say the word to change any)

- **Hosting:** one AWS deployment in Ireland for both pilots. You get one BAA and EU data stays in the EU; HIPAA doesn't require US hosting. Render and Fly don't sign BAAs on cheap plans [verify]. Expected cost is about €40–60/month plus SMS, well under €300.
- **Stack:** Node 24 + TypeScript, Postgres, a single process, React. No Redis and no queue service.
- **Patients confirm via a link in the SMS.** Portuguese SMS from a sender name like "FisioPorto" can't receive replies. US STOP/HELP replies are handled too. A reply like "I need to cancel tomorrow" both opts the patient out (US law requires it) **and** goes to the clinic.
- **Billing through Paddle**, which acts as the legal seller: it handles EU VAT and Texas sales tax and invoices the clinics. As a sole trader you then invoice only Paddle, once a month, through Portal das Finanças. Stripe receipts aren't valid Portuguese invoices [confirm with a contabilista].
- **Pricing:** €24 per practitioner per month in the EU (250 SMS included), $49 per provider in the US (400 included). The Porto clinic would pay €72, with about a 57% margin after SMS. A US dental practice gives about an 86% margin, so US clinics are worth about 3× more each.
- **Austin:** Dentrix usually runs on the practice's own server, and connecting to it needs Henry Schein's developer program, which isn't realistic before February. If their appointments can't reach us automatically by **17 Jan**, I'd swap them for a 4th Porto clinic and bring Austin in later.

## What to do this week (about 4 h, all slow to come back)

1. **AWS:** create the account, accept the BAA in AWS Artifact, request SMS production access and a higher spend limit.
2. **Google Cloud:** create the project and submit the OAuth consent screen for verification. Calendar access counts as a "sensitive" permission, so review can take weeks; until then users see a warning screen.
3. **Domain:** buy a short link domain. A long one pushes SMS over 1 segment.
4. **Insurance:** ask for professional-liability plus cyber quotes. As a sole trader you're personally liable.
5. **Porto clinic:** ask the 3 physios for 3 clinic names each.
6. **Code:** a Postgres version of the `Store` interface, built against `db/schema.sql`. Rerun the 38 tests against Postgres in Docker. I couldn't run Postgres here, so **the schema is written but has not been run**.

Run it: `cd clinic-reminders && npm test && npm run demo` (Node ≥ 22.18, no npm install needed).

## Proven so far

| You need | Where it is | How it was checked |
| :--- | :--- | :--- |
| Reminders at the right local time, in Lisbon and Austin | `planner.ts`, `time.ts` | Tests, including the March 2027 weeks when US and EU clocks change on different dates |
| Never a double or wrong-person SMS | `dispatcher.ts`, `ingest-google.ts` | Tests for repeated syncs, crashes, rescheduling 3×, and the 10 review findings |
| SMS bill capped | `dispatcher.ts`, `config/settings.json` | Tests for the caps, the +1 country check, the test-send limit and long clinic names |
| No 3am fixes | `dispatcher.ts`, `health.ts` | Tests for overnight catch-up, the deadline-to-call-list rule and stalled-worker alerts |
| Prices editable without rewriting history | `config/settings.json`, message log | Test: a price +20% leaves old entries unchanged |

## One thing only you can find out

**Ask your cousin:** which practice software they run (Dentrix G-series, Dentrix Ascend, or something else), what currently sends their reminders, and whether anyone puts appointments into Google Calendar. One line of answer is enough. It decides how Austin's appointments get in, and whether Austin stays in the first five.

## Files created
- `clinic-reminders/package.json`: test and demo scripts, no dependencies
- `clinic-reminders/config/settings.json`: everything that changes over time (prices, limits, keywords, templates, plans)
- `clinic-reminders/src/`:
  - `config.ts`, `sms-text.ts`, `time.ts`, `phone.ts`, `model.ts`
  - `ingest-google.ts`, `planner.ts`, `messages.ts`, `dispatcher.ts`
  - `inbound.ts`, `engine.ts`, `store.ts`, `providers.ts`, `health.ts`
- `clinic-reminders/test/`:
  - `helpers.ts`, `text-config-phone.test.ts`, `ingest.test.ts`
  - `scheduling.test.ts`, `red-team-fixes.test.ts` (38 tests)
- `clinic-reminders/demo/porto-calendar.json`, `clinic-reminders/demo/run-demo.ts`: complete run on a Porto-style calendar
- `clinic-reminders/db/schema.sql`: Postgres tables, with locks that stop region and message-log rows being edited (not yet run against a real Postgres)
- `LAUNCH-PLAN.md`: replaced by the v2 run sheet
- `_apex/TRACE.md`: updated list of every requirement with its status, plus 6 change scenarios that passed
- `_apex/DOMAIN-BRIEF.md`: added Portugal/Texas specifics
