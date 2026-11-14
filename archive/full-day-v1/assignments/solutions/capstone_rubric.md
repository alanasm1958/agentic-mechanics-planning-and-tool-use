# Capstone: Grading Rubric

Score each criterion 0, 1, or 2. Total out of 12. This is a beginner course, so a
clear, simple, working agent should reach full marks. Reward understanding and a
working result over polish.

| # | Criterion | 0 points | 1 point | 2 points |
|---|-----------|----------|---------|----------|
| 1 | **Runs** | Does not run, or errors before any answer | Runs with small fixes needed | Runs top to bottom with no errors |
| 2 | **Uses two or more tools** | One tool or none | Two tools, but one is barely used | Two or more tools, each used for the right request |
| 3 | **Plans across steps** | Single step only | Plans, but the loop is shaky | Clearly plans across more than one step using the loop |
| 4 | **Handles an error or missing value** | Crashes on a bad input | Recovers, but awkwardly | Reads the error and recovers or replans cleanly |
| 5 | **Written note** | Missing or unclear | Explains some of it | Clearly explains what it does, which tools, and one planning example |
| 6 | **Clarity** | Hard to follow | Mostly readable | Readable, sensible names, helpful comments |

## Suggested bands

- **11 to 12:** Excellent. A clear, working, well-explained agent.
- **8 to 10:** Good. Works and is understood, with small gaps.
- **5 to 7:** Developing. Runs in part, or the explanation is thin.
- **Below 5:** Needs another attempt. Offer specific, kind feedback and a retry.

## Notes for graders

- Ambition is welcome but never required. A simple field-data helper that meets
  every criterion deserves full marks.
- If a learner is stuck on wiring a tool, that is the most common issue. Point
  them to the `run_tool` dispatcher and the `tools` list.
- Encourage learners to read the Thought, Action, Observation lines aloud. Being
  able to narrate the loop is a strong sign of understanding.
