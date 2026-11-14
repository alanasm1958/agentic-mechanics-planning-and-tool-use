"""Build cafe_review.pptx from cafe_sales_clean.csv. Every number is computed here from the data."""
import csv
import collections
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / "cafe_review.pptx"
FONT = "Arial"
BLUE = RGBColor(0x00, 0x63, 0xAC)
NAVY = RGBColor(0x0B, 0x2E, 0x4F)
INK = RGBColor(0x1E, 0x2B, 0x3A)
MUTED = RGBColor(0x5B, 0x6B, 0x7C)
GREY_BAR = RGBColor(0xC5, 0xD0, 0xDB)
TINT = RGBColor(0xEE, 0xF4, 0xFA)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PALE_BLUE = RGBColor(0xA9, 0xCB, 0xEA)
SOURCE = "Source: Corner Café sales records, 1 September to 30 November 2026 (cleaned file, 946 rows)."
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DRINKS = ["Cappuccino", "Espresso", "Latte", "Tea", "Fresh Orange Juice", "Matcha Latte"]


def money(x):
    return "${:,}".format(int(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)))


def load():
    rows = list(csv.DictReader((HERE / "cafe_sales_clean.csv").open(encoding="utf-8")))
    for r in rows:
        r["d"] = date.fromisoformat(r["date"])
        r["q"] = int(r["quantity"])
        r["t"] = float(r["total"])
    return rows


def compute(rows):
    total = sum(r["t"] for r in rows)
    prod = collections.Counter()
    qty = collections.Counter()
    pdays = collections.defaultdict(set)
    day = collections.Counter()
    for r in rows:
        prod[r["product"]] += r["t"]
        qty[r["product"]] += r["q"]
        pdays[r["product"]].add(r["d"])
        day[r["d"]] += r["t"]
    wd_tot, wd_n = collections.Counter(), collections.Counter()
    for d, v in day.items():
        wd_tot[d.weekday()] += v
        wd_n[d.weekday()] += 1
    month, mdays = collections.Counter(), collections.Counter()
    for d, v in day.items():
        month[d.month] += v
        mdays[d.month] += 1
    return {
        "total": total,
        "items": sum(qty.values()),
        "days": len(day),
        "per_day": total / len(day),
        "prod": prod.most_common(),
        "share": {p: v / total for p, v in prod.items()},
        "cups_per_day": {p: qty[p] / len(pdays[p]) for p in qty},
        "weekday": [(WEEKDAYS[k], wd_tot[k] / wd_n[k]) for k in range(7)],
        "month": {m: month[m] for m in (9, 10, 11)},
        "month_per_day": {m: month[m] / mdays[m] for m in (9, 10, 11)},
        "matcha_first": min(pdays["Matcha Latte"]),
    }


def text(slide, x, y, w, h, runs, size=16, color=INK, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, space_after=0):
    """runs: a string, or a list of paragraphs; each paragraph a string or list of (text, opts)."""
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, 0)
    paras = runs if isinstance(runs, list) else [runs]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space_after)
        parts = para if isinstance(para, list) else [(para, {})]
        for t, opts in parts:
            run = p.add_run()
            run.text = t
            f = run.font
            f.name = FONT
            f.size = Pt(opts.get("size", size))
            f.bold = opts.get("bold", bold)
            f.color.rgb = opts.get("color", color)
    return box


def shape(slide, kind, x, y, w, h, fill, radius=None):
    s = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    s.line.fill.background()
    s.shadow.inherit = False
    style = s._element.find(qn("p:style"))
    if style is not None:
        s._element.remove(style)
    if radius is not None:
        s.adjustments[0] = radius
    return s


def background(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def content_slide(prs, title):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    background(s, WHITE)
    text(s, 0.6, 0.45, 12.1, 0.8, title, size=34, bold=True, color=NAVY, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 0.6, 6.95, 12.1, 0.3, SOURCE, size=10, color=MUTED)
    return s


def style_chart(chart, number_format):
    chart.has_legend = False
    chart.has_title = False
    chart.font.name = FONT
    chart.font.size = Pt(13)
    chart.font.color.rgb = INK
    va = chart.value_axis
    va.visible = False
    va.has_major_gridlines = False
    va.has_minor_gridlines = False
    ca = chart.category_axis
    ca.format.line.color.rgb = GREY_BAR
    ca.has_major_gridlines = False
    ca.tick_labels.font.size = Pt(13)
    ca.tick_labels.font.color.rgb = INK
    plot = chart.plots[0]
    plot.gap_width = 45
    plot.has_data_labels = True
    dl = plot.data_labels
    dl.number_format = number_format
    dl.number_format_is_linked = False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
    dl.font.size = Pt(13)
    dl.font.bold = True
    dl.font.color.rgb = INK


def colour_points(chart, highlight):
    series = chart.plots[0].series[0]
    for i, on in enumerate(highlight):
        fill = series.points[i].format.fill
        fill.solid()
        fill.fore_color.rgb = BLUE if on else GREY_BAR


def note_card(slide, x, y, w, h, heading, body):
    shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, TINT, radius=0.06)
    text(slide, x + 0.35, y + 0.35, w - 0.7, h - 0.7,
         [[(heading, {"size": 20, "bold": True, "color": NAVY})]] + [[(b, {})] for b in body],
         size=15, color=INK, space_after=10)


def slide_title(prs, k):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    background(s, NAVY)
    shape(s, MSO_SHAPE.OVAL, 8.9, -1.2, 6.2, 6.2, BLUE)
    shape(s, MSO_SHAPE.OVAL, 10.4, 4.6, 2.6, 2.6, RGBColor(0x1C, 0x4E, 0x7E))
    text(s, 0.9, 2.0, 8.0, 1.1, "Corner Café", size=60, bold=True, color=WHITE)
    text(s, 0.9, 3.1, 8.0, 0.7, "Three months in numbers", size=32, color=PALE_BLUE)
    text(s, 0.9, 4.3, 7.6, 1.2, [
        "Sales review, 1 September to 30 November 2026",
        "To help plan next month's menu and opening hours",
    ], size=18, color=WHITE, space_after=6)
    s.notes_slide.notes_text_frame.text = (
        f"This review covers {k['days']} trading days of sales. All numbers come from the cleaned sales file.")


def slide_headlines(prs, k):
    s = content_slide(prs, "Sales rose in October, then held steady")
    cards = [
        (money(k["total"]), "total sales over the three months"),
        (f"{k['items']:,}", "items sold"),
        (money(k["per_day"]), "average sales per trading day"),
    ]
    w, gap, x0, y0 = 3.8, 0.35, 0.6, 1.65
    for i, (num, label) in enumerate(cards):
        x = x0 + i * (w + gap)
        shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, x, y0, w, 2.5, TINT, radius=0.06)
        text(s, x + 0.35, y0 + 0.4, w - 0.7, 1.0, num, size=48, bold=True, color=BLUE)
        text(s, x + 0.35, y0 + 1.45, w - 0.7, 0.8, label, size=16, color=INK)
    m, mp = k["month"], k["month_per_day"]
    text(s, 0.6, 4.6, 12.1, 0.4, "Sales per month", size=16, bold=True, color=NAVY)
    names = {9: "September", 10: "October", 11: "November"}
    for i, mo in enumerate((9, 10, 11)):
        x = x0 + i * (w + gap)
        text(s, x, 5.0, w, 0.9, [[(names[mo], {"size": 16, "color": MUTED})],
                                 [(money(m[mo]), {"size": 28, "bold": True, "color": NAVY})]])
    text(s, 0.6, 6.05, 12.1, 0.6,
         f"November looks lower only because it had fewer trading days. Per day, November "
         f"({money(mp[11])}) matched October ({money(mp[10])}), up from {money(mp[9])} in September.",
         size=14, color=MUTED)
    s.notes_slide.notes_text_frame.text = "Two days have no records at all: 22 September and 10 November."


def slide_best_sellers(prs, k):
    s = content_slide(prs, "Cappuccino brings in a fifth of all sales")
    prod = k["prod"]
    data = CategoryChartData()
    data.categories = [p for p, _ in prod]
    data.add_series("Sales", [round(v, 2) for _, v in prod])
    gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.5), Inches(1.45),
                            Inches(8.1), Inches(5.35), data)
    chart = gf.chart
    style_chart(chart, '"$"#,##0')
    chart.category_axis.reverse_order = True
    colour_points(chart, [i == 0 for i in range(len(prod))])
    cap = k["share"]["Cappuccino"]
    lat, chk = dict(prod)["Latte"], dict(prod)["Chicken Sandwich"]
    note_card(s, 8.95, 1.65, 3.8, 4.9, "What this shows", [
        f"Cappuccino earned {money(dict(prod)['Cappuccino'])}, about {round(cap * 100)}% of all sales.",
        f"Latte ({money(lat)}) and Chicken Sandwich ({money(chk)}) are almost tied in second place.",
        "Sales here means the money taken for each product over the three months.",
    ])
    s.notes_slide.notes_text_frame.text = "Bars show total sales in dollars per product, highest first."


def slide_days(prs, k):
    s = content_slide(prs, "Weekends are busiest, Saturday most of all")
    wd = k["weekday"]
    data = CategoryChartData()
    data.categories = [n for n, _ in wd]
    data.add_series("Average sales per day", [round(v, 2) for _, v in wd])
    gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.5), Inches(1.45),
                            Inches(8.1), Inches(5.35), data)
    chart = gf.chart
    style_chart(chart, '"$"#,##0')
    colour_points(chart, [n in ("Saturday", "Sunday") for n, _ in wd])
    avg = dict(wd)
    note_card(s, 8.95, 1.65, 3.8, 4.9, "What this shows", [
        f"A typical Saturday brings in {money(avg['Saturday'])}, about "
        f"{avg['Saturday'] / avg['Monday']:.1f} times a typical Monday ({money(avg['Monday'])}).",
        "Monday and Tuesday are the quietest days.",
        "Bars show the average per day, because two Tuesdays have no records.",
    ])
    s.notes_slide.notes_text_frame.text = "Average sales per trading day, by day of the week."


def slide_not_selling(prs, k):
    s = content_slide(prs, "Matcha Latte has not caught on")
    cpd = k["cups_per_day"]
    shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.6, 1.65, 4.3, 4.9, TINT, radius=0.06)
    text(s, 0.95, 1.95, 3.6, 1.4, f"{cpd['Matcha Latte']:.1f}", size=96, bold=True, color=BLUE)
    text(s, 0.95, 3.4, 3.6, 0.5, "cups a day", size=22, bold=True, color=NAVY)
    first = k["matcha_first"]
    text(s, 0.95, 4.1, 3.6, 2.2, [
        f"On the menu since {first.day} {first.strftime('%B')}.",
        f"{money(dict(k['prod'])['Matcha Latte'])} in total, under 1% of all sales.",
    ], size=15, color=INK, space_after=10)
    drinks = sorted(DRINKS, key=lambda p: -cpd[p])
    data = CategoryChartData()
    data.categories = drinks
    data.add_series("Cups per day", [round(cpd[p], 1) for p in drinks])
    gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(5.3), Inches(1.45),
                            Inches(7.5), Inches(4.6), data)
    chart = gf.chart
    style_chart(chart, "0.0")
    chart.category_axis.reverse_order = True
    colour_points(chart, [p == "Matcha Latte" for p in drinks])
    text(s, 5.45, 6.15, 7.2, 0.5, "Average drinks sold per trading day, by drink", size=13, color=MUTED)
    s.notes_slide.notes_text_frame.text = "Cups per day counts only the days each drink was on sale."


def slide_actions(prs, k):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    background(s, NAVY)
    text(s, 0.6, 0.45, 12.1, 0.8, "Three things to try next month", size=34, bold=True,
         color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    prod, avg = dict(k["prod"]), dict(k["weekday"])
    top3 = prod["Cappuccino"] + prod["Latte"] + prod["Chicken Sandwich"]
    recs = [
        ("Keep the best sellers stocked",
         f"Cappuccino, Latte and Chicken Sandwich bring in {money(top3)}, almost half of all "
         f"sales ({round(100 * top3 / k['total'])}%). Make sure they never run out, above all at weekends."),
        ("Decide on Matcha Latte",
         "It sells about 1 cup a day. Either take it off the menu, or keep it for one more month "
         "with a clear target, then decide."),
        ("Staff the weekend, then measure hours",
         f"Saturday and Sunday are the busiest days ({money(avg['Saturday'])} and {money(avg['Sunday'])} "
         "a day on average), so add staff then. The records show days, not hours, so note the time "
         "of each sale for a month before changing opening hours."),
    ]
    w, gap, x0, y0, h = 3.8, 0.35, 0.6, 1.65, 4.6
    for i, (head, body) in enumerate(recs):
        x = x0 + i * (w + gap)
        shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, x, y0, w, h, WHITE, radius=0.05)
        circ = shape(s, MSO_SHAPE.OVAL, x + 0.35, y0 + 0.35, 0.7, 0.7, BLUE)
        tf = circ.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = str(i + 1)
        r.font.name, r.font.size, r.font.bold, r.font.color.rgb = FONT, Pt(22), True, WHITE
        text(s, x + 0.35, y0 + 1.3, w - 0.7, 0.9, head, size=20, bold=True, color=NAVY)
        text(s, x + 0.35, y0 + 2.25, w - 0.7, h - 2.5, body, size=15, color=INK)
    text(s, 0.6, 6.95, 12.1, 0.3, SOURCE, size=10, color=PALE_BLUE)
    s.notes_slide.notes_text_frame.text = "Each idea is small and can be checked again after one month."


def main():
    k = compute(load())
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    prs.core_properties.title = "Corner Café: three months in numbers"
    prs.core_properties.author = "Corner Café"
    for build in (slide_title, slide_headlines, slide_best_sellers, slide_days, slide_not_selling, slide_actions):
        build(prs, k)
    prs.save(OUT)
    print("saved", OUT)


if __name__ == "__main__":
    main()
