// PatchUp Lo-Fi — set all prototype links (Navigate to) on current page.
// Run: Plugins → Development → PatchUp — Prototype Links

const FILE_EDGES = [
  ["S-00", null, "S-01"],
  ["S-01", "I have an account", "S-10"],
  ["S-01", "I don't have an account", "S-20"],
  ["S-10", "Sign in", "S-30"],
  ["S-10", null, "S-30"],
  ["S-20", "Email", "S-23a"],
  ["S-20", null, "S-23a"],
  ["S-23a", "Next", "S-23b"],
  ["S-23b", "Next", "S-23c"],
  ["S-23c", "Create", "S-30"],
  ["S-30", "Scan", "S-40"],
  ["S-30", "Repair history", "S-90"],
  ["S-30", "history", "S-90"],
  ["S-30", "Profile", "S-100"],
  ["S-30", "Settings", "S-110"],
  ["S-40", "Take photo", "S-44"],
  ["S-40", "Upload", "S-44"],
  ["S-40", null, "S-44"],
  ["S-44", "Continue", "S-46"],
  ["S-44", null, "S-46"],
  ["S-46", "repair", "S-49"],
  ["S-46", "See repair", "S-49"],
  ["S-46", null, "S-49"],
  ["S-49", "yourself", "S-50"],
  ["S-49", "Try it", "S-50"],
  ["S-49", "caf", "S-60"],
  ["S-49", "Visit", "S-60"],
  ["S-49", "Not worth", "S-70"],
  ["S-50", "Finish", "S-80a"],
  ["S-60", null, "S-61"],
  ["S-61", "Request help", "S-62a"],
  ["S-61", "Request", "S-62a"],
  ["S-62a", "Next", "S-62b"],
  ["S-62b", "Next", "S-62c"],
  ["S-62c", "Send", "S-63"],
  ["S-63", "Back to home", "S-30"],
  ["S-63", "home", "S-30"],
  ["S-63", "Record outcome", "S-80a"],
  ["S-63", "outcome", "S-80a"],
  ["S-70", "Back to home", "S-30"],
  ["S-70", "home", "S-30"],
  ["S-70", null, "S-30"],
  ["S-80a", "Next", "S-80b"],
  ["S-80b", "Next", "S-80c"],
  ["S-80c", "Save", "S-90"],
  ["S-80c", null, "S-30"],
  ["S-100", "Edit profile", "S-101a"],
  ["S-100", "Edit", "S-101a"],
  ["S-101a", "Next", "S-101b"],
  ["S-101b", "Next", "S-101c"],
  ["S-101c", "Save", "S-100"],
  ["S-90", null, "S-30"],
  ["S-110", null, "S-30"],
];

const ERROR_EDGES = [
  ["S-23a", "Next", "S-23a-err"],
  ["S-23a-err", null, "S-23a"],
  ["S-43e", "Try again", "S-40"],
  ["S-62a", "Next", "S-62a-err"],
  ["S-62a-err", null, "S-62a"],
  ["S-101a", "Next", "S-101a-err"],
  ["S-101a-err", null, "S-101a"],
];

const SCREEN_ORDER = [
  "S-00", "S-01", "S-10", "S-20", "S-23a", "S-23a-err", "S-23b", "S-23c",
  "S-30", "S-40", "S-44", "S-43e", "S-46", "S-49", "S-50", "S-60", "S-61",
  "S-62a", "S-62a-err", "S-62b", "S-62c", "S-63", "S-70",
  "S-80a", "S-80b", "S-80c", "S-90", "S-100",
  "S-101a", "S-101a-err", "S-101b", "S-101c", "S-110",
];

function navReaction(destId) {
  return {
    trigger: { type: "ON_CLICK" },
    actions: [
      {
        type: "NODE",
        destinationId: destId,
        navigation: "NAVIGATE",
        transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.2 },
      },
    ],
  };
}

function getTopFrames(page) {
  return page.children.filter((n) => n.type === "FRAME" || n.type === "COMPONENT");
}

function buildIdMap(topFrames) {
  const idMap = {};
  const unmapped = [];

  for (const f of topFrames) {
    const m = f.name.match(/S-\d+[a-z]*(?:-err)?/);
    if (m) {
      if (!idMap[m[0]]) idMap[m[0]] = f.id;
    } else {
      unmapped.push(f);
    }
  }

  unmapped.sort((a, b) => a.x - b.x || a.y - b.y);
  let i = 0;
  for (const sid of SCREEN_ORDER) {
    if (!idMap[sid] && i < unmapped.length) {
      idMap[sid] = unmapped[i++].id;
    }
  }

  return idMap;
}

function frameForScreenId(topFrames, sid) {
  const f = topFrames.find(
    (n) =>
      n.name.startsWith(sid + " ") ||
      n.name === sid ||
      n.name.startsWith(sid + "·") ||
      n.name.includes(" " + sid + " ")
  );
  return f || topFrames.find((n) => n.name.includes(sid));
}

function findByLabel(root, label) {
  if (!label) return root;
  const needle = label.toLowerCase();
  const texts = root.findAll(
    (n) => n.type === "TEXT" && n.characters && n.characters.toLowerCase().includes(needle)
  );
  for (const t of texts) {
    let p = t.parent;
    while (p && p !== root) {
      if (p.type === "FRAME" || p.type === "INSTANCE" || p.type === "COMPONENT") return p;
      p = p.parent;
    }
  }
  return null;
}

async function applyEdge(page, topFrames, idMap, edge, applied, skipped) {
  const [fromSid, label, toSid] = edge;
  const fromFrame = frameForScreenId(topFrames, fromSid);
  const toId = idMap[toSid];
  if (!fromFrame || !toId) {
    skipped.push({ fromSid, label, toSid });
    return;
  }
  const target = findByLabel(fromFrame, label) || fromFrame;
  await target.setReactionsAsync([navReaction(toId)]);
  applied.push({ from: fromSid, to: toSid, label: label || "(frame)" });
}

(async () => {
  const page = figma.currentPage;
  const topFrames = getTopFrames(page);
  const idMap = buildIdMap(topFrames);
  const applied = [];
  const skipped = [];

  for (const e of FILE_EDGES) await applyEdge(page, topFrames, idMap, e, applied, skipped);
  for (const e of ERROR_EDGES) await applyEdge(page, topFrames, idMap, e, applied, skipped);

  const startFrame = frameForScreenId(topFrames, "S-00");
  if (startFrame) {
    page.prototypeStartNode = startFrame;
  }

  const msg =
    `Prototype: ${applied.length} linkova.\n` +
    (skipped.length ? `Preskočeno: ${skipped.length} (proveri imena frame-ova S-XX).\n` : "") +
    (startFrame ? "Start: S-00" : "Upozorenje: S-00 nije pronađen za start.");

  figma.closePlugin(msg);
})();
