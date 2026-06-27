# Course Outline (Master, full day)

Module: Agentic Mechanics, Planning & Tool Use
Audience: beginners and non-coders learning to build with AI assistance.
Format: full-day master set. Trim guidance for shorter formats is at the end.

## One line description

How an AI model stops being a chatbot and becomes an agent: it makes a plan, calls tools
to act in the world, looks at the results, and adjusts until the job is done.

## Plain-language promise to the learner

By the end of the day you will have built, with your own hands, a small AI agent that
decides what to do, uses tools to do it, checks its own work, and you will understand
every part of how it works. No prior coding required.

## Learning objectives

By the end of the session a learner can:

1. Explain in plain words what makes a system an agent, and name the steps of the agent loop.
2. Describe what a tool is and follow a full tool-use loop from request to result.
3. Describe the main planning patterns and pick one that fits a task.
4. Run and lightly modify a small agent that plans, uses more than one tool, and recovers from a mistake.
5. Judge when an agent is the right choice, and talk sensibly about cost, safety, and how to tell if it is working.

## Teaching order and why

We lead with tool use because watching a model call a tool is the clearest "aha" for a
beginner. Once tools feel real, planning makes sense, because planning is mostly about
deciding which tools to use and in what order. So the flow is: Foundations, then Tool Use,
then Planning, then putting it together.

## Full-day agenda (master)

Times are a guide. Breaks and lunch are marked. Hands-on blocks use the notebooks.

Morning
- 09:00 to 09:20  Welcome and framing. What you will be able to do by the end of the day.
- 09:20 to 09:45  Hook. Live demo of an agent that plans and uses tools to solve a real task.
- 09:45 to 10:30  Part A. Foundations: chatbot vs agent, the agent loop, the anatomy of an agent.
- 10:30 to 10:45  Break.
- 10:45 to 11:15  Notebook 0. Open Colab, enter your key safely, send your first message to the model.
- 11:15 to 12:15  Part B. Tool Use: what a tool is, the schema, the tool-use loop, errors, several tools, a first look at MCP.
- 12:15 to 12:45  Notebook 1. Your first tool-use loop.
- 12:45 to 13:45  Lunch.

Afternoon
- 13:45 to 14:30  Part C. Planning: why plan, Chain of Thought, ReAct, Plan and Execute, Reflection, replanning.
- 14:30 to 15:10  Notebook 2. A planning pattern you can watch think (ReAct).
- 15:10 to 15:25  Break.
- 15:25 to 15:55  Notebook 3. A multi-tool agent that picks the right tool.
- 15:55 to 16:25  Part D. Putting it together: agent shapes, evaluation, cost, and safety.
- 16:25 to 17:00  Notebook 4 and capstone kickoff. Reflection and replanning, then introduce the capstone.
- 17:00          Wrap. Where to go next and a tour of the resource library.

## Part A. Foundations (detail)

- A chatbot answers. An agent acts. The difference shown with one example.
- The agent loop: goal, plan, act, observe, repeat. A simple diagram learners will see again all day.
- The anatomy of an agent: a model (the brain), tools (the hands), memory (the notebook), and a loop (the heartbeat).
- Quick myth-busting: an agent is not magic and not conscious. It is this loop, run carefully.

## Part B. Tool Use (detail)

- What a tool is: a function the model is allowed to ask you to run for it.
- Why tools matter: the model cannot do maths reliably, see today's data, or take actions on its own. Tools fix that.
- The tool schema in plain terms: a name, a description, and the inputs it needs.
- The tool-use loop step by step: the model asks for a tool, your code runs it, you hand back the result, the model continues.
- Good tool descriptions, because the model chooses tools by reading them.
- When tools go wrong: bad inputs, errors, and how to hand a failure back gracefully.
- More than one tool: helping the model choose.
- A first look at the Model Context Protocol (MCP): a shared standard so tools built once can be reused anywhere.

## Part C. Planning (detail)

- Why plan: hard tasks need to be broken into steps.
- Chain of Thought: ask the model to think step by step before answering.
- ReAct: the model alternates between a thought and an action, so it reasons and uses tools together.
- Plan and Execute: write the whole plan first, then carry it out step by step.
- Reflection: the model reviews its own work and tries again if it is not good enough.
- Replanning: what to do when the world does not match the plan.
- Choosing a pattern: a short decision guide for beginners.

## Part D. Putting it together (detail)

- Useful agent shapes in plain language: routing (send the task to the right helper),
  orchestrator and workers (a manager that delegates), evaluator and optimizer (make, then judge, then improve).
- Watching the agent: logging and tracing so you can see what it did.
- Is it working: simple ways to evaluate quality.
- The practical trio: cost, speed, and safety, and how to keep them in check.
- When not to use an agent.

## Hands-on track (notebooks)

All notebooks run in Google Colab. Each one is narrated and ends with a small guided edit.
Each ships in two versions: a complete working version, and a fill-in-the-blank version.

- Notebook 0: Setup and first call. Open Colab, enter your API key with getpass, send a message, read the reply.
- Notebook 1: Your first tool-use loop. Give the model a single simple tool (for example a calculator), watch it ask for the tool, run it, and return the answer.
- Notebook 2: A planning pattern from scratch. Build a small ReAct loop and print the model's thoughts and actions so the reasoning is visible.
- Notebook 3: A multi-tool agent. Give the agent two or three tools and watch it pick the right one for each request.
- Notebook 4: Reflection and replanning. The agent checks its own answer and tries again when it falls short.
- Notebook 5: Capstone scaffold. A development-sector scenario, mostly built, with clearly marked spots for the learner to complete.

## Assessment and assignments

- A0: Concept check. Short multiple-choice and one-line-answer questions across Parts A to D.
- A1: Extend Notebook 1. Add a new tool of your own and get the agent to use it.
- A2: Improve Notebook 3. Add a second tool or better error handling and explain what changed.
- Capstone: Build a small agent for a scenario you choose from a provided list, then write a short note on how it plans and which tools it uses. Graded with a rubric.

## Suggested capstone scenarios (development-sector flavored)

- A field data lookup helper that answers questions from a small provided dataset.
- A multilingual FAQ assistant for a community program.
- A report-drafting helper that pulls figures from a small table and writes a short summary.
- A simple indicator calculator that turns raw numbers into program metrics.

## Glossary (to be expanded as terms appear)

agent, tool, function calling, schema, parameters, tool-use loop, Chain of Thought, ReAct,
Plan and Execute, reflection, replanning, Model Context Protocol (MCP), orchestrator,
evaluation, token, context window, hallucination, guardrail.

## Trim guidance for shorter formats

Half day (about 3 to 4 hours):
- Keep: Welcome and hook, Part A, Part B, Notebook 0, Notebook 1, a short version of Part C
  (Chain of Thought and ReAct only), and assignment A0.
- Cut: Part D depth, Notebooks 3 and 4, and the capstone (offer it as optional take-home).

Multi-session or self-paced:
- Session 1: Parts A and B with Notebooks 0 and 1.
- Session 2: Part C with Notebook 2.
- Session 3: Part D with Notebooks 3 and 4, then the capstone.
- Add short readings from the resource library between sessions.
