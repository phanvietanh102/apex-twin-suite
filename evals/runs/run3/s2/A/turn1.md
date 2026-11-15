I read all 8 files, recomputed the numbers and tested a copy of Felix's script. Your folder is unchanged.

**The short version**

- **The biggest risk is the allergen list, not the script.** The laminated "FINAL" list on both counters is from 03/2026 and is now wrong. Three confirmed orders involve a child at risk of anaphylaxis, a coeliac customer and a Kita with allergic children. Please make the phone calls in #1 before Saturday 21 Nov.
- **Felix's script silently drops orders.** Frau Müller's cheesecake today was one of them. It also leaves web-form dates in the wrong format.
- **Saturday 19 Dec has 17 Torten booked, but the Backstube cold room holds 12.**
- **Money is leaking in four places:** €1,618 of large orders have no deposit, no-shows cost about €250 in November, the deposit box doesn't match its slips, and the catering quote and the order list disagree (€460.10 vs €486.00).
- **Two staff issues have deadlines.** Sophie starts Tuesday without the Gesundheitsamt briefing, and Lena's planned December wage is below the 2026 minimum wage.
- There are three one-line questions at the end. After you answer them, I'll start the fixes.

---

## 1. The allergen information at the counter is out of date, and three confirmed orders are affected

- **Hazelnut in the Streuselkuchen:** since 09/2026 the Streusel mix contains **8% hazelnut** (`recipe_changes.txt` lines 6–8). Only `allergen_matrix_v3.csv` was updated. The laminated `allergen_matrix_FINAL.csv` in both shops (line 6) still shows no nuts.
  → **PO-1187, Familie Becker:** a Streuselkuchen Blech for a children's birthday, pickup Sat **21.11**. The order note says *"Sohn (6) Haselnuss-Allergie, Anaphylaxie!"*. The cake as you bake it today contains hazelnut.
- **PO-1189, Dr. Hoffmann:** the note reads "Zöliakie – deshalb Dinkel statt Weizen". **Spelt (Dinkel) is a type of wheat and contains gluten**, and EU allergen law names it explicitly. This bread is not safe for coeliac disease.
- **Sesame in the Dinkel-Saatenbrot:** the bread now has a sesame topping (`recipe_changes.txt` line 10), and neither list mentions it. On 07.11 Lena told a customer "laut Liste nein".
- **PO-1194, Kindergarten Sonnenblume:** the order is 6 Nikolaus-Hefezöpfe, and the note says one child has an egg allergy and two have a milk allergy. Your own v3 list (line 16) says Hefezopf contains egg and milk. Nobody has flagged this to the Kita.
- **Gaps in the list itself:**
  - It covers only **9 of the 14 EU allergens**. Lupin, sulphites, fish, crustaceans and molluscs are missing.
  - That matters right now. Mehmet thinks the new bread improver from supplier C contains lupin, and the data sheet hasn't been read yet (line 14). The candied peel and raisins in the Stollen often contain sulphites, and their labels have never been checked (line 18).
  - The Vegan Schokokuchen now uses oat milk, so its entry is outdated.
  - Some products you sell appear on neither list: Frankfurter Kranz (often made with nut brittle), the Hochzeitstorte and every catering item. The catering quote just says "Allergene: auf Nachfrage".
- **Why it matters:** for loose goods, German rules (the EU food-information regulation LMIV 1169/2011 plus the German LMIDV; *known*) require correct allergen information, with written documentation behind any verbal answer. A reaction in a child is the worst-case event for a family bakery.
- **What you can do this week, without any files:**
  - call the Beckers, Dr. Hoffmann and the Kita;
  - take the "FINAL" sheet off both counters;
  - read the supplier C data sheet.

## 2. The merge script loses orders without telling anyone

I ran a copy of `order_sync.py` on test data in a temporary folder, which I deleted afterwards.

- **It drops a second order for the same name and day.** Duplicates are detected by *customer name + pickup date* (lines 25–27). In the test, Müller Sabine had an Apfelkuchen at the Hauptladen and a Käsekuchen at the Filiale, both for 14.11, and only the Apfelkuchen came out. That is exactly what happened today: it cost you a €20 voucher and annoyed a regular. Two different customers called "Weber" would collide the same way.
- **Web-form dates stay unconverted.** They are written as `12/19/2026` and passed through as-is (line 16: "probably fine already"). See PO-1208 Neumann: any sort or filter by date misses it.
- **A missing shop export is silently skipped** (lines 30–31). The output file is rebuilt from scratch every night (line 33) and still prints "OK". That explains the "Liste sieht kürzer aus" on 06.11. With no exports at all, the script crashes.
- **Anything typed directly into `preorders_nov_dec.csv` (status, deposit) is wiped at the next evening run.**
- **Order numbers PO-1182, 1183, 1185, 1188, 1191 and 1207 are missing.** I can't tell whether they were cancelled or lost.
- **Phone orders written on paper** (chat, 05.11) stay outside the system until someone types them in the next day.

## 3. Saturday 19 December is overbooked: 17 Torten for a cold room that holds 12

- The Hauptladen has 9 (including web order Neumann, which the date bug hides) and the Filiale has 8, across 11 orders.
- The limit of 12 (`recipe_changes.txt` line 20) isn't recorded anywhere the shops check when taking orders, and Katrin's warning came after both shops had already filled the day.
- The Torten are made on Friday from 14:00, so **five cream cakes would have nowhere cold to stay overnight**. You need a decision now: extra cooling, staggered production, or calling five customers. After that, a per-day capacity check at order-taking prevents a repeat.

## 4. Money: deposits, no-shows, the deposit box and the catering quote

- **Large orders without deposits:** your rule is a deposit above €80 (chat, 03.11). **6 confirmed orders over €80 have €0 deposit, €1,618 in total.** They include Lorenz Haustechnik at **€796** (40 Stollen with company labels) and Steuerbüro Klein at €486.
- **No-shows:** there were 6 in November, about **€250 of cream cakes binned** (chat, 14.11). All were under €80, so the rule never applied. Weber (PO-1186) is a repeat no-show.
- **The deposit box doesn't add up.** On 04.11 the Hauptladen box held €260, but the slips added up to €220. The order list records only €140 of deposits in total. Deposits only go into the till at pickup. In Germany, VAT is due when a deposit is received (*known*), and cash should generally be recorded in the register on receipt (*likely*; please check with your Steuerberater).
- **The catering quote and the order list disagree.** Quote A-2026-031 says Brutto **€460.10**, but PO-1190 says **€486.00**, a difference of €25.90. And the customer is a tax firm.
- **The quote's VAT is likely wrong.** It charges 7% on everything ("MwSt immer 7 %, weil Lebensmittel", line 20). As of 2026, food in catering is taxed at 7%, but **drinks stay at 19%**. That covers the coffee and orange juice, €50 net (*likely*), and the delivery and service-staff lines may also need splitting. The correct gross would be €466.10–€479.90. The template repeats this on every catering job.
- **The quote has no validity date and no cancellation terms.**

## 5. Staff: two legal deadlines

- **Sophie** starts in the Filiale on Tuesday 17.11, but her Gesundheitsamt briefing is planned for "irgendwann im Dezember" (chat, 12.11). Under §43 IfSG the briefing has to come **before** she first works with unpackaged food (*known*).
- **Lena:** her December plan is €13.00/h × 52 h = €676 a month, "bleibt Minijob" (chat, 11.11).
  - The statutory minimum wage since 01.01.2026 is **€13.90/h** (*known*).
  - The 2026 Minijob ceiling is **€603 a month** (*likely*).
  - At €13.90 she would earn €722.80, which is no longer a Minijob. Please check with your payroll office before you run December payroll.

## 6. The cold chain and customer data

- **The Filiale display case runs warm:** 6 of 7 readings are above 7 °C (7–9.5 °C), and four of them are marked "ok" (`kuehl_temperatur_log.csv` lines 6, 8, 13, 17). For cream cakes, ≤ 7 °C is the usual standard (DIN 10508, *likely*; the Freiburg Lebensmittelüberwachung can confirm). No corrective action is recorded, and pressing the door shut twice suggests a faulty seal or unit.
- **Gaps in the temperature log:** the Hauptladen display case is not logged at all, and the Filiale is missing on open days (06.11, 12.11).
- **Customer health data:** the allergy and health notes (coeliac disease, anaphylaxis, Kita children) sit in a plain CSV. Jana keeps regulars' numbers on her private phone and reminds them via WhatsApp (chat, 10.11). Health data is special-category under GDPR (DSGVO Art. 9). The reminder habit itself is good, because it prevents no-shows; it should become a shop-owned process instead.

---

**What I'd build after your answers** (on the files you already use, with no new software to learn):

1. A verified backup of the current files.
2. An order merge that never loses an order, warns loudly about a missing export and produces a daily pickup list per shop.
3. Automatic checks on every merge: allergy note vs. product, cakes per day vs. cold-room limit, the deposit rule and real duplicates.
4. One 14-allergen master list that prints a dated counter sheet.
5. A corrected catering template and a deposit log that matches the box.
6. A temperature log with limits and an "action taken" column.

---

**Three quick questions (one line each is plenty):**

1. **Original vision:** what did you originally want the order system to do, start to finish? For example, one live list both shops see, or just an evening merge?
2. **Pain:** where do you lose the most time or money today? No-shows, phone orders on paper, the evening merge, or something else?
3. **Sacred:** what must stay exactly as it is? For example, the program the shops type orders into, the Hauptladen laptop, or the WhatsApp group.

## Files created

None. A temporary test copy of `order_sync.py` was made in a separate folder and deleted, and your folder was not touched.
