// CHECK for meal_planner_with_cost.html: change one price and confirm the total updates.
// Run: node checks/check_cost.mjs   (from the meal-planner folder)
import { launch, pickJs, readListJs } from "./cdp.mjs";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const url = pathToFileURL(join(here, "..", "meal_planner_with_cost.html")).href;
let failures = 0;
function same(label, actual, expected) {
  const ok = JSON.stringify(actual) === JSON.stringify(expected);
  if (!ok) failures++;
  console.log(`${ok ? "PASS" : "FAIL"}  ${label}`);
  if (!ok) console.log("   expected:", expected, "\n   actual:  ", actual);
}

// Worked out by hand from the example prices (per kg, per litre or per item):
// bread 1.20, carrot 4 x 0.15, cheese 0.1 kg x 9, chicken 1 kg x 6, chopped tomatoes 2 x 0.80,
// oil 0.18 l x 2.50, eggs 8 x 0.25, fish 0.8 kg x 9, garlic 10 x 0.10, pepper 0.40,
// beans 2 x 0.90, lemon 2 x 0.30, onion 6 x 0.20, pasta 0.5 kg x 1.50, potatoes 0.8 kg x 1,
// lentils 0.3 kg x 2, rice 0.9 kg x 1.80, tomato 4 x 0.30  =  29.92
const START_TOTAL = "$29.92";

const total = `document.getElementById("cost-total").textContent`;
const priceInput = (item) => `Array.from(document.querySelectorAll("#shopping li.priced")).find(li => li.querySelector(".name").textContent === ${JSON.stringify(item)}).querySelector("input")`;
const lineCost = (item) => `Array.from(document.querySelectorAll("#shopping li.priced")).find(li => li.querySelector(".name").textContent === ${JSON.stringify(item)}).querySelector(".line-cost").textContent`;

// Real typing: focus the box, select what is there, then insert text like a keyboard does.
async function typePrice(b, item, text) {
  await b.evaluate(`(() => { const i = ${priceInput(item)}; i.focus(); i.select(); return true; })()`);
  if (text === "") await b.send("Input.dispatchKeyEvent", { type: "keyDown", key: "Backspace", code: "Backspace", windowsVirtualKeyCode: 8 });
  else await b.send("Input.insertText", { text });
  await b.sleep(100);
}

const b = await launch(url);
try {
  same("no cost box before any meal is planned", await b.evaluate(`document.getElementById("cost-box").hidden`), true);
  const plan = [["Monday|Lunch", "Red lentil soup"], ["Monday|Dinner", "Chicken and rice"],
    ["Tuesday|Lunch", "Vegetable omelette with bread"], ["Tuesday|Dinner", "Rice and beans"],
    ["Wednesday|Lunch", "Pasta with tomato sauce"], ["Wednesday|Dinner", "Baked fish with potatoes"]];
  for (const [slot, dish] of plan) await b.evaluate(pickJs(`select[data-slot="${slot}"]`, dish));
  same("shopping list still adds up (18 lines)", (await b.evaluate(readListJs)).length, 18);
  same("estimated total with example prices", await b.evaluate(total), START_TOTAL);
  same("summary at the top shows the estimate", await b.evaluate(`document.getElementById("summary").textContent`), "6 meals planned, 18 items to buy. Estimated cost: $29.92.");
  same("chicken line cost 1 kg x 6.00", await b.evaluate(lineCost("Chicken")), "$6.00");
  same("every item has a price", await b.evaluate(`document.getElementById("cost-note").textContent`), "");

  // THE CHECK: change one price and confirm the total updates.
  await typePrice(b, "Chicken", "8");
  same("chicken line cost after price change", await b.evaluate(lineCost("Chicken")), "$8.00");
  same("total goes up by exactly 2.00", await b.evaluate(total), "$31.92");
  same("summary at the top updates too", (await b.evaluate(`document.getElementById("summary").textContent`)).endsWith("Estimated cost: $31.92."), true);
  same("price box keeps focus while typing", await b.evaluate(`document.activeElement === ${priceInput("Chicken")}`), true);

  // Decimal price typed in two steps, like a person would.
  await typePrice(b, "Rice", "2");
  await b.send("Input.insertText", { text: ".5" });
  await b.sleep(100);
  same("rice 0.9 kg x 2.50 after typing 2.5", await b.evaluate(lineCost("Rice")), "$2.25");
  same("total after rice price change (31.92 - 1.62 + 2.25)", await b.evaluate(total), "$32.55");

  // Clearing a price: item shows no price and the note warns the total is too low.
  await typePrice(b, "Bread", "");
  same("cleared price shows 'No price'", await b.evaluate(lineCost("Bread")), "No price");
  same("total without bread", await b.evaluate(total), "$31.35");
  same("warning about missing price", await b.evaluate(`document.getElementById("cost-note").textContent`), "1 item has no price yet, so the real cost will be higher.");

  // Prices survive a reload, and a meal change uses the new prices.
  await b.reload();
  same("prices kept after reload", await b.evaluate(total), "$31.35");
  await b.evaluate(pickJs(`select[data-slot="Monday|Dinner"]`, "No meal planned"));
  // Chicken and rice removed: chicken 8.00, rice 0.5 kg x 2.50 = 1.25, onion 0.40, carrot 0.30, oil 0.03 l x 2.50 = 0.075
  same("total after removing Monday dinner", await b.evaluate(total), "$21.33");
  same("chicken gone from list", (await b.evaluate(readListJs)).some((l) => l.startsWith("Chicken")), false);

  // Currency symbol.
  await b.evaluate(`(() => { const c = document.getElementById("currency"); c.focus(); c.select(); return true; })()`);
  await b.send("Input.insertText", { text: "TL" });
  await b.sleep(100);
  same("currency can be changed", await b.evaluate(total), "TL 21.33");

  // Own dish with an unknown ingredient gets "No price" until the family types one.
  same("no page errors or warnings", b.errors, []);

  // Screenshots.
  await b.setViewport(375, 812, true);
  await b.sleep(200);
  same("no sideways scrolling at 375 px", await b.evaluate(`document.documentElement.scrollWidth <= 375`), true);
  await b.evaluate(`document.getElementById("list-section").scrollIntoView()`);
  await b.sleep(200);
  await b.screenshot(join(here, "cost_phone_375.png"));
  await b.setViewport(1280, 900, false);
  await b.evaluate(`window.scrollTo(0, 0)`);
  await b.sleep(200);
  await b.screenshot(join(here, "cost_laptop_1280.png"));
  await b.send("Emulation.setEmulatedMedia", { media: "print" });
  await b.screenshot(join(here, "cost_print_view.png"));
  await b.send("Emulation.setEmulatedMedia", { media: "" });
} catch (e) {
  failures++;
  console.log("FAIL  test crashed:", e.message);
} finally {
  await b.close();
}
console.log(failures ? `\n${failures} check(s) failed` : "\nAll checks passed");
process.exit(failures ? 1 : 0);
