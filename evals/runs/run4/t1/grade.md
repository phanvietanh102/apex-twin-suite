# t1 grade: solo-dev clinic reminder SaaS (A vs B)

Grader ran both deliverables from copies in `t1/grader_tmp/` (A/, B/ untouched).

## 1. What was run

| Check | A | B |
|---|---|---|
| `npm test` (Node 24.14, no install) | 38/38 pass | 26/26 pass |
| Demo | `npm run demo`: Porto calendar → sync → 3 SMS (1 segment, GSM-7) + 1 email + 2 call-list items → patient confirm via link → next-day send. Runs clean. | None (no demo or end-to-end entry point) |
| `tsc --noEmit --strict` (TS 5.8.3, temp install) | Clean (src, test, demo) | Clean with its own tsconfig (needs TS ≥5.8 because of `erasableSyntaxOnly`) |
| Postgres schema | Not run (no Postgres or Docker on the grader machine). Both sides say honestly that it is unrun. | Same |
| Extra scripts | `_apex/unit_economics.py`, `sms_template_check.py` run OK (Python is outside the user's stack, but optional) | — |
| Spreadsheets | None | None |

What exists in code:
- **A** has ingest (Google event → patient/phone), a planner, a dispatcher (claim, quiet hours, deadline, retries, an "uncertain" state, caps, country allow-list, sandbox mode, email fallback), inbound STOP/HELP, confirm links, health alerts, a `Store` interface (in-memory only), `config/settings.json` holding prices, keywords and templates as data, and an append-only `message_log` trigger in the SQL.
- **B** has pure functions: scheduling (DST, late bookings, quiet hours, reschedule reconciliation, retry backoff), calendar parsing (drops descriptions), phone handling, SMS segmenting with transliteration and a cap, templates and tokens, plus a SQL schema with idempotency keys and a `FOR UPDATE SKIP LOCKED` claim query.
- **B has no dispatcher, no inbound handling and no end-to-end run.**
- Neither has a README with an env example, Docker, a seed or migration runner, or row-level security. B has a short README; A has none in the repo.

## 2. Checklist recall

| ID | Item (short) | A | B |
|---|---|---|---|
| 01 | End-to-end core loop, runnable, tested | ✓ (in-memory store, demo plus tests) | ◐ (pieces only, no send/inbound loop) |
| 02 | Runnable repo medium (README, env, migrations/seed, Docker, cheap deploy) | ◐ (no README/env/Docker; AWS deploy) | ◐ (README and schema; no env/Docker/seed; Render + pg-boss fits) |
| 03 | HIPAA BA, BAAs, vendor BAAs, minimum necessary | ✓ | ✓ (turn 1; US then deferred with reasons) |
| 04 | GDPR processor, DPA, subprocessors, Art. 9, EU hosting, transfers | ✓ (2021/915 SCC DPA, Art. 30, DPF note) | ✓ (transfer gap: Twilio/Postmark chosen in turn 2 without SCC/DPF mention) |
| 05 | 10DLC/toll-free, STOP/HELP, consent records, TCPA | ✓ (CANCEL trap, exemption conditions, opt-out log) | ◐ |
| 06 | EU sender ID, per-country price, language, opt-out | ✓ | ✓ |
| 07 | Unit economics, segments, SMS bundles/caps, email default | ✓ | ✓ |
| 08 | Tax/invoicing, MoR, certified invoicing, contabilista | ✓ | ✓ |
| 09 | SMS pumping/abuse mitigations | ✓ (geo allow-list incl. +1 Caribbean, caps, global ceiling, sandbox-before-live; threat not named) | ✓ (names pumping, geo-permissions, mobile-only, caps) |
| 10 | Durable queue, idempotency, retries, DLQ, receipts, alerts, fallback | ✓ | ✓ |
| 11 | UTC + IANA tz, DST, reschedule/cancel, quiet hours, tests | ✓ | ✓ |
| 12 | Tenant isolation (RLS), audit, retention, tested restore | ◐ | ◐ |
| 13 | MFA, roles, no PHI in logs, secrets, breach procedure | ✓ | ✓ |
| 14 | PMS reality, low-friction ingest, Dentrix on-prem difficulty | ✓ | ✓ |
| 15 | Positioning/niche, differentiators | ✓ | ✓ |
| 16 | Success metrics instrumented | ✓ (baseline, monthly "no-shows prevented", cost per message logged) | ◐ |
| 17 | Self-serve onboarding <15 min, defaults, low support | ✓ | ✓ |
| 18 | Solo / 12–15 h / €300 respected | ✓ (AWS is heavier than his stated Render/Fly) | ✓ |
| 19 | Built for change (config-as-data, pluggable channels, WhatsApp) | ✓ | ◐ |
| 20 | Legal pack incl. ToS liability cap, AUP | ◐ (no ToS liability cap or AUP; DPA/BAA/privacy/insurance) | ✓ (ToS liability cap, DPA, privacy, fixed-price lawyer) |
| 21 | 12–24-month regulation watch | ◐ (HIPAA Security Rule update, FCC revoke-all, EU Data Act; no MHMDA/EAA/AI Act) | ✗ |
| 22 | Dated plan back from 28 Feb with beta pricing | ✓ | ✓ |
| 23 | US dental is riskiest path, EU first | ✓ (17 Jan swap rule) | ✓ (drop Austin, decide in June; asks the user) |

**Recall:**
- **A:** 19 ✓ + 4 ◐ = 21/23 = **91%**
- **B:** 16 ✓ + 6 ◐ + 1 ✗ = 19/23 = **83%**

Valid points beyond the checklist:
- **A:**
  - The carrier "CANCEL" opt-out trap in reply instructions.
  - The TCPA healthcare-exemption limits (≤160 chars, 1/day, 3/week) as coded caps.
  - Alphanumeric senders cannot receive replies, so confirmation goes through a link.
  - France HDS and the German §203 secrecy clause.
  - Canadian and Caribbean +1 numbers handled as foreign (fraud and cost).
  - A long clinic name doubling the segment count, checked at sign-up.
  - Twilio SendGrid is not HIPAA-eligible.
  - Texas HB 300 [verify].
  - Portuguese clinics are VAT-exempt, so they bear 23% VAT.
  - Google OAuth sensitive-scope review lead time.
  - Google Workspace Marketplace as a distribution channel.
  - Professional-liability and cyber insurance for a sole trader.
  - At-most-once "uncertain" state.
  - The HHS SRA tool.
  - Recycled numbers as a breach source.
  - SPF, DKIM and DMARC for email.
- **B:**
  - Google OAuth refresh tokens expire after about 7 days in Testing mode (sharp and correct).
  - A shadow-mode week before patients see anything.
  - The parser discards event descriptions, so clinical notes never reach the DB (tested).
  - PT landlines are detected so they get no SMS.
  - A `#nolembrete` opt-out tag.
  - The cousin "paying out of kindness" trap.
  - Unipessoal Lda for liability.
  - The Paddle fee level.
  - DPO question for the lawyer.
  - Sitting with the first 5 clinics for 15 minutes (learning, not sales).

## 3. Silent deferral check (High-weight concerns pushed to "later" with no substance and no agreement)

- **A: 0.** Every open item (Postgres store, BAA, toll-free, MFA, restore test, retention job) has a dated week in the run sheet. Missing ToS liability cap and RLS are omissions, not deferrals.
- **B: 0.** US/HIPAA/10DLC is deferred to June 2027, but with substance (turn 1 explained the duties, turn 2 gave reasons). B also asks the user: "are you OK dropping Austin?". Note: this overrides the user's stated "including those two", openly rather than silently.

## 4. Delivery fit

- Both run in the user's stack (Node/TS) with zero dependencies and no errors, and type-check strictly.
- Both Postgres schemas are unexecuted.
- **A:**
  - Picks AWS (eu-west-1, RDS, SES, End User Messaging) to get one free BAA covering both pilots. This is coherent, but it adds ops surface beyond the "VPS/Render/Fly" he named.
  - Its helper scripts are Python (optional).
- **B:**
  - Picks Render Frankfurt, pg-boss, Twilio, Postmark, Sentry EU and free monitoring, which is a closer fit to his stated hosting preference.
  - States Node 22+ in the turn but 23.6+ in the README (minor).

## 5. Correctness flags

**A:**
- "Fines $500–1,500 per message": these are TCPA statutory damages, not fines.
- "A phone number in Sentry counts as a breach" is overstated. It is a presumed breach subject to a risk assessment.
- The TCPA exemption conditions omit "free to the end user" (tagged verify).
- AWS toll-free from eu-west-1 is tagged verify.
- Render/Fly BAA availability is tagged verify (unverified).
- Otherwise accurate and well tagged.

**B:**
- Claims EU data residency but sends message content through Twilio and Postmark (US) without mentioning SCC/DPF in turn 2.
- SMS price is tagged as unverified.
- Otherwise accurate: HIPAA not applicable for EU-only, Paddle MoR, AT-certified invoicing, Google 7-day token, UCS-2 maths.

## 6. Scores (1–10)

| Criterion | A | B |
|---|---|---|
| Beyond-knowledge insight | 9 | 8 |
| Correctness | 8 | 8 |
| Fit to constraints | 8 | 8 |
| Progress (working artifacts) | 8 | 6 |
| Low friction | 7 | 7 |
| Overall wow | 9 | 7 |
| **Total /60** | **49** | **44** |

## 7. Friction metrics

| | A | B |
|---|---|---|
| Words turn 1 / turn 2 | 930 / 1,328 | 1,334 / 1,959 |
| Extra reading | LAUNCH-PLAN 1,827, DOMAIN-BRIEF 2,300, TRACE 1,503 words | README 101 words |
| Setup to run | 1 step: `npm test && npm run demo` (Node ≥22.18) | 1 step: `npm test` (Node ≥23.6) |
| Installs beyond stack | AWS account and services; Python for optional helper scripts | None beyond Render-type hosting; SaaS accounts (Twilio, Postmark, Sentry, Healthchecks) |
| Questions left to user | 1 (the cousin's software) | 2, non-blocking (name/domain, OK to drop Austin) |

## 8. Verdict

A delivered more after two turns. It built a runnable end-to-end reminder engine: ingest, plan, dispatch with caps and quiet hours, inbound STOP and confirm link, and a call list. It has 38 tests and a demo, plus a tight dated run sheet and unusually deep, well-tagged domain traps (the CANCEL opt-out word, TCPA caps, sender IDs that can't take replies, +1 Caribbean numbers, HDS and §203). It keeps Austin in scope behind a dated fallback, as the user asked.

Its weaknesses:
- No ToS liability cap.
- AWS as host, which is heavier than the user wanted.
- A sprawling set of side documents.

B gave clearer, more focused advice that fits his hosting preference well: Portugal-first, the Google 7-day refresh-token trap, shadow mode, and a ToS liability cap. But its code is only tested building blocks with no dispatch or inbound loop, it has a gap on transfers to US vendors, and it has no regulation watch.

Both are honest about what is unverified. A is ahead.
