"""Pick three numbers shown on the slides and recompute each from cafe_sales_clean.csv."""
import csv
from datetime import date
from pathlib import Path
from pptx import Presentation

HERE = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((HERE / "cafe_sales_clean.csv").open(encoding="utf-8")))
prs = Presentation(HERE / "cafe_review.pptx")


def slide_text(i):
    return " ".join(sh.text_frame.text for sh in prs.slides[i].shapes if sh.has_text_frame)


def chart_values(i):
    for sh in prs.slides[i].shapes:
        if sh.has_chart:
            plot = sh.chart.plots[0]
            return dict(zip(plot.categories, plot.series[0].values))


# 1. Total sales on slide 2
total = sum(int(r["quantity"]) * float(r["unit_price"]) for r in rows)
print("1. Slide 2 total sales: shows $55,510 ->", "$55,510" in slide_text(1), "| data:", round(total, 2))

# 2. Cappuccino bar on slide 3
capp = sum(int(r["quantity"]) * float(r["unit_price"]) for r in rows if r["product"] == "Cappuccino")
print("2. Slide 3 Cappuccino bar:", chart_values(2)["Cappuccino"], "| data:", round(capp, 2))

# 3. Saturday average on slide 4
sat_days = {}
for r in rows:
    d = date.fromisoformat(r["date"])
    if d.weekday() == 5:
        sat_days[d] = sat_days.get(d, 0) + float(r["total"])
sat = sum(sat_days.values()) / len(sat_days)
print("3. Slide 4 Saturday bar:", chart_values(3)["Saturday"], "| data:", round(sat, 2), "over", len(sat_days), "Saturdays")
