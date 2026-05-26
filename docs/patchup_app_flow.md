# PatchUp — Application Flow (MVP)

This document describes the **complete application flow** for the lo-fi prototype. It contains **flow only** (screens, decisions, transitions, branches). It does not define visual design, components, copy text, or layout.

**Sources:** `patchup_project_prompt.md`, DTI/HTA on the FigJam board *PatchUp*, suggested MVP screens from the project brief.

**MVP focus:** primary user (*everyday user* — someone with a broken item and little or no technical knowledge). Volunteer and event-organizer flows are **not** part of this MVP flow (may be added later).

**Platform:** mobile app (mobile-first).

---

## 1. Overview of main flows

| ID | Flow | Short description |
|----|------|-------------------|
| F0 | App entry | First launch, account check |
| F1 | Registration | Account creation |
| F2 | Sign in | Login + forgot password |
| F3 | Home (hub) | Central navigation |
| F4 | Scan and AI diagnosis | Core business flow |
| F5 | Path: DIY | Tutorial + AI help |
| F6 | Path: Community | Repair café / volunteer |
| F7 | Path: Not worth it / unrepairable | Alternative to repair |
| F8 | Outcome and impact | Case closure |
| F9 | Repair history | Past cases |
| F10 | Profile | User data |
| F11 | Settings | App preferences |

**Most complex task (HTA/DTI):** F4 → (F5 | F6 | F7) → F8.

---

## 2. Document conventions

- **Screen** — one page/state in the app.
- **Decision** — system or user branch (Yes/No, path choice).
- **→** — standard transition.
- **↺** — return to an earlier screen (retry).
- **⊘** — end of flow or exit from a branch.

Screens are numbered for lo-fi reference (e.g. `S-04`).

---

## 3. F0 — App entry

### S-00 · Start (splash / welcome)

| | |
|---|---|
| **Entry** | First app launch or return after sign out |
| **Purpose** | Introduce the app |
| **User actions** | Continue |
| **Exit** | → S-01 |

---

### S-01 · Decision: does the user have an account?

| | |
|---|---|
| **Entry** | S-00 |
| **Purpose** | Route to sign in or registration |
| **Actions** | Choice: *I have an account* / *I don’t have an account* |
| **Exit** | *I have an account* → F2 (S-10) · *I don’t have an account* → F1 (S-20) |

---

## 4. F1 — Registration

### S-20 · Registration (method selection)

| | |
|---|---|
| **Entry** | S-01 (*I don’t have an account*) |
| **Purpose** | Create an account |
| **Actions** | Sign up with Google · Sign up with Facebook · Email and password |
| **Exit** | → corresponding sub-screen (S-21 / S-22 / S-23) |

### S-21 · Registration — Google (system OAuth)

| | |
|---|---|
| **Entry** | S-20 |
| **Purpose** | Authenticate via Google |
| **System** | OAuth flow outside app → return to app |
| **Exit** | → S-24 |

### S-22 · Registration — Facebook (system OAuth)

| | |
|---|---|
| **Entry** | S-20 |
| **Purpose** | Authenticate via Facebook |
| **System** | OAuth flow outside app → return to app |
| **Exit** | → S-24 |

### S-23 · Registration — email and password

| | |
|---|---|
| **Entry** | S-20 |
| **Purpose** | Manual account creation |
| **Actions** | Enter email, password, confirm password (and name if needed) · Confirm · Back |
| **Exit** | Confirm → S-24 · Back → S-20 |

### S-24 · Decision: registration successful?

| | |
|---|---|
| **Entry** | S-21, S-22, S-23 |
| **Purpose** | Validate registration |
| **System** | Check registration success |
| **Exit** | *Yes* → F3 (S-30) · *No* → ↺ S-20 (show error) |

---

## 5. F2 — Sign in

### S-10 · Sign in (method selection)

| | |
|---|---|
| **Entry** | S-01 (*I have an account*) |
| **Purpose** | Sign in existing user |
| **Actions** | Google login · Facebook login · Email and password · Forgot password? · Back |
| **Exit** | Methods → S-11 / S-12 / S-13 · Forgot password → S-14 · Back → S-01 |

### S-11 · Sign in — Google

| | |
|---|---|
| **Entry** | S-10 |
| **Exit** | → S-15 |

### S-12 · Sign in — Facebook

| | |
|---|---|
| **Entry** | S-10 |
| **Exit** | → S-15 |

### S-13 · Sign in — email and password

| | |
|---|---|
| **Entry** | S-10 |
| **Actions** | Enter email and password · Sign in · Back |
| **Exit** | Sign in → S-15 · Back → S-10 |

### S-14 · Decision: forgot password?

| | |
|---|---|
| **Entry** | S-10 (*Forgot password?* link) |
| **Purpose** | Password reset |
| **Actions** | Confirm reset · Cancel |
| **Exit** | Confirm → S-14a · Cancel → S-10 |

### S-14a · Password reset

| | |
|---|---|
| **Entry** | S-14 |
| **Actions** | Enter email · Send link/instructions · Back |
| **System** | Send reset email |
| **Exit** | Success → S-10 (message that email was sent) · Back → S-10 |

### S-15 · Decision: sign in successful?

| | |
|---|---|
| **Entry** | S-11, S-12, S-13 |
| **Purpose** | Validate sign in |
| **Exit** | *Yes* → F3 (S-30) · *No* → ↺ S-10 (error) |

---

## 6. F3 — Home (hub)

### S-30 · Home screen

| | |
|---|---|
| **Entry** | S-15 (*Yes*), S-24 (*Yes*), or return from other flows |
| **Purpose** | App hub; start main scenario |
| **Actions** | Scan item (primary) · Repair history · Profile · Settings |
| **Exit** | Scan → F4 (S-40) · History → F9 (S-90) · Profile → F10 (S-100) · Settings → F11 (S-110) |

**Note:** User can return to S-30 from sub-flows (global navigation / back to hub where defined in prototype).

---

## 7. F4 — Scan and AI diagnosis (core flow)

### S-40 · Scan item (diagnosis entry)

| | |
|---|---|
| **Entry** | S-30 |
| **Purpose** | Start broken-item intake |
| **Actions** | Take photo (camera) · Upload photo · Back |
| **Exit** | Camera → S-41 · Upload → S-42 · Back → S-30 |

### S-41 · Take photo (camera)

| | |
|---|---|
| **Entry** | S-40 |
| **Actions** | Capture · Cancel / Back |
| **Exit** | Capture → S-43 · Cancel → S-40 |

### S-42 · Upload photo

| | |
|---|---|
| **Entry** | S-40 |
| **Actions** | Choose file from gallery · Cancel |
| **Exit** | File chosen → S-43 · Cancel → S-40 |

### S-43 · Decision: image recognized successfully? (AI — object)

| | |
|---|---|
| **Entry** | S-41, S-42 |
| **Purpose** | AI recognizes item category from image |
| **System** | Object recognition |
| **Exit** | *Yes* → S-44 · *No* → S-43e |

### S-43e · Error: image not recognized

| | |
|---|---|
| **Entry** | S-43 (*No*) |
| **Purpose** | Inform user; offer retry |
| **Actions** | Try again · Back |
| **Exit** | Try again → ↺ S-40 · Back → S-40 |

### S-44 · Enter fault description (symptoms)

| | |
|---|---|
| **Entry** | S-43 (*Yes*) |
| **Purpose** | User adds context for AI |
| **Actions** | Short text (1–2 sentences) · Continue · Back |
| **Exit** | Continue → S-45 · Back → S-40 |

### S-45 · Decision: can the system recognize the fault? (AI — problem)

| | |
|---|---|
| **Entry** | S-44 |
| **Purpose** | AI estimates likely fault from image + description |
| **System** | Problem inference |
| **Exit** | *Yes* → S-46 · *No* → S-45e |

### S-45e · Error: fault not recognized

| | |
|---|---|
| **Entry** | S-45 (*No*) |
| **Actions** | Edit description · Scan again · Back |
| **Exit** | Edit description → ↺ S-44 · Scan again → ↺ S-40 · Back → S-40 |

### S-45b · (Optional) Item category selection

| | |
|---|---|
| **Entry** | S-45 when AI is **uncertain** (low confidence), or in parallel before S-46 |
| **Purpose** | User helps AI manually |
| **Actions** | Pick category from list · Continue |
| **Exit** | Continue → S-46 |

*Flow logic: if confidence is low, route through S-45b before S-46; if high, skip.*

### S-46 · AI diagnosis — result

| | |
|---|---|
| **Entry** | S-45 (*Yes*), optionally S-45b |
| **Purpose** | Show structured assessment |
| **System displays (informational)** | Recognized item · Probable fault · Difficulty / repairability · Success likelihood · Confidence indicator · Short explanation of recommendation |
| **Actions** | Continue to path choice · Back |
| **Exit** | Continue → S-47 · Back → S-44 |

### S-47 · System assesses fault severity (routing)

| | |
|---|---|
| **Entry** | S-46 |
| **Purpose** | Internal/logical decision for recommended path |
| **System** | Repair pathway recommendation + repairability score |
| **Exit** | → S-48 |

### S-48 · Decision: route by fault type

| | |
|---|---|
| **Entry** | S-47 |
| **Purpose** | Branch into three main paths |
| **Exit** | *Easier fault* → F5 (S-50) · *Harder fault* → F6 (S-60) · *Unrepairable / not worth it* → F7 (S-70) |

### S-49 · Repair path recommendation (aggregate screen)

| | |
|---|---|
| **Entry** | Alternative: right after S-46 instead of going straight to S-48 |
| **Purpose** | Show all path options explicitly |
| **Actions** | DIY · Community (repair café / volunteer) · Parts / recycling / not worth it |
| **Exit** | DIY → F5 · Community → F6 · Not worth it → F7 |

*Flow logic: S-48 may auto-open the recommended branch; S-49 allows manual choice. For lo-fi: both screens may exist or merge into one — pick one approach in the prototype (auto + link “Choose another path” → S-49).*

---

## 8. F5 — Path: DIY

### S-50 · Repair tutorial

| | |
|---|---|
| **Entry** | S-48 (*Easier fault*) or S-49 (DIY) |
| **Purpose** | Guide user through beginner repair |
| **Content (informational)** | Repair steps · Safety warnings · Tool list (if any) |
| **Actions** | Mark step complete · Open AI chat · Finish tutorial · Change path |
| **Exit** | AI chat → S-52 · Finish → S-54 · Change path → S-49 |

### S-52 · AI chat — additional clarification

| | |
|---|---|
| **Entry** | S-50, or S-53 (*No* — tutorial not clear) |
| **Purpose** | Clarify steps, reduce uncertainty |
| **Actions** | Ask question · Back |
| **Exit** | Back → S-50 or → S-53 |

### S-53 · Decision: are tutorials clear enough?

| | |
|---|---|
| **Entry** | S-50 (after reading / partial completion) |
| **Purpose** | Check understanding |
| **Actions** | Yes · No |
| **Exit** | *Yes* → S-54 · *No* → S-52 |

### S-54 · Decision: did the user fix the device?

| | |
|---|---|
| **Entry** | S-53 (*Yes*), or directly from S-50 (completion) |
| **Purpose** | Collect outcome before closing |
| **Exit** | *Yes* → F8 (S-80) · *No* → S-52 or → S-49 (community recommendation) or → F8 with outcome *not fixed* |

---

## 9. F6 — Path: Community (repair café / volunteer)

### S-60 · List of local repair cafés and volunteers

| | |
|---|---|
| **Entry** | S-48 (*Harder fault*) or S-49 (Community) |
| **Purpose** | Show local support |
| **System displays (informational)** | Events · Volunteers · Skill tags · Distance · Availability / estimated wait |
| **Actions** | Select item · Filter / sort (optional) · Back |
| **Exit** | Select → S-61 · Back → S-49 or S-46 |

### S-61 · Repair café / volunteer detail

| | |
|---|---|
| **Entry** | S-60 |
| **Purpose** | Information before contact |
| **Actions** | Request help / book · Back |
| **Exit** | Request help → S-62 · Back → S-60 |

### S-62 · Help request / booking

| | |
|---|---|
| **Entry** | S-61 |
| **Purpose** | Contact or reserve a slot |
| **Actions** | Enter message · Pick time slot (if available) · Send · Cancel |
| **System** | Create request / notify volunteer or organizer |
| **Exit** | Success → S-63 · Cancel → S-61 |

### S-63 · Request sent confirmation

| | |
|---|---|
| **Entry** | S-62 |
| **Purpose** | Confirm next step to user |
| **Actions** | Back to home · Record outcome later |
| **Exit** | Home → S-30 · Outcome → F8 (S-80) — e.g. outcome *in progress / waiting for help* |

*Optional later: request status screen (pending / accepted / declined) — not required for first lo-fi pass.*

---

## 10. F7 — Path: Not worth it / unrepairable

### S-70 · Message: repair not worth it or not feasible

| | |
|---|---|
| **Entry** | S-48 (*Unrepairable*) or S-49 (parts / recycling) |
| **Purpose** | Set realistic expectations; offer alternatives |
| **Actions** | Suggestion: parts / donation · Recycling · Get second opinion (community) · Finish |
| **Exit** | Community → F6 (S-60) · Finish → F8 (S-80) · Home → S-30 |

---

## 11. F8 — Outcome and impact

### S-80 · Record repair outcome

| | |
|---|---|
| **Entry** | S-54, S-63, S-70, or S-90 (update old case) |
| **Purpose** | Close case; collect impact data |
| **Actions** | Select outcome: fixed successfully · partially fixed · not fixed · used for parts · sent to recycling · (optional) add note · (optional) add after photo |
| **Exit** | Continue → S-81 |

### S-81 · Impact summary

| | |
|---|---|
| **Entry** | S-80 |
| **Purpose** | Feedback and motivation |
| **System displays (informational)** | Estimated savings · Estimated waste avoided · Skills learned (if DIY) · Community contribution |
| **Actions** | Back to home · View history |
| **Exit** | Home → S-30 · History → S-90 |

### S-82 · Case closed

| | |
|---|---|
| **Entry** | S-81 |
| **Purpose** | End of main flow |
| **Exit** | → S-30 (⊘ main flow) |

---

## 12. F9 — Repair history

### S-90 · Repair history list

| | |
|---|---|
| **Entry** | S-30, S-81 |
| **Purpose** | Review past cases |
| **Actions** | Select case · Back |
| **Exit** | Select → S-91 · Back → S-30 |

### S-91 · History case detail

| | |
|---|---|
| **Entry** | S-90 |
| **Purpose** | View diagnosis, path, outcome |
| **Actions** | Update outcome (if missing) · Back |
| **Exit** | Update outcome → S-80 · Back → S-90 |

---

## 13. F10 — Profile

### S-100 · User profile

| | |
|---|---|
| **Entry** | S-30 |
| **Purpose** | Personal data and stats (optional) |
| **Actions** | Edit profile · Sign out · Back |
| **Exit** | Edit → S-101 · Sign out → F0 (S-00 or S-01) · Back → S-30 |

### S-101 · Edit profile

| | |
|---|---|
| **Entry** | S-100 |
| **Actions** | Save · Cancel |
| **Exit** | Save → S-100 · Cancel → S-100 |

---

## 14. F11 — Settings

### S-110 · App settings

| | |
|---|---|
| **Entry** | S-30 |
| **Purpose** | Notifications, language, privacy, help |
| **Actions** | Toggle notifications · Language · Privacy policy · Help/FAQ · Back |
| **Exit** | Back → S-30 |

---

## 15. Screen map (quick reference)

| ID | Screen name | Flow |
|----|-------------|------|
| S-00 | Start | F0 |
| S-01 | Do you have an account? | F0 |
| S-10 | Sign in | F2 |
| S-11–S-13 | Sign in (OAuth / email) | F2 |
| S-14 | Forgot password? | F2 |
| S-14a | Password reset | F2 |
| S-15 | Sign in successful? | F2 |
| S-20 | Registration | F1 |
| S-21–S-23 | Registration (methods) | F1 |
| S-24 | Registration successful? | F1 |
| S-30 | Home | F3 |
| S-40 | Scan item | F4 |
| S-41 | Camera | F4 |
| S-42 | Upload | F4 |
| S-43 | Image recognized? | F4 |
| S-43e | Image not recognized | F4 |
| S-44 | Fault description | F4 |
| S-45 | Fault recognized? | F4 |
| S-45e | Fault not recognized | F4 |
| S-45b | Category selection (opt.) | F4 |
| S-46 | AI diagnosis — result | F4 |
| S-47 | Severity assessment | F4 |
| S-48 | Path routing | F4 |
| S-49 | Path choice (opt./alt.) | F4 |
| S-50 | DIY tutorial | F5 |
| S-52 | AI chat | F5 |
| S-53 | Tutorial clear? | F5 |
| S-54 | Repair successful? | F5 |
| S-60 | Café/volunteer list | F6 |
| S-61 | Café/volunteer detail | F6 |
| S-62 | Request / booking | F6 |
| S-63 | Request confirmation | F6 |
| S-70 | Not worth it / unrepairable | F7 |
| S-80 | Record outcome | F8 |
| S-81 | Impact summary | F8 |
| S-82 | Case closed | F8 |
| S-90 | History — list | F9 |
| S-91 | History — detail | F9 |
| S-100 | Profile | F10 |
| S-101 | Edit profile | F10 |
| S-110 | Settings | F11 |

**Total screens for lo-fi MVP:** ~45 (including errors and optional); for a minimal presentable set, merge S-47+S-48, skip S-49, treat OAuth screens as one “External login”.

---

## 16. Happy path (reference flow for presentation)

```
S-00 → S-01 (I have an account) → S-10 → S-13 → S-15 (Yes)
→ S-30 → S-40 → S-41 → S-43 (Yes) → S-44 → S-45 (Yes)
→ S-46 → S-47 → S-48 (easier fault) → S-50 → S-53 (Yes)
→ S-54 (Yes) → S-80 → S-81 → S-30
```

**Alternative happy path (community):** from S-48 → *harder fault* → S-60 → S-61 → S-62 → S-63 → S-80 → S-81.

---

## 17. Branches required in lo-fi (DTI coverage)

| Branch | From | Condition | To |
|--------|------|-----------|-----|
| Registration | S-01 | No account | F1 → S-30 |
| Login fail | S-15 | No | S-10 |
| Registration fail | S-24 | No | S-20 |
| Image fail | S-43 | No | S-43e → S-40 |
| Fault fail | S-45 | No | S-45e → S-44 / S-40 |
| DIY | S-48 | Easier | F5 |
| Community | S-48 | Harder | F6 |
| Unrepairable | S-48 | Unrepairable | F7 |
| Tutorial unclear | S-53 | No | S-52 |
| Repair failed | S-54 | No | S-49 or S-52 or S-80 |
| Forgot password | S-10 | Link | S-14 → S-14a |

---

## 18. Out of scope for MVP lo-fi (later)

- **Volunteer** interface (accept requests, skill tags).
- **Repair event organizer** interface (triage, scheduling).
- Real-time request status tracking (S-63+).
- Map / navigation to repair café.
- Offline mode.

---

## 19. Link to KT1 artifacts

| KT1 item | Where in flow |
|----------|----------------|
| DTI | Sections 3–14 (all screen transitions) |
| HTA most complex task | F4 + F5/F6/F7 + F8 (screens S-40–S-82) |
| MVP from brief | S-30, S-40–S-49, S-50/60/62, S-80–S-81 cover the 7 suggested screens; rest extends DTI |

---

*Last updated: aligned with `patchup_project_prompt.md` and DTI on FigJam board PatchUp.*
