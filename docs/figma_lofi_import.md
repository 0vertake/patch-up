# Import v05 Lo-Fi into Figma

**Design file (use this one):** https://www.figma.com/design/2fP7Qoa2u4KP5PR7hklFVJ

- Styled Lo-Fi wireframes (CSS **inlined** in HTML so Figma capture keeps gray buttons, placeholders, spacing)
- Prefer **PNG** import when `upload_assets` MCP quota is available (`design/lofi/screenshots/`)

**Do not use for defense:** https://www.figma.com/design/Gjc5WB8gO4MQRHwkPOOpj0 — html-to-design ran **without** CSS (looked like plain HTML paragraphs)

## Regenerate source wireframes

```bash
cd design/lofi
python3 scripts/generate_wireframes.py
./scripts/export_screenshots.sh
```

## Re-import to Figma (agent)

```bash
# 1) Serve HTML
cd design/lofi/html && python3 -m http.server 8765

# 2) Agent runs capture IDs + Playwright submit
python3 scripts/figma_orchestrate_all.py
# (requires /tmp/patchup_figma_captures.json from generate_figma_design batch)
```

## Prototype links (Navigate to) — MCP

Skripta za `use_figma` / `setReactionsAsync` (isti efekat kao ručni **Interaction → On click → Navigate to**):

`design/lofi/scripts/figma_prototype_apply.md`

Putanje: `design/lofi/flow-board-paths.md`

**Napomena:** Starter **View** plan ima ~6 MCP read poziva mesečno — ako agent javi rate limit, pokreni skriptu kad se kvota resetuje ili traži agenta ponovo.

## Optional Figma housekeeping (when MCP `use_figma` quota available)

On each frame: layout grid **4 columns**, margin **24**, gutter **16**.

## FigJam (unchanged)

DTI / HTA: https://www.figma.com/board/W968VgIikfTq7pltKLBW7W
