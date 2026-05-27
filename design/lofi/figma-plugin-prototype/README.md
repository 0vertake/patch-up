# PatchUp — Figma plugin (prototype links)

Postavlja **On click → Navigate to** za ceo Lo-Fi flow (kao ručni primer S-00 → S-01).

## Instalacija (jednom)

1. Otvori https://www.figma.com/design/2fP7Qoa2u4KP5PR7hklFVJ
2. **Plugins** → **Development** → **Import plugin from manifest…**
3. Izaberi: `design/lofi/figma-plugin-prototype/manifest.json`

## Pokretanje

1. Otvori stranicu sa svim ekranima
2. **Plugins** → **Development** → **PatchUp — Prototype Links**
3. Sačekaj poruku (npr. „Prototype: 45 linkova”)
4. **Prototype** tab → proveri start na **S-00** → **Present** ▶

## Imena frame-ova

Najbolje: `S-00 · Welcome`, `S-30 · Home`, …

Ako su frame-ovi još uvek samo **Container**, plugin ih mapira **redom sleva nadesno** prema `SCREEN_ORDER` u `code.js`.

## MCP

Agent ne može trenutno koristiti `use_figma` (Starter **View**, 6 poziva/mesec). Plugin radi isto lokalno u Figmi.
