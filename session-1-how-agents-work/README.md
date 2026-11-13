# Session 1: How AI agents think and act

Theory and mechanics, 45 or 60 minutes. No coding, no API key, no installs. Learners need
nothing.

## What is in this folder

| File | What it is |
|------|------------|
| `slides/deck.pdf` | The deck to present. 31 slides with speaker notes. |
| `slides/deck.html` | Same deck in a browser (press F for full screen). Use this one if you want the video to play inside the slides. |
| `slides/deck.md` | Editable source (Marp). |
| `slides/assets/cafe_promo.mp4` | The 30-second video for the opening hook. |
| `handouts/role-play-props.html` | Print before class: role signs, the tool card, request and result slips. |

## Before class (15 minutes)

- [ ] Print `handouts/role-play-props.html` (3 pages, A4). Bring sticky notes and a phone calculator.
- [ ] Check the video plays, inside `deck.html` or on its own.
- [ ] Set up the "Which level?" quiz as a poll (Mentimeter, Slido or hands up).

## Run sheet

| Slides | Block | 45 min | 60 min |
|:------:|-------|:------:|:------:|
| 1 to 3 | Welcome and the video hook | 3 | 4 |
| 4 to 7 | The five levels of AI setups | 8 | 10 |
| 8 to 9 | Quiz: which level would you use? | 3 | 5 |
| 10 to 13 | Inside an agent: the loop and its four parts | 6 | 7 |
| 14 to 20 | Tools, and the "be the agent" role-play | 10 | 12 |
| 21 | Rewrite challenge (marked Optional) | skip | 5 |
| 22 to 26 | Planning patterns | 7 | 8 |
| 27 to 28 | MCP, and staying in charge | 3 | 4 |
| 29 to 31 | Quick check, teaser for Session 2, thanks | 5 | 5 |

## The role-play in one paragraph

Two volunteers. **The Model** may only write requests on slips using the tool card, and
never touches the calculator. **The Computer** does exactly what each slip says and hands
back the result. The room reads the goal: *"A school has 4,750 students. 18% take the bus.
How many bus seats do we need?"* Round 1 runs cleanly (4,750 x 0.18 = 855). For round 2,
quietly ask the Model to write a vague request ("eighteen percent of the school"), so the
Computer hands back an error and the Model fixes it. Then ask the room: "What did the Model
never do?" It never pressed a button. That is tool use.

## Answers

**Which level would you use? (slide 8)**
1. LLM. 2. Augmented LLM. 3. Workflow. 4. Agent. 5. Multi-agent (and ask: would one agent do?)

**Quick check (slide 29)**
1. Goal, plan, act, observe, then repeat.
2. The computer. The model only asks.
3. ReAct.

## Key messages to land

- In a **workflow**, a person decides the steps. In an **agent**, the model decides.
- A tool is something the AI asks the computer to do. The model asks; the computer acts.
- The model picks a tool only by reading its description.
- Not everything needs an agent. Use the simplest level that does the job.
- Good agents ask before risky steps. You stay in charge.

## Re-rendering the slides after edits

```bash
cd slides && npx @marp-team/marp-cli deck.md --pdf --html --allow-local-files
```
