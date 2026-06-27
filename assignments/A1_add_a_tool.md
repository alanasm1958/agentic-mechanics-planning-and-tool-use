# A1: Add a Tool

**Goal:** give an agent a brand new tool of your own and get it to use the tool.

**Start from:** `notebooks/01_first_tool_use_loop_student.ipynb` in Google Colab.

## What to do

1. Finish the student notebook so the calculator loop runs (if you have not yet).
2. Add a **new tool** of your own. A simple one to start with is a tool that
   counts the number of characters in a piece of text. You will need to:
   - Write a tool definition (a name, a plain description, and one input).
   - Write the Python function that does the work.
   - Add your tool to the `tools` list.
   - Make sure the loop runs your tool when the model asks for it.
3. Ask the agent a question that needs your new tool, for example: "How many
   characters are in the word 'development'? Use the tool."

## What to submit

- Your finished notebook (or the cells you added).
- One or two sentences saying what your tool does and how you knew the agent used it.

## Hints

- Copy the shape of the calculator tool and change the name, description, and input.
- The description is how the model decides to use your tool, so make it clear.
- A sample solution is in `solutions/A1_sample_solution.md`. Try it yourself first.

## How it is graded

See `solutions/` for the rubric. In short: the tool is defined correctly, the
agent actually calls it, and you can explain what happened.
