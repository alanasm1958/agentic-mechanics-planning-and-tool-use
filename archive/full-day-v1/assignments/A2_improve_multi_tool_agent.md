# A2: Improve the Multi-Tool Agent

**Goal:** make the multi-tool agent better by adding a tool and handling a mistake
gracefully.

**Start from:** `notebooks/03_multi_tool_agent_student.ipynb` in Google Colab.

## What to do

1. Finish the student notebook so all three tools work.
2. Add a **fourth tool** of your own. One idea: a tool that reverses a piece of
   text. Another: a tool that returns today's date as a fixed string for the
   workshop. Define it, add it to the `tools` list, and add a branch in
   `run_tool`.
3. Make the agent **handle a bad input gracefully**. For example, make the fact
   lookup return a clear error when the fact is unknown (it already does this),
   then ask for a fact that does not exist and watch how the agent responds.
4. Ask three different questions so that the agent uses three different tools, and
   read the Thought, Action, Observation lines to confirm its choices.

## What to submit

- Your finished notebook (or the cells you changed).
- A short note (3 to 4 sentences) explaining what you added and how the agent
  chose between tools.

## Hints

- The hardest part is wiring the new tool into both the `tools` list and the
  `run_tool` dispatcher. Miss one and the agent cannot use it.
- A sample solution is in `solutions/A2_sample_solution.md`.

## How it is graded

See `solutions/` for the rubric. In short: a new working tool, sensible tool
selection across questions, and a clear explanation.
