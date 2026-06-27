# A0: Answer Key

Accept answers in the learner's own words. The points below are what to look for.

## Part A

1. A chatbot answers or talks back, while an agent takes action to get the task
   done (it plans and uses tools), not just replies.
2. Goal, plan, act, observe (then repeat). Accept "plan, act, observe" with the
   goal as the starting input.
3. **b) hands.** Tools are how the agent acts in the world.
4. **False.** An agent is not conscious. It is a loop run carefully, with a model
   choosing the next step.

## Part B

5. **Your code** runs the tool. The model only asks for it.
6. A **name**, a **description**, and the **inputs** it needs (its schema).
7. **a) name and description.** The model never sees the hidden code.
8. A clear error tells the model what went wrong so it can fix its request and
   try again, instead of the whole program stopping.

## Part C

9. **b) ReAct.**
10. **Chain of Thought.**
11. The agent reviews its own answer and improves it if it is not good enough
    (make, judge, improve).
12. Replanning is making a new plan when the world does not match the old one,
    for example when a tool fails or new information appears.

## Part D

13. Any task that a single prompt or a fixed script already handles, for example
    a simple one-off question with no steps that change. Accept reasonable
    examples.
14. A right answer can come from luck or from bad steps. Checking the path shows
    whether the agent reasoned and chose tools sensibly, which matters for trust
    and for catching problems early.
15. **Cost, speed, and safety.**
