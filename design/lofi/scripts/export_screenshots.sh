#!/usr/bin/env bash
# Export 375×812 PNG screenshots from HTML wireframes (requires Chromium).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HTML="$ROOT/html"
OUT="$ROOT/screenshots"
mkdir -p "$OUT"

if command -v chromium >/dev/null 2>&1; then
  CHROME=chromium
elif command -v google-chrome-stable >/dev/null 2>&1; then
  CHROME=google-chrome-stable
elif command -v google-chrome >/dev/null 2>&1; then
  CHROME=google-chrome
else
  echo "No Chromium/Chrome found. Install chromium or run from a machine with headless Chrome." >&2
  exit 1
fi

for f in "$HTML"/*.html; do
  base="$(basename "$f" .html)"
  url="file://${f}"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --window-size=375,812 \
    --screenshot="$OUT/${base}.png" \
    "$url" 2>/dev/null
  echo "Exported ${base}.png"
done

echo "Done: $(ls -1 "$OUT"/*.png 2>/dev/null | wc -l) screenshots"
