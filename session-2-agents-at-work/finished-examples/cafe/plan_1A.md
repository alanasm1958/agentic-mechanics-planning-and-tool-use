# Plan for Demo 1A: cleaning the café sales file

I looked at cafe_sales_messy.csv without changing it. It has 979 lines under the header,
covering 1 September to 30 November 2026. Here is what I found and what I plan to do.

## What I found

- Six different date styles: 2026-09-01, Sep 01 2026, 01/09/2026, 12.10.26, 12/10 and Oct 12.
  The last three have no year or a short year and all come from the hand-typed notebook week
  (12 to 18 October).
- 34 different spellings for 11 products (for example Croisant, Expresso, Late, OJ, Capp.).
- Prices written as $2.20, 2.20 USD, "2,20" (comma) and 2.2.
- 9 completely blank lines.
- 3 "TOTAL" lines (one per month) copied from the till.
- 14 lines that appear twice, exactly the same.
- 5 lines where the quantity is blank because it was smudged.
- 3 refund lines with a quantity of -1.

## What I will do

1. Leave the original file untouched. All work happens in a small Python script
   (checks/clean_cafe.py) that reads the original and writes new files.
2. Turn every date into YYYY-MM-DD. Dates with a slash are read as day/month (some have a
   day above 12, which proves it). Dates without a year get 2026, because the whole file
   covers September to November 2026.
3. Map every spelling to one standard product name, and check that each line's price matches
   that product's usual price. If a name or price does not fit, set the line aside.
4. Strip currency symbols and turn commas into decimal points, so prices are plain numbers.
5. Add a category for each product (Hot drinks, Cold drinks, Bakery, Food).
6. Remove blank lines, the TOTAL lines and the exact duplicates (keep one copy).
7. Set aside, without guessing: lines with a smudged quantity, and refund lines (they are
   money given back, not sales). Both are listed in the notes.
8. Use the till's monthly TOTAL lines as an independent check on my monthly sums.
9. Write cafe_sales_clean.csv, cleaning_notes.md and summary.md.

## How I will check

- Count rows in and out and explain every removed row.
- Recalculate total revenue from the clean file and confirm it matches summary.md.

## Correction after running the script

Two counts above were slightly off because I counted by eye before running the script:
there are 4 smudged lines, not 5 (the other blank quantities belong to blank lines and TOTAL
lines), and 33 spellings for the 11 products, not 34 (I had counted an empty name).
