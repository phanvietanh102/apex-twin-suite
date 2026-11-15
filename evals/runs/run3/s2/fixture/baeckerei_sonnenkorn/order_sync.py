"""Merge pre-orders from both shops + the website form into one file.
Written by Felix (Katrin's nephew), 2024. Run every evening on the Hauptladen laptop:
    python order_sync.py
"""
import csv
from datetime import datetime

SOURCES = ["orders_hauptladen.csv", "orders_filiale.csv", "webform_export.csv"]
OUT = "preorders_nov_dec.csv"


def norm_date(s):
    try:
        return datetime.strptime(s.strip(), "%d.%m.%Y").strftime("%Y-%m-%d")
    except ValueError:
        return s  # webform dates are probably fine already


rows, seen = [], set()
for src in SOURCES:
    try:
        with open(src, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                r["pickup_date"] = norm_date(r["pickup_date"])
                key = (r["customer"].strip().lower(), r["pickup_date"])
                if key in seen:
                    continue  # same order typed in both shops -> skip duplicate
                seen.add(key)
                rows.append(r)
    except FileNotFoundError:
        pass  # shop didn't export today, no problem

with open(OUT, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)

print("OK", len(rows), "orders")
