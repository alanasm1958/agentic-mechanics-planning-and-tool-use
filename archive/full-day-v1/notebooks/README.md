# Notebooks

Hands-on Jupyter notebooks for the module. They are written for beginners and
non-coders and are designed to run in **Google Colab** with no local setup. Each
notebook is narrated: read a cell, run it, look at the output, then make a small
guided edit.

## The notebooks, in order

| File | What the learner does |
|------|------------------------|
| `00_setup_and_first_message.ipynb` | Install the library, enter their API key, send a first message. |
| `01_first_tool_use_loop_*.ipynb` | Give the model a calculator tool and run a full tool-use loop. |
| `02_react_from_scratch_*.ipynb` | Build a small ReAct loop and watch it think, act, and observe. |
| `03_multi_tool_agent_*.ipynb` | Give the agent three tools and watch it pick the right one. |
| `04_reflection_and_replanning_*.ipynb` | The agent checks its own work and recovers from a tool error. |
| `05_capstone_*.ipynb` | Build a small field-data agent end to end (take-home). |

## Two versions of each hands-on notebook

- `*_instructor.ipynb`: the complete, working version.
- `*_student.ipynb`: the same notebook with the key learning cells left as
  guided `TODO`s for the learner to complete.

Notebook 0 has a single version (it is just setup).

## One-file option (lowest friction)

`agentic_mechanics_all_in_one.ipynb` holds every part in a single notebook (Part 1 through
Part 5, in order). Upload it once, install once, set the key once, then scroll from top to
bottom. Use this when you want one setup for the whole session instead of opening six files.
The separate notebooks above are better when you want each exercise on its own.

## Running in Google Colab

The smooth way (recommended for a class):

1. Host the notebooks once (a GitHub repo or a shared Google Drive folder) and give
   learners a one-click **"Open in Colab"** link per notebook. This avoids uploading.
2. On first open, each learner does **File then Save a copy in Drive** and works in their copy.
3. Run the three setup cells at the top, then the rest in order.

If you are not hosting them, learners can use **File then Upload notebook** in Colab and pick
the file, but they will need to upload each notebook once.

## Cutting the repeated friction

Colab gives each notebook a fresh machine, so a few things reset per session. Here is how to
keep it fast:

- **API key, set it once.** Store the key in **Colab Secrets** (the key icon in the left
  sidebar), named `ANTHROPIC_API_KEY`, with "Notebook access" turned on. The setup cell reads
  it automatically, so learners never paste it again. If no secret is set, the cell falls back
  to a one-time hidden prompt.
- **Do not re-upload.** Open from a link and Save a copy in Drive (above), so there is nothing
  to upload next time.
- **The install stays.** `!pip install -q anthropic` runs once per session (about 15 seconds).
  This cannot be avoided in Colab, but it is the only package and it is quick.

## API key and model

- Each learner uses their **own Anthropic API key**, read from **Colab Secrets** when set, or
  entered with a hidden prompt otherwise. Keys are never written into the notebooks.
- The model is set near the top with `MODEL = "claude-opus-4-8"`. For faster and cheaper
  practice runs, change it to `"claude-haiku-4-5"`.

## Regenerating the notebooks (for maintainers)

The notebooks are generated from one source file so the instructor and student
versions never drift. To rebuild after editing content:

```
python -m venv .venv && source .venv/bin/activate
pip install nbformat
python build_notebooks.py
```

`build_notebooks.py` is the single source of truth for notebook content.
