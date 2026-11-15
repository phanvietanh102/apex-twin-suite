That's everything I needed. I've made the calls and started the build: the core reminder logic is written and tested (26 passing tests), and the plan below runs from Monday to 28 February.

## The decisions

| Decision | My call | Why |
|---|---|---|
| First market | **Portugal only** (EU/GDPR) | You live there, speak the language, and your first clinic is there. One legal regime, one time zone, no HIPAA. |
| How appointments get in | **Google Calendar, read-only** | The Porto clinic already uses it, and so do lots of small physios, psychologists and osteopaths. No PMS integrations before March. |
| What patients get | **One reminder the day before at 10:00 clinic time.** SMS if there's a mobile number, plus email if there's an address. | Simple, and it keeps all sending inside your working day (see fear 3). |
| Confirm / cancel | **A link in the message** (`/r/<token>`), not SMS replies | Works over SMS *and* email, avoids two-way SMS numbers, and gives the clinic a dashboard: "Tomorrow: 23 appointments, 18 confirmed, 2 cancelled, 3 no answer." The front desk only calls the 3. That's the "less phone time" promise. |
| Pricing | **€25 per practitioner calendar per month, 200 SMS per seat (pooled). Founding price €19, locked for 12 months, for the first 10 clinics.** 14-day trial with 25 SMS. | Price scales with SMS usage. Porto clinic = 3 seats = €57/month. One prevented no-show per physio per month pays for it. |
| Billing | **Paddle (merchant of record)** | They handle VAT and invoice the clinics. You invoice Paddle once a month, which saves you from wiring Stripe into AT-certified Portuguese invoicing yourself. Confirm with your accountant. |
| Stack | Node 22+/TypeScript, Fastify, React (Vite), Postgres, **pg-boss** for jobs (no Redis), one repo with a web process and a worker process | Boring and familiar, with one database to back up. |
| Hosting | Render, **Frankfurt region**: web + worker + managed Postgres | EU data, managed backups, no server to patch. |
| Vendors | Twilio (SMS), Postmark (email), Sentry (EU region, PII scrubbing on), Healthchecks.io, UptimeRobot | All have DPAs. The free tiers cover monitoring. |

## The one change to your plan: Austin

I'd **leave the Austin practice out of the February target** and count 5 Portuguese clinics instead. Here's why:

- Serving them makes you a HIPAA business associate: BAAs with them and with every vendor, US SMS registration (A2P 10DLC), a US data setup. That's a second compliance project on 12–15 h/week.
- If they use Dentrix, integration means going through Henry Schein's developer program, which is slow, usually paid, and built around a server in the office. Not a February job.
- A 4-person front desk on Dentrix very likely **already has reminders**, either built in or through an add-on. Then your cousin would be paying out of kindness, which is exactly the trap behind your fear 4.

This week, ask your cousin two things: *which software exactly, and what do you use for reminders today?* If they have nothing, the US becomes a good second market for later in 2027. I'd schedule that decision for **June 2027**, not now.

## Your four fears, handled in the design

**1. Health data.** Plain version:
- **GDPR applies to you. HIPAA doesn't**, as long as you only serve EU clinics. HIPAA only kicks in when you work for US healthcare providers.
- Under GDPR the clinic is the *controller* and you're the *processor*. You need: a **DPA** (Art. 28) signed with each clinic at sign-up (a click-through is fine), a public **subprocessor list** (Render, Twilio, Postmark, Paddle, Sentry), EU hosting, security measures, and a duty to tell the clinic about a breach without delay. The clinic then reports to the CNPD.
- **Collect as little as possible.** That's the biggest protection you have, and it's already built in. The calendar parser reads the event description *only* to find a phone/email, then throws it away. Notes like "lombalgia" never reach your database (there's a test for this). Messages say only when and where. Appointments are deleted 30 days after the date, and patients 12 months after their last visit.
- **Spend the €1,000 on:** a Portuguese lawyer who does tech/GDPR for (a) Terms of Service with a **liability cap** (fees paid in the last 12 months), (b) the DPA, (c) the privacy policy, (d) one hour reviewing your data flow, including whether you need a DPO. Ask for a fixed price.
- **Ask your accountant** about moving from sole trader (unlimited personal liability) to a **Unipessoal Lda** once you have paying clinics. That and the liability cap are what actually protect your house.

**2. SMS bill.** Four layers, mostly already coded:
- **Accents cost money.** One "ã" or "ç" switches an SMS to UCS-2: 70 characters per segment instead of 160, so a normal reminder costs 2–3×. The default template is transliterated to GSM-7 ("terça" → "terca"; "às" survives) and must fit **1 segment** or it isn't sent.
- **Hard cap per clinic per month.** When it's hit, reminders fall back to email and the owner gets an "upgrade" email. Never an open-ended bill.
- **SMS only to the clinic's own country and only to mobiles.** This blocks SMS-pumping fraud through self-serve trials.
- At the account level: restrict Twilio's geo-permissions to Portugal and set usage alerts.

Rough cost: about 140 appointments per practitioner per month × roughly €0.04–0.06 per segment ≈ €6–8 per €25 seat. I can't check live prices from here, so look up Portugal in Twilio's pricing before you fix the plan.

**3. 3am pages.** Reminders go out at 10:00 the day before, and nothing is sent between 20:00 and 09:00. If the worker dies at 3am, it doesn't matter: nothing was due. When it comes back it sends whatever is still worth sending, and every failure has ~20 hours of slack. Monitoring: the worker pings Healthchecks.io every 5 minutes. At 10:30 a self-check alerts you if any reminder due before 10:00 is still unsent. A revoked Google connection emails the *clinic* automatically. Double sends are blocked by a unique key in the database, and crashed sends are marked "unknown" and checked with the provider, never blindly resent.

**4. Building something nobody pays for.** Gates with dates:
- **This week:** the Porto clinic agrees to €57/month from February *if* it works. Get that yes before you write the UI.
- **Shadow mode first:** for a week, the system only emails the clinic owner "here's what I *would* have sent tomorrow." It's a free check on parsing, and no patient sees a mistake.
- **31 January:** at least 3 clinics live. If not, figure out why before building anything else.
- **1 June 2027:** at least 25 paying clinics. €5k MRR is about 200 seats, or 65–80 clinics. That's ambitious for Portugal alone in 12 months, so June is when you'd add Spain, Outlook, WhatsApp or the US based on what customers ask for.

## Money

Fixed costs come to about **€70–90/month**: Render ~€45–60, Postmark ~€15, domain + email ~€8, monitoring on free tiers. SMS is passed through via the seat price, and Paddle takes about 5% + €0.50 per transaction. That's well under your €300.

## Plan to 28 February (~13 h/week, ~190 h)

| Dates | Build | Business |
|---|---|---|
| **16–22 Nov** | Repo, DB, Google Cloud project | Porto clinic visit (checklist below), Austin questions, book lawyer, accountant call, buy domain |
| **23 Nov – 6 Dec** | Google sign-in + calendar connect, sync (incremental, every 10 min), parser, "fix contacts" list, **shadow mode** | Landing page + privacy policy live (needed for Google verification) |
| **7–13 Dec** | Sending worker (pg-boss), email + SMS, confirm/cancel page, opt-out, monitoring | **Submit Google OAuth verification** (see note) |
| **14–20 Dec** | Fixes from shadow week | **Porto clinic live** with real reminders |
| 21 Dec – 3 Jan | Buffer / holidays | Lawyer docs arrive |
| **4–24 Jan** | Self-serve onboarding, clinic dashboard, Paddle checkout, retention jobs, daily "tomorrow" digest | Outreach: ask Porto clinic for 3 intros, contact ~40 small clinics in Porto (physio, psychology, osteopathy, podiatry) that book by phone/WhatsApp |
| **25 Jan – 7 Feb** | Polish what clinics trip over | Clinics 2–3 live; Porto converts to paid 1 Feb |
| **8–28 Feb** | Only fixes, no new features | Clinics 4–5 live and paying |

**Google verification note:** reading calendars is a "sensitive" scope. While your OAuth app is in *Testing* mode, refresh tokens expire after about 7 days, so syncs would silently die every week. Publish the app (the unverified warning screen is OK for a handful of clinics) and submit for verification in early December. It needs your homepage and privacy policy live and can take a few weeks.

**Self-serve vs. no sales calls:** the product is built for self-serve sign-up. Still, sit next to the first 5 clinics for 15 minutes while they set it up. That isn't sales. It's where you learn what to fix so clinic #20 never needs you.

**Not before March:** US/HIPAA, any PMS integration, Outlook, WhatsApp, SMS replies, online booking, waitlists, mobile app, multiple reminders per appointment.

## What I built

The core logic lives in a dependency-free TypeScript project. Node 24 runs it directly with `npm test`, and all 26 tests pass:

- **Scheduling:** day-before at 10:00 local time, correct across DST (Lisbon and Chicago tested), late bookings, quiet hours, reschedule/cancel reconciliation, retry backoff that gives up before it's too late.
- **Calendar parsing:** "João Silva - 912345678" → name + E.164 number. Skips lunch/holidays/all-day events and `#nolembrete`. Drops descriptions.
- **Phone numbers:** PT/ES/FR/GB/US. Porto landlines are recognised as non-mobile, so no SMS goes to them.
- **SMS:** segment counting, GSM-7 transliteration, per-clinic cap and country guard.
- **Messages:** PT/EN templates limited to when/where, and unguessable confirm/cancel tokens.
- **Postgres schema** with the unique keys that prevent double sends, plus the worker's claim query.

Not done or not verified yet: the schema hasn't been run against a real Postgres (none here), I didn't type-check with `tsc` (no packages installed, no network), and there's no web app, worker or Google/Twilio wiring yet. That's the 23 Nov – 13 Dec block.

## Your to-dos this week

1. **Porto clinic visit (1 hour):**
   - Look at their actual calendar entries. Do titles hold name + phone, or just a name?
   - Count no-shows over the last 4 weeks.
   - Ask how they remind patients today and how many minutes a day it takes.
   - Ask which patients prefer English.
   - Agree on the €57/month from February *if it works*.
   - Ask for 3 intros to other clinics.
2. **Cousin:** which software, and what do they use for reminders today?
3. **Lawyer:** book a fixed-price ToS + DPA + privacy policy + 1 h review.
4. **Accountant:** Paddle as merchant of record, VAT, and when to move to Unipessoal Lda.
5. **Accounts:** domain, Google Cloud project, Twilio (check the Portugal price and whether alphanumeric sender IDs need registration), Postmark, Paddle (approval needs live pricing, terms and refund pages).

Two quick questions, and neither blocks the next step: **do you have a product name/domain in mind**, and **are you OK dropping Austin from the February count?** Once you're back from the Porto clinic, tell me how they write their calendar entries and I'll tune the parser and start on the Google connect + sync code.

## Files created

All under `<scratch>/eval4/t1/B/work/clinic-reminders/`:

- `package.json`, `tsconfig.json`, `README.md`
- `db/001_init.sql`
- `src/core/time.ts`
- `src/core/schedule.ts`
- `src/core/phone.ts`
- `src/core/calendarEvent.ts`
- `src/core/sms.ts`
- `src/core/message.ts`
- `src/core/schedule.test.ts`
- `src/core/parsing.test.ts`
- `src/core/messaging.test.ts`
