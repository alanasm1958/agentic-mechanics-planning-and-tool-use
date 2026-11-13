# Slides

The presentation is a Marp deck. `deck.md` is the editable source. It is branded for the
UNDP Istanbul International Center for Private Sector in Development (IICPSD).

## Ready-to-use exports

- `deck.pdf` present or share
- `deck.pptx` open and edit in PowerPoint or Keynote
- `deck.html` open in any browser as a slideshow

## What the deck uses

- **Brand colour:** UNDP blue `#0063AC` (taken from the official logo file).
- **Logo:** `../assets/undp-logo.svg` (official UNDP logo) and
  `../assets/undp-logo-white.svg` (reversed, for the dark divider slides).
- **Diagrams:** SVG files in `../assets/` (chatbot vs agent, the agent loop, the
  four-part anatomy, the tool-use loop, a tool card, MCP, the ReAct loop, and the three
  agent shapes). They are plain SVG, editable in any vector tool or a text editor.

## Re-rendering after edits

The deck pulls in local SVG files (logo and diagrams), so pass `--allow-local-files`:

```
marp deck.md --pdf  --allow-local-files
marp deck.md --pptx --allow-local-files
marp deck.md --html --allow-local-files
```

Install the tool with `npm install -g @marp-team/marp-cli` if needed.

## Editing in VS Code (Marp extension)

The deck uses HTML blocks and local images, so set these once:

- Turn on **Markdown > Marp: Enable HTML** in settings.
- Trust the workspace so local images load.

Then open `deck.md`, use the live preview, and export from the Marp menu.

## Notes for trainers

- Every content slide carries **speaker notes**, visible in the Marp presenter view, with
  what to say and a question to ask the room.
- To adapt the branding for a different centre or programme, edit the `footer` in the
  frontmatter and the names on the title and closing slides.
- The diagrams use the brand blue. If you restyle, keep `#0063AC` as the primary colour.
