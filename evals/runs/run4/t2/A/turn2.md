Thank you, Margaret. That's exactly what I needed. The PI scare is the clearest possible statement of the problem: **a date that lives in one place, known to one person, isn't safe.** Everything below is built to make that impossible.

## My recommendation: build it on the Microsoft 365 you already pay for

I've gone with **Route B** rather than buying a legal practice management system. The reasons:

- **Budget.** £150 a month across five people is about £30 per user, which is tight for most legal case-management systems. And because your accounts stay in their own package, you'd be paying for a lot you wouldn't use.
- **Your 1 March deadline.** Moving 140 matters into a new system and learning it is risky in 15 weeks, particularly for you. Outlook stays, and everyone's screens look familiar.
- **The safety comes from the rules more than the software.** These are: two people on every date, a second solicitor checking every limitation date, escalating reminders, and a Monday review. Microsoft Lists and Power Automate (both already included in your licence) can do all of that.
- **You can change your mind later.** If you outgrow it, the clean matter list moves easily into a dedicated system after your sabbatical.

The honest downsides: it depends on your IT man setting it up properly and on Priya and David owning it, and automatic reminders can fail without anyone noticing. That last point is why the Monday digest email doubles as an alarm: if it doesn't arrive, something is wrong.

## What you'll end up with

- **A Matters list:** every open matter with a fee earner, a **named back-up**, its status, a one-line *"where it stands"* that anyone can read, and a link to its existing folder on the shared drive (the files don't move).
- **A Key Dates list:** limitation, completion, SDLT, search priority, IHT, Inheritance Act and tribunal deadlines. Each one has a responsible person and a back-up, and limitation-type dates are **checked by the second solicitor**. Every limitation date also gets an internal "act-by" date 3 months earlier.
- **Reminder emails to both people** at 90, 30, 14, 7, 3, 1 and 0 days. Overdue dates go to both partners every day until they're dealt with.
- **A Monday 7:30 email** to everyone: overdue items, the next 8 weeks, and anything unchecked. Priya prints it for you.
- **A Contact Log** that Sue fills in from her iPhone (calls, post, enquiries), with an **instant alert to both partners if anyone mentions bank details**.
- **Tighter email security,** aimed squarely at payment-diversion fraud: two-step sign-in for everyone, blocking the hidden forwarding rules fraudsters use, anti-spoofing settings on your domain, and protected apps on phones.

## Money

| | Estimate (please get quotes; prices change) |
|---|---|
| Upgrade to Microsoft 365 Business Premium (for the security features) | roughly £40–£50 a month for 5 users |
| Backup of your Microsoft 365 data | roughly £10–£20 a month |
| IT man, about 2 days | depends on his rate; should fit well within £2,000 |
| **Total** | **comfortably inside £150 a month and £2,000 set-up** |

## Something you can use from Monday

You don't have to wait for the new system to close your biggest risk. I've built a **Key Dates Register** spreadsheet that Priya can start filling in this week from the Excel sheet *and* both paper diaries. It has:

- a printable **Next 8 Weeks** page, with overdue items and those within 2 weeks shown in red
- a **Checks** page that counts problems (a matter with no back-up, an unchecked limitation date, a limitation date with no act-by date, anything overdue). Every number should be zero.

I tested its formulas in Excel. Its layout also matches the new lists, so it becomes the import file in December. **Target: every open matter and date in it, cross-checked by you and David, by Friday 4 December.** That's three months before your sabbatical.

## The plan to 1 March (full version in the procedures document)

- **Nov:** Priya fills in the register. The IT man does the security work. The payment-fraud rules start, including a warning in your client care letter.
- **Early Dec:** the IT man builds the lists and reminders, tested against a checklist I've written for him.
- **4 Jan:** the new system becomes the official record. Paper diaries carry on alongside.
- **11 Jan:** the new paralegal learns it from day one, which is a good test of "can anyone see where a matter stands?"
- **Jan:** you have three 30-minute sessions with Priya. You only really need three habits: read the Monday sheet, act on `[KEY DATE]` emails, and tick "→P" in your diary once you've told Priya about a date.
- **8–12 Feb: a "Margaret is off sick" drill.** You step back for a week, and David and Priya run everything from the system. This tests exactly what went wrong last spring.
- **Fri 26 Feb:** sign-off against a written "trusted" checklist, then hand over to David. Send the Key Dates Policy to your insurers.

**Your paper diary:** keep it as long as you like. Every Monday Priya will check it against the system, so it becomes a second safety net rather than the only one.

## Please note

- The **Date Rules** sheet (SDLT 14 days, IHT 6 and 12 months, ET claims 3 months less a day, PI 3 years and so on) is a **prompt, not legal advice**. You or David should check it, and work out every date on the file.
- I haven't seen your Microsoft 365 set-up. Your IT man should confirm the licence and that your data is held in the UK.
- **Please don't send me client data.** If you'd like help mapping the old Excel sheet, send just its **column headings**.

## What I need from you

1. Forward the IT specification to your IT man and book his two days before 11 December.
2. Have Priya start the register on Monday.
3. Read through the Key Dates Policy and the fraud procedure, and tell me anything you'd change. For example, is 3 months the right act-by margin for you?

I can also turn the two documents into Word files, or draft the client-care-letter wording and email signature, if that would help.

## Files created

All in `<scratch>/eval4/t2/A/work/`:

- `Key-Dates-Register.xlsx`: the interim register and import template (Start here, Next 8 Weeks, Checks, Matters, Key Dates, Date Rules, Lists). The example rows are marked EXAMPLE; delete them before you start.
- `IT-Setup-Specification.md`: for your IT man. Covers security, the SharePoint site, the three lists, the four reminder flows, and the tests to run before go-live.
- `Office-Procedures-and-Rollout.md`: the Key Dates Policy (for your insurers), who does what, the payment-fraud procedure, data-protection basics, the week-by-week plan, the "trusted" checklist and your one-page guide.
- `tools/build_register.py`: the script that generates the spreadsheet, so it can be rebuilt or changed.
