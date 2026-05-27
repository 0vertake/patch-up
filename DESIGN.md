---
name: PatchUp
description: Mobile-first AI-assisted community repair guidance (Lo-Fi prototype phase)
colors:
  canvas: "#f2f2f2"
  surface: "#ffffff"
  surface-muted: "#ebebeb"
  border: "#d4d4d4"
  border-strong: "#a3a3a3"
  text-primary: "#1c1c1c"
  text-secondary: "#5c5c5c"
  text-placeholder: "#8a8a8a"
  fill-primary: "#2b2b2b"
  fill-secondary: "#ffffff"
  fill-disabled: "#e5e5e5"
  state-error: "#6b6b6b"
  state-success: "#4a4a4a"
typography:
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", system-ui, sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "normal"
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: "normal"
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "normal"
rounded:
  sm: "4px"
  md: "8px"
  lg: "12px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
components:
  button-primary:
    backgroundColor: "{colors.fill-primary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: "12px 20px"
  button-secondary:
    backgroundColor: "{colors.fill-secondary}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.md}"
    padding: "12px 20px"
  input-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
---

# Design System: PatchUp

## Overview

**Creative North Star: "The Neighbor's Workbench"**

PatchUp is a **product** (mobile app UI), not a marketing site. The current design phase is **low-fidelity (Lo-Fi)**, aligned with HCI coursework (v04–v06): structure, layout, hierarchy, navigation, and primary actions matter more than visual polish.

The interface should feel **practical, calm, and trustworthy**: a non-expert with a broken household item should understand what to do next without feeling sold to or overwhelmed by technology. AI diagnosis is visible and explained; community repair (DIY, repair café, volunteer) is presented as support, not as a cold marketplace.

**Physical scene (drives layout and tone):** Someone at home, often in average indoor light, anxious about a broken lamp or small appliance, phone in one hand, wanting a clear answer in under a minute: *Can I fix this? Is it worth it? Who can help nearby?*

**Workshop alignment (what Lo-Fi must demonstrate):**

| Source | What it enforces in this file |
|--------|------------------------------|
| v04 Prototype & DTI | Wireframes = structure only; flow before pixels |
| v05 Lo-Fi spec | No color, no final images, no decoration; placeholders; realistic labels; clear button names |
| v05 Layout & hierarchy | Single-column mobile layouts; card lists where scanning matters; 3-level type scale; grouping and whitespace |
| v06 Figma basics | One **Frame** per screen (375px mobile); **4-column grid**; **8px spacing** system; **Auto Layout** for stacks and forms |

**Hi-fi note:** Brand color, photography, and motion are **out of scope** until after Lo-Fi sign-off. Section 2 documents grayscale tokens only; a future pass may add a restrained green/teal accent tied to repair and sustainability.

**Key characteristics:**

- Mobile-first, single-column screens with vertical scroll
- Lo-Fi grayscale only (contrast through tone, not hue)
- Realistic copy on every control (no "Lorem ipsum" on primary actions)
- Image areas as labeled placeholders (camera upload, item photo, avatar)
- Diagnosis and repair paths as **grouped information blocks**, not decorative cards-for-everything
- Figma: Frames (not Groups) for screens; consistent margins and gutters per v06

**Screen inventory:** See `docs/patchup_app_flow.md` (IDs `S-00` … `S-110`).

**Canonical Lo-Fi assets:** `design/lofi/html/` and `design/lofi/screenshots/` (exported from Google Stitch). See `design/lofi/manifest.json`. Compliance checklist: `docs/lofi_compliance.md`.

---

## Colors

This palette is **normative for the Lo-Fi prototype phase only**. Do not introduce brand hues, gradients, or status colors until hi-fi.

### Primary (interaction emphasis in grayscale)

- **Workbench Charcoal** (`#2b2b2b`): Primary buttons, key CTAs (*Scan item*, *Continue*, *Send request*). The darkest interactive fill on any screen.

### Neutral (surfaces and structure)

- **Paper White** (`#ffffff`): Main screen background inside the phone frame.
- **Bench Gray** (`#f2f2f2`): Figma canvas / outer artboard background (not inside app UI).
- **Muted Fill** (`#ebebeb`): Placeholder image blocks, disabled fields, secondary panels.
- **Hairline Border** (`#d4d4d4`): Input outlines, dividers, card borders in Lo-Fi.
- **Strong Border** (`#a3a3a3`): Focused or emphasized containers when a second border weight is needed.

### Text

- **Ink** (`#1c1c1c`): Headings and primary body.
- **Soft Ink** (`#5c5c5c`): Supporting text, metadata, helper lines.
- **Placeholder** (`#8a8a8a`): Input placeholder text and "Image placeholder" labels.

### Named Rules

**The Grayscale-Only Rule.** Until hi-fi, every fill and stroke is a neutral gray. No green "success", no red "error", no blue links. Communicate state with labels, icons (simple line), border weight, and layout, not color.

**The One Dark Fill Rule.** At most one dark gray (`#2b2b2b`) primary action per screen. Secondary actions use white fill + border. Tertiary actions are text-only.

**The No Pure Black/White Rule.** Do not use `#000000` or `#ffffff` as text on large fields without borders; pair `#1c1c1c` on `#ffffff` for body copy.

---

## Typography

**Display / Title font:** System UI stack (`-apple-system`, `Segoe UI`, `system-ui`, sans-serif)  
**Body font:** Same stack (one family for Lo-Fi; no display pairing yet)  
**Label font:** Same stack, medium weight for buttons and field labels

**Character:** Neutral, readable, slightly compact. Optimized for quick scanning by non-experts. No decorative or technical/monospace styling in Lo-Fi.

### Hierarchy (max 3 sizes on any screen, per workshop)

- **Title** (600 weight, 20px, line-height 1.25): Screen titles (*Home*, *Scan item*, *AI diagnosis*). One per screen.
- **Body** (400 weight, 16px, line-height 1.5, max ~40ch per paragraph): Explanations, diagnosis text, form labels. Primary reading size.
- **Label** (500 weight, 14px): Button labels, field labels, list row titles.
- **Caption** (400 weight, 12px): Timestamps, confidence hints, legal/helper lines. Use sparingly.

### Named Rules

**The Three-Size Rule.** Never use more than three distinct font sizes on one screen (Title / Body / Label or Caption counts as one step). Hierarchy comes from weight and spacing first.

**The Real Words Rule.** Buttons and nav items use action verbs or clear nouns: *Scan item*, *Continue*, *Request help*, not *Submit* or *OK* without context.

**The Line-Length Rule.** Body blocks cap at ~65–75 characters where possible; diagnosis explanations may use full width but break into short paragraphs.

---

## Elevation

Lo-Fi is **flat by default**. Depth is shown through **layout and grouping**, not shadows.

- **No drop shadows** on cards, buttons, or modals in Lo-Fi.
- **Separation:** 1px `#d4d4d4` borders or `#ebebeb` background blocks inside white screens.
- **Modals / sheets (if shown):** Full-width panel with top border only, or simple centered box with border, no blur.

### Named Rules

**The Flat-By-Default Rule.** If you reach for a shadow, use a border or background tint instead.

**The Squint Test Rule.** Blur the frame mentally: the primary CTA and screen title must still read as the two darkest/largest shapes.

---

## Components

All measurements assume **375×812** mobile frame, **24px** side margins, **16px** gutter, **4-column** layout grid, and an **8px** object spacing baseline (HCI defense rules). Use **Auto Layout** vertical stacks with **8px** gaps by default; use 16/24 only for section separation.

### Figma structure (v06)

- **One Frame = one screen** (e.g. `S-30 Home`). Name frames with screen ID from flow doc.
- **Never use Group** for screens; use Frame for constraints and layout grid.
- **Layout grid on each screen (mobile):** 4 columns, margin **24px**, gutter **16px**.
- **Layer naming (HCI):** rectangles/frames must be named by role, e.g. `Input / Email`, `Button / Primary`, `Card / Diagnosis`, not `Rectangle 12`.
- **Placeholder images:** Rectangle `#ebebeb` + centered Caption label (*Photo placeholder*, *Item image*).
- **Inputs/search bars:** build as a **Frame** (container) so internal alignment is easy; prefer Auto Layout inside.
- **Corner radius:** one value everywhere (recommended: 8px). Do not mix radii across controls.

### Buttons

- **Shape:** Medium corner radius (8px).
- **Primary:** Fill `#2b2b2b`, text `#ffffff`, Label 14px medium, min height 44px, full-width on mobile for main actions.
- **Secondary:** Fill `#ffffff`, 1px border `#d4d4d4`, text `#1c1c1c`.
- **Text / tertiary:** No fill; Label 14px, underline optional for *Forgot password?*
- **States in Lo-Fi:** Annotate with text note (*Error state*) or duplicate frame; do not rely on red/green.

### Inputs / fields

- **Style:** White fill, 1px `#d4d4d4` border, 8px radius, 12px vertical padding.
- **Placeholder:** `#8a8a8a` sample text (*Describe the problem in one sentence*).
- **Focus (Lo-Fi):** 2px `#a3a3a3` border (document in annotation or variant frame).

### Navigation

- **Top bar:** Title centered or left; back chevron left; optional text action right (*Skip*, *Help*). Height ~56px including safe area note.
- **Home hub:** Primary action as full-width button below short intro; secondary actions as list rows or second button, not five equal tiles.

### Image / media placeholders

- **Aspect ratio:** 4:3 or 1:1 for item photo; 16:9 only for hero if needed.
- **Label inside:** Caption *Tap to take photo* or *Upload image*.
- **No stock photos** in Lo-Fi.

### Diagnosis block (signature pattern)

Grouped block (border or muted background), not a floating card stack:

1. **Row:** Label *Recognized item* + value (*Table lamp*)
2. **Row:** *Likely issue* + value
3. **Row:** *Difficulty* + value (*Beginner / Moderate / Advanced*)
4. **Row:** *Repairability* + value (text or simple bar placeholder in gray)
5. **Row:** *Confidence* + value (*Medium*) + optional link *Why this result?*
6. **Primary CTA** below block: *See repair options*

Use **proximity grouping** (v05): labels and values closer to each other than to the next group.

### List rows (repair cafés, history)

- **Card layout (v05 #7):** One row per item: left placeholder 48×48, title + 1–2 caption lines, right chevron or *Details* text button.
- **Spacing:** 16px between rows; optional 1px divider instead of nested cards.

### Repair path options

- Three **stacked selectable rows** (not three identical marketing cards): title (*Try it yourself*, *Visit repair café*, *Not worth repairing*) + one-line description + radio or chevron.
- Selected state in Lo-Fi: `#ebebeb` background or thicker border, not color.

### Forms (sign-in, help request)

- **One column on mobile.** Fields stack vertically.
- **No asterisks by default.** If all fields are required, write a single line at the top: *All fields are required.*
- **Long/scrollable forms must be multi-step.** Use Step 1 → Step 2 → **Summary** (review all entered values) → Submit.
- **Validation timing:** do not show field errors immediately. Show errors only **after the user presses Next/Continue**.
- **Primary CTA enablement:** keep the primary CTA disabled until all required fields in the current step are valid.
- **Success feedback:** after the final step, show a confirmation line such as *Everything looks good, saved.*
- **Numeric keypad:** numeric fields must open a numeric keypad (phone, time slot, counts).
  - In specs, call out `inputmode="numeric"` / `type="tel"` (or platform equivalent).
- Show field labels above inputs (Label 14px), not only placeholders.

### Error / empty states

- Dedicated frames: icon placeholder (simple rectangle or ×), Title + Body explanation, one recovery action (*Try again*, *Go back*).

### Prototype linking

- Link frames following `docs/patchup_app_flow_en.md` transitions.
- Decision screens may be separate frames or notes; Lo-Fi does not require animated transitions.

---

## Do's and Don'ts

Grounded in workshop Lo-Fi rules (v05), wireframe practice (v04), Figma workflow (v06), and PatchUp product intent (`patchup_project_prompt.md`).

### Do:

- **Do** keep every Lo-Fi screen **grayscale** with the tokens in the frontmatter.
- **Do** use **realistic, domain-specific copy** (*Scan broken item*, *Repair café nearby*, *Mark as fixed*).
- **Do** use **image placeholders** with a short label, never final photography.
- **Do** design **mobile-first** at **375px** width with a **4-column grid** (margin 24px, gutter 16px).
- **Do** use **Frames + Auto Layout** for all screens and repeating components.
- **Do** apply the **8px spacing scale** (8, 16, 24, 32, 48) for padding and gaps.
- **Do** limit typography to **three sizes per screen** and establish hierarchy with weight and spacing.
- **Do** group related diagnosis fields in **one block** with clear labels.
- **Do** make **one primary action** obvious per screen (darkest button, full width when appropriate).
- **Do** align screens to **`docs/patchup_app_flow_en.md`** so DTI, HTA, and Lo-Fi stay consistent.
- **Do** leave whitespace so blocks "breathe" (v05 grouping); give the diagnosis block more padding than secondary metadata.

### Don't:

- **Don't** use **brand colors, gradients, or decorative illustrations** in Lo-Fi (course requirement).
- **Don't** use **final photos, icons packs, or emoji** as UI decoration.
- **Don't** use **lorem ipsum** on primary buttons, navigation, or diagnosis labels.
- **Don't** build **nested cards** (card inside card) or identical **icon + title + text** grids repeated endlessly.
- **Don't** use **colored left stripes** on list items or alerts (shared design ban; use full border or background tint).
- **Don't** use **gradient text** or **glass/blur** effects.
- **Don't** design PatchUp as a **cold service marketplace** (aggressive pricing, star ratings as hero, gig-economy tone).
- **Don't** hide the **AI role**: diagnosis must be labeled as system output with confidence, not magic copy.
- **Don't** use **Groups instead of Frames** for screens (breaks grid, constraints, and prototype structure).
- **Don't** rely on **color alone** for errors, success, or selection in Lo-Fi.
- **Don't** add **drop shadows** in Lo-Fi; use borders and spacing.
- **Don't** put more than **two** large Title-level elements competing on one screen.

---

*Aligned with: `docs/vezbe/` (v04–v06), `docs/patchup_app_flow_en.md`, `patchup_project_prompt.md`. Re-run `/impeccable document` in scan mode after hi-fi implementation to extract real tokens from code.*
