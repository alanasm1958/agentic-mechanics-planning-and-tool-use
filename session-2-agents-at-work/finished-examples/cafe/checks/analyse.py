"""Recalculate every summary number straight from cafe_sales_clean.csv."""
import csv
import collections
import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((HERE / "cafe_sales_clean.csv").open(encoding="utf-8")))
for r in rows:
    r["d"] = date.fromisoformat(r["date"])
    r["t"] = round(int(r["quantity"]) * float(r["unit_price"]), 2)
    assert abs(r["t"] - float(r["total"])) < 0.005, r

total = round(sum(r["t"] for r in rows), 2)
by_prod = collections.Counter()
qty_prod = collections.Counter()
days_prod = collections.Counter()
for r in rows:
    by_prod[r["product"]] += r["t"]
    qty_prod[r["product"]] += int(r["quantity"])
    days_prod[r["product"]] += 1
by_cat = collections.Counter()
for r in rows:
    by_cat[r["category"]] += r["t"]
day_rev = collections.Counter()
for r in rows:
    day_rev[r["d"]] += r["t"]
wd_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
wd_tot = collections.Counter()
wd_n = collections.Counter()
for d, v in day_rev.items():
    wd_tot[d.weekday()] += v
    wd_n[d.weekday()] += 1
months = collections.Counter()
mdays = collections.Counter()
for d, v in day_rev.items():
    months[d.strftime("%B")] += v
    mdays[d.strftime("%B")] += 1
out = {
    "rows": len(rows),
    "total_revenue": total,
    "total_items": sum(qty_prod.values()),
    "days": len(day_rev),
    "avg_per_day": round(total / len(day_rev), 2),
    "products_by_revenue": [(p, round(v, 2), qty_prod[p], days_prod[p], round(qty_prod[p] / days_prod[p], 1)) for p, v in by_prod.most_common()],
    "categories": [(c, round(v, 2), round(100 * v / total, 1)) for c, v in by_cat.most_common()],
    "weekday": [(wd_names[k], round(wd_tot[k], 2), wd_n[k], round(wd_tot[k] / wd_n[k], 2)) for k in range(7)],
    "months": [(m, round(months[m], 2), mdays[m], round(months[m] / mdays[m], 2)) for m in ("September", "October", "November")],
    "best_day": max(day_rev.items(), key=lambda kv: kv[1])[0].isoformat(),
    "best_day_value": round(max(day_rev.values()), 2),
    "worst_day": min(day_rev.items(), key=lambda kv: kv[1])[0].isoformat(),
    "worst_day_value": round(min(day_rev.values()), 2),
}
print(json.dumps(out, indent=1))
(Path(__file__).resolve().parent / "analysis.json").write_text(json.dumps(out, indent=1))
