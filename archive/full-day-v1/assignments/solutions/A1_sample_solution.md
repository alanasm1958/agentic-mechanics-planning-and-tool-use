# A1: Sample Solution

One good answer. Other tools are equally valid. The learner adds a tool that
counts characters in a piece of text.

## The new tool definition

```python
text_length_tool = {
    "name": "text_length",
    "description": "Count how many characters are in a piece of text. Use this when the user asks how long a word or phrase is.",
    "input_schema": {
        "type": "object",
        "properties": {
            "text": {"type": "string", "description": "The text to measure."}
        },
        "required": ["text"],
    },
}


def run_text_length(text):
    return str(len(text))
```

## Wiring it in

Add the tool to the list, and run it when the model asks:

```python
tools = [calculator_tool, text_length_tool]
```

In the loop, dispatch by tool name:

```python
for block in response.content:
    if block.type == "tool_use":
        if block.name == "calculator":
            result = run_calculator(block.input["expression"])
        elif block.name == "text_length":
            result = run_text_length(block.input["text"])
        tool_results.append({
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": result,
        })
```

## A question that uses it

```python
messages = [{"role": "user", "content": "How many characters are in the word 'development'? Use the tool."}]
```

## What to look for when grading

- The tool definition has a clear name, description, and one input.
- The tool is added to `tools` and run when requested.
- The agent actually calls the tool (the learner can point to the tool_use block).
