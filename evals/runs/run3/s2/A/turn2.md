Thanks, Katrin. That was exactly what I needed. I've done it, and your evening routine stays the same.

**In short**

- **Approach:** I fixed and extended what you already have rather than adding new software two weeks before Christmas. Same laptop, same `python order_sync.py` (or a double-click on `Abendlauf.bat`), same shop spreadsheets.
- **No more lost orders.** Felix's merge is replaced. In 13 test cases, including Frau Müller's, a missing shop export and messy Excel files, nothing was dropped.
- **Every allergy order is now checked against your current recipes.** On your real list it stops all four risky orders: Becker (hazelnut), Dr. Hoffmann (spelt = gluten), the Kita (egg and milk) and the catering job.
- **A new dated allergen list for the counters** covers all 14 EU allergens. Anything not yet checked prints as "?" ("please ask", not a guess).
- **Cold-room allowance:** 12 cakes per day, split 6 and 6 between the shops, on a sheet for each counter. **19 December now shows 17/12 in red** and is closed for new orders.
- **No-shows:** from Monday every chilled cake needs a deposit, there are reminder texts for the shop phone, and repeat no-shows are flagged.
- **Still needed from you this week:** 5 phone calls, removing the old laminated list, Sophie's health briefing and Lena's wage (see the list below).
- **Nothing you protected was touched:** the till, your recipes, the website form and all your old files. I made a verified backup first. 33 automated tests pass.

---

## What I found against your original idea

| | |
| :--- | :--- |
| **Keep** (works) | Ordering in either shop or online; your order list's columns; the evening run on the Hauptladen laptop; the temperature log habit; the deposit tin rule |
| **Built wrong** | The merge treated "same name + same day" as a duplicate and silently dropped orders. Web dates weren't converted. The allergen list was out of date and covered only 9 of the 14 allergens. "MwSt immer 7 %" on catering |
| **Never built** | Checking allergy orders against recipes; a cake limit per day; deposits for small cream cakes; a pickup list for each shop |
| **Extra I added** | Reminder texts, a warning when a pickup falls on a closed day (Krause, Filiale, Monday 30.11), a target amount for each deposit tin, temperature limits with "action missing", a bilingual paper order slip, and a catering quote template with the VAT split |

## What you do now

**Every evening (about 5 minutes)**

1. Put the three exports in the folder as before.
2. Double-click **`Abendlauf.bat`**. The daily report opens with the red items on top.
3. Print **`ausgabe/Abholliste.html`** (one page per shop, allergy orders in red) and **`ausgabe/Kuehlraum_Kontingent.html`** (one per counter; staff cross off each cake they accept).

**After you call an allergy customer**, add one line to `einstellungen/allergie_freigaben.csv` saying what you agreed. The order turns green. If the cake or the note changes later, it turns red again on its own.

**Changing rules** needs no programming; you just edit a cell in Excel:

| To change | Edit |
| :--- | :--- |
| A recipe or supplier, or a new product | `einstellungen/produkte_allergene.csv` |
| Cold-room size, an extra fridge, a special day | `einstellungen/kapazitaet.csv` |
| Deposit rules, opening hours | `einstellungen/einstellungen.csv` |

Five such changes are rehearsed as automatic tests.

## Please do these yourself (I can't)

| By | What |
| :--- | :--- |
| **Mon 16.11** | **Call Familie Becker** (PO-1187, pickup 21.11). Their Streuselkuchen contains hazelnut now, and their son has anaphylaxis. Offer another cake and mention traces. |
| Mon 16.11 | **Call Dr. Hoffmann** (PO-1189). Spelt contains gluten, so the bread isn't safe for coeliac disease. It also has sesame now. |
| Mon 16.11 | **Call the Kita** (PO-1194). The Hefezopf contains egg and milk. |
| Mon 16.11 | **Call Steuerbüro Klein** (PO-1190) about the allergen list and the price: the quote says €460.10, the order list says €486.00, and with correct VAT it's €466.10. |
| Mon 16.11 | **Call Krause** (PO-1193): the Filiale is closed on Monday 30.11. |
| Mon 16.11 | **Take the laminated "FINAL" list off both counters.** Hang the new `Allergenliste_Theke.html`. |
| **before Tue 17.11** | **Sophie** needs the Gesundheitsamt briefing (§43 IfSG) *before* she handles unpackaged food. |
| before December payroll | **Lena:** €13.00/h is below the 2026 minimum wage of €13.90, and €676 a month is over the Minijob limit (€603, please confirm with your payroll office). |
| Sun 22.11 | **Fill the "?" cells in the allergen list.** The most urgent are the supplier C bread improver (possible lupin), the sulphites in the Stollen fruit, and the Frankfurter Kranz. The daily report lists them all. |
| by 01.12 | **Decide on 19.12** (see below). |

**19 December, my recommendation:**

1. If your 2 Sachertorten don't need the cold room, set them to 0 places. That leaves 15.
2. Bake the remaining 3 fresh on Saturday morning, straight into the display cases.
3. Only if neither works: rent a fridge for 18–19.12, or offer a few customers Friday pickup.

## Before → after (measured on your real data)

| | Before | After |
| :--- | :--- | :--- |
| Orders lost or unreadable in the merge | 2 known (Müller, Neumann web date) | 0 in 13 test cases, plus a parity test against Felix's script |
| Allergy conflicts noticed | 0 of 4 | 4 of 4, plus unclear notes go to a human |
| Allergens covered at the counter | 9 of 14, undated, 2 wrong | 14, dated, open checks visible |
| 19.12 visible | 16 cakes, no limit | 17/12 in red, an allowance per shop |
| Missing deposits visible | none | 6 orders, €1,618 |

## Where everything is and how I checked it

| You need | Where it is | How it was checked |
| :--- | :--- | :--- |
| No lost orders | `order_sync.py` → `werkzeug/sonnenkorn.py` | 13 merge tests. Felix's script and the new one give identical results except the intended web-date fix |
| Allergy safety | `einstellungen/produkte_allergene.csv`, daily report §2, counter sheet | Real list: 4 STOPPs. Notes in German, English and Turkish and with typos are tested. An independent second review found 12 weak spots; all serious ones were fixed and re-tested |
| No overbooking | `einstellungen/kapazitaet.csv`, `ausgabe/Kuehlraum_Kontingent.html` | 19.12 = 17/12; changing the limit only changes that day |
| Fewer no-shows | deposit rule + reminder texts in the pickup list | Test: a €39 cake ordered from 16.11 gets a €20 deposit suggestion |
| Correct catering VAT | `vorlagen/Catering_Angebot_Vorlage.xlsx` | Recalculated independently: €466.10. **Not yet opened in Excel: please check that total once** |
| Backup and undo | `_sicherung/2026-11-14_vor_umbau/` (checksums verified, read-only) plus a nightly copy in `ausgabe/archiv/` | To undo: copy the old file back. Details in `APEX-COMPACT-REVIEW.md` §5 |

**What I couldn't verify:**

- **Real exports:** your real shop and web exports weren't in the folder. I tested on exports rebuilt from your order list, which reproduce it exactly. Please run it once with the real files and compare the count.
- **Rules to confirm:**
  - catering VAT (food 7%, drinks 19% since 01.01.2026; delivery and staff unclear): your Steuerberater;
  - booking deposits in the till when received: your Steuerberater;
  - the ≤7 °C display limit and the labelling of the 40 wrapped Stollen: Lebensmittelüberwachung Freiburg.

**After Christmas (planned):** the live shared order list you wanted in 2022 (a free Google Sheet on the iPads, with the same checks at night), and a shop phone with consent for reminders. The details are in `TRACE.md` and `IMPROVEMENT-LOG.md`, together with a prompt you can paste into Claude in a few months to review progress.

## Files created

All in `baeckerei_sonnenkorn/`:

- `order_sync.py`: replaced, same command; Felix's original is kept in `_sicherung/`
- `Abendlauf.bat`
- `werkzeug/sonnenkorn.py`
- `werkzeug/test_sonnenkorn.py`
- `einstellungen/produkte_allergene.csv`
- `einstellungen/einstellungen.csv`
- `einstellungen/kapazitaet.csv`
- `einstellungen/geraete.csv`
- `einstellungen/allergie_freigaben.csv`
- `vorlagen/Catering_Angebot_Vorlage.xlsx`
- `vorlagen/Bestellzettel.html`
- `ausgabe/Tagesbericht.html`
- `ausgabe/Abholliste.html` (sample for 21.11)
- `ausgabe/Kuehlraum_Kontingent.html`
- `ausgabe/Allergenliste_Theke.html`
- `_sicherung/2026-11-14_vor_umbau/`: copies of all 8 original files plus `SHA256SUMS.txt`
- `TRACE.md`
- `APEX-COMPACT-REVIEW.md`
- `IMPROVEMENT-LOG.md`
