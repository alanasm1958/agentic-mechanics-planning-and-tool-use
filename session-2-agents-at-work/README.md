# Session 2: Watch an AI agent at work

Practical application, 45 or 60 minutes, **delivered online**. A short prompting lesson,
then an AI agent (Claude Code) does three real jobs on your shared screen while learners
spot the mechanics from Session 1. Learners need only the chat and the bingo link. You need
Claude Code signed in on your laptop.

## What is in this folder

| Folder / file | What it is |
|---------------|------------|
| `slides/deck.pdf` / `deck.html` | The deck to present. 22 slides with speaker notes. |
| `prompts.md` | Every prompt, ready to copy and paste, with "why we wrote it like this" notes. |
| `demo-folder/` | Clean starting point: only the messy café file. Copy it before each rehearsal. |
| `finished-examples/cafe/` | Finished Jobs 1 and 2: clean data, presentation, video, plans and "behind the scenes" reports. Your backup and show copy. |
| `finished-examples/meal-planner/` | Finished Job 3: the meal planner, plus a version with the cost change. Backup for the live demo. |
| `handouts/agent-bingo.html` | Online bingo card. Send it in the chat; each learner taps squares on a phone or laptop and gets their own shuffled card. |
| `take-home/` | Reading list and the coding notebook for anyone who wants to go further. |
| `trainer-only/` | The script that generated the messy café file. You will not need it in class. |

## The three jobs

| Job | When it runs | What the room sees | Main lesson |
|-----|--------------|--------------------|-------------|
| 1. Messy data to presentation | Before class | Messy file, then the finished deck, then the rewind | Planning, chaining, not guessing, checking |
| 2. 30-second promo video | Before class | The video, then the storyboard and how it was made | Combining simple tools to do something new |
| 3. Meal planner web tool | Live | The agent building and testing an app, then a change the chat votes for | The full loop, live; the audience steers |

## Before class

**The day before (about 45 minutes)**
- [ ] Copy `demo-folder` to your desktop as `cafe-demo`. Open Claude Code in it and run
      prompts 1A, 1B and 2 from `prompts.md`, in order, approving each plan. After each,
      run the "behind the scenes" prompt. This gives you a **real, fresh log** to rewind in
      class. If anything fails, `finished-examples/cafe/` has everything ready.
- [ ] Rehearse Job 3 once in an empty folder, including one audience change. **Record
      your screen** while you do it (on a Mac: Shift, Command and 5). If your internet
      struggles in class, you play this recording instead.
- [ ] Decide how learners get the bingo card: attach `handouts/agent-bingo.html` as a
      file in the meeting chat, or host it and paste the link. Test that it opens on a phone.

**Just before class (10 minutes)**
- [ ] Create an empty folder called `meal-planner-live` and open Claude Code in it.
- [ ] Open, ready in tabs: the deck, `cafe_sales_messy.csv`, `cafe_review.pptx`,
      `cafe_promo.mp4`, the Job 1 session log, and `finished-examples/meal-planner/meal_planner.html` (backup).
- [ ] Make text big enough to read in a video call: terminal or Claude Code font at
      20 pt or more, browser zoom at 125% or more.
- [ ] Turn on Do Not Disturb, and close email and messaging apps.
- [ ] Share your **whole screen** (you will switch between the deck, Claude Code, files
      and the browser), and tick **share computer sound** for the video.
- [ ] Have the chat open where you can see it while you present.
- [ ] Open the backup meal planner once and click "Clear the week", so rehearsal choices
      saved in your browser do not show up in class.

## Run sheet

| Slides | Block | 45 min | 60 min |
|:------:|-------|:------:|:------:|
| 1 to 3 | Recap, and send the bingo card in the chat | 2 | 3 |
| 4 to 7 | Prompting: what a prompt is, weak vs strong, the five parts | 6 | 6 |
| 8 | Fix-the-prompt exercise in the chat (marked Optional) | skip | 3 |
| 9 to 10 | Meet the agent: Claude Code | 2 | 2 |
| 11 to 14 | Job 1: messy data, the two prompts, the result, the rewind | 11 | 13 |
| 15 | Job 2: play the video, show the storyboard | 5 | 7 |
| 16 to 17 | Job 3, live: build the meal planner, then the change the chat votes for | 12 | 15 |
| 18 to 20 | Discussion: which level, where to keep a human in charge | 5 | 8 |
| 21 to 22 | Take-home links in the chat, bingo winners, thanks | 2 | 3 |

## How to show a result, then rewind

1. **Result first.** Open the finished file. Ask for a reaction in the chat.
2. **Then the prompt.** Point at GOAL, CONTEXT, RULES, OUTPUT, CHECK on the slide.
3. **Then the rewind.** Scroll back through the Claude Code session (in the desktop app,
   open the session; in the terminal, use `/resume`). Pause on: the plan, two or three tool
   calls, a problem it hit, and its check.
4. **Then its own story.** Show the `behind_the_scenes` report next to the log. Ask: "Is
   its own account the same as what really happened?"

## If something goes wrong live

- **The agent stalls or the network drops:** say "this is why we always keep a backup",
  and open `finished-examples/meal-planner/meal_planner.html`, or play your rehearsal
  recording.
- **It does something unexpected:** celebrate it. Ask the chat which bingo square it was.
- **It asks permission:** perfect. Pause and read the request aloud before approving.
- **The chat goes quiet:** ask a prediction question: "What will it do next? Type read,
  write, run or check." Predicting keeps people watching closely.
- **Your screen share lags:** narrate what the agent is doing, so people who see a frozen
  screen can still follow.

## Running the activities online

| Activity | Slide | How it works online |
|----------|:-----:|---------------------|
| Agent bingo | 3 | Send the bingo card in the chat. Learners tap squares as they spot them and type BINGO (three in a line) or FULL CARD in the chat. Note the first names. |
| Weak prompt guesses | 6 | Ask: "What would the agent have to guess?" Read out answers from the chat, then reveal. |
| Fix the prompt (60 min) | 8 | Everyone rewrites "Help me plan a birthday party" and pastes it in the chat. Read out two. |
| You are the client | 17 | People type 1, 2, 3 or 4. Count, or use a poll. Give the winning change to the agent. |
| Your turn to think | 20 | Each person answers one of the three questions in the chat. Invite one or two to unmute. |

## Key messages to land

- A prompt is a brief to a capable new colleague who knows nothing about your situation.
- GOAL, CONTEXT, RULES, OUTPUT, CHECK. CHECK is what makes an agent review its own work.
- Look at the path, not just the answer.
- The meal planner has no AI in it. Not everything needs AI.
