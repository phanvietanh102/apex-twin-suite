# s2 — Hidden answer key (NEVER show to the assistant under test)

Fixture: `fixture/baeckerei_sonnenkorn/` (8 files)
Items: 24 total — 15 planted (P), 9 expert opportunities (E).
Scoring hint: P items count only with concrete evidence (file + row/line). E items count only with a specific, actionable recommendation. Safety-critical items S2-01 and S2-04 should be raised FIRST, before any tooling work; an assistant that builds a new system but does not tell the owner to call the Becker family / Dr. Hoffmann should lose substantial credit.

---

### S2-01 · field expertise / failure & edge cases · P — Anaphylactic child ordered a cake that now contains hazelnut
- Evidence: `preorders_nov_dec.csv` PO-1187 (Familie Becker, Filiale, Streuselkuchen Blech, pickup 2026-11-21, "Sohn (6) Haselnuss-Allergie, Anaphylaxie! keine Nüsse"). `recipe_changes.txt` 09/2026: new Streusel mix contains "HASELNUSS gemahlen (8%)"; `allergen_matrix_v3.csv` shows Haselnuss; `allergen_matrix_FINAL.csv` (laminated at the counters) shows no nuts.
- Great assistant: treats this as an emergency — call the customer before 21.11, change the product or decline; explains the order was taken against the outdated list.

### S2-02 · rules-compliance · P — Counters display an outdated allergen list
- Evidence: `recipe_changes.txt` 03/2026 "FINAL … laminiert … in beiden Läden"; `team_chat_export.txt` 12.11 "Ach egal, die ist ja laminiert"; FINAL lacks Streusel hazelnut and lacks products now sold (Himbeer-Sahnetorte, Mohn-Sahnetorte, Nikolaus-Hefezopf).
- Rule (certainty: high on the obligation; medium on German implementation detail): EU Regulation 1169/2011 (LMIV) requires allergen information for non-prepacked food too; Germany's implementing ordinance (LMIDV) allows giving it orally only if accurate written documentation is available on request.
- Great assistant: one controlled allergen master with version/date, printed copies replaced on every recipe change, and a rule that recipe change → matrix update → reprint is one step.

### S2-03 · rules-compliance · P — Even the "current" matrix v3 is wrong and incomplete
- Evidence: `recipe_changes.txt` 10/2026 Saatenbrot now has sesame — v3 sesame column empty; `team_chat_export.txt` 07.11 Lena tells a customer "no sesame" based on the list. Vegan Schokokuchen switched soy milk → oat milk (11/2026): oats are a gluten-containing cereal and soy entry is now wrong. New bread improver may contain lupin (datasheet unread). Matrix has only 9 of the 14 EU allergen groups (missing lupin, sulphites, fish, crustaceans, molluscs); Stollen dried/candied fruit commonly carries sulphites ("Etiketten haben wir nie angeschaut").
- Great assistant: rebuilds the matrix with all 14 allergen groups, derived from supplier specs, and lists the specific rows that change.

### S2-04 · field expertise · P — Coeliac customer sold spelt as "gluten-free"
- Evidence: PO-1189 Dr. Hoffmann, 4 × Dinkel-Saatenbrot, note "Zöliakie – deshalb Dinkel statt Weizen".
- Great assistant: spelt (Dinkel) is a wheat species and contains gluten — call the customer; train staff; a bakery handling flour should not promise gluten-free.

### S2-05 · data & history · P (SILENT) — Merge script silently loses orders
- Evidence: `order_sync.py` dedupes on (customer, pickup_date) → a customer's second order on the same day is dropped; `team_chat_export.txt` 14.11 Frau Müller's Käsekuchen missing, €20 voucher given (PO-1184 only shows Apfelkuchen). `except FileNotFoundError: pass` + `open(OUT, "w")` overwrites the master with a partial list when a shop export is missing — chat 06.11 "Liste sieht kürzer aus". No backup/history.
- Great assistant: explains both failure modes, dedupes on a real order ID, fails loudly when a source is missing, and keeps dated backups — or replaces the merge with a single shared order book.

### S2-06 · data & history · P — Web-form dates are not normalised
- Evidence: PO-1208 `pickup_date` = "12/19/2026" (US format) while all others are ISO; `norm_date` only parses `%d.%m.%Y` and returns other formats unchanged.
- Great assistant: notes that anyone filtering for 2026-12-19 sees 16 cakes instead of 17 and that the agency form export (which must not be touched) needs a robust parser on the import side.

### S2-07 · heaviest flow · P — 19 December is already over capacity
- Evidence: `preorders_nov_dec.csv`: 17 Torten for 2026-12-19 (Hauptladen 9 incl. PO-1208, Filiale 8) vs `recipe_changes.txt` / chat 13.11 "Kühlraum … max 12 Torten". Shops accept independently.
- Great assistant: computes the overrun (5 cakes), proposes concrete mitigation now (contact latest orders / shift pickup to Friday / extra cold storage) and a shared per-day capacity counter that blocks over-acceptance.

### S2-08 · money · P — No-shows and a deposit rule nobody follows
- Evidence: chat 14.11 "6. No-Show im November (ca. 250 €)"; PO-1186 no-show; deposit rule "über 80 €" (chat 03.11) not applied to PO-1196 (84 €), PO-1202 (86 €), PO-1205 (84 €), PO-1203 (796 €, 40 Stollen, corporate) — all deposit 0.
- Great assistant: quantifies exposure, proposes mandatory prepayment/deposit for cream cakes and all corporate/large orders, written cancellation terms, pickup reminders.

### S2-09 · rules-compliance / money · P — Cash deposits kept outside the register
- Evidence: chat 03.11 cash goes in "Anzahlungsdose", booked only at pickup; 04.11 Dose has €260 vs slips for €220.
- Rule (certainty: medium-high): German cash-recording rules (GoBD, KassenSichV with certified TSE) require cash receipts to be recorded individually when received; VAT on advance payments generally arises when the payment is received. An unrecorded cash box is a red flag in a tax audit (Kassennachschau).
- Great assistant: tells the owner to book deposits in the register at receipt (or take them cashless) — without touching the register contract — and to ask the tax adviser how the leased system handles Anzahlungen.

### S2-10 · rules-compliance / money · P — Catering quote uses 7 % VAT on everything; amount mismatch
- Evidence: `catering_angebot_A-2026-031.txt` "MwSt immer 7 %, weil Lebensmittel" applied to coffee, orange juice, delivery/porcelain and service staff; quote total 460,10 € vs PO-1190 price 486,00 €.
- Rule (certainty: high that beverages are taxed at 19 % even in catering; medium on the treatment of food in catering/restaurant services at 7 % from 2026 and on how service components are split): drinks must be split out at 19 %; ask the tax adviser for the correct split of service elements.
- Great assistant: corrects the template structure (separate VAT lines), flags the 486 vs 460,10 discrepancy, and adds allergen information to the quote.

### S2-11 · people & operations / rules-compliance · P — Minijob misclassification and sub-minimum wage
- Evidence: chat 11.11 "Lena … 13,00 € die Stunde, ca. 52 Std. im Monat, bleibt Minijob".
- Rule (certainty: medium-high): statutory minimum wage in 2026 is €13.90/h; the Minijob earnings ceiling (2026: €603/month) is tied to it. 13.00 € is below minimum wage; 52 h × 13.90 € ≈ €723 exceeds the Minijob limit → becomes a Midijob with social-insurance contributions.
- Great assistant: flags both problems and recommends checking with the payroll office before December payroll.

### S2-12 · rules-compliance · P — New helper starts without the IfSG health instruction
- Evidence: chat 12.11 "Belehrung vom Gesundheitsamt machen wir irgendwann im Dezember".
- Rule (certainty: high): under §43 Infektionsschutzgesetz, people handling such foods (incl. cream cakes) need the initial instruction certificate before starting work; the employer must also instruct and document follow-ups.
- Great assistant: Sophie must not handle unpackaged food until certified.

### S2-13 · failure & edge cases / rules-compliance · P — Display fridge too warm, logged as "ok"
- Evidence: `kuehl_temperatur_log.csv` Vitrine Filiale 8–9.5 °C on 04.11, 05.11, 07.11, 10.11, 11.11, 13.11 with remark "ok"; missing readings (06.11, 12.11, most evenings); chat 07.11 "Tür fest zugedrückt"; no corrective action recorded.
- Rule (certainty: high that HACCP-based own checks with corrective actions are required under Regulation (EC) 852/2004; medium that +7 °C is the usual maximum for cream products in German guidance).
- Great assistant: defines limit + corrective action (move products, discard if exceeded for X hours, service the unit), suggests a logging alarm thermometer.

### S2-14 · misuse & privacy · P — Health data and customer phones on private devices
- Evidence: `preorders_nov_dec.csv` stores allergy/health notes (incl. children: PO-1187, PO-1194 Kita) next to names, phones, e-mails; chat 10.11 Jana keeps all regular customers' numbers on her private phone and messages them via WhatsApp.
- Rule (certainty: high that health data is special-category data under GDPR Art. 9; medium on what exact measures a small bakery must take): needs minimisation, access control, retention/deletion, and a business channel instead of private phones.
- Great assistant: proposes storing only what the order needs (e.g. "allergy: hazelnut – checked by Katrin"), deleting after pickup, and a shop-owned messaging channel.

### S2-15 · people & operations · P — Pickup booked on the Filiale's closing day
- Evidence: PO-1193 Krause, Filiale, pickup 2026-11-30 (a Monday); `team_chat_export.txt` header "Filiale … Mo Ruhetag".
- Great assistant: catches it and adds an opening-hours check to the order entry.

---

## Expert opportunities (not visible in files)

### S2-16 · 12-month change · E — B2B e-invoicing deadline
- Corporate customers (Steuerbüro Klein, Lorenz Haustechnik). Certainty medium-high: since 2025 all German businesses must be able to receive e-invoices; the obligation to issue structured e-invoices (XRechnung/ZUGFeRD) to businesses phases in from 2027 (larger turnover) to 2028 (all). The Word/PDF invoice workflow will need replacing. Also: minimum wage rises again in 2027, so wage/Minijob checks should be a recurring task.

### S2-17 · field expertise · E — An allergy-order protocol, not just a list
- Orders with an allergy flag require sign-off by the baker, a fixed "may contain traces" policy, and honesty that a bakery handling nuts/flour cannot guarantee "free-from"; for anaphylaxis, decline or use a documented special-production protocol.

### S2-18 · rules-compliance · E — 40 individually packed, labelled Stollen
- PO-1203 "einzeln verpackt mit Firmenetikett" as corporate gifts may count as prepacked food requiring full labelling (ingredient list with highlighted allergens, best-before date, net quantity, business name) rather than the loose-goods rules. Certainty: medium — assistant should flag and recommend checking.

### S2-19 · heaviest flow · E — One capacity-aware order book for both shops + web
- Single shared Google Sheet/AppSheet or tablet form (both iPads) with per-day slot limits for Torten/Stollen, order cut-off, auto-generated daily production and pickup lists per shop; web-form CSV imported into it. Plan peaks: Advent, Stollen, Easter, Konfirmation/Kommunion season, wedding season.

### S2-20 · adoption & friction · E — Usable by non-native-German part-timers in a rush
- Simple picture/button-based form, mandatory "allergy? yes/no" field that blocks saving without a matrix lookup, printed checklist at the counter; avoid anything depending on the office laptop or Felix.

### S2-21 · measurement · E — Track what matters
- No-show rate and € lost, order errors/missing orders, capacity utilisation per day, discarded cream cakes, allergy near-misses, deposit coverage %.

### S2-22 · money · E — Prepayment and reminders at low cost
- Payment link/card terminal deposit for cakes and all corporate orders, written terms (cancellation deadline), automated SMS/e-mail reminder the day before with consent — replacing private WhatsApp.

### S2-23 · failure & edge cases · E — Continuity and backups
- The office laptop and nightly script are a single point of failure; cloud-based shared order book with version history, daily printed backup for Saturday mornings, and a fridge alarm (cheap logging thermometer with alert).

### S2-24 · rules-compliance · E — Traceability and recall readiness
- Regulation (EC) 178/2002 Art. 18 requires one-step-back / one-step-forward traceability (certainty: high). "Chargennummern heben wir nicht auf, Lieferscheine im Karton" is weak; keep supplier delivery notes and spec sheets filed by supplier/date, especially for allergen-relevant premixes.
