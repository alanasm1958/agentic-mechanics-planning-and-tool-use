"""Generate the messy café sales file used in the Session 2 demos.

Run:  python3 make_cafe_dataset.py
Writes ../demo-folder/cafe_sales_messy.csv. Uses only the standard library and a fixed
seed, so the file is the same every time.

The story baked into the data (what a good analysis should find):
- Cappuccino is the top seller by revenue; Saturday is the busiest day.
- Soup sales rise as the weather cools (September to November); orange juice falls.
- Matcha Latte, added in October, barely sells.
- 12 to 18 October the till was broken, so those days were typed by hand from a notebook
  (different date format, more typos).
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 2026
START = date(2026, 9, 1)
END = date(2026, 11, 30)
NOTEBOOK_WEEK = (date(2026, 10, 12), date(2026, 10, 18))
OUT = Path(__file__).resolve().parent.parent / "demo-folder" / "cafe_sales_messy.csv"

# name, base price, base daily quantity, category (category is NOT in the export)
PRODUCTS = [
    ("Espresso", 2.20, 22),
    ("Cappuccino", 3.50, 34),
    ("Latte", 3.80, 20),
    ("Tea", 1.80, 18),
    ("Fresh Orange Juice", 4.00, 14),
    ("Croissant", 2.50, 24),
    ("Cheese Pastry", 2.80, 16),
    ("Chocolate Cake", 4.50, 9),
    ("Chicken Sandwich", 6.50, 12),
    ("Soup of the Day", 5.00, 6),
    ("Matcha Latte", 4.80, 0),
]

MISSPELLINGS = {
    "Cappuccino": ["Cappucino", "cappuccino ", "CAPPUCCINO", "Capp."],
    "Latte": ["latte", "Late"],
    "Chocolate Cake": ["Choc cake", "chocolate cake", "Choc. Cake"],
    "Fresh Orange Juice": ["Orange juice", "OJ", "Fresh OJ"],
    "Chicken Sandwich": ["Chkn sandwich", "chicken sandwich"],
    "Soup of the Day": ["Soup", "soup of day"],
    "Cheese Pastry": ["Cheese pastry", "Cheese Pasty"],
    "Croissant": ["Croisant", "croissant"],
    "Espresso": ["Expresso", "espresso"],
}

WEEKDAY_FACTOR = [0.8, 0.85, 0.9, 0.95, 1.1, 1.45, 1.25]  # Mon..Sun


def daily_quantity(rng, name, base, day):
    days_in = (day - START).days
    factor = WEEKDAY_FACTOR[day.weekday()]
    if name == "Soup of the Day":
        base = 4 + days_in * 0.16  # rises as it gets colder
    if name == "Fresh Orange Juice":
        base = base - days_in * 0.08  # falls as it gets colder
    if name == "Matcha Latte":
        if day < date(2026, 10, 1):
            return 0
        base = 1.2
    qty = round(base * factor * rng.uniform(0.75, 1.25))
    return max(qty, 0)


def format_date(rng, day, hand_typed):
    if hand_typed:
        return rng.choice([f"{day.day}.{day.month}.26", f"{day.day}/{day.month}", day.strftime("%b %d")])
    return rng.choice([day.isoformat(), day.isoformat(), day.strftime("%d/%m/%Y"), day.strftime("%b %d %Y")])


def format_price(rng, price):
    return rng.choice([f"${price:.2f}", f"{price:.2f}", f"{price:.2f}".replace(".", ","), f"{price:g}", f"{price:.2f} USD"])


def format_name(rng, name, hand_typed):
    typo_chance = 0.45 if hand_typed else 0.12
    if name in MISSPELLINGS and rng.random() < typo_chance:
        return rng.choice(MISSPELLINGS[name])
    return name


def build_rows(rng):
    rows, month_totals = [], {}
    day = START
    while day <= END:
        hand_typed = NOTEBOOK_WEEK[0] <= day <= NOTEBOOK_WEEK[1]
        closed = day in (date(2026, 9, 22), date(2026, 11, 10))  # two closed days
        for name, price, base in PRODUCTS:
            qty = 0 if closed else daily_quantity(rng, name, base, day)
            if qty == 0:
                continue
            month_totals[day.month] = month_totals.get(day.month, 0) + qty * price
            note = "typed from notebook" if hand_typed else ""
            rows.append([format_date(rng, day, hand_typed), format_name(rng, name, hand_typed),
                         str(qty), format_price(rng, price), note])
        if day.month != (day + timedelta(days=1)).month:
            label = day.strftime("%B").upper()
            rows.append([f"TOTAL {label}", "", "", f"{month_totals[day.month]:.2f}", "month total from till"])
            rows.append(["", "", "", "", ""])
        day += timedelta(days=1)
    return rows


def add_mess(rng, rows):
    messy = list(rows)
    data_idx = [i for i, r in enumerate(messy) if r[0] and not r[0].startswith("TOTAL")]
    for i in sorted(rng.sample(data_idx, 14), reverse=True):  # exact duplicate rows
        messy.insert(i, list(messy[i]))
    for i in rng.sample(data_idx, 6):  # blank rows
        messy.insert(i, ["", "", "", "", ""])
    for i in rng.sample(data_idx, 3):  # refunds
        r = messy[i]
        messy.insert(i + 1, [r[0], r[1], "-1", r[3], "refund"])
    for i in rng.sample(data_idx, 4):  # missing quantity: should be set aside, not guessed
        messy[i] = [messy[i][0], messy[i][1], "", messy[i][3], "qty smudged"]
    return messy


def main():
    rng = random.Random(SEED)
    rows = add_mess(rng, build_rows(rng))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Item", "Qty", "Price", "Notes"])
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    main()
