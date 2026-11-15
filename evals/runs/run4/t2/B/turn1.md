Yes, I can help. You're right to treat this as a risk. Here's the short version:

- **Biggest risk:** limitation and court dates kept in personal paper diaries. If one diary is wrong, lost, or its owner is off sick, nothing else catches it. A missed limitation date is the classic negligence claim against a small firm.
- **Built today:** an interim **Key Dates & Limitation Register** in Excel (`Key-Dates-Register-DRAFT.xlsx`). You can start using it on Monday. It moves into whatever system we pick, so nothing typed into it is wasted.
- **My recommendation for the main system:** build it in Microsoft 365, which you probably already pay for through Outlook. Use a legal practice management system only if your answers below point that way.
- **What you do next:** answer the 3 questions at the end, and run the limitation sweep described below this week.

---

## Four things worth knowing before we design anything

You'll know the law better than I do. These points are about what the *system* needs to enforce so that the law is applied every time.

1. **Every date needs a second person, not a second diary.** Practitioners and PI insurers expect a central key-dates record where one person calculates each date and a different person checks it, plus an internal target date well before the last day. The SRA Code of Conduct for Firms requires effective systems and controls (para 2.1; *likely*, check the exact wording). Your PI renewal proposal form will probably ask how you manage key dates (*verify on your own form*). Paper diaries can't show who checked what, and they can't be backed up.
2. **Your matter list is also your conflict-check database.** A conflict search (SRA Code of Conduct for Solicitors 6.2) is only as good as the parties you recorded. That includes opponents and former clients, not just client names. If the current spreadsheet only has client names, your conflict checks have a blind spot today.
3. **Client emails in individual Outlook inboxes are not "the file."** If a solicitor is away, nobody can see what was promised to the client. A subject access request under UK GDPR also means finding everything you hold about a person, across Outlook, Excel and paper, within one month. Most of the risk in "communications" is about where emails are kept, not the software you use.
4. **If you do conveyancing, probate or company work, AML records belong on the matter.** The Money Laundering Regulations 2017 require client due diligence and a risk assessment per matter, with records kept 5 years after the relationship ends (reg 40). A matter system should show "CDD done / risk assessed" before work starts. I'll leave this out if you're not in scope.

A quick look ahead, all to verify: the Data (Use and Access) Act 2025 is being brought in stage by stage and changes some UK GDPR handling, including subject access requests and complaints. The Legal Ombudsman's time limits changed in April 2023, so check your client-care letter wording.

---

## The interim register (built and tested)

`Key-Dates-Register-DRAFT.xlsx` is a plain Excel file with no macros, so it works in any Excel from 2010 onward.

- **Key Dates sheet:** one row per date (limitation, court or tribunal deadline, claim form service, hearing, undertaking, completion). You enter the **last day**. The sheet then works out an **internal target** and a **warning date** and shows a flag: **OVERDUE / ACT NOW / WARNING / NOT CHECKED / OK**.
- **Two-person rule built in:** the row shows NOT CHECKED until a *different* person has initialled it.
- **Cross-check against the standard period:** enter the accrual date and pick a standard period (for example "Contract (simple)" or "Unfair dismissal (ET)", which is three months less one day). The sheet shows the standard expiry. If your date is *later*, for example because you rely on a date of knowledge or ACAS early conciliation, it says so, and the warnings count back from the **earlier** date.
- **Matters sheet:** flags every open matter where nobody has recorded a limitation decision ("Yes, it's on the Key Dates sheet" or "Not applicable").
- **Dashboard:** gives counts for your Monday 10-minute review. Anything above zero needs a named person that day.
- **Settings and Limitation guide:** warning periods and lists are changed in one place. The guide cites the Limitation Act 1980 sections and is labelled clearly as a prompt, not an answer.

**How I checked it:** I opened it in desktop Excel and recalculated: zero error cells. I also ran 10 test cases: overdue, act now, warning, same person checking their own date, done, matches standard, later than standard, ET three-months-less-a-day, unknown matter number, and missing limitation decision. All 10 gave the expected flag. The file you get has no sample data in it.

**Its limits:** it doesn't send reminders by itself. It only works if it sits in a shared place (OneDrive or SharePoint, with version history), not on one PC, and if someone opens it every Monday. That's why it's interim.

### This week: a limitation sweep (about 1–2 hours, the most valuable step)
1. Put the register in a shared folder everyone can open.
2. Go through every **open** matter in your current spreadsheet, and every forward entry in the paper diaries. Add each date to the register.
3. On the Matters sheet, give every open matter a limitation decision.
4. The other solicitor or the paralegal checks and initials each row.
5. Keep the paper diaries running alongside until the Dashboard shows zero NOT CHECKED.

---

## Where it should live long-term (a real choice for you)

| | How it works | Pros | Cons | Best if you want… |
| :--- | :--- | :--- | :--- | :--- |
| **A. Microsoft 365 (my recommendation)** | Microsoft Lists for matters, key dates and parties; a shared "Key Dates" calendar; a shared mailbox and matter-number email filing in Outlook; one automatic weekly reminder email | Probably no new subscription; you own the data; works on phones; builds on the register above | No time recording, billing or legal accounts; needs one person (likely the paralegal) to look after it | **Simple, low cost, using tools you already know** |
| **B. Legal practice management software** (e.g. Clio, LEAP, Actionstep, Osprey, Quill; prices vary, often charged per user per month, so check current quotes) | One purpose-built system | Key dates, conflict search, Outlook email filing, templates, time recording, billing, and often SRA-compliant client accounts | Monthly cost, data migration, training, dependence on the vendor (check you can export your data) | **To also fix billing and client account, or to grow** |
| **C. Improved Excel only** | The register above plus a tidied matters sheet on SharePoint | Available today, free | Reminders depend on discipline; gets clumsy with more people or more matters | **A stop-gap for 1–3 months** |

If your **accounts or billing software already has a case-management module**, switching that on may beat all three. That's why it's question 2 below.

---

## Three questions (one line each is fine)

1. **Which practice areas do you cover?** For example: *"civil litigation, employment, residential conveyancing, wills & probate."* This decides the limitation types, whether AML applies, the undertakings register and how long to keep files.
2. **Which Microsoft 365 plan do you have, and what do you use for client account and billing?** For example: *"M365 Business Standard; Xero plus a manual client ledger"* or *"we use Quill."*
3. **What has nearly gone wrong already, and is there anything you'd love the system to do?** For example: *"a court order arrived by post and only went into one diary,"* or *"I want reception to log every client call against the matter."*

Once you answer, I'll pick the route, list my assumptions, and build the main pieces: the matter and key-dates setup, conflict search, email filing, how incoming post and court-portal notices get logged, and the weekly routine.

## Files created
- `Key-Dates-Register-DRAFT.xlsx`: the interim register (Read me, Dashboard, Settings, Limitation guide, Matters, Key Dates)
- `_apex/TRACE.md`: my working checklist of every need and how it is covered
- `_apex/build_register.py`: rebuilds the register
- `_apex/verify_in_excel.ps1`: re-runs the Excel recalculation check
- `_apex/test-register.xlsx`: a copy with the 10 test cases, used for verification only
