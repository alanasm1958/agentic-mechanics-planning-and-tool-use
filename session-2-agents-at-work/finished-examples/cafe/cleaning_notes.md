# Cleaning notes: Corner Café sales, September to November 2026

The original file, cafe_sales_messy.csv, was not changed. (Its fingerprint was taken before
and after cleaning and is identical.) The cleaned copy is cafe_sales_clean.csv.

## Rows in and rows out

| | Rows |
|---|---:|
| Lines in the original file (not counting the header) | 979 |
| Removed: completely blank lines | 9 |
| Removed: "TOTAL" lines copied from the till | 3 |
| Removed: exact copies of another line | 14 |
| Set aside: quantity missing (smudged) | 4 |
| Set aside: refunds | 3 |
| **Rows in the clean file** | **946** |

979 minus 9, 3, 14, 4 and 3 leaves 946. Every missing row is accounted for.

## What I fixed

**Dates.** All dates are now written as YYYY-MM-DD. 431 rows were already in that style.
The other 515 rows were rewritten:

| Style in the original | Example | Rows |
|---|---|---:|
| Month name, day, year | Sep 01 2026 | 219 |
| Day/month/year | 01/09/2026 | 219 |
| Day.month.short year | 12.10.26 | 32 |
| Day/month, no year | 12/10 | 24 |
| Month name and day, no year | Oct 12 | 21 |

Dates with slashes were read as day first, then month. This is certain, not a guess: 134 of
these dates have a first number above 12 (for example 13/10/2026), and the rows sit in date
order next to rows written as Sep 01 2026. The 45 dates with no year all come from the
notebook week (12 to 18 October), and the whole file covers 2026 only, so they were given 2026.

**Product names.** 128 rows had a misspelled or differently written product name. There were
22 different variants for the 11 real products, for example:

- Croisant, croissant to Croissant
- Expresso, espresso to Espresso
- Late, latte to Latte
- Cappucino, Capp., CAPPUCCINO, "cappuccino " (with a space) to Cappuccino
- OJ, Fresh OJ, Orange juice to Fresh Orange Juice
- Choc cake, Choc. Cake, chocolate cake to Chocolate Cake
- Chkn sandwich, chicken sandwich to Chicken Sandwich
- Soup, soup of day to Soup of the Day
- Cheese Pasty, Cheese pastry to Cheese Pastry

As a safety check, every renamed row's price was compared with that product's usual price
(for example, "Late" rows all cost 3.80, the same as Latte). All 946 rows matched, so no
row needed to be set aside for a price that did not fit.

**Prices.** 590 prices were rewritten as plain numbers with two decimals:
201 had a dollar sign ($2.20), 197 had "USD" after the number (2.20 USD) and 192 used a
comma instead of a decimal point (2,20). The other 356 were already plain numbers.

**New columns.** Each row now has a category (Hot drinks, Cold drinks, Bakery, Food) and a
total, which is quantity times unit price.

## Rows set aside (not guessed)

| Line in original | Date | Product | Problem |
|---:|---|---|---|
| 353 | 05/10/2026 | Cheese Pastry | Quantity smudged, left blank |
| 528 | 21/10/2026 | Capp. (Cappuccino) | Quantity smudged, left blank |
| 804 | 2026-11-15 | Fresh Orange Juice | Quantity smudged, left blank |
| 884 | 2026-11-22 | Cheese Pastry | Quantity smudged, left blank |
| 134 | 2026-09-13 | Chicken Sandwich | Refund of 1 (6.50) |
| 628 | Oct 30 2026 | Capp. (Cappuccino) | Refund of 1 (3.50) |
| 795 | 2026-11-14 | Cheese Pastry | Refund of 1 (2.80) |

The smudged rows were not filled in because any number would be invented. Refunds are money
given back, not sales, so they are not in the sales file. Together the refunds come to 12.80.

## Removed rows

- **Blank lines (9):** lines 37, 120, 151, 161, 166, 301, 650, 922 and 980.
- **Till totals (3):** TOTAL SEPTEMBER (line 300), TOTAL OCTOBER (line 649), TOTAL NOVEMBER
  (line 979). These are sums, not sales, so keeping them would count sales twice.
- **Exact copies (14):** lines 104, 150, 320, 416, 497, 502, 524, 675, 712, 769, 778, 794,
  836 and 911. Each is identical to the line just above it. One copy of each was kept.

## Independent check against the till

The till's own monthly totals were used to check the result:

| Month | Clean file | Till total | Difference | Explained by |
|---|---:|---:|---:|---|
| September | 17,321.70 | 17,321.70 | 0.00 | Exact match |
| October | 19,729.40 | 19,872.90 | 143.50 | 2 smudged rows (5 and 21 October) |
| November | 18,459.30 | 18,549.70 | 90.40 | 2 smudged rows (15 and 22 November) |

September matches to the cent, which confirms that the duplicates were real copies and that
the till counts sales before refunds. The October and November gaps are only the sales on the
four smudged rows, which are missing from the clean file. The till total for October also
covers the notebook week, so the hand-typed rows agree with the till.

## Other things the owner should know

- **Two days have no records at all:** Tuesday 22 September and Tuesday 10 November. The
  original file has no rows for these dates. I cannot tell whether the café was closed or the
  records were lost. Because of this, comparisons between days of the week use the average per
  day, not the plain total.
- **Matcha Latte** first appears on 1 October, so September has 10 products a day and
  October and November have 11.
- **No times of day.** The file records the date of each sale but not the hour, so it can
  show busy days but not busy hours.
