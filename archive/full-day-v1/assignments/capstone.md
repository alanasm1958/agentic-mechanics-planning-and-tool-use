# Capstone: Build a Small Agent

**Goal:** build a small agent end to end that plans, uses more than one tool, and
gives a clear answer. This brings together everything from the day.

**Start from:** `notebooks/05_capstone_student.ipynb` in Google Colab.

## Pick a scenario

Choose one (or design your own with your trainer):

1. **Field data helper** (provided in the notebook): answers questions from a
   small program dataset, using a lookup tool and a calculator.
2. **Multilingual FAQ assistant**: answers a few common questions and can greet
   or reply in more than one language.
3. **Report helper**: pulls a few numbers from a small table and writes a short
   plain-language summary.
4. **Indicator calculator**: turns raw numbers (for example households and
   clinics) into simple program metrics.

## Requirements

Your agent must:

- Run from top to bottom without errors.
- Use **at least two tools**, and use them for the right requests.
- Use the **agent loop** so it can plan across more than one step.
- Handle at least one **error or missing value** without crashing.
- Come with a short written note (about half a page) that explains:
  - what your agent does,
  - which tools it uses and why,
  - one example of how it planned across steps.

## What to submit

- Your completed notebook.
- Your written note (in the notebook or a separate document).

## How it is graded

A detailed rubric is in `solutions/capstone_rubric.md`. The headline criteria are:
it runs, it uses tools sensibly, it plans across steps, it handles an error, and
you can explain how it works. Ambition is welcome but a clear, working, simple
agent scores full marks.
