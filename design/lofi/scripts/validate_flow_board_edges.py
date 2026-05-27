#!/usr/bin/env python3
"""Verify flow-board.html edge arrays match flow-board-paths.md slug list."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "flow-board-paths.md"
HTML = ROOT / "flow-board.html"


def parse_md_edges(text: str) -> tuple[set[tuple[str, str]], set[tuple[str, str]]]:
    solid, dash = set(), set()
    section = None
    for line in text.splitlines():
        if "**Glavne (solid):**" in line:
            section = "solid"
            continue
        if "**Retry / greška (dashed):**" in line:
            section = "dash"
            continue
        m = re.match(r"^\d+\.\s+([\w-]+)\s+→\s+([\w-]+)", line.strip())
        if not m:
            m = re.match(r"^-\s+([\w-]+)\s+→\s+([\w-]+)", line.strip())
        if m and section:
            pair = (m.group(1), m.group(2))
            (solid if section == "solid" else dash).add(pair)
    return solid, dash


def parse_html_edges(text: str, name: str) -> set[tuple[str, str]]:
    m = re.search(rf"const {name} = \[(.*?)\];", text, re.S)
    if not m:
        raise SystemExit(f"Missing {name} in flow-board.html")
    block = m.group(1)
    return set(re.findall(r'\["([\w-]+)"\s*,\s*"([\w-]+)"\]', block))


def main() -> int:
    md = MD.read_text(encoding="utf-8")
    html = HTML.read_text(encoding="utf-8")
    md_solid, md_dash = parse_md_edges(md)
    html_solid = parse_html_edges(html, "edgesSolid")
    html_dash = parse_html_edges(html, "edgesDash")
    ok = True
    for label, md_set, html_set in [
        ("solid", md_solid, html_solid),
        ("dash", md_dash, html_dash),
    ]:
        missing = md_set - html_set
        extra = html_set - md_set
        if missing:
            ok = False
            print(f"{label} missing in HTML:", sorted(missing))
        if extra:
            ok = False
            print(f"{label} extra in HTML:", sorted(extra))
    if ok:
        print(f"OK: {len(md_solid)} solid + {len(md_dash)} dashed edges match markdown")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
