# Lo-Fi compliance checklist (PatchUp)

Reference: `docs/vezbe/v05/Specifikacija-LoFi-prototip.md`, `Osnove-Dizajna-Rasporeda-i-Vizuelne-Hijerarhije.md`, `v06/Figma-osnove.md`, `DESIGN.md`.

## v05 Lo-Fi rules

| Requirement | Status | Notes |
|-------------|--------|-------|
| No colors | **Pass** | `design/lofi/wireframes` uses grayscale tokens only |
| No final images | **Pass** | Gray blocks + text labels |
| No decoration | **Pass** | No icons, emoji, or illustrations |
| Image placeholders | **Pass** | "Photo placeholder", "Logo placeholder", 48×48 list thumbs |
| Realistic titles | **Pass** | Domain copy on all screens |
| Clear button names | **Pass** | e.g. "Scan item", "See repair options" |
| Layout / hierarchy / grouping | **Pass** | Diagnosis block, list rows, path rows |
| Navigation visible | **Pass** | Back, hub links, chevrons as text `›` |
| Primary actions clear | **Pass** | One `#2b2b2b` primary per screen |

## v05 layout & hierarchy

| Requirement | Status | Notes |
|-------------|--------|-------|
| Single-column (mobile) | **Pass** | 375px wireframes |
| Card layout for lists | **Pass** | Community, history |
| Max ~3 font sizes | **Pass** | 20 / 16 / 14–12 |
| Grouping / proximity | **Pass** | Diagnosis block rows |
| Whitespace | **Pass** | 16px padding, spaced sections |

## v06 Figma (when imported)

| Requirement | Status | Notes |
|-------------|--------|-------|
| Frame = screen (not Group) | **Manual** | Trace PNG or rebuild in Figma |
| 375×812 mobile | **Pass** | In HTML/PNG export |
| Grid 4 col, margin 24, gutter 16 | **Manual** | Add in Figma per frame (`DESIGN.md`) |
| 8px spacing scale | **Pass** | CSS uses 8/16/24 |
| Auto Layout | **Manual** | Apply in Figma after import |
| Prototype links | **Manual** | Connect per `patchup_app_flow.md` |

## Flow coverage (MVP)

| Area | Status | Notes |
|------|--------|-------|
| F0 entry | **Pass** | S-00, S-01 |
| F1 registration | **Partial** | S-20 + multi-step email registration (S-23a/b/c); OAuth screens not included |
| F2 sign in | **Partial** | S-10 shown with disabled CTA state; forgot-password screen not included |
| F3 home | **Pass** | S-30 |
| F4 scan + AI | **Partial** | S-40, S-44, S-46, S-43e (no S-41/42 camera split) |
| F5 DIY | **Partial** | S-50 (no S-52 chat) |
| F6 community | **Pass** | S-60, S-61 + multi-step booking (S-62a/b/c) + confirmation S-63 |
| F7 not worth it | **Pass** | S-70 |
| F8 outcome | **Partial** | Multi-step outcome (S-80a/b/c); impact summary screen not included |
| F9 history | **Partial** | S-90 (no S-91 detail) |
| F10 profile | **Partial** | S-100 + multi-step edit profile (S-101a/b/c) |
| F11 settings | **Pass** | S-110 |

**Defense line:** Lo-Fi covers the **MVP happy path** and main branches; full flow document lists optional and system screens for KT1/DTI.

## What was fixed (vs Stitch export)

- Removed Material colors, Tailwind theme, and Material Symbols icons
- Regenerated **33** screens as native grayscale wireframes (no Tailwind, no Material colors/icons)
- Multi-step forms + **error only after Next** + **Summary** + **Everything looks good** message
- Numeric fields annotated for numeric keypad (help time, phone)
- No asterisks; **All fields are required** where applicable
- Primary CTA **disabled** until valid on step 1 screens
- PNG screenshots under `design/lofi/screenshots/`
- Raw Stitch export: `design/lofi/archive/stitch-raw-2026-05-26/`

## Figma file

Figma file with all **33** compliant screens: https://www.figma.com/design/Gjc5WB8gO4MQRHwkPOOpj0 (html-to-design import). Prototype/grid polish may need one more `use_figma` pass when MCP quota resets.
