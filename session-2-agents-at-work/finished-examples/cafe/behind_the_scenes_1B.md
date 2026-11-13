# Behind the scenes: Demo 1B (the presentation)

**1. The plan.** Write a six-slide outline first, with one message per slide and the exact
numbers each slide would show. All numbers came from the clean file. Before building, I
revised my outline: a sharper slide 2 title, and a third chart on slide 5.

**2. Tools, in order.**
- *A slide-making guide (skill)*, for design rules. It suggested a JavaScript library that was not installed, so I used the Python library that was.
- *A font check.* Calibri existed only inside PowerPoint, so I chose Arial, which looks the same everywhere.
- *A Python script* that reads the clean data and builds the deck, so the numbers cannot drift from the data.
- *LibreOffice and a PDF-to-image tool* to turn each slide into a picture I could look at.
- *A file checker*, to confirm the file is valid.

**3. What went wrong.**
- The first render showed automatic chart titles ("Sales") and shadows I did not want. I removed both and rendered again.
- A safety check blocked a command that deleted old images. I overwrote them instead.

**4. How I checked.** I looked at every slide image for cut-off text and readable charts.
A separate script then compared three slide numbers with the clean data: total sales
($55,510), the Cappuccino bar ($11,406.50) and the Saturday average ($877.75). All matched.

I only checked the deck in LibreOffice, not in PowerPoint itself.
