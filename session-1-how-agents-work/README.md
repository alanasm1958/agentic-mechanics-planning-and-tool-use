# Session 1: How AI agents think and act

Theory and mechanics, 45 or 60 minutes, **delivered online**. No coding, no API key, no
installs. Learners need nothing but the chat.

## What is in this folder

| File | What it is |
|------|------------|
| `slides/deck.html` | The deck to present (press F for full screen). The opening video plays inside it. |
| `slides/deck.pdf` | Same deck as a PDF, as a backup. The video does not play in the PDF. |
| `slides/deck.md` | Editable source (Marp). |
| `animation/agent-step-by-step.html` | The live animation: an agent working, step by step. Three scenarios. Works offline. |
| `slides/assets/cafe_promo.mp4` | The 30-second video for the opening hook. |

## Before class (10 minutes)

- [ ] Open `slides/deck.html` in Chrome or Edge, and `animation/agent-step-by-step.html` in a second tab.
- [ ] When you share your screen, share the browser tab and tick **share tab audio**, so the video has sound.
- [ ] Optional: set up the two quizzes as Mentimeter or Slido polls. Otherwise people type answers in the chat.
- [ ] Step through all three scenarios once, so you know where the "Ask the room" pauses are.

## How to drive the animation

- **Right arrow, space or Next:** forward one step. **Left arrow:** back. **Home:** restart.
- **1, 2, 3:** switch scenario. **L:** show the log (what happened so far). **A:** auto-play.
- When a yellow **Ask the room** box appears, pause and ask the chat before moving on.
- Links in the deck open a scenario directly. You can also add a step: `#2-9` opens scenario 2 at step 9.

| Scenario | Shown on slide | What it teaches |
|----------|:--------------:|-----------------|
| 1. School buses | 19 | Why a model needs tools (it guesses maths), and the plan, act, observe loop, twice |
| 2. Meeting room | 21 | The result changes the plan (replanning), asking before acting, recovering from an error |
| 3. Four habits, one job | 30 | All four planning habits in one job, and who decided to use each one |

## Run sheet

| Slides | Block | 45 min | 60 min |
|:------:|-------|:------:|:------:|
| 1 to 3 | Welcome and the video hook | 3 | 4 |
| 4 to 9 | The five levels of AI setups, and the quiz | 9 | 12 |
| 10 to 13 | Inside an agent: the loop in plain words, the four parts | 4 | 5 |
| 14 to 21 | Tools, animations 1 and 2, when a tool fails | 10 | 12 |
| 22 | Steering wheel challenge in the chat (marked Optional) | skip | 4 |
| 23 to 34 | Planning: four habits, animation 3, who decides, quiz | 14 | 17 |
| 35 to 36 | MCP, and staying in charge | 2 | 2 |
| 37 to 39 | Quick check, teaser for Session 2, thanks | 3 | 4 |

## How the planning part is built

This is the part learners find most confusing, so it follows one rule: **plain name first,
one example for everything, official name second.**

1. **You already have these habits** (slide 24). Start from a job they know: a budget update
   for their manager. They name the habits themselves.
2. **Why four** (slide 25). Each habit fixes a different way work goes wrong:

   | How work goes wrong | Habit | Official name | Example used |
   |---------------------|-------|---------------|--------------|
   | Rushing to an answer | Think step by step | Chain of Thought | The last Friday of the month |
   | Missing information | Look it up as you go | ReAct | Free rooms on Thursday |
   | Losing track in a long job | To-do list first | Plan and Execute | The café note |
   | Mistakes in the first draft | Check and fix | Reflection | $11,047 vs $11,407 |

3. **One slide per habit** (26 to 29), each with: the example, how it works, when it is
   used, and who decides.
4. **Watch them together** (animation 3). They are not four machines. They are habits one
   agent switches between.
5. **Who decides** (31) and **how** (32): the model decides in the moment, and you decide
   through your instructions. The choice follows the shape of the job.

If someone asks "is ReAct the same as the loop?": yes. ReAct is the research name for the
plan, act, observe loop from Part 2.

## Answers

**Which level would you use? (slide 8)**
1. LLM. 2. Augmented LLM. 3. Workflow. 4. Agent. 5. Multi-agent (and ask: would one agent do?)

**Which habit helps most? (slide 33)**
1. Think step by step (09:40 plus 2 h 35 min is 12:15).
2. Look it up as you go (today's rate is fresh information).
3. To-do list first (many parts).
4. Check and fix (a mistake is costly).
Bonus: a whole workshop within budget needs all four.

**Quick check (slide 37)**
1. Plan = decide the next step. Act = use a tool. Observe = read what came back.
2. The computer. The model only asks.
3. Think step by step, look it up as you go, to-do list first, check and fix. The room booking mostly used "look it up as you go".

## Key messages to land

- In a **workflow**, a person decides the steps. In an **agent**, the model decides.
- Plan = decide the next step. Act = use a tool. Observe = read what came back. Repeat until done.
- The model asks; the computer acts. The model picks a tool by reading its description.
- Four planning habits, because there are four ways work goes wrong. One job can use all four.
- The model picks habits by itself, but if a habit matters to you, ask for it.
- Good agents ask before risky steps. You stay in charge.

## Impact survey (last 3 minutes)

On the thanks slide, paste the Google Form link in the chat and give people 3 minutes to
fill it in before you close. One anonymous form, 10 questions, with a "before today / now"
self-rating and three short knowledge checks. Questions, answer key and how to read the
results: `evaluation/impact-survey.md`.

## Further reading (for you, and to recommend)

The **Hugging Face Agents Course, Unit 1** (free) explains the same loop with a friendly
example. They call it Thought, Action, Observation.
<https://huggingface.co/learn/agents-course/unit1/introduction>

## Re-rendering after edits

```bash
cd slides && npx @marp-team/marp-cli deck.md --pdf --allow-local-files && npx @marp-team/marp-cli deck.md --html --allow-local-files
```

To update the animation screenshots on slides 19, 21 and 30, open the animation at the
same step (for example `#1-8`) and take a 1280 by 800 screenshot into `slides/assets/`.
