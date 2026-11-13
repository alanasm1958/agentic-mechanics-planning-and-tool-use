"""Build an interactive, on-brand HTML resource library from README.md + quotes.json.

Run:  python build_library.py
Output: library.html (open in any browser).

It parses the Markdown reading list, merges in a short pulled quote per source,
and renders searchable, filterable cards in the UNDP brand. No dependencies.
"""

import html
import json
import re
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def parse_readme(path):
    """Return a list of entry dicts parsed from the Markdown reading list."""
    lines = open(path, encoding="utf-8").read().splitlines()
    entries = []
    section = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            section = line[3:].strip()
            i += 1
            continue
        if line.startswith("- **") and section:
            # Title is between the first pair of **.
            first = line.index("**")
            second = line.index("**", first + 2)
            title = line[first + 2:second]
            rest = line[second + 2:]
            meta_part = rest.split("`")[0].strip()
            if meta_part.startswith("(") and meta_part.endswith(")"):
                meta_part = meta_part[1:-1]
            if ", " in meta_part:
                source, year = meta_part.rsplit(", ", 1)
            else:
                source, year = meta_part, ""
            tags = re.findall(r"`\[([^\]]+)\]`", line)
            level = tags[0] if len(tags) > 0 else ""
            typ = tags[1] if len(tags) > 1 else ""
            access = tags[2] if len(tags) > 2 else ""
            url = lines[i + 1].strip() if i + 1 < len(lines) else ""
            annot = lines[i + 2].strip() if i + 2 < len(lines) else ""
            entries.append({
                "section": section, "title": title, "source": source.strip(),
                "year": year.strip(), "level": level, "type": typ,
                "access": access, "url": url, "annot": annot,
            })
            i += 3
            continue
        i += 1
    return entries


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


LEVEL_CLASS = {"intro": "lvl-intro", "core": "lvl-core", "deep": "lvl-deep"}
ACCESS_CLASS = {"free": "acc-free", "account-required": "acc-account", "paywalled": "acc-paywalled"}

CSS = """
  :root { --undp:#0063AC; --tint:#e8f1f8; --ink:#1a1a1a; --muted:#5a6b80; }
  * { box-sizing:border-box; }
  body { margin:0; font-family:'Helvetica Neue', Arial, sans-serif; color:var(--ink); background:#f4f6f9; line-height:1.5; }
  .wrap { max-width:900px; margin:0 auto; padding:30px 24px 64px; }
  header.top { display:flex; align-items:center; justify-content:space-between; gap:20px; border-bottom:4px solid var(--undp); padding-bottom:16px; }
  header.top h1 { color:var(--undp); font-size:30px; margin:0 0 4px; }
  header.top .sub { color:var(--muted); font-size:15px; }
  header.top img { height:60px; }
  .intro { font-size:15.5px; color:#33404f; margin:20px 0 6px; }
  .legend { display:flex; flex-wrap:wrap; gap:8px; margin:12px 0 8px; }
  .controls { position:sticky; top:0; background:#f4f6f9; padding:12px 0 10px; border-bottom:1px solid #e1e8f0; z-index:5; margin-bottom:6px; }
  #q { width:100%; max-width:440px; padding:10px 14px; border:2px solid #cfe0f1; border-radius:10px; font-size:15px; outline:none; }
  #q:focus { border-color:var(--undp); }
  .filtrow { display:flex; flex-wrap:wrap; gap:7px; margin-top:10px; align-items:center; }
  .flabel { font-size:13px; color:var(--muted); font-weight:700; margin:0 2px 0 6px; }
  .fchip { border:1.5px solid #cfe0f1; background:#fff; color:#33404f; font-size:13px; font-weight:700; padding:5px 12px; border-radius:999px; cursor:pointer; }
  .fchip.on { background:var(--undp); color:#fff; border-color:var(--undp); }
  #clear { font-size:13px; color:var(--undp); cursor:pointer; text-decoration:underline; margin-left:6px; }
  .count { color:var(--muted); font-size:13px; margin-top:8px; }
  .nav { display:flex; flex-wrap:wrap; gap:6px; margin:14px 0 4px; }
  .nav a { font-size:13px; color:var(--undp); text-decoration:none; border:1px solid #dbe6f3; border-radius:999px; padding:4px 12px; background:#fff; }
  .nav a:hover { background:var(--tint); }
  h2.section { color:var(--undp); font-size:22px; margin:30px 0 4px; scroll-margin-top:120px; }
  .card { background:#fff; border:1px solid #e1e8f0; border-radius:12px; padding:16px 20px; margin:12px 0; box-shadow:0 1px 3px rgba(16,42,79,.06); }
  .card-head { display:flex; justify-content:space-between; align-items:flex-start; gap:14px; }
  .card .title { color:var(--undp); font-weight:700; font-size:18px; text-decoration:none; }
  .card .title:hover { text-decoration:underline; }
  .tags { display:flex; flex-wrap:wrap; gap:6px; flex-shrink:0; }
  .pill { display:inline-block; font-size:11.5px; font-weight:700; padding:3px 10px; border-radius:999px; }
  .lvl-intro { background:var(--tint); color:var(--undp); }
  .lvl-core  { background:var(--undp); color:#fff; }
  .lvl-deep  { background:#003a66; color:#fff; }
  .type      { background:#eef1f5; color:var(--muted); }
  .acc-free  { background:#e7f4ec; color:#2e7d46; }
  .acc-account { background:#fff3e0; color:#b36b00; }
  .acc-paywalled { background:#fdecea; color:#c0392b; }
  .meta { color:var(--muted); font-size:13.5px; margin:7px 0 5px; }
  .annot { margin:5px 0 11px; font-size:15px; color:#2a3542; }
  blockquote.quote { margin:0 0 11px; padding:9px 15px; background:var(--tint); border-left:5px solid var(--undp); border-radius:6px; font-size:15.5px; color:#1f3a57; font-style:italic; }
  blockquote.quote cite { display:block; font-style:normal; font-size:12.5px; color:var(--muted); margin-top:5px; }
  .watch { display:inline-block; background:var(--tint); color:var(--undp); font-size:12.5px; font-weight:700; padding:3px 11px; border-radius:6px; margin-bottom:11px; }
  .open { color:var(--undp); font-weight:600; font-size:14px; text-decoration:none; }
  .open:hover { text-decoration:underline; }
  .empty { display:none; color:var(--muted); font-size:15px; padding:18px; text-align:center; }
  .note { margin-top:28px; padding:14px 18px; background:#fff; border:1px dashed #c9d6ef; border-radius:10px; color:var(--muted); font-size:14px; }
  footer.foot { margin-top:36px; padding-top:16px; border-top:1px solid #e1e8f0; color:var(--muted); font-size:13px; text-align:center; }
"""


def card_html(e, quotes):
    lvl_cls = LEVEL_CLASS.get(e["level"], "type")
    acc_cls = ACCESS_CLASS.get(e["access"], "type")
    url = e["url"]
    title = html.escape(e["title"])
    source = html.escape(e["source"])
    year = html.escape(e["year"])
    annot = html.escape(e["annot"])
    quote = quotes.get(url, "")
    text = " ".join([e["title"], e["source"], e["annot"], quote]).lower()
    data_text = html.escape(text, quote=True)
    meta = source + (" &middot; " + year if year else "")

    if quote:
        body_extra = ('<blockquote class="quote">' + html.escape(quote)
                      + '<cite>from ' + source + '</cite></blockquote>')
    elif e["type"] == "video":
        body_extra = '<span class="watch">Video</span><br>'
    else:
        body_extra = ""

    open_label = "Watch on YouTube" if e["type"] == "video" else "Open the resource"

    return (
        f'<div class="card" data-level="{e["level"]}" data-access="{e["access"]}" '
        f'data-type="{e["type"]}" data-text="{data_text}">'
        f'<div class="card-head">'
        f'<a class="title" href="{html.escape(url)}" target="_blank" rel="noopener">{title}</a>'
        f'<div class="tags">'
        f'<span class="pill {lvl_cls}">{html.escape(e["level"])}</span>'
        f'<span class="pill type">{html.escape(e["type"])}</span>'
        f'<span class="pill {acc_cls}">{html.escape(e["access"])}</span>'
        f'</div></div>'
        f'<div class="meta">{meta}</div>'
        f'<p class="annot">{annot}</p>'
        f'{body_extra}'
        f'<a class="open" href="{html.escape(url)}" target="_blank" rel="noopener">{open_label} &rarr;</a>'
        f'</div>'
    )


def build():
    entries = parse_readme(os.path.join(HERE, "README.md"))
    quotes = json.load(open(os.path.join(HERE, "quotes.json"), encoding="utf-8"))

    # Group by section, preserving first-seen order.
    order = []
    by_section = {}
    for e in entries:
        if e["section"] not in by_section:
            by_section[e["section"]] = []
            order.append(e["section"])
        by_section[e["section"]].append(e)

    nav = " ".join(f'<a href="#{slug(s)}">{html.escape(s)}</a>' for s in order)

    sections_html = []
    for s in order:
        cards = "\n".join(card_html(e, quotes) for e in by_section[s])
        sections_html.append(
            f'<h2 class="section" id="{slug(s)}">{html.escape(s)}</h2>\n{cards}'
        )

    total = len(entries)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Resource Library — Agentic Mechanics: Planning &amp; Tool Use</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <div>
      <h1>Resource Library</h1>
      <div class="sub">Agentic Mechanics: Planning &amp; Tool Use &nbsp;&middot;&nbsp; {total} curated resources</div>
    </div>
    <img src="../assets/undp-logo.svg" alt="UNDP">
  </header>

  <p class="intro">A curated reading and watching list. Each resource is tagged by <b>level</b>,
  <b>type</b>, and <b>access</b>, and most include a short quote from the source. Use the search box
  and filters to find what fits you.</p>

  <div class="legend">
    <span class="pill lvl-intro">intro</span>
    <span class="pill lvl-core">core</span>
    <span class="pill lvl-deep">deep</span>
    <span class="pill acc-free">free</span>
    <span class="pill acc-account">account-required</span>
    <span class="pill acc-paywalled">paywalled</span>
  </div>

  <div class="controls">
    <input id="q" type="text" placeholder="Search titles, sources, and notes...">
    <div class="filtrow">
      <span class="flabel">Level</span>
      <button class="fchip" data-f="level" data-v="intro">intro</button>
      <button class="fchip" data-f="level" data-v="core">core</button>
      <button class="fchip" data-f="level" data-v="deep">deep</button>
      <span class="flabel">Access</span>
      <button class="fchip" data-f="access" data-v="free">free</button>
      <button class="fchip" data-f="access" data-v="account-required">account</button>
      <button class="fchip" data-f="access" data-v="paywalled">paywalled</button>
      <span id="clear">clear</span>
    </div>
    <div class="count" id="count"></div>
  </div>

  <div class="nav">{nav}</div>

  {"".join(sections_html)}

  <div class="empty" id="empty">No resources match your search and filters.</div>

  <div class="note">Links in this fast-moving field go stale quickly. Revisit every few months to
  confirm each link works and still reflects current guidance, and replace anything that has moved
  or been superseded.</div>

  <footer class="foot">UNDP Istanbul International Center for Private Sector in Development (IICPSD)
  &nbsp;&middot;&nbsp; Agentic AI &amp; Vibe Coding &nbsp;&middot;&nbsp; Prepared by Alan Al-Jammoor</footer>
</div>

<script>
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('h2.section'));
  var active = {{ level:new Set(), access:new Set() }};
  var q = document.getElementById('q');

  function apply() {{
    var term = q.value.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function(c) {{
      var okText = !term || c.dataset.text.indexOf(term) !== -1;
      var okLevel = active.level.size === 0 || active.level.has(c.dataset.level);
      var okAccess = active.access.size === 0 || active.access.has(c.dataset.access);
      var vis = okText && okLevel && okAccess;
      c.style.display = vis ? '' : 'none';
      if (vis) shown++;
    }});
    // Hide section headers with no visible cards.
    sections.forEach(function(h) {{
      var n = h.nextElementSibling, any = false;
      while (n && !(n.tagName === 'H2')) {{
        if (n.classList && n.classList.contains('card') && n.style.display !== 'none') any = true;
        n = n.nextElementSibling;
      }}
      h.style.display = any ? '' : 'none';
    }});
    document.getElementById('count').textContent = 'Showing ' + shown + ' of ' + cards.length + ' resources';
    document.getElementById('empty').style.display = shown === 0 ? 'block' : 'none';
  }}

  document.querySelectorAll('.fchip').forEach(function(b) {{
    b.addEventListener('click', function() {{
      var set = active[b.dataset.f];
      if (set.has(b.dataset.v)) {{ set.delete(b.dataset.v); b.classList.remove('on'); }}
      else {{ set.add(b.dataset.v); b.classList.add('on'); }}
      apply();
    }});
  }});
  q.addEventListener('input', apply);
  document.getElementById('clear').addEventListener('click', function() {{
    q.value = '';
    active.level.clear(); active.access.clear();
    document.querySelectorAll('.fchip').forEach(function(b) {{ b.classList.remove('on'); }});
    apply();
  }});
  apply();
</script>
</body>
</html>
"""
    out = os.path.join(HERE, "library.html")
    open(out, "w", encoding="utf-8").write(page)
    print("wrote", out, "with", total, "entries across", len(order), "sections")


if __name__ == "__main__":
    build()
