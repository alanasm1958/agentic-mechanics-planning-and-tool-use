# Behind the scenes: Demo 3, meal planner

**1. My plan.** Pick 8 cheap, common dishes and give each ingredient an amount and a unit. Build one page with three parts: pick meals, shopping list, add your own dish. Make the list add up the same ingredient across meals. Then test it.

**2. Tools, in order.**
- Read the prompt file, to get the brief.
- Write, to create meal_planner.html.
- The Playwright browser, to open the page. It refused file links, so I served the folder on this computer instead.
- A small test script driving a separate, private Chrome that could open the file directly.
- Screenshots, to see the page at phone and laptop width.
- Edit, to fix what I saw.

**3. What surprised me.** In the first browser test, a meal I had not touched changed, then the page went blank. I think another session was sharing that browser, but I cannot prove it. In my private browser it never happened again. The screenshots showed the list sat far below the meals on a phone, so I added a "See shopping list" button.

**4. How I checked.** I planned three days and compared every line of the list with totals I worked out by hand. I swapped one dinner, removed another, and checked again. I also tested adding my own dish, the phone layout and the print view. I did not open a real printer; I checked a PDF of the print view instead.
