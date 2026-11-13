// CHECK for meal_planner.html: open it in a real browser via file://, plan three days,
// confirm the shopping list adds up and updates when a meal changes.
// Run: node checks/check_meal_planner.mjs   (from the meal-planner folder)
import { launch, pickJs, typeJs, readListJs } from "./cdp.mjs";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, join, basename } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const file = process.argv[2] || join(here, "..", "meal_planner.html");
const url = pathToFileURL(file).href;
const shot = (name) => join(here, basename(file, ".html") + "_" + name);
let failures = 0;

function same(label, actual, expected) {
  const ok = JSON.stringify(actual) === JSON.stringify(expected);
  if (!ok) failures++;
  console.log(`${ok ? "PASS" : "FAIL"}  ${label}`);
  if (!ok) console.log("   expected:", expected, "\n   actual:  ", actual);
}

// Expected totals worked out by hand from the recipe amounts (not from the page code).
const AFTER_3_DAYS = [
  "Bread = 1 loaf", "Carrot = 4", "Cheese = 100 g", "Chicken = 1 kg", "Chopped tomatoes = 2 cans",
  "Cooking oil = 180 ml", "Eggs = 8", "Fish fillets = 800 g", "Garlic = 10 cloves", "Green pepper = 1",
  "Kidney beans = 2 cans", "Lemon = 2", "Onion = 6", "Pasta = 500 g", "Potatoes = 800 g",
  "Red lentils = 300 g", "Rice = 900 g", "Tomato = 4"];
const AFTER_SWAP = [
  "Bread = 1 loaf", "Carrot = 4", "Cheese = 100 g", "Chicken = 1 kg", "Chickpeas = 2 cans",
  "Chopped tomatoes = 2 cans", "Cooking oil = 165 ml", "Eggs = 8", "Garlic = 10 cloves", "Green pepper = 1",
  "Kidney beans = 2 cans", "Lemon = 1", "Onion = 7", "Pasta = 500 g", "Potatoes = 600 g",
  "Red lentils = 300 g", "Rice = 900 g", "Tomato = 7"];
const AFTER_CLEAR_TUE_DINNER = [
  "Bread = 1 loaf", "Carrot = 4", "Cheese = 100 g", "Chicken = 1 kg", "Chickpeas = 2 cans",
  "Chopped tomatoes = 2 cans", "Cooking oil = 135 ml", "Eggs = 8", "Garlic = 8 cloves", "Green pepper = 1",
  "Lemon = 1", "Onion = 6", "Pasta = 500 g", "Potatoes = 600 g",
  "Red lentils = 300 g", "Rice = 500 g", "Tomato = 5"];
const WITH_CUSTOM = [
  "Bread = 1 loaf", "Carrot = 4", "Cheese = 100 g", "Chicken = 1 kg", "Chickpeas = 2 cans",
  "Chopped tomatoes = 2 cans", "Cooking oil = 135 ml", "Eggs = 8", "Garlic = 8 cloves", "Green pepper = 1",
  "Kidney beans = 2 cans", "Lemon = 1", "Onion = 7", "Pasta = 500 g", "Potatoes = 1.1 kg",
  "Red lentils = 300 g", "Rice = 500 g", "Tomato = 5"];

const b = await launch(url);
try {
  const sel = (slot) => `select[data-slot="${slot}"]`;
  same("14 meal slots on the page", await b.evaluate(`document.querySelectorAll("#days select").length`), 14);
  same("each menu has 'No meal planned' + 8 dishes",
    await b.evaluate(`document.querySelector("#days select").options.length`), 9);
  same("empty list message at start", await b.evaluate(`document.getElementById("summary").textContent`), "No meals planned yet.");

  // Plan three days.
  const plan = [["Monday|Lunch", "Red lentil soup"], ["Monday|Dinner", "Chicken and rice"],
    ["Tuesday|Lunch", "Vegetable omelette with bread"], ["Tuesday|Dinner", "Rice and beans"],
    ["Wednesday|Lunch", "Pasta with tomato sauce"], ["Wednesday|Dinner", "Baked fish with potatoes"]];
  for (const [slot, dish] of plan) await b.evaluate(pickJs(sel(slot), dish));
  same("shopping list after planning 3 days", await b.evaluate(readListJs), AFTER_3_DAYS);
  same("summary after 3 days", (await b.evaluate(`document.getElementById("summary").textContent`)).startsWith("6 meals planned, 18 items to buy."), true);

  // Change one meal.
  await b.evaluate(pickJs(sel("Wednesday|Dinner"), "Chickpea and potato stew"));
  same("list updates when Wednesday dinner changes", await b.evaluate(readListJs), AFTER_SWAP);
  same("other slots untouched after the change",
    await b.evaluate(`Array.from(document.querySelectorAll("#days select")).filter(s => s.value).map(s => s.options[s.selectedIndex].text)`),
    ["Red lentil soup", "Chicken and rice", "Vegetable omelette with bread", "Rice and beans", "Pasta with tomato sauce", "Chickpea and potato stew"]);

  // Remove one meal.
  await b.evaluate(pickJs(sel("Tuesday|Dinner"), "No meal planned"));
  same("list updates when a meal is removed", await b.evaluate(readListJs), AFTER_CLEAR_TUE_DINNER);

  // Plan survives closing and reopening.
  await b.reload();
  same("plan is still there after reload", await b.evaluate(readListJs), AFTER_CLEAR_TUE_DINNER);

  // Add own dish: validation first.
  await b.evaluate(`document.querySelector("#add-form button[type=submit]").click()`);
  same("empty dish name is refused", await b.evaluate(`document.getElementById("form-message").textContent`), "Please give your dish a name.");
  await b.evaluate(typeJs("#dish-name", "rice and beans"));
  await b.evaluate(`document.querySelector("#add-form button[type=submit]").click()`);
  same("duplicate dish name is refused", (await b.evaluate(`document.getElementById("form-message").textContent`)).startsWith("There is already a dish"), true);
  await b.evaluate(typeJs("#dish-name", "Bean soup"));
  await b.evaluate(`document.querySelector("#add-form button[type=submit]").click()`);
  same("dish with no ingredients is refused", await b.evaluate(`document.getElementById("form-message").textContent`), "Please add at least one ingredient.");
  const rows = (n, part) => `#ing-rows .ing-row:nth-child(${n}) .${part}`;
  await b.evaluate(typeJs(rows(1, "ing-name"), "Kidney beans"));
  await b.evaluate(`document.querySelector("${rows(1, "ing-unit")}").value = "can"`);
  await b.evaluate(`document.querySelector("#add-form button[type=submit]").click()`);
  same("ingredient without amount is refused", await b.evaluate(`document.getElementById("form-message").textContent`), "Please give \"Kidney beans\" an amount bigger than 0.");
  await b.evaluate(typeJs(rows(1, "ing-amount"), "2"));
  await b.evaluate(typeJs(rows(2, "ing-amount"), "1"));
  await b.evaluate(typeJs(rows(2, "ing-name"), "onion"));
  await b.evaluate(typeJs(rows(3, "ing-amount"), "0.5"));
  await b.evaluate(`document.querySelector("${rows(3, "ing-unit")}").value = "kg"`);
  await b.evaluate(typeJs(rows(3, "ing-name"), "Potatoes"));
  await b.evaluate(`document.querySelector("#add-form button[type=submit]").click()`);
  same("own dish saved", await b.evaluate(`document.getElementById("form-message").textContent`), "\"Bean soup\" was added. You can now pick it in any meal.");
  same("own dish appears in every menu", await b.evaluate(`Array.from(document.querySelectorAll("#days select")).every(s => Array.from(s.options).some(o => o.textContent === "Bean soup"))`), true);
  await b.evaluate(pickJs(sel("Thursday|Lunch"), "Bean soup"));
  same("own dish adds into the list (onion merged, kg converted)", await b.evaluate(readListJs), WITH_CUSTOM);

  // Remove own dish: its slot is cleared.
  await b.evaluate(`document.querySelector("#my-dishes button").click()`);
  await b.sleep(200);
  same("removing own dish clears its meal", await b.evaluate(readListJs), AFTER_CLEAR_TUE_DINNER);
  same("removal is confirmed in words", await b.evaluate(`document.getElementById("form-message").textContent`), "\"Bean soup\" was removed.");

  // Print button.
  await b.evaluate(`window.__printed = 0; window.print = () => { window.__printed++; }; document.getElementById("print-list").click(); window.__printed`).then((n) => same("Print button calls the browser print", n, 1));
  await b.send("Emulation.setEmulatedMedia", { media: "print" });
  same("print view hides the planner and form",
    await b.evaluate(`["plan-section","add-section"].map(id => getComputedStyle(document.getElementById(id)).display)`), ["none", "none"]);
  await b.screenshot(shot("print_view.png"));
  await b.send("Emulation.setEmulatedMedia", { media: "" });
  await b.pdf(shot("print.pdf"));

  // Phone and laptop screenshots.
  await b.setViewport(375, 812, true);
  await b.sleep(200);
  same("no sideways scrolling at 375 px", await b.evaluate(`document.documentElement.scrollWidth <= 375`), true);
  await b.evaluate(`window.scrollTo(0, 0)`);
  await b.sleep(300);
  same("phone: shortcut to the list shows while list is off screen",
    await b.evaluate(`[document.getElementById("jump").hidden, document.getElementById("jump").textContent.startsWith("See shopping list (17 items")]`), [false, true]);
  await b.screenshot(shot("phone_375_top.png"), false);
  await b.evaluate(`document.getElementById("list-section").scrollIntoView()`);
  await b.sleep(300);
  same("phone: shortcut hides when the list is on screen", await b.evaluate(`document.getElementById("jump").hidden`), true);
  await b.screenshot(shot("phone_375.png"));
  await b.setViewport(1280, 900, false);
  await b.sleep(200);
  await b.screenshot(shot("laptop_1280.png"), false);

  // Clear the week.
  await b.evaluate(`document.getElementById("clear-week").click()`);
  await b.sleep(200);
  same("Clear the week asks first", b.dialogs.includes("Clear all the meals for this week?"), true);
  same("Clear the week empties the list", await b.evaluate(`document.getElementById("summary").textContent`), "No meals planned yet.");
  same("Print button disabled when list is empty", await b.evaluate(`document.getElementById("print-list").disabled`), true);

  same("no page errors or warnings", b.errors, []);
} catch (e) {
  failures++;
  console.log("FAIL  test crashed:", e.message);
} finally {
  await b.close();
}
console.log(failures ? `\n${failures} check(s) failed` : "\nAll checks passed");
process.exit(failures ? 1 : 0);
