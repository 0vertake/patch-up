#!/usr/bin/env python3
"""Run Playwright Figma html-to-design capture for one screen."""
from __future__ import annotations

import json
import sys
from playwright.sync_api import sync_playwright

PORT = 8765


def run(slug: str, capture_id: str) -> dict:
    endpoint = f"https://mcp.figma.com/mcp/capture/{capture_id}/submit"
    url = f"http://localhost:{PORT}/{slug}.html"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 375, "height": 812})
        page.goto(url, wait_until="load", timeout=30000)
        js = page.context.request.get(
            "https://mcp.figma.com/mcp/html-to-design/capture.js", timeout=30000
        ).text()
        page.evaluate(
            "(s) => { const el = document.createElement('script'); el.textContent = s; document.head.appendChild(el); }",
            js,
        )
        page.wait_for_timeout(600)
        result = page.evaluate(
            """async ({ captureId, endpoint }) => {
              if (!window.figma?.captureForDesign) return { ok: false, error: 'no API' };
              window.figma.captureForDesign({
                captureId, endpoint, selector: '.screen', includeStyles: true
              }).catch(() => {});
              await new Promise((r) => setTimeout(r, 3000));
              return { ok: true, submitted: true };
            }""",
            {"captureId": capture_id, "endpoint": endpoint},
        )
        browser.close()
    return {"slug": slug, "captureId": capture_id, **result}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: figma_batch_capture.py <slug> <captureId>", file=sys.stderr)
        sys.exit(1)
    out = run(sys.argv[1], sys.argv[2])
    print(json.dumps(out))
