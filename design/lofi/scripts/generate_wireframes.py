#!/usr/bin/env python3
"""Generate HCI-compliant Lo-Fi wireframes (v05/v06) for PatchUp."""

from __future__ import annotations

import html
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_DIR = ROOT / "html"
HTML_DIR.mkdir(parents=True, exist_ok=True)
SHARED_CSS = (ROOT / "wireframes" / "shared.css").read_text(encoding="utf-8")


def page(screen_id: str, title: str, body: str, *, back: bool = False, subtitle: str = "") -> str:
    back_el = '<p class="back">Back</p>' if back else ""
    sub_el = f'<p class="subtitle">{html.escape(subtitle)}</p>' if subtitle else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{html.escape(screen_id)} · {html.escape(title)}</title>
  <style>
{SHARED_CSS}
  </style>
</head>
<body>
  <div class="screen">
    <span class="screen-id">{html.escape(screen_id)}</span>
    <header class="topbar">
      {back_el}
      <h1>{html.escape(title)}</h1>
      {sub_el}
    </header>
    {body}
  </div>
</body>
</html>
"""


def input_frame(label: str, value: str, *, error: bool = False, err_msg: str = "", hint: str = "", numeric: bool = False) -> str:
    cls = "input-frame error" if error else "input-frame"
    type_note = ' <span class="field-hint">(numeric keypad)</span>' if numeric else ""
    err = f'<p class="note-strong">{html.escape(err_msg)}</p>' if err_msg else ""
    hint_el = f'<p class="field-hint">{html.escape(hint)}</p>' if hint else ""
    return f"""
    <p class="label">{html.escape(label)}{type_note}</p>
    <div class="{cls}" data-figma-name="Input / {html.escape(label)}">
      <div class="field">{html.escape(value)}</div>
      {hint_el}
    </div>
    {err}
"""


def btn_primary(text: str, *, disabled: bool = False) -> str:
    cls = "btn btn-primary disabled" if disabled else "btn btn-primary"
    dis = " disabled" if disabled else ""
    return f'<button type="button" class="{cls}"{dis} data-figma-name="Button / Primary">{html.escape(text)}</button>'


def btn_secondary(text: str) -> str:
    return f'<button type="button" class="btn btn-secondary" data-figma-name="Button / Secondary">{html.escape(text)}</button>'


SCREENS: list[dict] = [
    {
        "id": "S-00",
        "slug": "s-00-welcome",
        "title": "Welcome",
        "body": """
    <div class="placeholder-img" style="width:80px;aspect-ratio:1;margin:16px auto 8px" data-figma-name="Image / Logo placeholder">Logo placeholder</div>
    <p class="lead" style="max-width:none;text-align:center">AI-assisted repair guidance for broken household items.</p>
    <div class="spacer"></div>
    """ + btn_primary("Continue"),
    },
    {
        "id": "S-01",
        "slug": "s-01-account-check",
        "title": "Account",
        "body": """
    <p class="lead">Do you already have a PatchUp account?</p>
    <div class="spacer"></div>
    """ + btn_secondary("I have an account") + btn_secondary("I don't have an account"),
    },
    {
        "id": "S-10",
        "slug": "s-10-sign-in",
        "title": "Sign in",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    """ + input_frame("Email", "you@example.com")
    + input_frame("Password", "Password")
    + """<div class="spacer"></div>"""
    + btn_primary("Sign in", disabled=True)
    + '<button type="button" class="btn btn-text">Forgot password?</button>'
    + '<button type="button" class="btn btn-text">Create account</button>',
    },
    {
        "id": "S-20",
        "slug": "s-20-registration-method",
        "title": "Create account",
        "back": True,
        "body": """
    <p class="lead">Choose how to sign up.</p>
    """ + btn_secondary("Sign up with Google")
    + btn_secondary("Sign up with Facebook")
    + btn_secondary("Email and password"),
    },
    {
        "id": "S-23",
        "slug": "s-23-registration-step-1",
        "title": "Create account",
        "subtitle": "Step 1 of 3",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    """ + input_frame("Name", "Your name")
    + input_frame("Email", "you@example.com")
    + """<div class="spacer"></div>"""
    + btn_primary("Next", disabled=True)
    + btn_secondary("Back"),
    },
    {
        "id": "S-23-err",
        "slug": "s-23-step-1-error-state",
        "title": "Create account",
        "subtitle": "Step 1 of 3 · Error after Next",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    """ + input_frame("Name", "Your name", error=True, err_msg="Please enter your name.")
    + input_frame("Email", "you@example.com", error=True, err_msg="Please enter a valid email.")
    + """<div class="spacer"></div>"""
    + btn_primary("Next")
    + btn_secondary("Back"),
    },
    {
        "id": "S-23",
        "slug": "s-23-registration-step-2",
        "title": "Create account",
        "subtitle": "Step 2 of 3",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    """ + input_frame("Password", "Password")
    + input_frame("Confirm password", "Confirm password")
    + """<div class="spacer"></div>"""
    + btn_primary("Next", disabled=True)
    + btn_secondary("Back"),
    },
    {
        "id": "S-23",
        "slug": "s-23-registration-summary",
        "title": "Create account",
        "subtitle": "Summary",
        "back": True,
        "body": """
    <p class="note">Review your details before creating the account.</p>
    <div class="block" data-figma-name="Card / Summary">
      <div class="row"><span class="k">Name</span><span>Alex User</span></div>
      <div class="row"><span class="k">Email</span><span>alex@example.com</span></div>
      <div class="row"><span class="k">Password</span><span>••••••••</span></div>
    </div>
    <div class="success-banner">Everything looks good.</div>
    <div class="spacer"></div>
    """ + btn_primary("Create account")
    + btn_secondary("Back"),
    },
    {
        "id": "S-30",
        "slug": "s-30-home-hub",
        "title": "Home",
        "body": """
    <p class="lead">Scan a broken item to get repair guidance.</p>
    """ + btn_primary("Scan item")
    + """<div class="list-row" style="border:1px solid var(--border);border-radius:8px;padding:12px;margin-top:8px">
      <div class="list-body"><div class="list-title">Repair history</div></div><span class="chevron">›</span></div>
    <div class="list-row" style="border:1px solid var(--border);border-radius:8px;padding:12px;margin-top:8px">
      <div class="list-body"><div class="list-title">Profile</div></div><span class="chevron">›</span></div>
    <div class="list-row" style="border:1px solid var(--border);border-radius:8px;padding:12px;margin-top:8px">
      <div class="list-body"><div class="list-title">Settings</div></div><span class="chevron">›</span></div>""",
    },
    {
        "id": "S-40",
        "slug": "s-40-scan-item",
        "title": "Scan item",
        "back": True,
        "body": """
    <div class="placeholder-img" data-figma-name="Image / Item photo">Photo placeholder · Tap to take photo</div>
    """ + btn_primary("Take photo")
    + btn_secondary("Upload photo"),
    },
    {
        "id": "S-44",
        "slug": "s-44-describe-fault",
        "title": "Describe the problem",
        "back": True,
        "body": """
    <p class="lead">Add a short description to help the system.</p>
    """ + input_frame("What is wrong?", "Describe what is wrong in one or two sentences", hint="Text area")
    + """<div class="spacer"></div>"""
    + btn_primary("Continue", disabled=True),
    },
    {
        "id": "S-43e",
        "slug": "s-43e-error-not-recognized",
        "title": "Could not recognize item",
        "back": True,
        "body": """
    <div class="block block-muted"><p style="font-size:14px">We could not identify the item. Try a clearer photo.</p></div>
    <div class="spacer"></div>
    """ + btn_primary("Try again")
    + btn_secondary("Back"),
    },
    {
        "id": "S-46",
        "slug": "s-46-ai-diagnosis-result",
        "title": "AI diagnosis",
        "back": True,
        "body": """
    <p class="note">System-generated assessment</p>
    <div class="block" data-figma-name="Card / Diagnosis">
      <div class="row"><span class="k">Recognized item</span><span>Table lamp</span></div>
      <div class="row"><span class="k">Likely issue</span><span>Loose wire</span></div>
      <div class="row"><span class="k">Difficulty</span><span>Beginner</span></div>
      <div class="row"><span class="k">Repairability</span><span>Medium</span></div>
      <div class="bar-track"><div class="bar-fill"></div></div>
      <div class="row"><span class="k">Confidence</span><span>Medium</span></div>
      <span class="link">Why this result?</span>
    </div>
    """ + btn_primary("See repair options"),
    },
    {
        "id": "S-49",
        "slug": "s-49-choose-repair-path",
        "title": "Repair options",
        "back": True,
        "body": """
    <p class="lead">Choose the best next step.</p>
    <div class="path-row selected"><div class="path-title">Try it yourself</div><div class="path-desc">Beginner-friendly steps</div></div>
    <div class="path-row"><div class="path-title">Visit repair café</div><div class="path-desc">Local volunteers nearby</div></div>
    <div class="path-row"><div class="path-title">Not worth repairing</div><div class="path-desc">Parts or recycling</div></div>
    """,
    },
    {
        "id": "S-50",
        "slug": "s-50-diy-tutorial",
        "title": "Repair tutorial",
        "back": True,
        "body": """
    <div class="steps">
      <p class="step">1. Unplug the lamp and remove the base cover.</p>
      <p class="step">2. Check wire connections at the switch.</p>
      <p class="step">3. Tighten loose terminals and reassemble.</p>
    </div>
    <p class="note">Safety: disconnect power before opening.</p>
    """ + btn_secondary("Mark step done")
    + btn_secondary("Ask AI for help")
    + btn_primary("Finish tutorial"),
    },
    {
        "id": "S-60",
        "slug": "s-60-community-list",
        "title": "Repair cafés nearby",
        "back": True,
        "body": """
    <div class="list-row"><div class="placeholder-img square">Img</div><div class="list-body"><div class="list-title">Repair Café Novi Sad</div><div class="list-meta">2.1 km · Sat 10:00</div></div><span class="chevron">›</span></div>
    <div class="list-row"><div class="placeholder-img square">Img</div><div class="list-body"><div class="list-title">Community Workshop</div><div class="list-meta">4.5 km</div></div><span class="chevron">›</span></div>
    <div class="list-row"><div class="placeholder-img square">Img</div><div class="list-body"><div class="list-title">Electronics Meetup</div><div class="list-meta">6.0 km</div></div><span class="chevron">›</span></div>
    """,
    },
    {
        "id": "S-61",
        "slug": "s-61-caf-detail",
        "title": "Repair café detail",
        "back": True,
        "body": """
    <div class="placeholder-img">Photo placeholder</div>
    <p style="font-size:14px;font-weight:500;margin-bottom:8px">Repair Café Novi Sad</p>
    <p class="note">Address placeholder · Sat 10:00–14:00</p>
    <p class="note">Skills: lamps, small appliances</p>
    <div class="spacer"></div>
    """ + btn_primary("Request help"),
    },
    {
        "id": "S-62",
        "slug": "s-62-help-request-step-1",
        "title": "Request help",
        "subtitle": "Step 1 of 3",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    """ + input_frame("Message", "Describe your item and issue", hint="Text area")
    + input_frame("Preferred time", "10:30", numeric=True, hint="inputmode=numeric")
    + """<div class="spacer"></div>"""
    + btn_primary("Next", disabled=True)
    + btn_secondary("Back"),
    },
    {
        "id": "S-62-err",
        "slug": "s-62-step-1-error-state",
        "title": "Request help",
        "subtitle": "Step 1 of 3 · Error after Next",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    """ + input_frame("Message", "Describe your item and issue", error=True, err_msg="Please enter a message.")
    + input_frame("Preferred time", "10:30", error=True, err_msg="Please enter a time.", numeric=True)
    + """<div class="spacer"></div>"""
    + btn_primary("Next")
    + btn_secondary("Back"),
    },
    {
        "id": "S-62",
        "slug": "s-62-help-request-step-2",
        "title": "Request help",
        "subtitle": "Step 2 of 3 (optional)",
        "back": True,
        "body": """
    <p class="note">Optional field.</p>
    """ + input_frame("Preferred date", "Select date (optional)")
    + """<div class="spacer"></div>"""
    + btn_primary("Next")
    + btn_secondary("Back"),
    },
    {
        "id": "S-62",
        "slug": "s-62-help-request-summary",
        "title": "Request help",
        "subtitle": "Summary",
        "back": True,
        "body": """
    <p class="note">Review your request before sending.</p>
    <div class="block">
      <div class="row"><span class="k">Message</span><span>Broken lamp, loose wire</span></div>
      <div class="row"><span class="k">Time</span><span>10:30</span></div>
      <div class="row"><span class="k">Date</span><span>—</span></div>
    </div>
    <div class="success-banner">Everything looks good.</div>
  """ + btn_primary("Send request") + btn_secondary("Back"),
    },
    {
        "id": "S-63",
        "slug": "s-63-request-sent-confirmation",
        "title": "Request sent",
        "back": True,
        "body": """
    <div class="block block-muted"><p style="font-size:14px">Your request was sent successfully.</p></div>
    <div class="spacer"></div>
    """ + btn_primary("Back to home")
    + btn_secondary("Record outcome later"),
    },
    {
        "id": "S-70",
        "slug": "s-70-not-worth-repairing",
        "title": "Not worth repairing",
        "back": True,
        "body": """
    <p class="lead">Repair may cost more than the item is worth. Consider parts or recycling.</p>
    """ + btn_secondary("Find recycling info")
    + btn_primary("Back to home"),
    },
    {
        "id": "S-80",
        "slug": "s-80-record-outcome-step-1",
        "title": "Record outcome",
        "subtitle": "Step 1 of 3",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    <p class="lead">Select the outcome.</p>
    """ + btn_secondary("Fixed successfully")
    + btn_secondary("Partially fixed")
    + btn_secondary("Not fixed")
    + """<div class="spacer"></div>"""
    + btn_primary("Next", disabled=True)
    + btn_secondary("Back"),
    },
    {
        "id": "S-80",
        "slug": "s-80-record-outcome-step-2",
        "title": "Record outcome",
        "subtitle": "Step 2 of 3",
        "back": True,
        "body": """
    <p class="note">Optional.</p>
    """ + input_frame("Notes", "Add a short note (optional)", hint="Text area")
    + """<div class="spacer"></div>"""
    + btn_primary("Next")
    + btn_secondary("Back"),
    },
    {
        "id": "S-80",
        "slug": "s-80-outcome-summary",
        "title": "Record outcome",
        "subtitle": "Summary",
        "back": True,
        "body": """
    <p class="note">Review before saving.</p>
    <div class="block">
      <div class="row"><span class="k">Outcome</span><span>Fixed successfully</span></div>
      <div class="row"><span class="k">Notes</span><span>—</span></div>
    </div>
    <div class="success-banner">Everything looks good, saved.</div>
    """ + btn_primary("Save outcome")
    + btn_secondary("Back"),
    },
    {
        "id": "S-90",
        "slug": "s-90-repair-history-list",
        "title": "Repair history",
        "back": True,
        "body": """
    <div class="list-row"><div class="placeholder-img square">Img</div><div class="list-body"><div class="list-title">Table lamp</div><div class="list-meta">12 Mar · Fixed</div></div><span class="chevron">›</span></div>
    <div class="list-row"><div class="placeholder-img square">Img</div><div class="list-body"><div class="list-title">Toaster</div><div class="list-meta">2 Feb · Repair café</div></div><span class="chevron">›</span></div>
    """,
    },
    {
        "id": "S-100",
        "slug": "s-100-profile",
        "title": "Profile",
        "back": True,
        "body": """
    <div class="placeholder-img square" style="width:72px;height:72px;margin:0 auto 8px">Avatar placeholder</div>
    <p style="text-align:center;font-size:14px;font-weight:500">Alex User</p>
    <p style="text-align:center;font-size:12px;color:var(--soft);margin-bottom:16px">alex@example.com</p>
    """ + btn_secondary("Edit profile")
    + '<button type="button" class="btn btn-text">Sign out</button>',
    },
    # S-101 multi-step (HCI: long form split; replaces single Stitch screen)
    {
        "id": "S-101",
        "slug": "s-101-edit-profile-step-1",
        "title": "Edit profile",
        "subtitle": "Step 1 of 3",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    """ + input_frame("Name", "Alex User")
    + input_frame("Email", "alex@example.com")
    + """<div class="spacer"></div>"""
    + btn_primary("Next", disabled=True)
    + btn_secondary("Back"),
    },
    {
        "id": "S-101-err",
        "slug": "s-101-edit-profile-step-1-error",
        "title": "Edit profile",
        "subtitle": "Step 1 of 3 · Error after Next",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    """ + input_frame("Name", "Alex User", error=True, err_msg="Please enter your name.")
    + input_frame("Email", "alex@example.com", error=True, err_msg="Please enter a valid email.")
    + """<div class="spacer"></div>"""
    + btn_primary("Next")
    + btn_secondary("Back"),
    },
    {
        "id": "S-101",
        "slug": "s-101-edit-profile-step-2",
        "title": "Edit profile",
        "subtitle": "Step 2 of 3",
        "back": True,
        "body": """
    <p class="note">All fields are required.</p>
    """ + input_frame("Phone", "+381 6X XXX XXXX", numeric=True, hint="type=tel, inputmode=numeric")
    + """<div class="spacer"></div>"""
    + btn_primary("Next", disabled=True)
    + btn_secondary("Back"),
    },
    {
        "id": "S-101",
        "slug": "s-101-edit-profile-summary",
        "title": "Edit profile",
        "subtitle": "Summary",
        "back": True,
        "body": """
    <p class="note">Review your changes before saving.</p>
    <div class="block">
      <div class="row"><span class="k">Name</span><span>Alex User</span></div>
      <div class="row"><span class="k">Email</span><span>alex@example.com</span></div>
      <div class="row"><span class="k">Phone</span><span>+381 6X XXX XXXX</span></div>
    </div>
    <div class="success-banner">Everything looks good, saved.</div>
    """ + btn_primary("Save")
    + btn_secondary("Back"),
    },
    {
        "id": "S-110",
        "slug": "s-110-settings",
        "title": "Settings",
        "back": True,
        "body": """
    <div class="toggle-row"><span>Notifications</span><div class="toggle"></div></div>
    <div class="toggle-row"><span>Location for nearby cafés</span><div class="toggle"></div></div>
    <div class="toggle-row" style="border:none"><span>Save diagnosis history</span><div class="toggle"></div></div>
    """,
    },
]


def main() -> None:
    manifest = {
        "source": "HCI-compliant wireframes (v05/v06)",
        "basedOn": "Stitch project 17554208072889623118",
        "exportedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "grid": {"columns": 4, "margin": 24, "gutter": 16, "objectSpacing": 8},
        "screens": [],
    }
    for s in SCREENS:
        content = page(
            s["id"],
            s["title"],
            s["body"],
            back=s.get("back", False),
            subtitle=s.get("subtitle", ""),
        )
        path = HTML_DIR / f"{s['slug']}.html"
        path.write_text(content, encoding="utf-8")
        manifest["screens"].append(
            {
                "id": s["id"],
                "slug": s["slug"],
                "title": s["title"],
                "html": f"html/{s['slug']}.html",
            }
        )
        print(f"Wrote {s['slug']}.html")

    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\nTotal: {len(SCREENS)} screens")


if __name__ == "__main__":
    main()
