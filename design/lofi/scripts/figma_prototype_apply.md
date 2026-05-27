# Figma prototype — Navigate to

**File:** https://www.figma.com/design/2fP7Qoa2u4KP5PR7hklFVJ  
**Putanje:** `design/lofi/flow-board-paths.md`

## Brzo (preporučeno) — Figma plugin

MCP `use_figma` je na **View** limitu. Umesto toga pokreni plugin (30 s):

→ `design/lofi/figma-plugin-prototype/README.md`

---

## Alternativa — MCP `use_figma` (kad limit dozvoljava)

## Kako radi

1. Pronalazi **top-level Frame** po imenu (`S-00`, `S-30`, …).
2. **Linearan tok:** `ON_CLICK` na ceo frame → **Navigate to** destinacija (`navigation: 'NAVIGATE'`).
3. **Grane:** traži dugme po tekstu unutra (npr. „I have an account”) i vezuje hotspot, ne ceo ekran.

## MCP poziv (jedan `use_figma`)

Kopiraj `code` ispod u `use_figma` sa `fileKey: "2fP7Qoa2u4KP5PR7hklFVJ"` i `skillNames: "figma-use"`.

```javascript
const FILE_EDGES = [
  ["S-00", null, "S-01"],
  ["S-01", "I have an account", "S-10"],
  ["S-01", "I don't have an account", "S-20"],
  ["S-10", "Sign in", "S-30"],
  ["S-10", null, "S-30"],
  ["S-20", "Email and password", "S-23a"],
  ["S-20", null, "S-23a"],
  ["S-23a", "Next", "S-23b"],
  ["S-23b", "Next", "S-23c"],
  ["S-23c", "Create account", "S-30"],
  ["S-30", "Scan item", "S-40"],
  ["S-30", "Repair history", "S-90"],
  ["S-30", "Profile", "S-100"],
  ["S-30", "Settings", "S-110"],
  ["S-40", "Take photo", "S-44"],
  ["S-40", "Continue", "S-44"],
  ["S-40", null, "S-44"],
  ["S-44", "Continue", "S-46"],
  ["S-44", null, "S-46"],
  ["S-46", "See repair options", "S-49"],
  ["S-46", null, "S-49"],
  ["S-49", "Try it yourself", "S-50"],
  ["S-49", "Visit repair", "S-60"],
  ["S-49", "Not worth", "S-70"],
  ["S-50", "Finish", "S-80a"],
  ["S-60", null, "S-61"],
  ["S-61", "Request help", "S-62a"],
  ["S-62a", "Next", "S-62b"],
  ["S-62b", "Next", "S-62c"],
  ["S-62c", "Send request", "S-63"],
  ["S-63", "Back to home", "S-30"],
  ["S-63", "Record outcome", "S-80a"],
  ["S-70", "Back to home", "S-30"],
  ["S-70", null, "S-30"],
  ["S-80a", "Next", "S-80b"],
  ["S-80b", "Next", "S-80c"],
  ["S-80c", "Save", "S-90"],
  ["S-80c", null, "S-30"],
  ["S-100", "Edit profile", "S-101a"],
  ["S-101a", "Next", "S-101b"],
  ["S-101b", "Next", "S-101c"],
  ["S-101c", "Save", "S-100"],
  ["S-90", null, "S-30"],
  ["S-110", null, "S-30"],
];

const ERROR_EDGES = [
  ["S-23a", "Next", "S-23a-err"],
  ["S-43e", "Try again", "S-40"],
  ["S-62a", "Next", "S-62a-err"],
  ["S-101a", "Next", "S-101a-err"],
];

function navReaction(destId) {
  return {
    trigger: { type: "ON_CLICK" },
    actions: [{
      type: "NODE",
      destinationId: destId,
      navigation: "NAVIGATE",
      transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.2 },
    }],
  };
}

const page = figma.currentPage;
const topFrames = page.children.filter((n) => n.type === "FRAME");

function frameForScreenId(sid) {
  const exact = topFrames.find((f) => f.name.startsWith(sid + " ") || f.name === sid || f.name.includes(" · " + sid));
  if (exact) return exact;
  return topFrames.find((f) => f.name.includes(sid));
}

function findByLabel(root, label) {
  if (!label) return root;
  const texts = root.findAll((n) => n.type === "TEXT" && n.characters && n.characters.toLowerCase().includes(label.toLowerCase()));
  for (const t of texts) {
    let p = t.parent;
    while (p && p !== root) {
      if (p.type === "FRAME" || p.type === "INSTANCE" || p.type === "COMPONENT") return p;
      p = p.parent;
    }
  }
  return null;
}

const idMap = {};
for (const f of topFrames) {
  const m = f.name.match(/^(S-\d+[a-z]*(?:-err)?)/);
  if (m) idMap[m[1]] = f.id;
}

const applied = [];
const skipped = [];

async function applyEdge([fromSid, label, toSid]) {
  const fromFrame = frameForScreenId(fromSid);
  const toId = idMap[toSid];
  if (!fromFrame || !toId) {
    skipped.push({ fromSid, label, toSid, reason: "missing frame" });
    return;
  }
  const target = findByLabel(fromFrame, label) || fromFrame;
  await target.setReactionsAsync([navReaction(toId)]);
  applied.push({ from: fromFrame.name, label: label || "(frame)", to: toSid, nodeId: target.id });
}

for (const e of FILE_EDGES) await applyEdge(e);
for (const e of ERROR_EDGES) await applyEdge(e);

const start = frameForScreenId("S-00");
if (start) page.prototypeStartNode = start;

return {
  page: page.name,
  frameCount: topFrames.length,
  idMap,
  appliedCount: applied.length,
  skipped,
  sampleApplied: applied.slice(0, 8),
  prototypeStart: start ? start.name : null,
};
```

## Posle pokretanja

1. U Figmi: **Prototype** tab → proveri da je **S-00** start (play ikona).
2. **Present** (▶) → klik po flow-u.
3. Ako neki link ne radi: frame ime mora počinjati sa `S-XX` (npr. `S-30 · Home`).

## Limitacija (Starter View)

`use_figma` / `get_metadata` su limitirani (~6 read/mesec). `upload_assets` / `create_new_file` nisu.

Kad limit padne, agent ponovo pokrene gornji `use_figma` blok.

## Ako si već ručno povezao S-00 → S-01

Skripta **prepisuje** `reactions` na target nodu. Za S-00 možeš izbaciti prvi red iz `FILE_EDGES` ili posle run-a ručno dodati samo grane koje skripta nije pogodila.
