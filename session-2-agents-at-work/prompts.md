# Session 2: Prompting Lesson and Demo Prompts

Every prompt in this file uses the same five-part structure. That is on purpose: learners
meet the structure in the prompting lesson, then see it used in every demo, so by the end
of the session they can read a prompt and name its parts.

---

## Part 1: The prompting lesson (6 to 8 minutes)

### What is a prompt?

A **prompt** is the instructions you give an AI. The most useful way to think about it:

> A prompt is a brief to a very capable new colleague on their first day. They are smart
> and fast, but they know nothing about your situation except what you tell them.

This ties back to Session 1: the model chooses a tool only by reading its card, and it
does your task only by reading your prompt. If it is not written down, it does not exist.

### The five-part structure

| Part | The question it answers | Why it matters for an agent |
|------|------------------------|-----------------------------|
| **GOAL** | What do you want, and why? | The agent loops until the goal is met, so it needs to know what "met" means. |
| **CONTEXT** | Who is it for? What files, facts or background does it need? | The agent cannot read your mind or see your situation. |
| **RULES** | How should it work? What must it never do? | Keeps it safe and on track. "Show me a plan first" adds a human checkpoint. |
| **OUTPUT** | What exactly should it hand back, in what format, with what name? | You get something you can use, and the next step can pick it up. |
| **CHECK** | How should it test its own work before saying it is done? | Switches on the "observe" step of the loop: the agent reviews and fixes its own work. |

Short tasks can drop a part or two. The bigger the task, the more each part earns its place.

### Weak vs strong (the slide)

**Weak:**

> Make a presentation about my sales data.

Questions the agent has to guess: Which file? For whom? How long? What counts as good?
Which numbers can it trust? Is it allowed to change the file?

**Strong:** show Prompt 1B below and point to each of the five parts.

### Chat exercise (60-minute version only, 2 minutes)

Ask everyone to rewrite this weak prompt with the five parts and paste it in the chat:

> Help me plan a birthday party.

Read out two answers. Point out which part each person added that changes the result most
(usually CONTEXT or OUTPUT).

---

## Part 2: Demo prompts

Set up one demo folder before class containing `cafe_sales_messy.csv`. Open Claude Code
in that folder. Run prompts 1A, 1B and 2 before class; run prompt 3 live.

### Demo 1A: clean the messy data (run before class)

```
GOAL
Clean and organise three months of sales records for a small neighbourhood café, so the
owner can see what sells and when.

CONTEXT
The file cafe_sales_messy.csv in this folder came partly from the café's till and partly
from a notebook typed in by hand. Expect mixed date formats, misspelled product names,
prices written with currency symbols, blank rows, duplicate rows and stray "total" lines.
The owner is not technical.

RULES
- Show me a short plan before you change anything.
- Never edit the original file. Work on a copy.
- If a row is unclear, do not guess. Set it aside and list it in the notes.
- Use only tools on this computer. No online services.

OUTPUT
1. cafe_sales_clean.csv with the columns: date (YYYY-MM-DD), product, category, quantity,
   unit_price, total.
2. cleaning_notes.md: in plain language, what you fixed, how many rows each fix affected,
   and which rows you set aside and why.
3. summary.md: 5 to 8 bullet points covering the top 5 products by revenue, the busiest
   day of the week, and the revenue trend month by month.

CHECK
Before you finish, compare the number of rows in and out and explain the difference.
Recalculate total revenue from the clean file and confirm it matches summary.md.
```

**Why we wrote it like this**
- *"Show me a short plan before you change anything"*: this is Plan and Execute, with a human checkpoint before any action.
- *"Never edit the original file"*: safety. An agent can act, so we limit what it can damage.
- *"If a row is unclear, do not guess"*: stops the model filling gaps with made-up data.
- *Exact file and column names*: so the next prompt (1B) can pick up the result. This is how steps chain together.
- *The CHECK section*: makes the agent look at its own result and fix mismatches. That is the observe step of the loop.

### Demo 1B: turn it into a presentation (run before class)

```
GOAL
Turn the cleaned café data into a short presentation the owner can use to decide next
month's menu and opening hours.

CONTEXT
Use cafe_sales_clean.csv and summary.md from the previous step. The audience is the café
owner and one business partner. Neither is technical. They will look at it on a laptop.

RULES
- Every number on a slide must come from the clean data.
- Plain language, no jargon, one idea per slide.
- Show me the slide outline before you build the deck.

OUTPUT
A 6-slide PowerPoint file called cafe_review.pptx:
1. Title
2. Three headline numbers for the three months
3. Best sellers (chart)
4. Busiest days (chart)
5. What is not selling
6. Three practical recommendations
Include at least two charts.

CHECK
Render each slide to an image and look at it: text must fit, charts must be readable.
Then pick three numbers from the slides and confirm each one against the clean data.
```

**Why we wrote it like this**
- *"Use ... from the previous step"*: the output of one step becomes the input of the next.
- *"Every number must come from the clean data"*: keeps the presentation honest.
- *A numbered slide list*: removes guessing about length and order.
- *"Render each slide ... and look at it"*: the agent cannot see the slides unless it uses a tool to look. Watch for this tool call in the log.

### Demo 2: 30-second promo video (run before class)

```
GOAL
Make a 30-second promotional video for the café's social media, based on what the sales
data showed.

CONTEXT
Use summary.md for the best sellers and the busiest day. The café is called Corner Café
and is open every day from 07:00 to 19:00. The audience is local people scrolling on their
phones. The tone is warm and friendly.

RULES
- Show me a storyboard first: about 5 scenes, each with its text and its timing.
- Use only free tools that run on this computer, for example Python and ffmpeg.
  No stock footage, no downloads, no voiceover.
- Do not invent prices, offers or claims that are not in the data.
- Text must be large enough to read on a phone.

OUTPUT
cafe_promo.mp4: vertical (1080 by 1920), 30 seconds long, about 5 scenes of animated text,
colour and simple shapes, ending on the café name and opening hours.

CHECK
Confirm the file plays and lasts 30 seconds, give or take one second. Take one still frame
from each scene and look at it: text must be readable and nothing cut off. Fix any scene
that fails.
```

**Why we wrote it like this**
- *"Show me a storyboard first"*: a plan, in a form a non-technical person can approve.
- *"Only free tools on this computer"*: the agent has no "make video" button. It has to combine tools (write code, run it, check frames). That is the lesson.
- *"Do not invent prices or claims"*: marketing is where AI is most tempted to exaggerate.
- *"Take one still frame from each scene and look at it"*: the agent checks what it made rather than assuming it worked.

### Demo 3: everyday web tool (live, about 10 minutes)

```
GOAL
Build a simple weekly meal planner that turns the meals I pick into one shopping list, so
a family can plan the week and shop once.

CONTEXT
It is for a family who cooks at home. They are not technical and will open it on a laptop
or a phone.

RULES
- One single HTML file that works offline. No sign-in, no internet, no outside libraries.
- Simple design, large text, easy to use on a phone.
- Start with 8 common, affordable home dishes with their ingredients built in, and let the
  user add their own dish.

OUTPUT
meal_planner.html with:
- a 7-day grid with lunch and dinner, where the user picks a dish for each slot
- a shopping list that adds up the ingredients automatically
- a "Print shopping list" button

CHECK
Open the file in the browser, plan three days, and confirm the shopping list adds up the
ingredients correctly and updates when a meal is changed. Fix anything that does not work
before you finish.
```

**Why we wrote it like this**
- *"One single HTML file that works offline"*: keeps the live demo fast and low-risk, and the result opens with a double-click.
- *"8 dishes built in"*: the tool is useful the moment it opens.
- *The CHECK section*: the agent opens its own app and tests it. Ask the chat to watch for this.
- *Point to make in the discussion*: the finished meal planner contains no AI at all. The agent used AI to build an ordinary tool. Not everything needs AI.

**Audience change requests (tested in rehearsal, offer these as options):**

- "Add a switch to show the planner in [a language the audience speaks]."
- "Add an estimated cost for the week's shopping."
- "Mark which dishes are vegetarian, and add a filter."
- "Make the shopping list group items by type: vegetables, dairy, dry goods."

Give the request as a short prompt with its own CHECK, for example:

```
Add an estimated cost for the week's shopping. Use a simple price per ingredient that the
user can edit. CHECK: change one price and confirm the total updates.
```

---

## Part 3: The "behind the scenes" prompt

Run this straight after each demo made in advance (1A, 1B, 2) and save the answer. In
class, show it next to the real log.

```
Look back at what you just did. Explain it for a beginner audience in under 250 words:
1. The plan you made.
2. Each tool you used, in order, and why you chose it.
3. Any point where something went wrong or surprised you, and how you changed course.
4. How you checked the result.
Be honest: if you are unsure about a step, say so.
```

**Teaching point:** an agent's own account of its work can be tidier than what really
happened. Compare it with the log. This is "check the path, not just the answer" from
Session 1.
