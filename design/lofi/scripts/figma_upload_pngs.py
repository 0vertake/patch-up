#!/usr/bin/env python3
"""
POST Lo-Fi PNGs to Figma MCP upload URLs (from upload_assets).
Usage: agent provides JSON array of {slug, uploadUrl} in /tmp/patchup_figma_uploads.json
"""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

SCREENSHOTS = Path(__file__).resolve().parents[1] / "screenshots"
UPLOADS = Path("/tmp/patchup_figma_uploads.json")


def post_png(url: str, png: Path) -> dict:
    data = png.read_bytes()
    boundary = "----patchup"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{png.name}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode() + data + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())


def main() -> int:
    if not UPLOADS.exists():
        print(f"Missing {UPLOADS}", file=sys.stderr)
        return 1
    batch = json.loads(UPLOADS.read_text())
    for item in batch:
        slug = item["slug"]
        url = item["uploadUrl"]
        png = SCREENSHOTS / f"{slug}.png"
        if not png.exists():
            print(f"skip missing {png.name}")
            continue
        print(f"upload {slug} …")
        item["response"] = post_png(url, png)
    UPLOADS.write_text(json.dumps(batch, indent=2) + "\n", encoding="utf-8")
    print(f"Done {len(batch)} uploads")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
