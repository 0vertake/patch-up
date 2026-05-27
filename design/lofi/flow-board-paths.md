# PatchUp Lo-Fi — Flow board paths

Izvor: `docs/patchup_app_flow.md` (MVP), mapirano na **33 postojeća** Lo-Fi ekrana u `design/lofi/screenshots/`.

Legenda:
- `→` glavni prelaz (puna strelica)
- `↺` povratak / retry (isprekidana strelica)
- Ekrani koji **nisu** u Lo-Fi setu (OAuth S-11/12/21/22, S-41/42/43, S-45, S-52–54, S-81/82, S-91) su spojeni na najbliži ekvivalent.

---

## F0 — Ulaz

| Od | Akcija / uslov | Do |
|----|----------------|-----|
| S-00 Welcome | Continue | S-01 Account |
| S-01 Account | I have an account | S-10 Sign in |
| S-01 Account | I don't have an account | S-20 Registration method |

---

## F1 — Registracija (email put u Lo-Fi)

| Od | Akcija / uslov | Do |
|----|----------------|-----|
| S-20 Registration method | Email and password | S-23a Registration step 1 |
| S-23a Registration step 1 | Next (invalid) | S-23a-err Registration error |
| S-23a-err | ↺ fix fields | S-23a Registration step 1 |
| S-23a Registration step 1 | Next (valid) | S-23b Registration step 2 |
| S-23b Registration step 2 | Next | S-23c Registration summary |
| S-23c Registration summary | Create account | **S-30 Home** |

*Google/Facebook na S-20 → u punom flow-u OAuth → S-24 → S-30; u Lo-Fi nije poseban ekran.*

---

## F2 — Prijava

| Od | Akcija / uslov | Do |
|----|----------------|-----|
| S-10 Sign in | Sign in (success) | **S-30 Home** |

*Forgot password (S-14) nije u Lo-Fi setu.*

---

## F3 — Home (hub)

| Od | Akcija | Do |
|----|--------|-----|
| S-30 Home | Scan item | S-40 Scan |
| S-30 Home | Repair history | S-90 History |
| S-30 Home | Profile | S-100 Profile |
| S-30 Home | Settings | S-110 Settings |

---

## F4 — Skeniranje i AI dijagnoza

| Od | Akcija / uslov | Do |
|----|----------------|-----|
| S-40 Scan | Take / upload photo → opis | S-44 Describe fault |
| S-44 Describe fault | Continue (OK) | S-46 AI diagnosis |
| S-44 Describe fault | Not recognized | S-43e Error not recognized |
| S-43e Error not recognized | Try again ↺ | S-40 Scan |
| S-46 AI diagnosis | See repair options | S-49 Repair options |

---

## F5 / F6 / F7 — Izbor puta popravke

| Od | Akcija | Do |
|----|--------|-----|
| S-49 Repair options | Try it yourself | S-50 DIY tutorial |
| S-49 Repair options | Visit repair café | S-60 Community list |
| S-49 Repair options | Not worth repairing | S-70 Not worth |

### F5 — DIY

| Od | Akcija | Do |
|----|--------|-----|
| S-50 DIY tutorial | Finish tutorial | S-80a Outcome step 1 |

### F6 — Zajednica

| Od | Akcija / uslov | Do |
|----|----------------|-----|
| S-60 Community list | Select café | S-61 Café detail |
| S-61 Café detail | Request help | S-62a Help step 1 |
| S-62a Help step 1 | Next (invalid) | S-62a-err Help error |
| S-62a-err | ↺ fix | S-62a Help step 1 |
| S-62a Help step 1 | Next (valid) | S-62b Help step 2 |
| S-62b Help step 2 | Next | S-62c Help summary |
| S-62c Help summary | Send request | S-63 Request sent |
| S-63 Request sent | Back to home | **S-30 Home** |
| S-63 Request sent | Record outcome later | S-80a Outcome step 1 |

### F7 — Ne isplati se

| Od | Akcija | Do |
|----|--------|-----|
| S-70 Not worth | Back to home | **S-30 Home** |
| S-70 Not worth | (finish / record) | S-80a Outcome step 1 |

---

## F8 — Ishod

| Od | Akcija | Do |
|----|--------|-----|
| S-80a Outcome step 1 | Next | S-80b Outcome step 2 |
| S-80b Outcome step 2 | Next | S-80c Outcome summary |
| S-80c Outcome summary | Save | S-90 History |
| S-80c Outcome summary | (implicit home) | **S-30 Home** |

---

## F9 / F10 / F11 — Istorija, profil, podešavanja

| Od | Akcija / uslov | Do |
|----|----------------|-----|
| S-90 History | Back | **S-30 Home** |
| S-100 Profile | Edit profile | S-101a Edit step 1 |
| S-101a Edit step 1 | Next (invalid) | S-101a-err Edit error |
| S-101a-err | ↺ fix | S-101a Edit step 1 |
| S-101a Edit step 1 | Next (valid) | S-101b Edit step 2 |
| S-101b Edit step 2 | Next | S-101c Edit summary |
| S-101c Edit summary | Save | S-100 Profile |
| S-110 Settings | Back | **S-30 Home** |

---

## Lista ivica za `flow-board.html` (slug → slug)

**Glavne (solid):**

1. s-00-welcome → s-01-account-check  
2. s-01-account-check → s-10-sign-in  
3. s-01-account-check → s-20-registration-method  
4. s-10-sign-in → s-30-home-hub  
5. s-20-registration-method → s-23-registration-step-1  
6. s-23-registration-step-1 → s-23-registration-step-2  
7. s-23-registration-step-2 → s-23-registration-summary  
8. s-23-registration-summary → s-30-home-hub  
9. s-30-home-hub → s-40-scan-item  
10. s-30-home-hub → s-90-repair-history-list  
11. s-30-home-hub → s-100-profile  
12. s-30-home-hub → s-110-settings  
13. s-40-scan-item → s-44-describe-fault  
14. s-44-describe-fault → s-46-ai-diagnosis-result  
15. s-44-describe-fault → s-43e-error-not-recognized  
16. s-46-ai-diagnosis-result → s-49-choose-repair-path  
17. s-49-choose-repair-path → s-50-diy-tutorial  
18. s-49-choose-repair-path → s-60-community-list  
19. s-49-choose-repair-path → s-70-not-worth-repairing  
20. s-50-diy-tutorial → s-80-record-outcome-step-1  
21. s-60-community-list → s-61-caf-detail  
22. s-61-caf-detail → s-62-help-request-step-1  
23. s-62-help-request-step-1 → s-62-help-request-step-2  
24. s-62-help-request-step-2 → s-62-help-request-summary  
25. s-62-help-request-summary → s-63-request-sent-confirmation  
26. s-63-request-sent-confirmation → s-30-home-hub  
27. s-63-request-sent-confirmation → s-80-record-outcome-step-1  
28. s-70-not-worth-repairing → s-30-home-hub  
29. s-70-not-worth-repairing → s-80-record-outcome-step-1  
30. s-80-record-outcome-step-1 → s-80-record-outcome-step-2  
31. s-80-record-outcome-step-2 → s-80-outcome-summary  
32. s-80-outcome-summary → s-90-repair-history-list  
33. s-80-outcome-summary → s-30-home-hub  
34. s-100-profile → s-101-edit-profile-step-1  
35. s-101-edit-profile-step-1 → s-101-edit-profile-step-2  
36. s-101-edit-profile-step-2 → s-101-edit-profile-summary  
37. s-101-edit-profile-summary → s-100-profile  
38. s-90-repair-history-list → s-30-home-hub  

**Retry / greška (dashed):**

- s-23-registration-step-1 → s-23-step-1-error-state  
- s-23-step-1-error-state → s-23-registration-step-1  
- s-43e-error-not-recognized → s-40-scan-item  
- s-62-help-request-step-1 → s-62-step-1-error-state  
- s-62-step-1-error-state → s-62-help-request-step-1  
- s-101-edit-profile-step-1 → s-101-edit-profile-step-1-error  
- s-101-edit-profile-step-1-error → s-101-edit-profile-step-1  

---

## Raspored kolona (flow board)

| Kolona | Faza | Ekrani (redom odozgo) |
|--------|------|------------------------|
| 0 | F0 | S-00, S-01 |
| 1 | Sign in | S-10 |
| 2 | Registration | S-20 |
| 3 | Reg steps | S-23a, S-23a-err, S-23b, S-23c |
| 4 | F3 hub | S-30 |
| 5 | F4 scan | S-40, S-44, S-43e |
| 6 | F4 diag | S-46, S-49 |
| 7 | F5 | S-50 |
| 8 | F6 | S-60, S-61, S-62a, S-62a-err, S-62b, S-62c, S-63 |
| 9 | F7 | S-70 |
| 10 | F8 | S-80a, S-80b, S-80c |
| 11 | F9–F11 | S-90, S-100, S-101a, S-101a-err, S-101b, S-101c, S-110 |
