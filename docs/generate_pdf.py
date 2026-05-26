#!/usr/bin/env python3
"""Generate PDF version of PatchUp spec with embedded survey screenshots."""

import base64
import os
import re
import sys
from pathlib import Path

import markdown

SCREENSHOTS = Path(os.path.expanduser("~/Marko/Faks/semestar6/human_computer_interaction/screenshots"))
MD_FILE = Path(__file__).parent / "Specifikacija_projekta_PatchUp.md"
OUT_PDF = Path(__file__).parent / "Specifikacija_projekta_PatchUp.pdf"

# Filenames use U+202F (narrow no-break space) before PM
NBSP = " "

FILES = {
    "age":        f"Screenshot 2026-05-06 at 3.19.30{NBSP}PM.png",
    "actions":    f"Screenshot 2026-05-06 at 3.19.50{NBSP}PM.png",
    "barriers":   f"Screenshot 2026-05-06 at 3.21.15{NBSP}PM.png",
    "app_interest": f"Screenshot 2026-05-06 at 3.20.19{NBSP}PM.png",
    "ai_explain": f"Screenshot 2026-05-06 at 3.20.32{NBSP}PM.png",
    "community":  f"Screenshot 2026-05-06 at 3.20.37{NBSP}PM.png",
    "motivators": f"Screenshot 2026-05-06 at 3.20.52{NBSP}PM.png",
    "features":   f"Screenshot 2026-05-06 at 3.20.59{NBSP}PM.png",
}


def img_b64(key: str) -> str:
    path = SCREENSHOTS / FILES[key]
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode()
    return f'data:image/png;base64,{b64}'


def img_b64_path(path: Path) -> str:
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode()
    return f'data:image/png;base64,{b64}'


def img_tag(key: str, caption: str) -> str:
    src = img_b64(key)
    return f"""
<figure>
  <img src="{src}" class="chart" alt="{caption}">
  <figcaption>{caption}</figcaption>
</figure>
"""


def diagram_tag(path: Path, css_class: str = "diagram") -> str:
    src = img_b64_path(path)
    return f'<figure><img src="{src}" class="{css_class}" alt="{path.stem}"></figure>'


# Each tuple: (text marker in markdown, HTML to insert right after it)
CHART_INJECTIONS = [
    (
        "Grupa 36–50 nije bila zastupljena.",
        img_tag("age", "Slika 1 — Starosna distribucija ispitanika (28 odgovora)"),
    ),
    (
        "Ništa ih ne sprečava                  | 7,1%            |",
        img_tag("barriers", "Slika 2 — Barijere koje sprečavaju ispitanike da pokušaju popravku"),
    ),
    (
        "direktno potvrđuje potrebu za transparentnom AI dijagnozom.",
        img_tag("app_interest", "Slika 3 — Interes za korišćenje AI aplikacije za procenu kvara") +
        img_tag("ai_explain", "Slika 4 — Važnost objašnjenja razloga AI preporuke (skala 1–5)"),
    ),
    (
        "latentni interes koji može biti aktiviran pravim informacijama i usmeravanjem.",
        img_tag("community", "Slika 5 — Iskustvo ispitanika sa lokalnim zajednicama za popravku"),
    ),
    (
        "Ekologija (manje otpada) | 21,4%           |",
        img_tag("motivators", "Slika 6 — Motivatori za popravku umesto odbacivanja predmeta"),
    ),
    (
        "Povezivanje sa lokalnim majstorima / volonterima  | 39,3%           |",
        img_tag("features", "Slika 7 — Željene funkcionalnosti aplikacije"),
    ),
]


CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: 'Helvetica Neue', Arial, 'DejaVu Sans', sans-serif;
    font-size: 11pt;
    line-height: 1.65;
    color: #1a1a2e;
    background: #fff;
}

h1 {
    font-size: 20pt;
    font-weight: 700;
    color: #1a3a5c;
    margin-bottom: 6pt;
    line-height: 1.25;
    page-break-after: avoid;
}

h2 {
    font-size: 13.5pt;
    font-weight: 700;
    color: #1a3a5c;
    margin-top: 20pt;
    margin-bottom: 7pt;
    padding-bottom: 3pt;
    border-bottom: 2px solid #3b82f6;
    page-break-after: avoid;
}

h3 {
    font-size: 11pt;
    font-weight: 700;
    color: #2d5a8e;
    margin-top: 13pt;
    margin-bottom: 4pt;
    page-break-after: avoid;
}

h4 {
    font-size: 10.5pt;
    font-weight: 700;
    color: #374151;
    margin-top: 9pt;
    margin-bottom: 3pt;
    page-break-after: avoid;
}

p {
    margin-bottom: 7pt;
    text-align: justify;
    orphans: 3;
    widows: 3;
}

strong { font-weight: 700; color: #111827; }
em { font-style: italic; }

ul, ol {
    margin: 5pt 0 7pt 16pt;
}
li { margin-bottom: 2pt; }

table {
    width: 100%;
    border-collapse: collapse;
    margin: 8pt 0 10pt 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}
th {
    background: #1a3a5c;
    color: #fff;
    font-weight: 700;
    padding: 5pt 7pt;
    text-align: left;
}
td {
    padding: 4pt 7pt;
    border-bottom: 1px solid #e5e7eb;
    vertical-align: top;
}
tr:nth-child(even) td { background: #f8fafc; }

code {
    font-family: 'Courier New', monospace;
    font-size: 8.5pt;
    background: #f1f5f9;
    padding: 0 2pt;
}

pre {
    font-family: 'Courier New', monospace;
    font-size: 7.5pt;
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #3b82f6;
    padding: 8pt 10pt;
    margin: 6pt 0 10pt 0;
    white-space: pre;
    line-height: 1.4;
    page-break-inside: avoid;
}

hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 14pt 0;
}

figure {
    margin: 10pt 0 12pt 0;
    text-align: center;
    page-break-inside: avoid;
}

figure img.chart {
    max-width: 88%;
    max-height: 190px;
    border: 1px solid #e2e8f0;
    border-radius: 4pt;
    box-shadow: 0 1pt 4pt rgba(0,0,0,0.1);
}

figure img.diagram {
    max-width: 100%;
    border: 1px solid #e2e8f0;
    border-radius: 4pt;
    box-shadow: 0 1pt 4pt rgba(0,0,0,0.1);
}

figcaption {
    font-size: 8.5pt;
    color: #6b7280;
    margin-top: 4pt;
    font-style: italic;
}

blockquote {
    border-left: 3px solid #3b82f6;
    margin: 7pt 0;
    padding: 5pt 10pt;
    background: #eff6ff;
    font-style: italic;
    color: #374151;
}

@page {
    size: A4;
    margin: 22mm 18mm 22mm 20mm;
    @bottom-center {
        content: counter(page);
        font-size: 8.5pt;
        color: #9ca3af;
    }
    @top-right {
        content: "PatchUp — Specifikacija projekta";
        font-size: 8pt;
        color: #9ca3af;
    }
}

@page :first {
    @bottom-center { content: none; }
    @top-right { content: none; }
}
"""


def inject_charts(md_text: str) -> str:
    for marker, chart_html in CHART_INJECTIONS:
        if marker in md_text:
            md_text = md_text.replace(marker, marker + "\n\n" + chart_html + "\n\n", 1)
        else:
            print(f"WARNING: marker not found: {marker[:60]!r}", file=sys.stderr)
    return md_text


def postprocess_html(html: str) -> str:
    """Replace HTA/DTI section bodies with diagram images, strip [cite:N] refs."""

    # Strip all [cite:NNN] references
    html = re.sub(r'\[cite:\d+\]', '', html)

    hta_img = diagram_tag(SCREENSHOTS / "hta.png")
    dti_img = diagram_tag(SCREENSHOTS / "dti.png")

    # Replace everything between <h2>9. HTA...</h2> and <h2>10. ... with just the image.
    # The h2 heading stays; only the body content is swapped.
    html = re.sub(
        r'(<h2>[^<]*9\.[^<]*HTA[^<]*</h2>).*?(<h2>[^<]*10\.)',
        rf'\1\n{hta_img}\n\2',
        html,
        flags=re.DOTALL,
    )

    # Replace everything after <h2>10. DTI...</h2> until </body> with just the image.
    html = re.sub(
        r'(<h2>[^<]*10\.[^<]*DTI[^<]*</h2>).*?(</body>)',
        rf'\1\n{dti_img}\n\2',
        html,
        flags=re.DOTALL,
    )

    return html


def build_html(md_text: str) -> str:
    md_with_charts = inject_charts(md_text)

    md_parser = markdown.Markdown(
        extensions=["tables", "fenced_code"],
    )
    body_html = md_parser.convert(md_with_charts)

    full_html = f"""<!DOCTYPE html>
<html lang="sr">
<head>
<meta charset="UTF-8">
<title>PatchUp — Specifikacija projekta</title>
<style>
{CSS}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""
    return postprocess_html(full_html)


def main():
    md_text = MD_FILE.read_text(encoding="utf-8")
    html = build_html(md_text)

    html_out = OUT_PDF.with_suffix(".html")
    html_out.write_text(html, encoding="utf-8")
    print(f"HTML written to {html_out}")

    # Use Chrome DevTools Protocol for PDF generation (no headers/footers)
    import asyncio
    import json
    import subprocess
    import time
    import urllib.request

    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    html_abs = str(html_out.resolve())
    url = f"file://{html_abs}"

    async def generate_pdf_via_cdp():
        import websockets

        # Start Chrome pointing at about:blank so a page target is created
        proc = subprocess.Popen(
            [
                chrome,
                "--headless=new",
                "--no-sandbox",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--remote-debugging-port=9222",
                "about:blank",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            # Wait for Chrome to start and expose a page target
            ws_url = None
            for _ in range(30):
                time.sleep(0.5)
                try:
                    resp = urllib.request.urlopen("http://localhost:9222/json/list", timeout=2)
                    targets = json.loads(resp.read())
                    page_targets = [t for t in targets if t.get("type") == "page"]
                    if page_targets:
                        ws_url = page_targets[0]["webSocketDebuggerUrl"]
                        break
                except Exception:
                    pass
            if not ws_url:
                raise RuntimeError("Chrome did not start in time")

            async with websockets.connect(ws_url, max_size=50 * 1024 * 1024) as ws:
                msg_id = 1

                async def send(method, params=None):
                    nonlocal msg_id
                    _id = msg_id
                    msg_id += 1
                    await ws.send(json.dumps({"id": _id, "method": method, "params": params or {}}))
                    return _id

                async def recv_until(target_id):
                    while True:
                        raw = await asyncio.wait_for(ws.recv(), timeout=30)
                        msg = json.loads(raw)
                        if msg.get("id") == target_id:
                            if "error" in msg:
                                raise RuntimeError(f"CDP error: {msg['error']}")
                            return msg.get("result", {})

                # Enable Page domain and navigate to our HTML file
                await send("Page.enable")
                nav_id = await send("Page.navigate", {"url": url})
                # Wait for navigation to complete
                await recv_until(nav_id)
                # Also wait for loadEventFired
                await asyncio.sleep(2)

                # Print to PDF without headers/footers
                print_id = await send("Page.printToPDF", {
                    "displayHeaderFooter": False,
                    "printBackground": True,
                    "paperWidth": 8.27,
                    "paperHeight": 11.69,
                    "marginTop": 0.87,
                    "marginBottom": 0.87,
                    "marginLeft": 0.79,
                    "marginRight": 0.71,
                    "preferCSSPageSize": False,
                })
                result = await recv_until(print_id)
                pdf_data = base64.b64decode(result["data"])
                OUT_PDF.write_bytes(pdf_data)
        finally:
            proc.terminate()
            proc.wait()

    asyncio.run(generate_pdf_via_cdp())
    print(f"PDF written to {OUT_PDF}")
    size_kb = OUT_PDF.stat().st_size // 1024
    print(f"File size: {size_kb} KB")


if __name__ == "__main__":
    main()
