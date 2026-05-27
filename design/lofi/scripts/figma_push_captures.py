#!/usr/bin/env python3
"""
Drive Figma html-to-design captures for all Lo-Fi screens.
Requires: manifest + /tmp/patchup_figma_captures.json (list of {slug, captureId})
           local server on port 8765 serving design/lofi/html/

Run captures with Playwright (install: pip install playwright && playwright install chromium)
"""
from __future__ import annotations

import json
import sys
import time
import urllib.parse
from pathlib import Path

MANIFEST = Path(__file__).resolve().parents[1] / "manifest.json"
CAPTURES_JSON = Path("/tmp/patchup_figma_captures.json")
PORT = 8765
FIGMA_DELAY_MS = 2500


def capture_url(slug: str, capture_id: str) -> str:
    endpoint = f"https://mcp.figma.com/mcp/capture/{capture_id}/submit"
    q = urllib.parse.urlencode(
        {
            "figmacapture": capture_id,
            "figmaendpoint": endpoint,
            "figmadelay": str(FIGMA_DELAY_MS),
        }
    )
    return f"http://localhost:{PORT}/{slug}.html#{q}"


def main() -> int:
    if not CAPTURES_JSON.exists():
        print(f"Missing {CAPTURES_JSON} — agent must write capture IDs first.", file=sys.stderr)
        return 1
    captures = json.loads(CAPTURES_JSON.read_text())
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Install: pip install playwright && playwright install chromium", file=sys.stderr)
        return 1

    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 375, "height": 812})
        for item in captures:
            slug = item["slug"]
            cid = item["captureId"]
            url = capture_url(slug, cid)
            print(f"Capturing {slug} …")
            page.goto(url, wait_until="networkidle", timeout=60000)
            time.sleep(FIGMA_DELAY_MS / 1000 + 1)
            results.append({"slug": slug, "captureId": cid, "url": url})
        browser.close()

    out = Path("/tmp/patchup_figma_capture_done.json")
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(results)} pages opened for capture)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
