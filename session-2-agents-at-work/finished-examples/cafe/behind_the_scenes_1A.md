# Behind the scenes: Demo 1A (cleaning the data)

**1. The plan.** Look at the file without touching it, list every kind of mess, then write a
small program that reads the original and writes a clean copy. Set aside anything unclear.

**2. Tools, in order.**
- *Shell commands* to list the folder and peek at the first lines.
- *Short Python checks* to count date styles, spellings, price styles, blanks and duplicates. Counting beats reading 979 lines by eye.
- *A file writer* to save the plan before changing anything.
- *A Python cleaning script*, so every row got exactly the same fixes. Plain Python only, as pandas was not installed.
- *A second script* that re-reads only the clean file to work out the summary.

**3. Surprises.**
- My plan said 5 smudged rows and 34 spellings. The script found 4 and 33. I added a correction to the plan.
- The till's monthly totals were a free cross-check. September matched to the cent, which showed the till leaves out refunds, so I did too.
- Two Tuesdays have no data, so I compared weekdays by average, not total.
- The file-writing tool refused to save summary.md, so I saved it with a shell command.

**4. How I checked.** 979 rows in, minus every removed row, equals 946 out. I recalculated
total revenue from the clean file ($55,510.40) and it matches summary.md. The original
file's fingerprint was unchanged.

My one judgement call: treating refunds as "not sales".
