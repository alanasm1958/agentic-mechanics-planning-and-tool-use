# Session 2: Watch an AI agent at work

Practical application, 45 or 60 minutes. A short prompting lesson, then an AI agent
(Claude Code) does three real jobs while the room spots the mechanics from Session 1.
Learners need nothing. You need Claude Code signed in on your laptop.

## What is in this folder

| Folder / file | What it is |
|---------------|------------|
| `slides/deck.pdf` / `deck.html` | The deck to present. 22 slides with speaker notes. |
| `prompts.md` | Every prompt, ready to copy and paste, with "why we wrote it like this" notes. |
| `demo-folder/` | Clean starting point: only the messy café file. Copy it before each rehearsal. |
| `finished-examples/cafe/` | Finished Jobs 1 and 2: clean data, presentation, video, plans and "behind the scenes" reports. Your backup and show copy. |
| `finished-examples/meal-planner/` | Finished Job 3: the meal planner, plus a version with the cost change. Backup for the live demo. |
| `handouts/agent-bingo.html` | Print before class: 12 different bingo cards, 2 per page. |
| `take-home/` | Reading list and the coding notebook for anyone who wants to go further. |
| `trainer-only/` | The script that generated the messy café file. You will not need it in class. |

## The three jobs

| Job | When it runs | What the room sees | Main lesson |
|-----|--------------|--------------------|-------------|
| 1. Messy data to presentation | Before class | Messy file, then the finished deck, then the rewind | Planning, chaining, not guessing, checking |
| 2. 30-second promo video | Before class | The video, then the storyboard and how it was made | Combining simple tools to do something new |
| 3. Meal planner web tool | Live | The agent building and testing an app, then a change the room votes for | The full loop, live; the room steers |

## Before class

**The day before (about 45 minutes)**
- [ ] Copy `demo-folder` to your desktop as `cafe-demo`. Open Claude Code in it and run
      prompts 1A, 1B and 2 from `prompts.md`, in order, approving each plan. After each,
      run the "behind the scenes" prompt. This gives you a **real, fresh log** to rewind in
      class. If anything fails, `finished-examples/cafe/` has everything ready.
- [ ] Rehearse Job 3 once in an empty folder, including one audience change.
- [ ] Print `handouts/agent-bingo.html`.

**Just before class (10 minutes)**
- [ ] Create an empty folder called `meal-planner-live` and open Claude Code in it.
- [ ] Open, ready in tabs: the deck, `cafe_sales_messy.csv`, `cafe_review.pptx`,
      `cafe_promo.mp4`, the Job 1 session log, and `finished-examples/meal-planner/meal_planner.html` (backup).
- [ ] Zoom the terminal text so the back row can read it.
- [ ] Open the backup meal planner once and click "Clear the week", so rehearsal choices
      saved in your browser do not show up in class.

## Run sheet

| Slides | Block | 45 min | 60 min |
|:------:|-------|:------:|:------:|
| 1 to 3 | Recap and agent bingo | 2 | 3 |
| 4 to 7 | Prompting: what a prompt is, weak vs strong, the five parts | 6 | 6 |
| 8 | Pair exercise (marked Optional) | skip | 3 |
| 9 to 10 | Meet the agent: Claude Code | 2 | 2 |
| 11 to 14 | Job 1: messy data, the two prompts, the result, the rewind | 11 | 13 |
| 15 | Job 2: play the video, show the storyboard | 5 | 7 |
| 16 to 17 | Job 3, live: build the meal planner, then the room's change | 12 | 15 |
| 18 to 20 | Discussion: which level, where to keep a human in charge | 5 | 8 |
| 21 to 22 | Take-home, bingo winners, thanks | 2 | 3 |

## How to show a result, then rewind

1. **Result first.** Open the finished file. Let the room react.
2. **Then the prompt.** Point at GOAL, CONTEXT, RULES, OUTPUT, CHECK on the slide.
3. **Then the rewind.** Scroll back through the Claude Code session (in the desktop app,
   open the session; in the terminal, use `/resume`). Pause on: the plan, two or three tool
   calls, a problem it hit, and its check.
4. **Then its own story.** Show the `behind_the_scenes` report next to the log. Ask: "Is
   its own account the same as what really happened?"

## If something goes wrong live

- **The agent stalls or the network drops:** say "this is why we always keep a backup",
  and open `finished-examples/meal-planner/meal_planner.html`.
- **It does something unexpected:** celebrate it. Ask the room which bingo square it was.
- **It asks permission:** perfect. Pause and read the request aloud before approving.

## Key messages to land

- A prompt is a brief to a capable new colleague who knows nothing about your situation.
- GOAL, CONTEXT, RULES, OUTPUT, CHECK. CHECK is what makes an agent review its own work.
- Look at the path, not just the answer.
- The meal planner has no AI in it. Not everything needs AI.
