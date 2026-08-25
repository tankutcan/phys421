#!/usr/bin/env python3
"""Copy lecture notes from the Obsidian vault into this repo, translating
Obsidian-only syntax into something pandoc understands.

    ./publish.py "Lecture 11"              # one note — the weekly case
    ./publish.py "Lecture 11" "Lecture 12" # several
    ./publish.py --list                    # what's published, with titles

Publishing is always explicit: only the notes you name are read. There is
deliberately no --all, so nothing reaches students unreviewed.

TITLES
    Give a lecture a title by adding a `title:` line to its frontmatter in
    Obsidian:

        ---
        dg-publish: true
        title: Carnot's Theorem and the Clausius Inequality
        ---

    Failing that, a heading like `# 9/11 - Entropy and Microstates` donates
    its text. Failing that, the note's filename is used.

DATES
    Dates live in the course calendar, not in the lectures. A heading that is
    just a date (`# 10/7`) is stripped on publish.

URLS
    The page URL comes from the vault filename, so "Lecture 11" is always
    notes/lecture-11.html. Retitling a lecture never breaks a link.
"""

import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote

VAULT = Path.home() / "Documents" / "Obsidian Vault"
SOURCE = VAULT / "Physics 421"
IMAGES = VAULT / "images"

REPO = Path(__file__).parent
NOTES = REPO / "notes"
NOTE_IMAGES = NOTES / "images"

EMBED = re.compile(r"!\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")   # ![[img.png]] or ![[img.png|300]]
WIKILINK = re.compile(r"(?<!!)\[\[([^\]|]+?)(?:\|([^\]]*))?\]\]")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

# "# 10/7", "#  9/9", "# 9/11 - Entropy, Macrostates, and Microstates"
DATE_HEADING = re.compile(
    r"\A#{1,6}[ \t]*\d{1,2}/\d{1,2}[ \t]*(?:[-–—:][ \t]*(?P<rest>.+?))?[ \t]*\Z"
)


def slug(name):
    """'Lecture 11' -> 'lecture-11'"""
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def split_frontmatter(text):
    """Return (dict of frontmatter keys, body). Tolerates a missing block."""
    m = FRONTMATTER.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip("\"'")
    return meta, text[m.end():]


def strip_date_heading(body):
    """Drop a leading date-only heading. Returns (body, title_or_None).

    A heading like `# 9/11 - Entropy and Microstates` donates its text as a
    fallback title on the way out.
    """
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        m = DATE_HEADING.match(line.strip())
        if m:
            del lines[i]
            return "\n".join(lines), (m.group("rest") or "").strip() or None
        break   # first non-blank line isn't a date heading — leave it alone
    return body, None


def normalise_rules(body):
    """Turn `---` / `-----` separators into `***`.

    Obsidian renders any run of 3+ dashes as a horizontal rule. Pandoc does
    not: depending on context it reads them as a table delimiter or a second
    YAML metadata block, which swallows the surrounding content or fails the
    build outright. `***` is unambiguous in both.

    Only converts a dash run that follows a blank line, so a setext heading
    (text on one line, dashes underneath) is left alone.
    """
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if not re.fullmatch(r"[ \t]*-{3,}[ \t]*", line):
            continue
        if i == 0 or not lines[i - 1].strip():
            lines[i] = "***"
    return "\n".join(lines)


def convert(text, images_used):
    """Rewrite Obsidian syntax. Mutates images_used with filenames seen."""
    text = normalise_rules(text)

    def embed(m):
        fn = m.group(1).strip()
        images_used.add(fn)
        # Percent-encode: these filenames are full of spaces.
        return f"![]({quote('images/' + fn)})"

    def link(m):
        target = m.group(1).strip()
        label = (m.group(2) or "").strip()
        # Obsidian writes both "Lecture 5" and "Physics 421/Lecture 5".
        target = target.split("/")[-1]
        return f"[{label or target}]({slug(target)}.html)"

    text = EMBED.sub(embed, text)
    text = WIKILINK.sub(link, text)
    return text.strip() + "\n"


def publish(name):
    src = SOURCE / f"{name}.md"
    if not src.exists():
        print(f"  !  no such note: {src}")
        return None

    raw = src.read_text(encoding="utf-8")
    if not raw.strip():
        print(f"  !  {name} is empty — skipping")
        return None

    meta, body = split_frontmatter(raw)
    body, heading_title = strip_date_heading(body)

    # frontmatter title  >  text from a dated heading  >  the filename
    title = meta.get("title") or heading_title or name
    untitled = not (meta.get("title") or heading_title)

    images_used = set()
    body = convert(body, images_used)

    NOTES.mkdir(exist_ok=True)
    out = NOTES / f"{slug(name)}.md"
    esc = title.replace('"', '\\"')
    out.write_text(f'---\ntitle: "{esc}"\n---\n\n{body}', encoding="utf-8")

    copied, missing = 0, []
    for fn in sorted(images_used):
        srcimg = IMAGES / fn
        if srcimg.exists():
            NOTE_IMAGES.mkdir(parents=True, exist_ok=True)
            shutil.copy2(srcimg, NOTE_IMAGES / fn)
            copied += 1
        else:
            missing.append(fn)

    print(f"  ok {name} -> notes/{out.name}  ({copied} images)")
    print(f"       title: {title}" + ("   <- no title set; add one in Obsidian" if untitled else ""))
    for fn in missing:
        print(f"       missing image: {fn}")
    return (title, f"{slug(name)}.html")


def read_title(path):
    meta, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    return meta.get("title") or path.stem


def published():
    """(title, filename) for every published lecture, in lecture-number order."""
    pages = [p for p in NOTES.glob("*.md") if p.stem != "index"]
    pages.sort(key=lambda p: (
        int(m.group(1)) if (m := re.search(r"(\d+)", p.stem)) else 999, p.stem))
    return [(read_title(p), f"{p.stem}.html") for p in pages]


def write_index():
    """Regenerate notes/index.md, listing lectures by title."""
    lines = ['---\ntitle: "Physics 421 — Lecture Notes"\n---\n',
             "[← Syllabus](../index.html)\n"]
    for title, href in published():
        lines.append(f"- [{title}]({href})")
    (NOTES / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  ok notes/index.md ({len(published())} lectures)")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)

    if args[0] == "--list":
        for title, href in published():
            print(f"{href:24} {title}")
        sys.exit(0)

    results = [publish(a) for a in args]
    if any(results):
        write_index()
        print("\nPaste into the Schedule table in syllabus.md:\n")
        for r in results:
            if r:
                print(f"    [{r[0]}](notes/{r[1]})")
        print("\nthen:  ./build.sh --open")
