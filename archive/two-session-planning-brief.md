# Trainer Brief: Tool Use and Agentic Mechanics (two sessions)

Delivered by UNDP IICPSD for a **public audience**: mixed, mostly beginners and non-coders.
Two sessions of 45 to 60 minutes each.

- **Session 1, "How agents think and act":** the map of AI setups, the agent loop, tools
  and planning. Theory, but hands-on in spirit (polls, a role-play, quick quizzes).
- **Session 2, "Watch an agent at work":** a short lesson on writing prompts, then real
  projects done by an AI agent (Claude Code), with the mechanics from Session 1 pointed out
  as they happen.

The prompts for every Session 2 demo are in
[session2-demo-prompts.md](session2-demo-prompts.md).

---

## The story across both sessions

Session 1 gives people the lens. Session 2 gives them something real to look through it at.

One storyline runs through the demos: **a small neighbourhood café** with three months of
messy sales records. An agent cleans the data, turns it into a presentation for the owner,
and makes a 30-second promotional video from what it found. Then, live, the agent builds a
small everyday web tool (a weekly meal planner) and the audience steers what it adds.

A single story means beginners do not have to re-orient for every demo, and it shows a
key idea in action: the output of one step becomes the input of the next.

---

## Session 1: How agents think and act

**Promise:** "By the end you can explain how an AI agent decides what to do, how it uses
tools, and how it differs from other kinds of AI."

| Block | 45 min | 60 min | What happens |
|-------|:------:|:------:|--------------|
| **Hook** | 3 | 4 | Play the 30-second café video (made in advance in Demo 2). "An AI agent made this, starting from a messy spreadsheet. Today: how. Next session: you watch it work." |
| **The five levels of AI setups** | 8 | 10 | The map (see below). Build it one level at a time, one everyday example per level. |
| **"Which level would you use?"** | 3 | 5 | Quick-fire quiz, hands up or a poll (questions below). Message in passing: not everything needs an agent. |
| **The agent loop and its four parts** | 6 | 7 | Goal, plan, act, observe, repeat. Brain (model), hands (tools), notebook (memory), heartbeat (loop). |
| **Tools + "Be the agent" role-play** | 10 | 12 | What a tool is, the tool card, the tool-use loop. Then act it out: one volunteer is the Model (can only write requests on sticky notes), one is the Code (holds a phone calculator). Include one error and a retry. |
| **Rewrite challenge** | cut | 5 | Pairs rewrite a weak tool description ("does data stuff") in 60 seconds. "The model only reads the card." |
| **Planning patterns** | 8 | 8 | Chain of Thought, ReAct, Plan and Execute, Reflection and replanning. End on the "pick the simplest pattern" cheat sheet. |
| **MCP and staying in charge** | 4 | 4 | MCP as a USB-C port for tools. Humans approve risky actions. |
| **Close and teaser** | 3 | 5 | Three quick questions from A0 (Q2, Q5, Q9). "Next time you will see all of this inside a real tool." |

### The five levels (the map)

Each level adds one thing to the one before. Show it as a ladder.

| Level | What it is | Everyday example |
|-------|------------|------------------|
| **1. LLM** (large language model) | Text in, text out. Knows only what it learned in training. | Ask it to rewrite an email more politely. |
| **2. Augmented LLM** | The same model plus extras: search, your documents, memory, a tool or two. Still one question, one answer. | Ask a question and it searches the web or your PDF before answering. |
| **3. Workflow** | Several AI steps joined in a **fixed order that a person designed**. | Every Monday: summarise new feedback forms, sort them by topic, draft the weekly report. Same steps every time. |
| **4. Agent** | The model **decides its own steps** in a loop, using tools until the goal is met. | "Plan a community event within this budget": it searches venues, compares prices, notices one is full, and changes plan. |
| **5. Multi-agent** | Several agents with different roles working together, often with a manager agent handing out the work. | A researcher agent, a writer agent and a fact-checker agent producing one report. |

The line that matters most is between levels 3 and 4: **in a workflow, a person decides
the steps; in an agent, the model decides.** The existing "Three handy agent shapes"
diagram (routing, orchestrator and workers, evaluator and optimizer) can illustrate levels
3 and 5.

### "Which level would you use?" quiz

1. Translate a paragraph into French. **LLM**
2. Answer questions about this year's bus timetable PDF. **Augmented LLM**
3. Every Friday, turn the week's sign-up sheet into the same summary email. **Workflow**
4. Find a venue, caterer and date for a 50-person event under a budget, adapting when options fall through. **Agent**
5. Write a 20-page market study with research, writing and fact-checking done by separate specialists. **Multi-agent** (and ask: would one agent be enough?)

---

## Session 2: Watch an agent at work

**Promise:** "Today you will see a real AI agent clean data, build a presentation, make a
video and build an app, and you will spot every mechanic from last time."

**How the demos work:** projects 1 and 2 run **before class**, like a cooking show. In
class: show the result first (the wow), then rewind through what the agent did, then show
its "behind the scenes" report next to the real log. Project 3 runs **live**.

**Agent bingo:** every learner gets a card with six squares: *made a plan, used a tool, hit
an error, tried again, asked permission, checked its own work*. They call out when they
spot one.

| Block | 45 min | 60 min | What happens |
|-------|:------:|:------:|--------------|
| **Recap** | 2 | 3 | The loop and the five levels on one slide. Hand out bingo cards. |
| **Prompting** | 6 | 8 | What a prompt is, the five-part structure, weak vs strong. In the 60-minute version, pairs upgrade a weak prompt. (Details in the prompts file.) |
| **Demo 1: messy data to presentation** (made in advance) | 12 | 15 | Show the messy file, then the finished deck. Read the two prompts together and point to each of the five parts. Rewind the log: plan, tools, the rows it set aside, its checks. |
| **Demo 2: 30-second promo video** (made in advance) | 5 | 8 | Play it. Key point: the agent has no "make video" button. It wrote a small program that draws the video, then checked frames of it. Tools combined to do something none of them does alone. |
| **Demo 3: everyday web tool** (live) | 12 | 14 | Read the prompt together and have the room name the five parts. Run it. Before each step ask "what will it do next?". Open the result in the browser. Then the room picks **one change** and you give it to the agent live. |
| **Discussion** | 6 | 9 | Which level was each demo? (All agents. The meal planner it built has no AI in it at all: not everything needs AI.) Where would you keep a human in charge? What would you hand to an agent? |
| **Close** | 2 | 3 | Bingo winners. Take-home: the resource library "Start here" list; the coding notebooks for anyone who wants to see the loop in code. |

---

## Engagement checklist

- Change the activity type every 8 to 10 minutes: slide, question, activity.
- Use everyday examples (café, events, family meals, bus timetables), not office jargon.
- Celebrate errors out loud. An agent recovering from an error is the best moment of the demo.
- Keep text on screen large; zoom the terminal and browser.
- Ask before you show: "What will it do next?" turns watching into predicting.

## Before-delivery checklist

- [ ] Rename the course in the deck to "Tool Use and Agentic Mechanics"; remove "full day" wording.
- [ ] Add the five-levels slides and the quiz to the Session 1 deck; remove the hands-on notebook slides.
- [ ] Create the messy café dataset (`cafe_sales_messy.csv`) in a demo folder.
- [ ] Run Demo 1 and Demo 2 in advance; save the outputs, the logs and the "behind the scenes" reports.
- [ ] Rehearse Demo 3 live twice, including one audience change. Keep a finished copy as backup.
- [ ] Record a backup screen video of Demo 3 in case the network or the tool misbehaves.
- [ ] Print bingo cards, the role-play tool card and sticky notes.
- [ ] Prepare the "Which level?" poll and the three closing questions.
