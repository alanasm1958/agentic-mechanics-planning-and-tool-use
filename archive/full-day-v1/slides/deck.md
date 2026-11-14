---
marp: true
paginate: true
size: 16:9
header: 'Agentic Mechanics: Planning & Tool Use'
footer: 'UNDP IICPSD  ·  Agentic AI & Vibe Coding'
---

<style>
section { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 26px; color: #1a1a1a; padding: 56px 64px 64px; }
h1 { color: #0063AC; font-size: 46px; line-height: 1.12; }
h2 { color: #0063AC; font-size: 34px; margin-bottom: 10px; }
strong { color: #004e87; }
ul, ol { line-height: 1.5; }
section img { display: block; margin: 8px auto; }
.takeaway { font-size: 26px; color: #3b4252; text-align: center; margin-top: 8px; }
.accent { color: #0063AC; font-weight: 700; }
.muted { color: #5a6b80; }
.bigdef { font-size: 33px; line-height: 1.45; max-width: 86%; margin: 22px auto 0; text-align: center; }
.statement { font-size: 30px; line-height: 1.45; }
.cols { display: flex; gap: 30px; margin-top: 14px; }
.col { flex: 1; background: #f6f8fc; border: 2px solid #dbe6f3; border-radius: 12px; padding: 16px 22px; font-size: 23px; }
.col h3 { margin: 0 0 8px; color: #0063AC; font-size: 23px; }
.ex { color: #5a6b80; }
.note { font-size: 21px; line-height: 1.6; color: #3b4252; text-align: center; margin-top: 12px; }
.note b { color: #0063AC; }
.hands { display: inline-block; background: #0063AC; color: #fff; font-size: 20px; font-weight: 700; padding: 6px 16px; border-radius: 8px; margin-bottom: 8px; }
section.lead { text-align: center; }
section.lead h1 { font-size: 50px; }
section.center { text-align: center; }
section.divider { background: #0063AC; color: #ffffff; }
section.divider h1 { color: #ffffff; }
section.divider p { color: #dbe9f7; font-size: 26px; }
section.handson { background: #f3f8fc; }
section::before { content: ''; position: absolute; top: 22px; right: 46px; width: 74px; height: 64px; background: url('../assets/undp-logo.svg') no-repeat right center; background-size: contain; }
section.divider::before { background-image: url('../assets/undp-logo-white.svg'); }
section.lead::before { display: none; }
</style>

<!-- _class: lead -->

![h:150](../assets/undp-logo.svg)

# Agentic Mechanics: Planning & Tool Use

A hands-on day for beginners: how AI agents plan and use tools

**UNDP Istanbul International Center for Private Sector in Development**
<span class="muted">Agentic AI & Vibe Coding</span>

<span class="muted">Prepared by Alan Al-Jammoor</span>

<!-- Speaker notes: Welcome everyone warmly. This is a full day built for beginners and non-coders. No prior coding needed. Ask the room what made them curious enough to join. -->

---

## Who this is for, and our promise

- Beginners and non-coders are warmly welcome
- No prior coding experience needed, we start from zero
- We explain every term in plain words, the first time it appears
- By the end of today, you will have built a small AI agent yourself

<!-- Speaker notes: Make the promise concrete. Some people may feel out of place; tell them this day was designed for exactly them. Ask: "Who here has never written a line of code?" -->

---

## The day at a glance

- **Foundations**  what an agent is, and the loop at its heart
- **Tool Use**  how an agent reaches out and does things
- **Planning**  how an agent decides what to do next
- **Putting it together**  shapes, safety, and good judgement
- **Hands-on notebooks**  you read, run, and edit small agents all day

<!-- Speaker notes: Walk the arc of the day. Stress the rhythm: a little theory, then a notebook, repeated, so the ideas always land in something they can run. -->

---

## How today works

- We read, run, and observe together in **Google Colab**, nothing to install
- Ask a question at any time, nothing is too basic
- You use your own **Anthropic API key**, entered safely at run time
- We go at a beginner pace and pause often

<!-- Speaker notes: Set the working rhythm: read a little, run a cell, watch, then make a small edit. Reassure about the key, it is entered privately and never saved into a file. -->

---

<!-- _class: divider -->

# Part A: Foundations

What an agent is, and the loop at its heart.

---

## A chatbot answers. An agent acts.

![w:840](../assets/chatbot-vs-agent.svg)

<p class="takeaway">A chatbot tells you what to do. An <span class="accent">agent</span> goes and does it.</p>

<!-- Speaker notes: Walk the trip example left to right. The chatbot stops at a list; the agent keeps going and finishes the job. Ask: "Which one would actually save you an afternoon?" -->

---

<!-- _class: center -->

## So, what is an agent?

<p class="bigdef">An <span class="accent">agent</span> is an AI system that works toward a goal by deciding the next step, acting with a tool, looking at the result, and repeating until the goal is met.</p>

<!-- Speaker notes: Read it slowly. The key words are goal, step, tool, result, repeat. The same model sits inside a plain chatbot; what makes it an agent is the loop around it. -->

---

## The loop at the heart of every agent

![w:660](../assets/agent-loop.svg)

<p class="takeaway">The goal goes in once. Then it plans, acts, and observes, over and over, until the job is done.</p>

<!-- Speaker notes: Trace the loop with your finger. The agent takes one step, looks at what happened, and only then decides the next step. That is why it handles messy tasks. -->

---

## Four parts, working together

![w:900](../assets/agent-anatomy.svg)

<p class="takeaway">The model decides, the tools act, memory remembers, and the loop keeps it all going.</p>

<!-- Speaker notes: Name each part and tie it back to the loop. Every agent we build today has these same four parts. Ask: "Which part does the actual booking, the brain or the hands?" -->

---

<!-- _class: center -->

# It is not magic. It is this loop, run with care.

<p class="statement">You set the goal. You choose the tools. You can see every step.<br><br>Next, we give an agent its first <span class="accent">tool</span>.</p>

<!-- Speaker notes: Demystify before the hands-on. Powerful, but no mystery inside, which is exactly what keeps you in control. Build anticipation for tools. -->

---

<!-- _class: divider -->

# Part B: Tool Use

How an agent reaches out and does things.

---

<!-- _class: center -->

## What is a tool?

<p class="bigdef">A <span class="accent">tool</span> is a function the model can ask your code to run for it. The model proposes; your code does the work.</p>

<!-- Speaker notes: Use the analogy of a colleague who can say "please use the calculator" but cannot press the buttons. The model asks, your code acts. -->

---

## On its own, a model has three gaps

<div class="cols">
<div class="col"><h3>No exact math</h3>It guesses at arithmetic.</div>
<div class="col"><h3>No fresh data</h3>It cannot see today.</div>
<div class="col"><h3>No actions</h3>It can only produce text.</div>
</div>

<p class="takeaway">A <span class="accent">calculator</span>, a <span class="accent">search</span>, and an <span class="accent">action</span> tool fix all three.</p>

<!-- Speaker notes: These are not small flaws, they are the whole reason tools exist. Each gap maps to a kind of tool. -->

---

## A tool is just a card the model reads

![h:330](../assets/tool-card.svg)

<p class="takeaway">Name, description, inputs. The model chooses a tool by reading its <span class="accent">description</span>.</p>

<!-- Speaker notes: This three-part description is called a tool schema, a simple recipe card. The model never sees your code, only the card. -->

---

## The tool-use loop: ask, run, return, continue

![w:820](../assets/tool-use-loop.svg)

<p class="takeaway">Four steps, on repeat. The model asks, your code runs it and hands the result back.</p>

<!-- Speaker notes: Walk it one step per finger. The key idea is turn-taking, like passing a baton. We run this exact loop in Notebook 1. -->

---

## The description is the steering wheel

<div class="cols">
<div class="col"><h3>Weak</h3>"does currency stuff"<br><br><span class="ex">The model is left guessing.</span></div>
<div class="col"><h3>Strong</h3>"converts an amount from one currency to another, using today's rate"<br><br><span class="ex">It knows exactly when to use it.</span></div>
</div>

<!-- Speaker notes: Read both aloud and let the contrast land. The strong one names the inputs and the moment to use the tool. -->

---

## When a tool fails, hand the failure back

<p class="statement">A good tool returns a clear message, not a crash. The agent reads it and tries again.</p>

<p class="takeaway"><span class="muted">weather("Springfield")  gives  </span>"Error: many Springfields, add a country"<span class="muted">,  so the agent retries  </span>weather("Springfield, USA")</p>

<!-- Speaker notes: Errors are messages, not dead ends. A good error tells the model how to fix its request. -->

---

## MCP: one standard plug for tools

![w:840](../assets/mcp-connector.svg)

<p class="takeaway"><span class="accent">MCP</span> (Model Context Protocol) is a shared standard, like a USB-C port for tools.</p>

<!-- Speaker notes: A first look only. The big idea: one shared way to connect tools, so a tool built once works everywhere. -->

---

<!-- _class: handson -->

## Hands-on: Notebook 1

<span class="hands">Open Google Colab</span>

- Give a model a single calculator tool
- Watch it ask, your code run it, and the result go back
- See the model finish the answer on its own

<p class="takeaway">You write your first agent code here.</p>

<!-- Speaker notes: Get everyone into Colab and confirm Notebook 1 is open. Walk slowly; this is the first time they see the loop run for real. -->

---

<!-- _class: divider -->

# Part C: Planning

How an agent decides what to do next.

---

<!-- _class: center -->

## Why plan?

<p class="bigdef"><span class="accent">Planning</span> means breaking a hard task into small steps, the same way a person would. Models do better one step at a time.</p>

<!-- Speaker notes: Ask how they would plan a weekend trip. You do not book everything in one breath; you list steps. Models work better the same way. -->

---

## Chain of Thought: think step by step

<p class="statement">Ask the model to show its working before the answer. The phrase that does it: <span class="accent">"let us think step by step."</span></p>

<p class="takeaway"><span class="muted">3 boxes of 8 apples, some sold  gives  </span>"3 times 8 is 24, then subtract the ones sold..."</p>

<!-- Speaker notes: Chain of Thought is just asking the model to show its working. It is the simplest trick in the whole day. -->

---

## ReAct: think, act, observe, repeat

![w:660](../assets/react-loop.svg)

<p class="takeaway">The agent reasons and uses tools in the same flow. This is the key pattern for tool use.</p>

<!-- Speaker notes: The most important pattern in this section. Walk the weather example. This loop is exactly what they watch in Notebook 2. -->

---

## Plan and Execute: write the plan, then do it

<p class="statement">Best when the steps are known up front, like following a recipe.</p>

<div class="cols">
<div class="col"><h3>1. Plan</h3>Find the customer email, draft a reply, send it.</div>
<div class="col"><h3>2. Execute</h3>Do step 1, then step 2, then step 3.</div>
</div>

<!-- Speaker notes: Contrast with ReAct. Here the model writes the whole plan before touching a tool. Great when the path is clear. -->

---

## Two habits that make agents reliable

<div class="cols">
<div class="col"><h3>Reflection</h3>The agent checks its own answer and improves it, like proofreading before you submit.</div>
<div class="col"><h3>Replanning</h3>When a tool fails, it makes a new plan. The flight tool is down, so it tries the train.</div>
</div>

<!-- Speaker notes: Reflection raises quality; replanning adds resilience. Both separate a robust agent from a fragile script. -->

---

## Pick the simplest pattern that fits

<div class="cols">
<div class="col"><h3>Simple task</h3>Just ask, or Chain of Thought.</div>
<div class="col"><h3>Tool-heavy task</h3>Use ReAct.</div>
</div>
<div class="cols">
<div class="col"><h3>Steps known up front</h3>Plan and Execute.</div>
<div class="col"><h3>Quality matters most</h3>Add Reflection.</div>
</div>

<!-- Speaker notes: The cheat sheet to photograph. Patterns can combine, like ReAct plus Reflection. Most beginners start with plain ReAct. -->

---

<!-- _class: handson -->

## Hands-on: Notebook 2

<span class="hands">Open Google Colab</span>

- Build a small ReAct loop from scratch
- Watch it print every Thought, Action, and Observation
- You literally see the agent reason

<p class="takeaway">A planning pattern you can watch think.</p>

<!-- Speaker notes: Run Notebook 2 together. The agent prints each Thought, Action, and Observation so they can watch it reason. Walk the room. -->

---

<!-- _class: divider -->

# Part D: Putting it together

Shapes, safety, and good judgement.

---

## Three handy agent shapes

![w:760](../assets/agent-shapes.svg)

<div class="note">
<b>Routing</b> is best for many kinds of request, sending each one to the right specialist.<br>
<b>Orchestrator and workers</b> is best for one big task split into parts, for breadth and speed.<br>
<b>Evaluator and optimizer</b> is best when quality matters most: make, judge, then improve.
</div>

<!-- Speaker notes: Read the diagram, then the line below each idea: routing for variety, orchestrator for breadth and speed, evaluator for quality. Most real agents mix these. Ask which shape fits a task from their own work. -->

---

## Watch what the agent actually did

<p class="statement"><span class="accent">Logging</span> and <span class="accent">tracing</span> record each step in order, so you can find exactly where it went wrong.</p>

<p class="takeaway"><span class="muted">searched, read the result, </span>called the calculator <span class="muted">(went wrong here)</span><span class="muted">, wrote the answer</span></p>

<!-- Speaker notes: Without logs a wrong answer is a mystery; with logs it is a detective case you can solve. Like a plane's black box. -->

---

<!-- _class: center -->

## Check the path, not just the answer

<p class="bigdef">A right answer can come from luck. Look at the steps and tools the agent chose, not only the final result.</p>

<!-- Speaker notes: Judging only the final answer hides bad habits that bite later. Like a student who gets the right total with messy, lucky math. -->

---

## Keep three things in check

<div class="cols">
<div class="col"><h3>Cost</h3>Cap the number of steps.</div>
<div class="col"><h3>Speed</h3>Use the smallest model that works.</div>
<div class="col"><h3>Safety</h3>Ask before risky actions.</div>
</div>

<p class="takeaway">These pull against each other. The job is balance, not perfection.</p>

<!-- Speaker notes: The simplest safety habit: require a human yes before anything that spends money or deletes data. -->

---

<!-- _class: center -->

# Sometimes you should not use an agent

<p class="statement">If one prompt or a fixed script does the job, use that. Agents add cost, delay, and surprises. Reach for one only when the steps really vary.</p>

<!-- Speaker notes: The most senior advice of the day: avoid complexity you do not need. You do not hire a project manager to make a cup of tea. -->

---

<!-- _class: handson -->

## Hands-on: Notebooks 3 and 4

<span class="hands">Open Google Colab</span>

- **Notebook 3**: a multi-tool agent that picks the right tool
- **Notebook 4**: an agent that checks its own work and replans
- Then the **capstone** ties it all together

<p class="takeaway">You build a small agent end to end.</p>

<!-- Speaker notes: Run Notebooks 3 and 4 together, then point ahead to the capstone. Ask what task from their work would make a good capstone. -->

---

## What we built today

![w:540](../assets/agent-loop.svg)

<p class="takeaway">Every agent today was this one loop: <span class="accent">goal, plan, act, observe</span>, run with care.</p>

<!-- Speaker notes: Bring the day full circle to the loop we opened with. Tools, planning patterns, and shapes are all ways to make this loop better. -->

---

## Your capstone

<p class="statement">Build one small agent end to end. You pick the goal, the tools, and the pattern.</p>

<p class="takeaway">The brief and starter files are in the <span class="accent">assignments</span> folder.</p>

<!-- Speaker notes: Frame the capstone as the natural next step, not a test. They already have every piece they need from today. -->

---

## Keep learning

<p class="statement">A curated <span class="accent">resource library</span> sits alongside this deck, every link tagged by level and free to open.</p>

<p class="takeaway">Begin with the <span class="accent">Start here</span> list, then explore by topic.</p>

<!-- Speaker notes: The Start here list is the gentle on-ramp, every entry beginner-friendly and free. Encourage them to bookmark it. -->

---

<!-- _class: lead -->

![h:140](../assets/undp-logo.svg)

# Thank you

You built a small AI agent today. Keep going.

**UNDP Istanbul International Center for Private Sector in Development**

<span class="muted">Prepared by Alan Al-Jammoor</span>

<!-- Speaker notes: Close warmly and celebrate what the room accomplished, especially the non-coders. Invite final questions. -->
