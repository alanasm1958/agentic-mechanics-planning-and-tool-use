---
marp: true
paginate: true
size: 16:9
header: 'Tool Use and Agentic Mechanics'
footer: 'UNDP IICPSD  ·  Session 1: How AI agents think and act'
---

<style>
section { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 26px; color: #1a1a1a; padding: 56px 64px 64px; }
h1 { color: #0063AC; font-size: 46px; line-height: 1.12; }
h2 { color: #0063AC; font-size: 34px; margin-bottom: 10px; }
strong { color: #004e87; }
ul, ol { line-height: 1.5; }
section img { display: block; margin: 8px auto; }
table { font-size: 21px; margin: 10px auto 0; border-collapse: collapse; }
th { background: #0063AC; color: #fff; padding: 8px 14px; text-align: left; }
td { padding: 7px 14px; border-bottom: 1px solid #dbe6f3; }
.takeaway { font-size: 26px; color: #3b4252; text-align: center; margin-top: 8px; }
.accent { color: #0063AC; font-weight: 700; }
.muted { color: #5a6b80; }
.bigdef { font-size: 33px; line-height: 1.45; max-width: 86%; margin: 22px auto 0; text-align: center; }
.statement { font-size: 30px; line-height: 1.45; }
.cols { display: flex; gap: 30px; margin-top: 14px; }
.col { flex: 1; background: #f6f8fc; border: 2px solid #dbe6f3; border-radius: 12px; padding: 16px 22px; font-size: 23px; }
.col h3 { margin: 0 0 8px; color: #0063AC; font-size: 23px; }
.ex { color: #5a6b80; }
.hands { display: inline-block; background: #0063AC; color: #fff; font-size: 20px; font-weight: 700; padding: 6px 16px; border-radius: 8px; margin-bottom: 8px; }
.quiz li { margin-bottom: 6px; }
section.lead { text-align: center; }
section.lead h1 { font-size: 50px; }
section.center { text-align: center; }
section.divider { background: #0063AC; color: #ffffff; }
section.divider h1 { color: #ffffff; }
section.divider p { color: #dbe9f7; font-size: 26px; }
section.activity { background: #f3f8fc; }
.optbadge { position: absolute; left: 64px; top: 48px; font-size: 16px; font-weight: 700; color: #ffffff; background: #8a6d00; padding: 4px 12px; border-radius: 6px; }
section::before { content: ''; position: absolute; top: 22px; right: 46px; width: 74px; height: 64px; background: url('assets/undp-logo.svg') no-repeat right center; background-size: contain; }
section.divider::before { background-image: url('assets/undp-logo-white.svg'); }
section.lead::before { display: none; }
video { display: block; margin: 0 auto; height: 470px; border-radius: 12px; }
</style>

<!-- _class: lead -->

![h:140](assets/undp-logo.svg)

# Tool Use and Agentic Mechanics

Session 1: How AI agents think and act

**UNDP Istanbul International Center for Private Sector in Development**

<span class="muted">Prepared by Alan Al-Jammoor</span>

<!-- Welcome everyone. No coding today and nothing to install. Ask: "Who has used ChatGPT, Claude or a similar assistant?" Most hands go up. "Today we look at what happens when that kind of AI stops just answering and starts doing." -->

---

<!-- _class: center -->

## An AI agent made this

<video src="assets/cafe_promo.mp4" controls></video>

<!-- HOOK, 3 minutes. Play the 30 second video. Then say: "An AI agent made this, starting from a messy spreadsheet of café sales. Nobody edited it. Today you learn how that works. Next session, you watch it happen." If the video does not play inside the slides, open assets/cafe_promo.mp4 directly. -->

---

## Today, in plain words

- **Five ways to set up AI**, and why an agent is different
- **Inside an agent**: the loop that powers it
- **Tools**: how an AI reaches out and does things
- **Planning**: how it decides what to do next

<p class="takeaway">No coding. Lots of questions. One volunteer role-play.</p>

<!-- Keep this quick, under a minute. Promise: by the end, everyone can explain how an AI agent works to a friend. -->

---

<!-- _class: divider -->

# Part 1: Five ways to set up AI

Not all AI is the same. Here is the map.

---

## A ladder of five levels

![w:900](assets/five-levels.svg)

<!-- Walk up the ladder one step at a time, about a minute each. Each level adds one thing to the one before. 1: just the model, text in and text out. 2: the same model with extras, like search or your files. 3: several AI steps in a fixed order that a PERSON designed. 4: the model decides its own steps, in a loop. 5: a team of agents. Point to the bracket at the bottom: that is the line that matters. -->

---

## One everyday example per level

| Level | Example |
|-------|---------|
| **1. LLM** (large language model) | "Rewrite this email to sound more polite." |
| **2. Augmented LLM** | "What time is the last bus?" It reads the timetable PDF first. |
| **3. Workflow** | Every Monday: summarise new feedback, sort it by topic, draft the report. Same steps every time. |
| **4. Agent** | "Plan an event for 50 people under this budget." It searches, compares, finds a venue is full, and changes plan. |
| **5. Multi-agent** | A researcher agent, a writer agent and a fact checker agent produce one report together. |

<!-- Read two or three rows aloud, not all. Ask: "Which of these have you already used without knowing the name?" Most people have used 1 and 2. Define LLM: a large language model, the AI that reads and writes text. -->

---

<!-- _class: center -->

# Who decides the steps?

<p class="statement">In a <span class="accent">workflow</span>, a person decides the steps.<br>In an <span class="accent">agent</span>, the model decides.</p>

<p class="takeaway">That one difference is what this whole course is about.</p>

<!-- Pause here. This is the most important sentence of Part 1. A workflow is like a recipe you wrote. An agent is like a cook you hired: you give the goal, it decides the steps. -->

---

<!-- _class: activity -->

## Quick quiz: which level would you use?

<span class="hands">Hands up or poll</span>

<ol class="quiz">
<li>Translate a paragraph into French.</li>
<li>Answer questions about this year's bus timetable PDF.</li>
<li>Every Friday, turn the sign-up sheet into the same summary email.</li>
<li>Find a venue, caterer and date for 50 people under a budget, adapting when options fall through.</li>
<li>Write a 20-page market study, with research, writing and fact checking done by separate specialists.</li>
</ol>

<!-- 3 minutes. Read each one, count to three, hands up for the level number. Reveal on the next slide. -->

---

## Answers

<div class="cols">
<div class="col"><h3>1. LLM</h3>Text in, text out.</div>
<div class="col"><h3>2. Augmented LLM</h3>It needs the PDF.</div>
<div class="col"><h3>3. Workflow</h3>Same steps every week.</div>
</div>
<div class="cols">
<div class="col"><h3>4. Agent</h3>The steps change as it goes.</div>
<div class="col"><h3>5. Multi-agent</h3>Different roles. But would one agent do?</div>
</div>

<p class="takeaway">Not everything needs an agent. Use the <span class="accent">simplest level that does the job</span>.</p>

<!-- The point in passing: higher is not better. Agents cost more, take longer and can surprise you. You do not hire a project manager to make a cup of tea. -->

---

<!-- _class: divider -->

# Part 2: Inside an agent

The loop at the heart of every agent.

---

<!-- _class: center -->

## So, what is an agent?

<p class="bigdef">An <span class="accent">agent</span> is an AI that works toward a goal by deciding the next step, acting with a tool, looking at the result, and repeating until the goal is met.</p>

<!-- Read it slowly. Key words: goal, step, tool, result, repeat. The same model sits inside a plain chatbot. What makes it an agent is the loop around it. -->

---

## The loop

![w:640](assets/agent-loop.svg)

<p class="takeaway">The goal goes in once. Then plan, act, observe, again and again, until the job is done.</p>

<!-- Trace the loop with your finger. It takes one step, looks at what happened, and only then decides the next step. That is why it copes with messy, real tasks. -->

---

## Four parts, working together

![w:880](assets/agent-anatomy.svg)

<p class="takeaway">The model decides, the tools act, memory remembers, and the loop keeps it going.</p>

<!-- Brain, hands, notebook, heartbeat. Ask: "When an agent books a meeting room, which part does the booking, the brain or the hands?" The hands: a tool. That leads into Part 3. -->

---

<!-- _class: divider -->

# Part 3: Tools

How an AI reaches out and does things.

---

<!-- _class: center -->

## What is a tool?

<p class="bigdef">A <span class="accent">tool</span> is something the AI can ask your computer to do for it: search, calculate, read a file, send an email. The model asks. The computer does the work.</p>

<!-- Analogy: a very smart colleague who can say "please use the calculator" but cannot press the buttons. -->

---

## On its own, a model has three gaps

<div class="cols">
<div class="col"><h3>No exact maths</h3>It guesses at arithmetic.</div>
<div class="col"><h3>No fresh information</h3>It cannot see today.</div>
<div class="col"><h3>No actions</h3>It can only produce text.</div>
</div>

<p class="takeaway">A <span class="accent">calculator</span>, a <span class="accent">search</span> and an <span class="accent">action</span> tool fix all three.</p>

<!-- These gaps are the whole reason tools exist. Each gap maps to a kind of tool. -->

---

## A tool is just a card the model reads

![h:320](assets/tool-card.svg)

<p class="takeaway">Name, description, inputs. The model picks a tool by reading its <span class="accent">description</span>.</p>

<!-- The model never sees the code behind the tool, only this card. Hold up the printed tool card you will use in the role-play. -->

---

## The tool-use loop: ask, run, return, continue

![w:800](assets/tool-use-loop.svg)

<!-- Four steps, like passing a baton. The model asks for a tool, the computer runs it, the result goes back, the model continues. Now we act it out. -->

---

<!-- _class: activity -->

## Activity: be the agent

<span class="hands">Two volunteers, 6 minutes</span>

- **The Model**: may only write requests on sticky notes, using the tool card. Cannot touch the calculator.
- **The Computer**: holds the calculator. Does exactly what the note says, writes the result, hands it back.
- **The room** gives the goal:

<p class="takeaway">"A school has 4,750 students. 18% take the bus. How many bus seats do we need?"</p>

<!-- Round 1: Model writes "calculator: 4750 x 0.18", Computer returns 855, Model announces the answer. Round 2: secretly ask the Model to write a broken request, like "calculator: eighteen percent of the school". Computer hands back "Error: please write numbers only". Model fixes it. Applause. Then ask the room: "What did the Model never do?" It never pressed a button. That is tool use. -->

---

## When a tool fails, hand the failure back

<p class="statement">A good tool returns a clear message, not a crash. The agent reads it and tries again.</p>

<p class="takeaway"><span class="muted">weather("Springfield")  returns  </span>"Error: many Springfields, add a country"<span class="muted">,  so the agent tries  </span>weather("Springfield, USA")</p>

<!-- Exactly what happened in round 2 of the role-play. Errors are messages, not dead ends. -->

---

<!-- _class: optional activity -->

<div class="optbadge">Optional: 60 min version</div>

## The description is the steering wheel

<div class="cols">
<div class="col"><h3>Weak</h3>"does data stuff"<br><br><span class="ex">The model is left guessing.</span></div>
<div class="col"><h3>Your turn, in pairs</h3>Rewrite it in 60 seconds so a model knows exactly <b>what</b> it does and <b>when</b> to use it.</div>
</div>

<!-- 60 minute version only. Example strong answer: "Looks up a number from the sales table, such as total sales for a month. Use it when the question needs a figure from the sales data." Hear two answers. -->

---

<!-- _class: divider -->

# Part 4: Planning

How an agent decides what to do next.

---

<!-- _class: center -->

## Why plan?

<p class="bigdef"><span class="accent">Planning</span> means breaking a big task into small steps, the way a person would. AI does better one step at a time.</p>

<!-- Ask: "How would you plan a weekend trip?" Nobody books everything in one breath. You list steps. -->

---

## Four planning patterns

<div class="cols">
<div class="col"><h3>Chain of Thought</h3>"Think step by step" before answering. Shows its working.</div>
<div class="col"><h3>ReAct</h3>Think, act, observe, repeat. Reasoning and tools together.</div>
</div>
<div class="cols">
<div class="col"><h3>Plan and Execute</h3>Write the whole plan first, then follow it, like a recipe.</div>
<div class="col"><h3>Reflection and replanning</h3>Check its own work. If something fails, make a new plan.</div>
</div>

<!-- About 2 minutes. ReAct is the one most agents use, and it is the loop you just acted out. Plan and Execute: find the email, draft the reply, send it. Replanning: the flight tool is down, so it tries the train. -->

---

## ReAct: the pattern you will see next session

![w:620](assets/react-loop.svg)

<!-- This loop is exactly what you will watch a real agent do in Session 2. Thought, action, observation, again and again. -->

---

## Pick the simplest pattern that fits

<div class="cols">
<div class="col"><h3>Simple question</h3>Just ask, or "think step by step".</div>
<div class="col"><h3>Needs tools</h3>ReAct.</div>
</div>
<div class="cols">
<div class="col"><h3>Steps known up front</h3>Plan and Execute.</div>
<div class="col"><h3>Quality matters most</h3>Add Reflection.</div>
</div>

<!-- The cheat sheet to photograph. Patterns combine: ReAct plus Reflection is common. -->

---

## MCP: one standard plug for tools

![w:800](assets/mcp-connector.svg)

<p class="takeaway"><span class="accent">MCP</span> (Model Context Protocol) is a shared standard for connecting tools, like a USB-C port.</p>

<!-- One minute. Build a connection to a tool once, and any AI app that speaks MCP can use it. -->

---

<!-- _class: center -->

# You stay in charge

<p class="statement">Agents can act, so good agents <span class="accent">ask before risky steps</span>: spending money, sending messages, deleting things.<br><br>You set the goal. You approve the big moves. You can see every step.</p>

<!-- Next session you will see the agent stop and ask permission. That is not a weakness, it is a safety feature. -->

---

<!-- _class: activity -->

## Quick check

<span class="hands">Call out the answer</span>

1. Name the four steps of the agent loop.
2. Who actually runs the tool: the model or the computer?
3. Which pattern mixes thinking and acting, step by step?

<!-- Answers: 1. Goal, plan, act, observe (then repeat). 2. The computer. The model only asks. 3. ReAct. -->

---

<!-- _class: center -->

## Next session: watch an agent at work

<p class="statement">A real AI agent will clean messy data, build a presentation, make that video, and build a small app, live.<br><br>Your job: <span class="accent">spot everything you learned today</span>.</p>

<p class="takeaway">Nothing to install. Just bring your curiosity.</p>

<!-- Build anticipation. Tell them there will be a game: agent bingo. -->

---

<!-- _class: lead -->

![h:130](assets/undp-logo.svg)

# Thank you

You now know how an AI agent thinks and acts.

**UNDP Istanbul International Center for Private Sector in Development**

<span class="muted">Prepared by Alan Al-Jammoor</span>
