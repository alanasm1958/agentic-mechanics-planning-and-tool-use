# A2: Sample Solution

One good answer. The learner adds a fourth tool that reverses text, and confirms
the agent picks the right tool for each question.

## The new tool

```python
reverse_tool = {
    "name": "reverse_text",
    "description": "Return a piece of text reversed, back to front. Use this when the user asks to reverse or flip text.",
    "input_schema": {
        "type": "object",
        "properties": {
            "text": {"type": "string", "description": "The text to reverse."}
        },
        "required": ["text"],
    },
}


def run_reverse(text):
    return text[::-1]
```

## Wiring it in

```python
tools = [calculator_tool, lookup_tool, greeting_tool, reverse_tool]

def run_tool(name, tool_input):
    if name == "calculator":
        return run_calculator(tool_input["expression"])
    if name == "lookup_fact":
        return run_lookup(tool_input["name"])
    if name == "greet_in_language":
        return run_greeting(tool_input["language"])
    if name == "reverse_text":
        return run_reverse(tool_input["text"])
    return "Error: unknown tool."
```

## Showing tool selection and a graceful error

```python
print(run_agent("Reverse the word 'kanju'."))            # uses reverse_text
print(run_agent("How do I say hello in Arabic?"))        # uses greet_in_language
print(run_agent("What is the population of Atlantis?"))  # lookup returns an error, agent recovers
```

## What to look for when grading

- A new tool that is defined and wired into both the list and the dispatcher.
- Three questions that each use a different tool, shown by the Action lines.
- A clear explanation of how the agent chose, and how it handled the unknown fact.
