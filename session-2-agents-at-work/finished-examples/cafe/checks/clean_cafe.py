"""Clean cafe_sales_messy.csv into cafe_sales_clean.csv. Never writes to the original."""
import csv
import collections
import json
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SRC = HERE / "cafe_sales_messy.csv"
OUT = HERE / "cafe_sales_clean.csv"
STATS = Path(__file__).resolve().parent / "clean_stats.json"
YEAR = 2026
MONTHS = {"Sep": 9, "Oct": 10, "Nov": 11}

NAME_MAP = {
    "espresso": "Espresso", "expresso": "Espresso",
    "cappuccino": "Cappuccino", "cappucino": "Cappuccino", "capp.": "Cappuccino",
    "latte": "Latte", "late": "Latte",
    "matcha latte": "Matcha Latte",
    "tea": "Tea",
    "fresh orange juice": "Fresh Orange Juice", "orange juice": "Fresh Orange Juice",
    "oj": "Fresh Orange Juice", "fresh oj": "Fresh Orange Juice",
    "croissant": "Croissant", "croisant": "Croissant",
    "cheese pastry": "Cheese Pastry", "cheese pasty": "Cheese Pastry",
    "chocolate cake": "Chocolate Cake", "choc cake": "Chocolate Cake", "choc. cake": "Chocolate Cake",
    "chicken sandwich": "Chicken Sandwich", "chkn sandwich": "Chicken Sandwich",
    "soup of the day": "Soup of the Day", "soup of day": "Soup of the Day", "soup": "Soup of the Day",
}
CATEGORY = {
    "Espresso": "Hot drinks", "Cappuccino": "Hot drinks", "Latte": "Hot drinks",
    "Matcha Latte": "Hot drinks", "Tea": "Hot drinks",
    "Fresh Orange Juice": "Cold drinks",
    "Croissant": "Bakery", "Cheese Pastry": "Bakery", "Chocolate Cake": "Bakery",
    "Chicken Sandwich": "Food", "Soup of the Day": "Food",
}


def parse_date(raw):
    """Return (date, style) or (None, reason)."""
    s = raw.strip()
    try:
        if m := re.fullmatch(r"(\d{4})-(\d\d)-(\d\d)", s):
            return date(int(m[1]), int(m[2]), int(m[3])), "YYYY-MM-DD"
        if m := re.fullmatch(r"([A-Z][a-z]{2}) (\d\d) (\d{4})", s):
            return date(int(m[3]), MONTHS[m[1]], int(m[2])), "Mon DD YYYY"
        if m := re.fullmatch(r"(\d\d)/(\d\d)/(\d{4})", s):
            return date(int(m[3]), int(m[2]), int(m[1])), "DD/MM/YYYY"
        if m := re.fullmatch(r"(\d\d)\.(\d\d)\.(\d\d)", s):
            return date(2000 + int(m[3]), int(m[2]), int(m[1])), "DD.MM.YY"
        if m := re.fullmatch(r"(\d\d)/(\d\d)", s):
            return date(YEAR, int(m[2]), int(m[1])), "DD/MM (no year)"
        if m := re.fullmatch(r"([A-Z][a-z]{2}) (\d\d)", s):
            return date(YEAR, MONTHS[m[1]], int(m[2])), "Mon DD (no year)"
    except (KeyError, ValueError) as exc:
        return None, f"date not understood ({exc})"
    return None, "date not understood"


def parse_price(raw):
    s = raw.strip()
    style = ("$" if "$" in s else "USD" if "USD" in s else "comma" if "," in s else "plain")
    s = s.replace("$", "").replace("USD", "").strip().replace(",", ".")
    return float(s), style


def main():
    with SRC.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        raw_rows = [(i, r) for i, r in enumerate(reader, start=2)]

    counts = collections.Counter()
    set_aside = []
    candidates = []
    seen = {}
    for line, r in raw_rows:
        d_raw, item, qty_raw, price_raw, note = (r + [""] * 5)[:5]
        if not any(x.strip() for x in r):
            counts["blank"] += 1
            continue
        if d_raw.strip().upper().startswith("TOTAL"):
            counts["total_line"] += 1
            set_aside.append({"line": line, "row": r, "reason": "till month total, not a sale"})
            continue
        key = tuple(x.strip() for x in r)
        if key in seen:
            counts["exact_duplicate"] += 1
            set_aside.append({"line": line, "row": r, "reason": f"exact copy of line {seen[key]}"})
            continue
        seen[key] = line
        if not qty_raw.strip():
            counts["smudged_qty"] += 1
            set_aside.append({"line": line, "row": r, "reason": "quantity missing (smudged)"})
            continue
        qty = int(qty_raw)
        if qty < 0:
            counts["refund"] += 1
            set_aside.append({"line": line, "row": r, "reason": "refund, not a sale"})
            continue
        d, style = parse_date(d_raw)
        if d is None:
            set_aside.append({"line": line, "row": r, "reason": style})
            continue
        counts["date_" + style] += 1
        product = NAME_MAP.get(item.strip().lower())
        if product is None:
            set_aside.append({"line": line, "row": r, "reason": "product name not recognised"})
            continue
        if item != product:
            counts["name_fixed"] += 1
            counts["name:" + item + " -> " + product] += 1
        price, pstyle = parse_price(price_raw)
        counts["price_" + pstyle] += 1
        candidates.append({"line": line, "row": r, "date": d, "product": product,
                           "quantity": qty, "unit_price": price, "notebook": note == "typed from notebook"})

    usual = {}
    for p in CATEGORY:
        usual[p] = collections.Counter(c["unit_price"] for c in candidates if c["product"] == p).most_common(1)[0][0]
    clean = []
    pair_seen = {}
    for c in candidates:
        if abs(c["unit_price"] - usual[c["product"]]) > 1e-9:
            set_aside.append({"line": c["line"], "row": c["row"], "reason": f"price differs from usual {usual[c['product']]:.2f}"})
            continue
        k = (c["date"], c["product"])
        if k in pair_seen:
            set_aside.append({"line": c["line"], "row": c["row"], "reason": f"same day and product as line {pair_seen[k]}, different numbers"})
            continue
        pair_seen[k] = c["line"]
        clean.append(c)

    clean.sort(key=lambda c: (c["date"], list(CATEGORY).index(c["product"])))
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "product", "category", "quantity", "unit_price", "total"])
        for c in clean:
            w.writerow([c["date"].isoformat(), c["product"], CATEGORY[c["product"]], c["quantity"],
                        f"{c['unit_price']:.2f}", f"{c['quantity'] * c['unit_price']:.2f}"])

    days = sorted({c["date"] for c in clean})
    per_day = collections.Counter(c["date"] for c in clean)
    stats = {
        "rows_in": len(raw_rows), "rows_out": len(clean), "counts": dict(counts),
        "usual_prices": usual, "first_day": days[0].isoformat(), "last_day": days[-1].isoformat(),
        "days_present": len(days),
        "days_with_unusual_product_count": {d.isoformat(): n for d, n in per_day.items() if n not in (10, 11)},
        "notebook_rows_kept": sum(c["notebook"] for c in clean),
        "set_aside": [{"line": s["line"], "row": s["row"], "reason": s["reason"]} for s in set_aside],
    }
    STATS.write_text(json.dumps(stats, indent=2))
    print(json.dumps({k: v for k, v in stats.items() if k != "set_aside"}, indent=2))
    for s in set_aside:
        print(s["line"], s["row"], s["reason"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
