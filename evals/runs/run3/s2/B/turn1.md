I went through all the files. The script is the smallest problem. Several of your current orders conflict with **allergies**, and those need a phone call before the weekend is out. Urgent items first, then what I changed in the script.

## Do these first (next few days)

**1. Familie Becker, PO-1187, Streuselkuchen, pickup Sat 21.11.** The note says the son (6) has a hazelnut allergy with anaphylaxis. Since 09/2026 your Streusel mix from supplier B contains **8 % ground hazelnut** (your own `recipe_changes.txt`). The laminated "FINAL" list on both counters still says Streuselkuchen has no nuts, so whoever took the order probably checked that list. Please call them. You also make Nussecke and Bienenstich in the same bakery, so be honest that you can't promise "nut-free" for any product.

**2. Dr. Hoffmann, PO-1189, 4× Dinkel-Saatenbrot, Sat 21.11.** The note says "Zöliakie – deshalb Dinkel statt Weizen". **Dinkel (spelt) is a kind of wheat and contains gluten**, so it isn't safe for someone with coeliac disease. Since 10/2026 the bread also has sesame on top. Please call before Saturday.

**3. Kindergarten Sonnenblume, PO-1194, 6× Nikolaus-Hefezopf, 04.12.** One child has an egg allergy and two have a milk allergy, and the Hefezopf contains both. Talk to the Kita now. Either those three children get something else, or the Kita takes care of it.

**4. Take both laminated allergen lists down from the counters.** They are wrong in at least three places:
- Streuselkuchen now contains hazelnut.
- Saatenbrot now contains sesame. On 07.11 Lena told a customer it had none, going by the list.
- Vegan Schokokuchen is now made with oat milk, so it contains oats instead of soy.

The list also leaves out products you sell (Himbeer- and Mohn-Sahnetorte, Hefezopf, Frankfurter Kranz). It has only 9 of the 14 allergens you have to declare: lupin, sulphites, fish, crustaceans and molluscs are missing. Two open checks:
- Mehmet thinks the new bread improver for the Weizenbrötchen may contain **lupin flour**. Someone needs to read that datasheet.
- The Stollen raisins and candied peel are often **sulphured**, and nobody has read those labels.

Until the list is fixed, staff should say "I'll check and call you back" rather than "no".

**5. Sophie (new staff member, starts Tuesday 17.11).** She needs the Gesundheitsamt instruction (*Belehrung nach § 43 IfSG*) **before** her first shift handling food. "Sometime in December" is too late. Many health offices run it online at short notice.

**6. Lena's December pay.** 13.00 €/h is below the 2026 minimum wage of 13.90 €/h. Also, 52 h × 13.00 € = 676 €, which is over the 603 € minijob limit for 2026, so she wouldn't stay a minijobber. At 13.90 €/h about 43 hours a month keeps her a minijobber. Please check this with whoever does your payroll before December.

## Saturday 19.12: 17 cakes ordered, room for 12

The new check script (below) counted all open cake orders for 19.12:
- Filiale: 8 (matches Jana)
- Hauptladen: 8
- Web: 1. This is Neumann's Sachertorte. The web form stored its date as `12/19/2026`, so it doesn't show up when you filter for the 19th.

That's **5 more than the cold room holds**. If the 2 Sachertorten don't need cooling, it's still 15. Stop taking cakes for that day now. You could:
- move some pickups to Friday 18.12,
- rent a second cooler for that weekend, or
- make the afternoon cakes (13:00–15:30 pickups) on Saturday morning.

## The order script: why it "sort of works"

Felix's script has four bugs, and they explain things in your team chat:

| Bug | What it caused |
|---|---|
| Treats two orders as duplicates if the **customer + pickup day** are the same, and silently drops the second | Frau Müller's Käsekuchen vanished (and you gave a 20 € voucher). There's a gap at **PO-1185**, right after her PO-1184, which fits this bug. Two different customers with the same surname on the same day would also lose one order. |
| If a shop's export is missing it says "no problem" and **writes the list without that shop's orders** | Matches Katrin's note on 06.11 that the list "looks shorter" |
| Web-form dates are US style (`12/19/2026`) and are left as they are | Web orders are invisible when sorting or filtering by date |
| No backup, crashes if no export exists, only works when started from the right folder | Risk of losing the whole list |

**What I did:**
- `order_sync.py` is rewritten. Felix's version is saved as `order_sync_ORIGINAL_2024.py`. You still run it the same way: `python order_sync.py`. Changes:
  - Orders are matched by **order number only**. Nothing already in the list is ever deleted; cancelled orders should get status `cancelled`.
  - A missing export gives a loud **"EXPORT MISSING"** warning. Rows without an order number, and two orders sharing one number, are reported instead of silently dropped.
  - Web dates are converted correctly.
  - The old list is copied into a `backups` folder before every save.
  - It tells you if the list is open in Excel.
- `order_check.py` is new and runs automatically after the sync. It doesn't change anything; it prints a report and saves it to `bestell_check.txt`. It checks:
  - allergy notes against the allergen list, which is how it found the Becker, Hoffmann and Kita conflicts above
  - cakes per day against the 12-cake limit
  - orders over 80 € with no deposit
  - orders with no phone or e-mail
  - pickup days that have passed but are still open
  - products missing from the allergen list
  - gaps in the order numbers
- `allergene_ENTWURF_2026-11.csv` is a **draft** of one single allergen list: all 14 allergens, all products, and the changes from your notes. Anything not yet confirmed is marked `PRÜFEN` or `?`. **It is not ready to hang up.** Someone has to check it against the supplier datasheets first. After that it should be the only list, and every recipe or supplier change should update it.

**How I tested it:** I ran the check on your real list. I tested the sync on a copy, with made-up exports (Müller's two items, a missing shop export, web dates, a duplicate order number). Both of Müller's orders were kept and the dates were fixed. A second run with nothing new changed nothing. I have **not** run the sync on your real list, because the shop exports aren't in the folder. Your data files are unchanged. The first real run will also fix Neumann's date.

## Money and paperwork worth a look

- **Deposits:** your own rule is "deposit over 80 €", but 6 open orders worth **1,618 €** have none. That includes the 796 € Stollen order and the 486 € catering. With 6 no-shows in November (~250 €), I'd ask for a deposit on every cream cake, and always take a phone number. Weber, the repeat no-show, has none on file.
- **The deposit tin:** cash sits outside the till until pickup, and on 04.11 the Hauptladen tin had 40 € more than its slips. Deposits normally have to go through the till (and are subject to VAT) when you receive them. Worth asking your tax advisor how to handle this properly.
- **Catering offer A-2026-031:**
  - "MwSt immer 7 %" is very likely wrong here. Drinks (coffee, juice) are always 19 %. With porcelain, set-up and a service person on site, the whole job will probably count as catering at 19 %. Please ask your tax advisor.
  - The order list says **486.00 €**, but the offer says 460.10 €. One of them is wrong.
  - The customer has 2 vegan and 1 lactose-free guest, but the offer has no vegan items and says "Allergene: auf Nachfrage". Butterbrezeln contain milk.
- **Stollen for Lorenz Haustechnik (40 pieces, individually packed with company label):** these are pre-packed, so each one probably needs a proper label with ingredients, allergens in bold, weight and best-before date. That's another reason to read the raisin and candied-peel labels for sulphites.

## Hygiene and data protection

- **Display fridge in the Filiale:** it reads 7–9.5 °C almost every day, and several of those readings are marked "ok". The usual limit for cream cakes is 7 °C. Mehmet pressing the door shut hints at a bad door seal. Get a technician in, and until then keep cream cakes out of it. Write the limit on the log and add a "what we did" column.
- **Missing logs:** there is no log at all for the Hauptladen display, and several days are missing for both fridges.
- **Customer data:** customer phone numbers on Jana's private phone, reminders sent through her private WhatsApp, and allergy and health notes in the order list all count as sensitive under GDPR. Reminders should go out from a shop phone or account.

## Questions for you

1. **How are orders taken today?** What exactly creates `orders_hauptladen.csv`, `orders_filiale.csv` and `webform_export.csv` (Excel, paper typed up later, a website plugin)? The long-term fix may be one shared order list that both shops and the web form write into directly, with no nightly merging. Would that suit you?
2. **Does anyone type changes straight into `preorders_nov_dec.csv`?** At the moment the shop export wins when they differ, so a manual change could be overwritten.
3. **Do PO-1182, 1183, 1185, 1188, 1191 and 1207 exist?** Cancelled, or lost? And were Jana's three paper orders from 05.11 ever entered?
4. **Should the script messages be in German for the team?** Once someone has checked the `PRÜFEN` points, I can also turn the allergen list into a printable German counter sheet.

## Files created
All in `<scratch>/eval3/s2/B/work/baeckerei_sonnenkorn/`:
- `order_sync.py`: rewritten merge script (replaces the old one)
- `order_sync_ORIGINAL_2024.py`: Felix's original, unchanged
- `order_check.py`: new check and report script
- `allergene_ENTWURF_2026-11.csv`: draft of a single allergen list with all 14 allergens (not for display yet)
- `bestell_check.txt`: today's check report on your current order list
