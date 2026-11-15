Thank you, that helps a lot. My choice: **replace the nightly script with one shared order book in Google Sheets.** Both shop iPads and the office laptop work in the same list, live. I've built it and filled it with your current orders.

## Why this and not something else

| Option | Fit for you |
|---|---|
| Keep improving the Python script | Merging every night is the reason orders "disappear". Nobody can maintain it now that Felix is in Berlin. **No.** |
| Dedicated bakery or pre-order software | Could be good later (SMS reminders, online prepayment). But a new system two weeks before Christmas, with a website you can't change, is too risky. **Look at it again in January.** |
| **One shared Google Sheet** | You already know Sheets. It works on the old iPads, costs little, and the till and the website stay as they are. Every change is saved with **who and when** (File → Version history), so nothing can vanish unseen. **Yes.** |

## What I built: `Bestellbuch_Sonnenkorn.xlsx`

You upload it to Google Drive and open it as a Google Sheet. It has these tabs:

- **Start:** the first screen for staff. It shows:
  - the next order number;
  - red counters for unchecked allergy orders, allergy conflicts, missing deposits and pickups due tomorrow;
  - a **cold-room calendar** with free cake places per day, through to end of January.

  **Before taking any cake order, staff look here.** Right now 19.12 shows **−5**.
- **Bestellungen:** the order list. Blue columns are typed in. Grey columns fill in automatically:
  - the product's allergens appear right next to the customer's allergy note;
  - an **ALLERGY CONFLICT** column turns red;
  - a "Hinweise" column must be empty before an order counts as complete. It flags: cold room full, deposit missing, no phone number, customer who didn't turn up before, "MORGEN – Kunde erinnern" (remind them, pickup is tomorrow), duplicate order number, pickup day passed but status still open.

  All 22 current orders are already in. Neumann's date is corrected. "ohne Alkohol" and "Geschenke" moved out of the allergy column into "Details".
- **Produkte:** the **one and only allergen list**, with all 14 allergens plus a cold-room yes/no per product. It includes every change from your notes. Unverified points are yellow (`PRÜFEN` / `?`), and every product shows red until you enter a "checked on" date.
- **Aushang:** the counter sheet, built automatically from Produkte. Its header reads "NOCH NICHT ALLES GEPRÜFT – NICHT AUSHÄNGEN" ("not everything checked yet – don't hang it up") until every product has a check date. After that it shows the oldest check date. It has a "never guess – we'll call you back" line in German and English. Best shown on the iPad; print it only after a change.
- **Web_Import / Web_Neu:** Tom imports the website CSV. Web_Neu converts the US dates and shows which web orders are **NEW** and still need copying into Bestellungen. It finds columns by name, so the column order of the export doesn't matter.
- **Änderungen:** a log of recipe and supplier changes, already filled with the 6 open items from your notes (lupin datasheet, Stollen sulphites, etc.).
- **Anleitung:** a 14-step guide in simple German and English.
- **Einstellungen:** cold-room limit (12), deposit rules. You change these in one cell.

**Testing:** I opened it in Excel and recalculated everything: no formula errors. The current data gives the expected results: 19.12 has 17 cakes against a limit of 12, and Becker, Hoffmann, the Kita and the catering are all flagged red. A test web import with US dates, comma prices and shuffled columns came through correctly. **I could not test it inside Google Sheets itself.** Please check that the dropdowns and colours work after uploading (step 2 below).

## Decisions I made for you (each easy to undo)

1. **Deposit for every cold-room cake, plus anything over 80 €.** This targets the cream cakes that end up in the bin. Switch it off in Einstellungen (`ja` → `nein`). Today it flags 13 open orders. For existing orders, I'd ask for a deposit **only** on the 19.12 cakes and the two large business orders (Stollen 796 €, catering).
2. **Only you or Tom approve an allergy order**, by typing initials in column Q. Everyone else writes down what the customer says and promises a call back.
3. **Rows are never deleted.** Cancellations get status "storniert".
4. **Deposits go through the till** (the Anleitung says so), not the tin. You're not changing the till, just using it. Ask your till provider or tax advisor which key to use for an "Anzahlung".
5. **Felix's script and my rewrite from last time retire on go-live day.** Until then, keep running my version, because it doesn't lose orders.

## Plan for the next 2 weeks

**This weekend / Monday (your Sunday office time):**
1. The calls from last time: Becker and Dr. Hoffmann (both pickups Sat 21.11), the Kita. Sophie's Belehrung before Tuesday. Lena's December pay.
2. Set up Google Workspace, Business Starter. Use a business account, not a private Gmail, because the sheet holds allergy and health information. Accept Google's data-processing agreement in the admin console. Create 3 users: you, "Hauptladen", "Filiale". That's roughly €25–30/month at current prices (please check). Turn on 2-step login.
3. Upload the file, then open it as a Google Sheet:
   - In File → Settings, set the locale to **Germany**.
   - Protect columns S–W and the Produkte tab (Data → Protect range).
   - Share it with the two shop accounts.
4. On 19.12, set the cold-room limit as a real decision. My recommendation: **rent a second commercial fridge for 18–19.12** (a one-off, usually in the low hundreds). That keeps all 17 customers. Then type the new limit (e.g. 20) into the 19.12 row on Start. Also look at 23./24.12 now, before they fill up.

**Mon 16. – Sat 21.11 (test week):**
- Install the Google Sheets app on both iPads and log in with the shop accounts.
- 15-minute briefing in each shop, with Tom and Mehmet taking the lead.
- New orders go into **both** the old way and the new sheet.
- Your job: work through the yellow `PRÜFEN` items with the supplier datasheets, enter check dates, then show the Aushang. Throw away both laminated lists.

**From Mon 23.11: the sheet is the only order book.**
- Paper only if the internet is down, and entered the same day.
- Tom does the web import every day on the laptop.
- Each evening the shop lead sends reminder texts to "MORGEN" customers.
- Before 27.11: fix the catering offer (19 % VAT question, vegan items, allergens per item). Before 15.12: Stollen labels with sulphites checked.

**Reminders:** don't use Jana's private phone. One cheap prepaid smartphone per shop (one-off, ~€100–150 each) fits your budget, and the Anleitung has the text template.

## Questions for you

1. **Can you send me one real website export (CSV)?** I built the import from what the old list implies: same column names, US pickup dates, ISO order dates. One real file would confirm it.
2. **Who else may approve allergy orders besides you and Tom?** Mehmet, for the Filiale?
3. **Which languages does the team read best?** I can add a third language to the Anleitung and the Aushang.
4. **Who assigns the "PO-" numbers on the website?** Shops and web seem to share one number range. The Start tab takes this into account, but if the website counts on its own, the two could collide. The sheet would flag "NR. DOPPELT", but better to know.

## Files created
- `<scratch>/eval3/s2/B/work/baeckerei_sonnenkorn/Bestellbuch_Sonnenkorn.xlsx`: the shared order book to upload to Google Sheets, with your current orders already in it.
- `<scratch>/eval3/s2/B/work/_build/build_bestellbuch.py`: my build script for the workbook (only for me to make changes later; you don't need it).
