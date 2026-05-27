#!/usr/bin/env python3
"""
Capture all Lo-Fi screens into Figma via html-to-design.
Input: /tmp/patchup_figma_captures.json — [{slug, captureId}, ...]
Requires: python3 -m http.server 8765 in design/lofi/html
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

CAPTURES = Path("/tmp/patchup_figma_captures.json")
SCRIPT = Path(__file__).resolve().parent / "figma_batch_capture.py"
PORT = 8765


def main() -> int:
    if not CAPTURES.exists():
        print(f"Missing {CAPTURES}", file=sys.stderr)
        return 1
    items = json.loads(CAPTURES.read_text())
    done = []
    for i, item in enumerate(items, 1):
        slug = item["slug"]
        cid = item["captureId"]
        if item.get("skip") or item.get("done"):
            print(f"  skip (done)")
            continue
        print(f"[{i}/{len(items)}] {slug}")
        r = subprocess.run(
            [sys.executable, str(SCRIPT), slug, cid],
            capture_output=True,
            text=True,
            timeout=90,
        )
        if r.returncode != 0:
            print(r.stderr or r.stdout, file=sys.stderr)
            item["error"] = (r.stderr or r.stdout)[:500]
        else:
            try:
                item["result"] = json.loads(r.stdout)
            except json.JSONDecodeError:
                item["result"] = {"raw": r.stdout[:200]}
        done.append(item)
        time.sleep(2)
    CAPTURES.write_text(json.dumps(items, indent=2) + "\n", encoding="utf-8")
    print(f"Finished {len(done)} captures. Poll via Figma MCP generate_figma_design captureId.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
