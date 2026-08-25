#!/usr/bin/env bash
# Build the site locally into _site/ — same commands the GitHub Action runs.
# Use this to check a lecture renders before pushing it to students.
#
#   ./build.sh          build
#   ./build.sh --open   build, then open in your browser

set -euo pipefail
cd "$(dirname "$0")"

KATEX="https://cdn.jsdelivr.net/npm/katex@0.16/dist/"

rm -rf _site && mkdir -p _site

pandoc syllabus.md \
  --standalone --katex="$KATEX" --css style.css \
  --metadata pagetitle="Physics 421 — Thermodynamics & Statistical Mechanics" \
  --output _site/index.html
cp style.css _site/

if compgen -G "notes/*.md" > /dev/null; then
  mkdir -p _site/notes
  for f in notes/*.md; do
    pandoc "$f" \
      --standalone --katex="$KATEX" --css ../style.css \
      --metadata pagetitle="Physics 421" \
      --output "_site/notes/$(basename "${f%.md}").html"
  done
  [ -d notes/images ] && cp -r notes/images _site/notes/
fi

[ -d hw ] && cp -r hw _site/ || true

echo "built _site/  ($(find _site -name '*.html' | wc -l | tr -d ' ') pages)"
[ "${1:-}" = "--open" ] && open _site/index.html
exit 0
