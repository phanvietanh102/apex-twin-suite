Yes. Here's where it stands so far:

- **Main finding:** sending the SMS is the easy part. The harder parts are getting appointments into your system without the front desk retyping them, and the legal and carrier rules around sending (detailed below).
- **What I built:** a first-draft launch plan (`LAUNCH-PLAN.md`). It covers which market to start in, the order to build things, the architecture choices that are cheap now and expensive later, a compliance checklist for each market, pricing math, a script for talking to clinics, and a 30-day plan. I also wrote two small scripts that check the numbers and the message templates.
- **Your next step:** answer the 3 questions at the bottom. That decides whether you start in the US or one EU country, and which specialty, and then we build the first piece.

---

## Four things that will shape this product

**1. Your real competitor is the clinic's own scheduling software.**
- Dentrix, Open Dental, WebPT, Jane, Cliniko, SimplePractice and Doctolib all send reminders already, and so do US dental vendors like Weave and RevenueWell.
- So the flow that carries all your volume is **getting appointments in without double entry**: calendar sync or CSV import first, then one integration with whatever software your first clinics actually use.
- If the front desk has to retype appointments, clinics usually drop the tool within weeks.

**2. In the US you'll be a HIPAA "business associate", and that limits which vendors you can use.**
- Clinics will need you to sign a business associate agreement (BAA). In turn, you need a BAA from **every** vendor that touches patient data: hosting, SMS, email, and also your error tracking and logs.
- Some popular email APIs don't sign BAAs. For example, Twilio SendGrid has historically been outside Twilio's list of HIPAA-eligible services [verify].
- A phone number plus "appointment at a therapy practice" showing up in Sentry counts as a breach. Check BAA availability before you write any integration code.

**3. US SMS has two traps that newcomers rarely see coming.**
- **Registration delay:** you must register each clinic for business texting (10DLC, or toll-free number verification) before its messages will go through. Approval takes days to weeks, so a 14-day trial can expire before the first SMS is ever sent.
- **The "CANCEL" trap:** carriers treat CANCEL, END and QUIT as opt-out words. If your reminder says "Reply CANCEL to cancel", a patient who replies is unsubscribed from *all* future reminders. Use "Reply C to confirm, R to reschedule".
- **Legal limits:** to stay within the TCPA's healthcare exemption, keep reminders to 160 characters or fewer, at most 1 per day and 3 per week, with no marketing [verify the exact conditions with a US attorney]. Fines are $500–1,500 per message, and class actions are common.

**4. "The EU" is really 27 markets, and SMS there costs 5–10× more.**
- I checked the cost math with a script (`_apex/unit_economics.py`). For a 3-practitioner physio clinic, SMS costs about **$11–24 a month in the US but €47–80 a month in a Germany-like country**, so a flat "€49, unlimited SMS" plan loses money.
- **Language changes the price.** In my test, a German reminder fit in 1 message. A Polish one of the same length needed 2, because a single "ł" switches the whole SMS to a costlier format.
- **Each country has its own extra rules.** France requires a special health-data hosting certification (HDS), so skip France at first. Germany needs a professional-secrecy clause in your data processing agreement (DPA).
- **Text-message replies often don't work.** EU messages often come from a name instead of a phone number ("PraxisNord"), and patients can't reply to those. Use a confirm/cancel link instead.

## What I recommend

Start with **one country, one specialty (physio by default) and one scheduling tool**, and aim for 10 paying clinics there. Build the database so adding the second region later is a config change, not a rewrite.

- **Why physio:** patients come for a series of visits, the content is less sensitive than therapy, and the competition is weaker than in dental.
- **What would change my mind:** if you have a network among dentists or therapists, or if the clinics you talk to already have good two-way reminders.
- **Before going deep on code:** talk to 10 clinics. The plan has a 5-question script and a pass/fail threshold.

## Three questions

1. **Where are you based, and is there one country where you could talk to 5–10 clinics in the next two weeks?** (e.g. "Netherlands; my sister runs a physio practice")
2. **How many hours a week can you put in, and by when do you want your first paying clinic?** (e.g. "15 h/week next to my job, first paying clinic by March")
3. **What made you think of this idea?** For example, a clinic you saw struggling, a tool that annoyed you, or a feature you already have in mind that nobody does well.

## Files created
- `LAUNCH-PLAN.md`: draft launch plan (market choice, build order, architecture choices, compliance checklist per market, pricing math, clinic-interview script, 30-day plan, risks)
- `_apex/DOMAIN-BRIEF.md`: background research on the field: rules with certainty tags, costs, what experienced practitioners check, the next 12–24 months, open points to verify
- `_apex/TRACE.md`: list of every requirement, yours and the ones I found, with its status, plus 5 planned "what if things change" tests
- `_apex/unit_economics.py`: SMS cost vs. value of prevented no-shows, per clinic size and market
- `_apex/sms_template_check.py`: checks message length, encoding, segment count and opt-out-word collisions in reminder templates
