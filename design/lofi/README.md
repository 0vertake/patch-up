# PatchUp Lo-Fi (HCI v05/v06 compliant)

Grayscale wireframes aligned with course exercises and defense rules. Based on flow in `docs/patchup_app_flow.md` and Stitch project `17554208072889623118` (raw export archived).

| Folder | Contents |
|--------|----------|
| `html/` | Compliant HTML wireframes (375×812) |
| `screenshots/` | PNG exports for Figma import |
| `wireframes/shared.css` | Lo-Fi design tokens (grayscale, grid spacing) |
| `scripts/` | `generate_wireframes.py`, `export_screenshots.sh` |
| `manifest.json` | Screen list and paths |
| `archive/stitch-raw-2026-05-26/` | Original Stitch HTML/PNG (not v05-compliant) |

## Regenerate

```bash
cd design/lofi
python3 scripts/generate_wireframes.py
./scripts/export_screenshots.sh
```

## Screens (33)

Includes Stitch flow **plus** HCI extras: S-43e error, S-62 step 2, S-80 step 2, S-101 edit profile as multi-step + error + summary, S-110 settings.

| ID | Slug |
|----|------|
| S-00 | `s-00-welcome` |
| S-01 | `s-01-account-check` |
| S-10 | `s-10-sign-in` |
| S-20 | `s-20-registration-method` |
| S-23 | `s-23-registration-step-1`, `s-23-step-1-error-state`, `s-23-registration-step-2`, `s-23-registration-summary` |
| S-30 | `s-30-home-hub` |
| S-40 | `s-40-scan-item` |
| S-43e | `s-43e-error-not-recognized` |
| S-44 | `s-44-describe-fault` |
| S-46 | `s-46-ai-diagnosis-result` |
| S-49 | `s-49-choose-repair-path` |
| S-50 | `s-50-diy-tutorial` |
| S-60–63 | community list, café detail, help request (steps + error + summary), confirmation |
| S-70 | `s-70-not-worth-repairing` |
| S-80 | outcome steps 1–2 + summary |
| S-90 | `s-90-repair-history-list` |
| S-100–101 | profile + edit profile (steps + error + summary) |
| S-110 | `s-110-settings` |

## Compliance

See `docs/lofi_compliance.md` and `DESIGN.md` (margin **24**, gutter **16**, 8px object spacing, form rules).

## Figma

**Figma:** https://www.figma.com/design/2fP7Qoa2u4KP5PR7hklFVJ (see `docs/figma_lofi_import.md`). HTML uses **inlined** `shared.css` so imports are styled.

**Flow board (PNG + strelice):**
- Putanje: `design/lofi/flow-board-paths.md`
- Pregled: otvori `design/lofi/flow-board.html` u browseru
- Screenshot: `design/lofi/flow-board-preview.png`
