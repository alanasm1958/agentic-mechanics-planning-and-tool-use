"""Build the Jupyter notebooks for the module from a single source of truth.

Run:  python build_notebooks.py
Output: the .ipynb files in this folder.

Why a builder: it keeps the instructor and student versions in sync, guarantees
valid notebook JSON, and lets us reuse the shared setup cells across notebooks.

Audience: beginners and non-coders. Code is short, heavily commented, and the
notebooks run in Google Colab. Each learner uses their own Anthropic API key,
entered at runtime with getpass. Model: claude-opus-4-8 (swappable).
No em dashes anywhere.
"""

import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


def md(text):
    return new_markdown_cell(text.strip("\n"))


def code(src):
    return new_code_cell(src.strip("\n"))


def write_notebook(cells, filename, title):
    nb = new_notebook()
    nb["cells"] = cells
    nb["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
        "colab": {"name": title, "provenance": []},
    }
    with open(filename, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print("wrote", filename)


# ---------------------------------------------------------------------------
# Shared setup cells. Every notebook is self contained, so it repeats setup.
# ---------------------------------------------------------------------------

def setup_cells():
    return [
        md(
            """
## Setup: run these first

Every notebook starts the same way: install the library, load your key, and
pick a model. Run the next three cells in order.

**Save yourself time:** store your API key once in Colab Secrets (the key icon on
the left sidebar). Add a secret named `ANTHROPIC_API_KEY`, paste your key as the
value, and turn on "Notebook access". After that, every notebook picks it up
automatically and you never paste it again.
"""
        ),
        code(
            """
# 1) Install the Anthropic library (Colab forgets it between sessions, so we
#    install each time). The -q just keeps the output quiet.
!pip install -q anthropic
"""
        ),
        code(
            """
# 2) Load your Anthropic API key.
#    Easiest: store it once in Colab Secrets (key icon on the left), named
#    ANTHROPIC_API_KEY, with "Notebook access" on. Then this reads it for you.
import anthropic

api_key = None
try:
    from google.colab import userdata
    api_key = userdata.get("ANTHROPIC_API_KEY")
except Exception:
    api_key = None  # not on Colab, or no secret set yet

if not api_key:
    # Fallback: ask once if no secret is found. The input is hidden and not saved.
    from getpass import getpass
    api_key = getpass("Paste your Anthropic API key (input is hidden): ")

client = anthropic.Anthropic(api_key=api_key)
print("Your client is ready.")
"""
        ),
        code(
            """
# 3) Choose the model. claude-opus-4-8 is the most capable. For faster, cheaper
#    runs while practising you can switch this to "claude-haiku-4-5".
MODEL = "claude-opus-4-8"
print("Using model:", MODEL)
"""
        ),
    ]


# ---------------------------------------------------------------------------
# Shared building blocks the notebooks reuse.
# ---------------------------------------------------------------------------

CALCULATOR_TOOL = '''
import ast
import operator

# A tool is described by a name, a plain description, and the inputs it needs.
# The model reads the description to decide when to use the tool.
calculator_tool = {
    "name": "calculator",
    "description": "Evaluate a basic arithmetic expression and return the result. Use this whenever the user asks for a calculation.",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "An arithmetic expression, for example '12 * 37'.",
            }
        },
        "required": ["expression"],
    },
}

# The safe operations our calculator allows: plus, minus, times, divide, and
# negative numbers. Nothing else is permitted.
_SAFE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _safe_eval(node):
    # Walk the parsed expression and only allow numbers and the safe operations
    # above. Anything else (names, function calls) raises an error, so no
    # arbitrary code can run. This is the safe alternative to eval().
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _SAFE_OPS:
        return _SAFE_OPS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _SAFE_OPS:
        return _SAFE_OPS[type(node.op)](_safe_eval(node.operand))
    raise ValueError("unsupported expression")


def run_calculator(expression):
    # Beginners can treat this as a black box: give it an expression, get the
    # result. It parses the text and evaluates only safe arithmetic, so it
    # cannot run arbitrary code.
    try:
        tree = ast.parse(expression, mode="eval")
        return str(_safe_eval(tree))
    except Exception:
        return "Error: I could only handle a simple arithmetic expression like '12 * 37'."
'''


# ---------------------------------------------------------------------------
# Notebook 0: Setup and your first message
# ---------------------------------------------------------------------------

def notebook_0():
    cells = [
        md(
            """
# Notebook 0: Setup and your first message

Welcome. By the end of this short notebook you will have sent your first message
to an AI model and read its reply. No prior coding needed. Just read each cell,
then press the run button (the small triangle) on the left of the cell.

**You will need:** an Anthropic API key. Your trainer will tell you where to get
one. Your key is private, like a password, so do not share it.
"""
        ),
    ]
    cells += setup_cells()
    cells += [
        md(
            """
## Send your first message

The model does not remember anything between calls, so each time we send the
whole conversation as a list of messages. A message has a role ("user" is you)
and some content. The reply comes back as a list of blocks. We print the text.
"""
        ),
        code(
            """
response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "In one friendly sentence, introduce yourself to a beginner."}
    ],
)

# The reply is a list of content blocks. We print the text blocks.
for block in response.content:
    if block.type == "text":
        print(block.text)
"""
        ),
        md(
            """
## What just happened

- We sent a list of **messages**. The first one had role **user** (that is you).
- The model replied. Its reply is a list of **content blocks**.
- We looped over the blocks and printed the ones whose type is **text**.

That is the whole idea of talking to the model. Everything else this course
builds on top of this.
"""
        ),
        md(
            """
## Your turn

Change the message below to anything you like, then run the cell. Try asking it
to explain something simple in one sentence.
"""
        ),
        code(
            """
my_question = "Explain what a tool is, in one simple sentence for a beginner."

response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    messages=[{"role": "user", "content": my_question}],
)
for block in response.content:
    if block.type == "text":
        print(block.text)
"""
        ),
        md(
            """
Nicely done. Next we give the model a **tool** so it can do things, not just talk.
"""
        ),
    ]
    write_notebook(cells, "00_setup_and_first_message.ipynb", "Notebook 0: Setup and first message")


# ---------------------------------------------------------------------------
# Notebook 1: Your first tool-use loop
# ---------------------------------------------------------------------------

def notebook_1(student):
    cells = [
        md(
            """
# Notebook 1: Your first tool-use loop

A model is good with words but cannot do exact arithmetic on its own. So we give
it a **calculator tool**. You will watch the model **ask** to use the calculator,
your code **run** it, you **return** the answer, and the model **continue**.

That four step rhythm (ask, run, return, continue) is the heart of tool use.
"""
        ),
    ]
    cells += setup_cells()
    cells += [
        md(
            """
## Step 1: define the tool

A tool has a name, a plain description, and the inputs it needs. The model reads
the description to decide when to use it. We also write the actual Python that
does the work.
"""
        ),
        code(CALCULATOR_TOOL),
        md(
            """
## Step 2: ask a question that needs the tool

We send the question along with the list of tools. If the model wants the
calculator, the reply will have `stop_reason` equal to `"tool_use"`.
"""
        ),
        code(
            """
tools = [calculator_tool]

messages = [
    {"role": "user", "content": "What is 12 times 37? Use the calculator."}
]

response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    tools=tools,
    messages=messages,
)

print("Stop reason:", response.stop_reason)
for block in response.content:
    if block.type == "tool_use":
        print("The model wants to run:", block.name, "with", block.input)
    elif block.type == "text":
        print("The model said:", block.text)
"""
        ),
        md(
            """
## Step 3: run the tool and hand the result back

This is the important cell. We do four things:
1. Add the model's turn (which holds the tool request) to the conversation.
2. Run the requested tool in our own code.
3. Send the result back as a new turn.
4. Ask the model to continue, now that it has the answer.
"""
        ),
    ]
    if student:
        cells += [
            code(
                """
# YOUR TURN. Fill in the four steps. The instructor notebook has the full answer.

# 1) Add the model's turn (it holds the tool request) to the conversation.
messages.append({"role": "assistant", "content": response.content})

# 2) Find each tool request, run it, and collect the results.
tool_results = []
for block in response.content:
    if block.type == "tool_use":
        # TODO: call run_calculator with block.input["expression"] and save it as `result`.
        result = None  # replace this line
        tool_results.append({
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": result,
        })

# 3) Hand the results back to the model as a new user turn.
messages.append({"role": "user", "content": tool_results})

# 4) Ask the model to continue now that it has the result.
followup = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    tools=tools,
    messages=messages,
)
for block in followup.content:
    if block.type == "text":
        print("Model's final answer:", block.text)
"""
            )
        ]
    else:
        cells += [
            code(
                """
# 1) Add the model's turn (it holds the tool request) to the conversation.
messages.append({"role": "assistant", "content": response.content})

# 2) Find each tool request, run it, and collect the results.
tool_results = []
for block in response.content:
    if block.type == "tool_use":
        print("The model asked to run", block.name, "with", block.input)
        result = run_calculator(block.input["expression"])
        print("Our code computed:", result)
        tool_results.append({
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": result,
        })

# 3) Hand the results back to the model as a new user turn.
messages.append({"role": "user", "content": tool_results})

# 4) Ask the model to continue now that it has the result.
followup = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    tools=tools,
    messages=messages,
)
for block in followup.content:
    if block.type == "text":
        print("\\nModel's final answer:", block.text)
"""
            )
        ]
    cells += [
        md(
            """
## Recap

You just ran a full tool-use loop:

1. **Ask**: the model requested the calculator.
2. **Run**: your code did the math.
3. **Return**: you sent the result back.
4. **Continue**: the model finished the answer.

## Your turn

Change the question in Step 2 to a different calculation and run the cells again.
Then try a harder one that needs two calculations and see what happens.
"""
        ),
    ]
    suffix = "student" if student else "instructor"
    write_notebook(cells, f"01_first_tool_use_loop_{suffix}.ipynb", f"Notebook 1: First tool-use loop ({suffix})")


# ---------------------------------------------------------------------------
# Notebook 2: A planning pattern (ReAct) from scratch
# ---------------------------------------------------------------------------

REACT_TOOLS = '''
# Two small tools. One looks up an approximate fact, one does arithmetic.
facts = {
    "geneva population": "200000 (approximate, for the workshop)",
    "zurich population": "430000 (approximate, for the workshop)",
    "bern population": "135000 (approximate, for the workshop)",
}

lookup_tool = {
    "name": "lookup_fact",
    "description": "Look up an approximate fact by name, for example 'geneva population'. Use this when you need a number you do not know.",
    "input_schema": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "The fact to look up, lowercase."}
        },
        "required": ["name"],
    },
}


def run_lookup(name):
    return facts.get(name.lower().strip(), "Error: I do not have that fact. Try another name.")
'''

REACT_DISPATCH = '''
tools = [lookup_tool, calculator_tool]

# A small helper that runs whichever tool the model asked for.
def run_tool(name, tool_input):
    if name == "lookup_fact":
        return run_lookup(tool_input["name"])
    if name == "calculator":
        return run_calculator(tool_input["expression"])
    return "Error: unknown tool."

SYSTEM = (
    "You are a careful assistant. Think step by step. "
    "When you need a fact or a calculation, use the tools provided, one step at a time. "
    "After you have everything you need, give a short final answer."
)
'''


def notebook_2(student):
    cells = [
        md(
            """
# Notebook 2: A planning pattern you can watch think (ReAct)

ReAct means the model alternates a **thought** and an **action**, looking at the
result (an **observation**) before the next thought. It is the most important
pattern for tool-using agents.

In this notebook we build a small ReAct loop from scratch and print every
Thought, Action, and Observation, so you can literally watch the agent reason.
"""
        ),
    ]
    cells += setup_cells()
    cells += [
        md("## Step 1: the tools\n\nWe give the agent a fact lookup tool and the calculator from before."),
        code(CALCULATOR_TOOL),
        code(REACT_TOOLS),
        code(REACT_DISPATCH),
        md(
            """
## Step 2: the ReAct loop

The loop keeps going while the model asks for tools. Each pass it prints the
model's Thought, runs the Action, and prints the Observation. When the model
stops asking for tools, it has a final answer.
"""
        ),
    ]
    if student:
        cells += [
            code(
                """
# YOUR TURN. Complete the two marked lines. The instructor notebook has the answer.

def run_agent(question, max_steps=5):
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            system=SYSTEM,
            tools=tools,
            messages=messages,
        )

        # Print the model's reasoning (its text) as a Thought.
        for block in response.content:
            if block.type == "text" and block.text.strip():
                print("Thought:", block.text.strip())

        # If the model is not asking for a tool, it is done.
        if response.stop_reason != "tool_use":
            for block in response.content:
                if block.type == "text":
                    return block.text
            return ""

        # Otherwise, run each requested tool and record the observations.
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print("Action:", block.name, block.input)
                # TODO: run the tool with run_tool(block.name, block.input) and save as `observation`.
                observation = None  # replace this line
                print("Observation:", observation)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": observation,
                })
        # TODO: add the tool_results back to messages as a user turn (see Notebook 1).
        pass  # replace this line

    return "Stopped after the maximum number of steps."
"""
            )
        ]
    else:
        cells += [
            code(
                """
def run_agent(question, max_steps=5):
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            system=SYSTEM,
            tools=tools,
            messages=messages,
        )

        # Print the model's reasoning (its text) as a Thought.
        for block in response.content:
            if block.type == "text" and block.text.strip():
                print("Thought:", block.text.strip())

        # If the model is not asking for a tool, it is done.
        if response.stop_reason != "tool_use":
            for block in response.content:
                if block.type == "text":
                    return block.text
            return ""

        # Otherwise, run each requested tool and record the observations.
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print("Action:", block.name, block.input)
                observation = run_tool(block.name, block.input)
                print("Observation:", observation)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": observation,
                })
        messages.append({"role": "user", "content": tool_results})

    return "Stopped after the maximum number of steps."
"""
            )
        ]
    cells += [
        md("## Step 3: run it\n\nThis question needs two lookups and one calculation, so watch the loop work."),
        code(
            """
answer = run_agent("What is the combined population of Geneva and Zurich? Use the tools.")
print("\\nFinal answer:", answer)
"""
        ),
        md(
            """
## Recap

You watched the agent **think**, **act** (use a tool), and **observe**, over and
over, until it had everything it needed. That loop is ReAct.

## Your turn

Ask a question that needs the population of Bern as well, and see how the agent
plans across three lookups.
"""
        ),
    ]
    suffix = "student" if student else "instructor"
    write_notebook(cells, f"02_react_from_scratch_{suffix}.ipynb", f"Notebook 2: ReAct from scratch ({suffix})")


# ---------------------------------------------------------------------------
# Notebook 3: A multi-tool agent
# ---------------------------------------------------------------------------

GREETING_TOOL = '''
# A third tool with a clearly different job: return a greeting in a language.
greetings = {
    "french": "Bonjour",
    "spanish": "Hola",
    "arabic": "Marhaba",
    "swahili": "Jambo",
}

greeting_tool = {
    "name": "greet_in_language",
    "description": "Return a greeting word in a given language. Use this when the user asks how to greet someone in another language.",
    "input_schema": {
        "type": "object",
        "properties": {
            "language": {"type": "string", "description": "The language, lowercase, for example 'french'."}
        },
        "required": ["language"],
    },
}


def run_greeting(language):
    return greetings.get(language.lower().strip(), "Error: I do not know that language yet.")
'''


def notebook_3(student):
    cells = [
        md(
            """
# Notebook 3: A multi-tool agent

Now the agent has **three** tools: a calculator, a fact lookup, and a greeting
tool. The model chooses the right one for each request by reading the tool
descriptions. We reuse the ReAct loop from Notebook 2.
"""
        ),
    ]
    cells += setup_cells()
    cells += [
        md("## Step 1: three tools"),
        code(CALCULATOR_TOOL),
        code(REACT_TOOLS),
        code(GREETING_TOOL),
    ]
    if student:
        cells += [
            md(
                """
## Step 2: register the tools

Complete the tools list and the dispatcher so the agent can reach all three
tools. The instructor notebook has the answer.
"""
            ),
            code(
                """
# TODO: include all three tools in this list.
tools = [calculator_tool, lookup_tool]  # add greeting_tool

def run_tool(name, tool_input):
    if name == "calculator":
        return run_calculator(tool_input["expression"])
    if name == "lookup_fact":
        return run_lookup(tool_input["name"])
    # TODO: add a branch for "greet_in_language" that calls run_greeting.
    return "Error: unknown tool."

SYSTEM = (
    "You are a helpful assistant. Use the tools when they fit the request, "
    "one step at a time, then give a short final answer."
)
"""
            ),
        ]
    else:
        cells += [
            md("## Step 2: register the tools\n\nAll three tools go in one list, and the dispatcher routes to each."),
            code(
                """
tools = [calculator_tool, lookup_tool, greeting_tool]

def run_tool(name, tool_input):
    if name == "calculator":
        return run_calculator(tool_input["expression"])
    if name == "lookup_fact":
        return run_lookup(tool_input["name"])
    if name == "greet_in_language":
        return run_greeting(tool_input["language"])
    return "Error: unknown tool."

SYSTEM = (
    "You are a helpful assistant. Use the tools when they fit the request, "
    "one step at a time, then give a short final answer."
)
"""
            ),
        ]
    cells += [
        md("## Step 3: the agent loop\n\nThis is the same loop you built in Notebook 2, ready to reuse."),
        code(
            """
def run_agent(question, max_steps=5):
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        response = client.messages.create(
            model=MODEL, max_tokens=1024, system=SYSTEM, tools=tools, messages=messages,
        )
        for block in response.content:
            if block.type == "text" and block.text.strip():
                print("Thought:", block.text.strip())
        if response.stop_reason != "tool_use":
            for block in response.content:
                if block.type == "text":
                    return block.text
            return ""
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print("Action:", block.name, block.input)
                observation = run_tool(block.name, block.input)
                print("Observation:", observation)
                tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": observation})
        messages.append({"role": "user", "content": tool_results})
    return "Stopped after the maximum number of steps."
"""
        ),
        md("## Step 4: watch it choose\n\nEach question below should make the agent reach for a different tool."),
        code(
            """
print("=== Calculation ===")
print(run_agent("What is 45 plus 67? Use the calculator."))
print("\\n=== Lookup ===")
print(run_agent("What is the approximate population of Bern?"))
print("\\n=== Greeting ===")
print(run_agent("How do I say hello in Swahili?"))
"""
        ),
        md(
            """
## Your turn

Add a brand new tool of your own (for example a tool that reverses a piece of
text) and a question that uses it. You will need to: define the tool, add it to
the `tools` list, and add a branch in `run_tool`. This is also assignment A2.
"""
        ),
    ]
    suffix = "student" if student else "instructor"
    write_notebook(cells, f"03_multi_tool_agent_{suffix}.ipynb", f"Notebook 3: Multi-tool agent ({suffix})")


# ---------------------------------------------------------------------------
# Notebook 4: Reflection and replanning
# ---------------------------------------------------------------------------

WEATHER_TOOL = '''
# A weather tool that fails on its own when the city is ambiguous, so we can see
# the agent read the error and try again with a better input.
weather_data = {
    "geneva, switzerland": "18 degrees C and cloudy",
    "nairobi, kenya": "26 degrees C and sunny",
}

weather_tool = {
    "name": "get_weather",
    "description": "Get the weather for a city. Include the country, for example 'Geneva, Switzerland'.",
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "City and country, for example 'Nairobi, Kenya'."}
        },
        "required": ["city"],
    },
}


def run_weather(city):
    key = city.lower().strip()
    if "," not in key:
        # The error message tells the model how to fix its request.
        return "Error: many cities share that name. Please include the country, like 'Geneva, Switzerland'."
    return weather_data.get(key, "Error: no data for that city. Try Geneva, Switzerland or Nairobi, Kenya.")
'''


def notebook_4(student):
    cells = [
        md(
            """
# Notebook 4: Reflection and replanning

Two ideas that make agents more reliable:

- **Reflection**: the model reviews its own answer and improves it.
- **Replanning**: when a tool fails, the agent reads the error and tries again.

We will see both.
"""
        ),
    ]
    cells += setup_cells()
    cells += [
        md(
            """
## Part A: reflection (make, judge, improve)

First we ask for a quick draft. Then we ask the model to critique its own draft
and write a better version. This is the make, judge, improve loop in two steps.
"""
        ),
    ]
    if student:
        cells += [
            code(
                """
def ask(prompt):
    response = client.messages.create(
        model=MODEL, max_tokens=1024, messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in response.content if b.type == "text")

draft = ask("Write a 2 sentence summary of why planning helps an AI agent.")
print("DRAFT:\\n", draft)

# TODO: write a prompt that asks the model to critique the draft above and then
# produce an improved version. Use an f-string that includes `draft`.
critique_prompt = ""  # replace this line
improved = ask(critique_prompt)
print("\\nIMPROVED:\\n", improved)
"""
            )
        ]
    else:
        cells += [
            code(
                """
def ask(prompt):
    response = client.messages.create(
        model=MODEL, max_tokens=1024, messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in response.content if b.type == "text")

draft = ask("Write a 2 sentence summary of why planning helps an AI agent.")
print("DRAFT:\\n", draft)

critique_prompt = (
    "Here is a draft:\\n"
    + draft
    + "\\nName one concrete way to improve it, then write the improved 2 sentence version."
)
improved = ask(critique_prompt)
print("\\nIMPROVED:\\n", improved)
"""
            )
        ]
    cells += [
        md(
            """
## Part B: replanning when a tool fails

The weather tool below returns an error if the city has no country. Watch the
agent read that error and retry with a corrected request. We reuse the agent
loop, and we surface tool errors with `is_error` so the model knows it failed.
"""
        ),
        code(WEATHER_TOOL),
        code(
            """
tools = [weather_tool]

def run_agent(question, max_steps=5):
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        response = client.messages.create(
            model=MODEL, max_tokens=1024, tools=tools, messages=messages,
        )
        for block in response.content:
            if block.type == "text" and block.text.strip():
                print("Thought:", block.text.strip())
        if response.stop_reason != "tool_use":
            for block in response.content:
                if block.type == "text":
                    return block.text
            return ""
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print("Action:", block.name, block.input)
                observation = run_weather(block.input["city"])
                print("Observation:", observation)
                is_error = observation.startswith("Error")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": observation,
                    "is_error": is_error,
                })
        messages.append({"role": "user", "content": tool_results})
    return "Stopped after the maximum number of steps."
"""
        ),
        code(
            """
# Ask in a way that first triggers the error (no country), so we can watch the
# agent notice the problem and replan with a corrected city.
print(run_agent("What is the weather in Geneva?"))
"""
        ),
        md(
            """
## Recap

- Reflection turned a rough draft into a better answer.
- Replanning let the agent recover from a failed tool call instead of giving up.

## Your turn

Add a second city and country to `weather_data`, then ask about it. Try asking
about a city that is not in the data and see how the agent responds to the error.
"""
        ),
    ]
    suffix = "student" if student else "instructor"
    write_notebook(cells, f"04_reflection_and_replanning_{suffix}.ipynb", f"Notebook 4: Reflection and replanning ({suffix})")


# ---------------------------------------------------------------------------
# Notebook 5: Capstone scaffold
# ---------------------------------------------------------------------------

CAPSTONE_DATA = '''
# A tiny, made-up dataset for the workshop: a few program indicators by region.
# In a real project this might come from a spreadsheet or a database.
program_data = {
    "north": {"households_reached": 1200, "clinics": 4, "literacy_rate": 0.71},
    "south": {"households_reached": 900, "clinics": 3, "literacy_rate": 0.63},
    "east": {"households_reached": 1500, "clinics": 6, "literacy_rate": 0.78},
}

lookup_indicator_tool = {
    "name": "lookup_indicator",
    "description": "Look up one indicator for one region. Regions: north, south, east. Indicators: households_reached, clinics, literacy_rate.",
    "input_schema": {
        "type": "object",
        "properties": {
            "region": {"type": "string", "description": "north, south, or east"},
            "indicator": {"type": "string", "description": "households_reached, clinics, or literacy_rate"},
        },
        "required": ["region", "indicator"],
    },
}


def run_lookup_indicator(region, indicator):
    region = region.lower().strip()
    indicator = indicator.lower().strip()
    if region not in program_data:
        return "Error: unknown region. Use north, south, or east."
    if indicator not in program_data[region]:
        return "Error: unknown indicator. Use households_reached, clinics, or literacy_rate."
    return str(program_data[region][indicator])
'''


def notebook_5(student):
    cells = [
        md(
            """
# Notebook 5: Capstone

Now you build a small agent end to end. The scenario is a **field data helper**
that answers questions from a small program dataset. Most of it is built. Your
job is to finish the marked TODOs and then try your own questions.

Other scenario ideas you can adapt this to: a multilingual FAQ assistant, a
report-drafting helper, or a simple indicator calculator. Pick one that fits
your work.
"""
        ),
    ]
    cells += setup_cells()
    cells += [
        md("## The dataset and the first tool\n\nA lookup tool is provided and works."),
        code(CAPSTONE_DATA),
        md("## A calculator tool (so the agent can compute, for example averages)"),
        code(CALCULATOR_TOOL),
    ]
    if student:
        cells += [
            md(
                """
## Your tasks

1. Register both tools in the `tools` list and the `run_tool` dispatcher below.
2. Run the agent and ask it a question that needs a lookup and a calculation,
   for example: "What is the total number of clinics across all three regions?"
3. Stretch goal: add one more tool of your own (for example one that returns the
   region with the most households).

The instructor notebook shows one complete solution.
"""
            ),
            code(
                """
# TODO: include both tools.
tools = [lookup_indicator_tool]  # add calculator_tool

def run_tool(name, tool_input):
    if name == "lookup_indicator":
        return run_lookup_indicator(tool_input["region"], tool_input["indicator"])
    # TODO: add a branch for "calculator" that calls run_calculator.
    return "Error: unknown tool."

SYSTEM = (
    "You are a field data helper. Use the tools to look up indicators and to do "
    "any arithmetic, one step at a time, then give a short, clear answer."
)
"""
            ),
        ]
    else:
        cells += [
            md("## Register both tools"),
            code(
                """
tools = [lookup_indicator_tool, calculator_tool]

def run_tool(name, tool_input):
    if name == "lookup_indicator":
        return run_lookup_indicator(tool_input["region"], tool_input["indicator"])
    if name == "calculator":
        return run_calculator(tool_input["expression"])
    return "Error: unknown tool."

SYSTEM = (
    "You are a field data helper. Use the tools to look up indicators and to do "
    "any arithmetic, one step at a time, then give a short, clear answer."
)
"""
            ),
        ]
    cells += [
        md("## The agent loop\n\nThe same reusable loop from earlier notebooks."),
        code(
            """
def run_agent(question, max_steps=8):
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        response = client.messages.create(
            model=MODEL, max_tokens=1024, system=SYSTEM, tools=tools, messages=messages,
        )
        for block in response.content:
            if block.type == "text" and block.text.strip():
                print("Thought:", block.text.strip())
        if response.stop_reason != "tool_use":
            for block in response.content:
                if block.type == "text":
                    return block.text
            return ""
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print("Action:", block.name, block.input)
                observation = run_tool(block.name, block.input)
                print("Observation:", observation)
                tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": observation})
        messages.append({"role": "user", "content": tool_results})
    return "Stopped after the maximum number of steps."
"""
        ),
        md("## Try it"),
        code(
            """
question = "What is the total number of clinics across all three regions?"
print(run_agent(question))
"""
        ),
        md(
            """
## Wrap up

You built an agent that plans, looks up real data, computes, and answers. That
is the same loop behind much larger agents. Well done.

When you are ready, write a short note on which tools your agent uses and how it
plans. That note plus this notebook is your capstone submission.
"""
        ),
    ]
    suffix = "student" if student else "instructor"
    write_notebook(cells, f"05_capstone_{suffix}.ipynb", f"Notebook 5: Capstone ({suffix})")


def notebook_combined():
    """One notebook with every part in order: install once, key once, then Part 1 to 5."""
    cells = [
        md(
            """
# Agentic Mechanics: Planning and Tool Use

## All-in-one notebook

This single notebook runs the whole day in order: a first tool-use loop, a planning
pattern (ReAct), a multi-tool agent, reflection and replanning, and a capstone. You
install once and load your key once at the top, then work straight down the notebook.
"""
        ),
    ]
    cells += setup_cells()

    # Part 1: tool-use loop
    cells += [
        md("## Part 1: Your first tool-use loop\n\nGive the model a calculator and watch the loop: ask, run, return, continue."),
        code(CALCULATOR_TOOL),
        code(
            """
# A single tool-use loop, by hand.
tools = [calculator_tool]
messages = [{"role": "user", "content": "What is 12 times 37? Use the calculator."}]

response = client.messages.create(model=MODEL, max_tokens=1024, tools=tools, messages=messages)
messages.append({"role": "assistant", "content": response.content})

tool_results = []
for block in response.content:
    if block.type == "tool_use":
        print("The model asked to run", block.name, "with", block.input)
        result = run_calculator(block.input["expression"])
        print("Our code computed:", result)
        tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": result})

messages.append({"role": "user", "content": tool_results})
followup = client.messages.create(model=MODEL, max_tokens=1024, tools=tools, messages=messages)
for block in followup.content:
    if block.type == "text":
        print("Model's final answer:", block.text)
"""
        ),
    ]

    # Part 2: ReAct loop (defined once, reused below)
    cells += [
        md("## Part 2: A planning pattern (ReAct)\n\nThe agent thinks, acts, and observes, over and over. We build the loop once here and reuse it for the rest of the notebook."),
        code(REACT_TOOLS),
        code(REACT_DISPATCH),
        code(
            """
# The ReAct loop, defined once and reused for every part below.
# It reads the current tools, run_tool, and SYSTEM each time it is called.
def run_agent(question, max_steps=6):
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        response = client.messages.create(
            model=MODEL, max_tokens=1024, system=SYSTEM, tools=tools, messages=messages,
        )
        for block in response.content:
            if block.type == "text" and block.text.strip():
                print("Thought:", block.text.strip())
        if response.stop_reason != "tool_use":
            for block in response.content:
                if block.type == "text":
                    return block.text
            return ""
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print("Action:", block.name, block.input)
                observation = run_tool(block.name, block.input)
                print("Observation:", observation)
                tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": observation})
        messages.append({"role": "user", "content": tool_results})
    return "Stopped after the maximum number of steps."
"""
        ),
        code('print(run_agent("What is the combined population of Geneva and Zurich? Use the tools."))'),
    ]

    # Part 3: multi-tool
    cells += [
        md("## Part 3: A multi-tool agent\n\nAdd a third tool and watch the agent pick the right one. We reuse run_agent from Part 2."),
        code(GREETING_TOOL),
        code(
            """
tools = [calculator_tool, lookup_tool, greeting_tool]

def run_tool(name, tool_input):
    if name == "calculator":
        return run_calculator(tool_input["expression"])
    if name == "lookup_fact":
        return run_lookup(tool_input["name"])
    if name == "greet_in_language":
        return run_greeting(tool_input["language"])
    return "Error: unknown tool."

SYSTEM = "You are a helpful assistant. Use the tools when they fit the request, one step at a time, then give a short final answer."
"""
        ),
        code(
            """
print(run_agent("How do I say hello in Swahili?"))
print("\\n-----\\n")
print(run_agent("What is the approximate population of Bern?"))
print("\\n-----\\n")
print(run_agent("What is 45 plus 67? Use the calculator."))
"""
        ),
    ]

    # Part 4: reflection and replanning
    cells += [
        md("## Part 4: Reflection and replanning"),
        code(
            """
# Reflection: make a draft, then judge and improve it.
def ask(prompt):
    response = client.messages.create(model=MODEL, max_tokens=1024, messages=[{"role": "user", "content": prompt}])
    return "".join(b.text for b in response.content if b.type == "text")

draft = ask("Write a 2 sentence summary of why planning helps an AI agent.")
print("DRAFT:\\n", draft)

critique = ask("Here is a draft:\\n" + draft + "\\nName one concrete way to improve it, then write the improved 2 sentence version.")
print("\\nIMPROVED:\\n", critique)
"""
        ),
        code(WEATHER_TOOL),
        code(
            """
# Replanning: the weather tool returns an error if the city has no country.
# Watch the agent read the error and try again. We reuse run_agent.
tools = [weather_tool]

def run_tool(name, tool_input):
    if name == "get_weather":
        return run_weather(tool_input["city"])
    return "Error: unknown tool."

SYSTEM = "You are a helpful assistant. Use the weather tool. If it returns an error, read the message and try again with a better input."

print(run_agent("What is the weather in Geneva?"))
"""
        ),
    ]

    # Part 5: capstone
    cells += [
        md("## Part 5: Capstone, a field data helper\n\nA small agent that looks up program data and does arithmetic. Reuses run_agent."),
        code(CAPSTONE_DATA),
        code(
            """
tools = [lookup_indicator_tool, calculator_tool]

def run_tool(name, tool_input):
    if name == "lookup_indicator":
        return run_lookup_indicator(tool_input["region"], tool_input["indicator"])
    if name == "calculator":
        return run_calculator(tool_input["expression"])
    return "Error: unknown tool."

SYSTEM = "You are a field data helper. Use the tools to look up indicators and to do any arithmetic, one step at a time, then give a short, clear answer."

print(run_agent("What is the total number of clinics across all three regions?"))
"""
        ),
        md("## Done\n\nIn one notebook you ran a tool-use loop, a ReAct agent, a multi-tool agent, reflection and replanning, and a capstone. The same loop powered all of them."),
    ]

    write_notebook(cells, "agentic_mechanics_all_in_one.ipynb", "Agentic Mechanics: all in one")


def main():
    notebook_0()
    notebook_combined()
    for student in (False, True):
        notebook_1(student)
        notebook_2(student)
        notebook_3(student)
        notebook_4(student)
        notebook_5(student)


if __name__ == "__main__":
    main()
