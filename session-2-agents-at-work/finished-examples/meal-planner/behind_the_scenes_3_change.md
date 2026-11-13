# Behind the scenes: Demo 3 change, weekly cost

**1. My plan.** Copy the planner to a new file so the original stays safe. Give every ingredient an example price, per kg, per litre or per item. Under each shopping line, add a price box and that line's cost. Add the line costs into one weekly total, and save prices on the device.

**2. Tools, in order.**
- A copy command, to make meal_planner_with_cost.html.
- Edit, to add the prices, price boxes and total.
- A test script driving a private Chrome, to type into the price boxes like a person.
- Screenshots, to see the phone, laptop and print views.
- Edit again to fix what I saw, then the tests again.

**3. What surprised me.** On a phone, the total sat below a long list, so after changing a price near the top you could not see it change. I added the estimate to the summary at the top too, and lined up the price boxes. I worried a total ending in exactly half a cent might round down. A test showed it did not, but I added a small safety step anyway.

**4. How I checked.** I worked out the starting total by hand: 29.92. I changed the chicken price from 6 to 8 per kg and the total rose by exactly 2.00, to 31.92. I also tested a decimal price, an empty price, reloading, changing a meal and changing the currency. I confirmed the original file was unchanged.
