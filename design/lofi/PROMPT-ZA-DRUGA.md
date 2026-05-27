# PatchUp Lo-Fi — prompt za nastavak (copy-paste u Cursor)

Kopiraj **ceo blok ispod** u novi Cursor chat u repou `patch-up`. Cilj: izmene dizajna po feedback-u sa vežbi + povezati sve ekrane u prototip (Figma i/ili flow board), isto kao što je Miloš krenuo.

---

## COPY-PASTE ZA AGENTA

```
Radiš na PatchUp HCI Lo-Fi prototipu (vežbe v05/v06). Repo: patch-up.

KONTEKST:
- Izvor istine za TOK: design/lofi/flow-board-paths.md i docs/patchup_app_flow.md
- Vizuelni flow board (strelice): design/lofi/flow-board.html — već ispravan, ne diraj osim ako dodaš nove ekrane
- HTML wireframe-i: design/lofi/html/*.html (grayscale, 375×812, margin 24, gutter 16)
- Generator (preferirano za izmene): design/lofi/scripts/generate_wireframes.py → python3 design/lofi/scripts/generate_wireframes.py
- PNG export: design/lofi/scripts/export_screenshots.sh
- Figma prototip (klik → Navigate to): design/lofi/figma-plugin-prototype/ + design/lofi/scripts/figma_prototype_apply.md
- Figma fajl: https://www.figma.com/design/2fP7Qoa2u4KP5PR7hklFVJ

ZADATAK U 2 DELA:

=== A) IZMENE DIZAJNA (feedback tima, 26.5.2026) ===

1) GOOGLE + FACEBOOK (login I registracija)
   - Na S-20 već postoje tekstualna dugmad "Sign up with Google/Facebook" — DODAJ i na S-10 Sign in ista dva dugmeta SA LOGOIMA (Lo-Fi: sivi pravougaonik + placeholder ikonica + tekst, kao na DTI).
   - Dugmad iznad email/password polja ili odmah ispod naslova; zatim separator "ili" pa forma.
   - Prototip: Google/Facebook na S-10 i S-20 → direktno S-30 Home (nema OAuth ekrana u Lo-Fi).

2) ZABORAVLJENA LOZINKA (novi ekrani)
   - Dodaj S-14 i S-14a prema docs/patchup_app_flow.md:
     - S-14: potvrda ("Send password reset email?" Confirm / Cancel)
     - S-14a: unos email-a + "Send reset link" → poruka da je email poslat → nazad na S-10
   - S-10 već ima link "Forgot password?" — poveži prototipom.
   - Novi fajlovi: html/s-14-forgot-password.html, html/s-14a-password-reset.html (+ screenshots, manifest, flow-board-paths, flow-board.html, figma plugin).

3) POGREŠAN UNOS FORME (već delimično urađeno — proveri/popravi)
   - Mora postojati bar jedan jasan primer: crveni/obod oko polja + poruka ispod (npr. "Please enter a valid email.").
   - Već postoje: S-23a-err, S-62a-err, S-101a-err — proveri da izgledaju kao na vežbama, ne samo disabled dugme.
   - Ukloni zbunjujući subtitle "Error after Next" → zameni npr. "Check the fields below" ili ostavi samo step broj.

4) PREGLED PRE SLANJA (summary) — već postoji, samo proveri
   - Registracija S-23c, Help S-62c, Edit profile S-101c, Outcome S-80c — lista unetog + primary CTA.

5) REQUEST HELP — DATUM (kalendar, ne ručni unos)
   - Na S-62b (step 2): polje datuma mora izgledati kao DATE PICKER (Lo-Fi: input + mali kalendar popup ispod ili modal sa mrežom dana — sivo, bez boja).
   - Ne slobodan tekst "dd/mm/yyyy" — kao na vežbi (picker koji "iskače").
   - Step 1 ostaje "Preferred time" (vreme popravke); step 2 = datum zakazivanja.
   - Summary S-62c: prikaži konkretan datum (npr. "27 May 2026"), ne "—".

6) PHONE NUMBER — konzistentnost
   - Profesor: "zašto u edit profile imam phone a nigde drugde ne".
   - ODLUKA (preporuka): UKLONI phone iz edit profile (S-101b, summary, error ako ima) ILI dodaj phone u registraciju S-23a — izaberi jedno i budi konzistentan kroz ceo prototip. Default: ukloni iz profila jer nije u registraciji.

7) OPCIONO (Figma polish, ne blokira)
   - Layout grid 4 kolone (margin 24, gutter 16) u Figmi — spomenuto na vežbi.
   - Constraints na dugmad/inpute ako želiš responzivnost u Figmi.

=== B) POVEZI PROTOTIP (strelice / klik) ===

Ne piši dug dokument — dovoljno su strelice + Figma prototype.

1) Proveri design/lofi/flow-board.html (otvori u browseru) — mora odgovarati flow-board-paths.md.
2) U Figmi: Plugins → Development → PatchUp — Prototype Links (design/lofi/figma-plugin-prototype/README.md).
3) Frame imena: "S-00 · Welcome", "S-10 · Sign in", itd.
4) Grane vezuj na TEKST dugmeta (vidi figma_prototype_apply.md), ne ceo frame gde ima više izlaza.
5) KRITIČNO: S-10 Sign in → S-30 Home (NE na S-20 registraciju).
6) Error grane (Next na pogrešnom unosu): S-23a→err, S-62a→err, S-101a→err, pa retry nazad.
7) Video referenca prototipa (1 min): YouTube PLb1LkI2etMb index 8 @ 1:23:55

Posle izmena: regenerate HTML → export PNG → ažuriraj manifest.json, flow-board-paths.md (+ flow-board.html ako novi ekrani), figma plugin code.js.

Ne commituj osim ako te eksplicitno zamole.
```

---

## Šta je Miloš već uradio (ne kreni ispočetka)

| Stavka | Status |
|--------|--------|
| 33 Lo-Fi ekrana (HTML + PNG) | ✅ `design/lofi/html/`, `design/lofi/screenshots/` |
| Flow board sa strelicama | ✅ `design/lofi/flow-board.html` (usklađeno sa markdownom) |
| Google/Facebook na **registraciji** S-20 | ✅ (bez logoa — samo tekst) |
| Google/Facebook na **prijavi** S-10 | ❌ **fali** |
| Zaboravljena lozinka S-14 / S-14a | ❌ **fali** (link na S-10 postoji, ekran ne) |
| Error state ekrani (reg, help, profile) | ✅ postoje |
| Summary ekrani | ✅ postoje |
| Datum na help request | ⚠️ polje postoji, **nije picker UI** |
| Phone u edit profile | ⚠️ **nekonzistentno** sa registracijom |
| Figma prototype plugin | ✅ spreman, treba pokrenuti + dopuniti za nove ekrane |

---

## Izmene dizajna — detaljno (iz WhatsApp poruka)

### 1. Google i Facebook (prioritet: "bukvalno ono dva dugmeta sa logoima")

| Gde | Fajl | Šta uraditi |
|-----|------|-------------|
| Prijava | `design/lofi/html/s-10-sign-in.html` | Dodaj **Continue with Google** i **Continue with Facebook** (ikona + tekst, `btn-secondary`) |
| Registracija | `design/lofi/html/s-20-registration-method.html` | Već ima dugmad — **dodaj logo placeholdere** (mali kvadrat 20×20 levo od teksta) |
| Generator | `design/lofi/scripts/generate_wireframes.py` | Izmeni `S-10` i `S-20` definicije, pa `python3 design/lofi/scripts/generate_wireframes.py` |

**Prototip tok:** oba dugmeta → **S-30 Home** (bez posebnog OAuth ekrana).

### 2. Zaboravljena / reset lozinke

| ID | Novi fajl (predlog) | Sadržaj |
|----|---------------------|---------|
| S-14 | `design/lofi/html/s-14-forgot-password.html` | "Reset password?" + email prikaz + Confirm / Cancel |
| S-14a | `design/lofi/html/s-14a-password-reset.html` | Email polje + "Send reset link" + success banner "Check your email" |

**Tok:** S-10 → (Forgot password?) → S-14 → (Confirm) → S-14a → (Back / done) → S-10

### 3. Neispravan unos forme

| Ekran | Fajl | Napomena |
|-------|------|----------|
| Registracija step 1 greška | `design/lofi/html/s-23-step-1-error-state.html` | `.input-frame.error` + `.field-error` poruke |
| Help step 1 greška | `design/lofi/html/s-62-step-1-error-state.html` | Isto; popravi subtitle |
| Edit profile greška | `design/lofi/html/s-101-edit-profile-step-1-error.html` | Isto |

Profesor traži **jedan jasan primer** — proveri da bar jedan ekran na screenshot-u očigledno pokazuje crveni okvir + tekst greške.

### 4. Pregled unetog (summary) — već OK, samo proveri

| Ekran | Fajl |
|-------|------|
| Registracija | `design/lofi/html/s-23-registration-summary.html` |
| Help | `design/lofi/html/s-62-help-request-summary.html` |
| Profil | `design/lofi/html/s-101-edit-profile-summary.html` |
| Ishod | `design/lofi/html/s-80-outcome-summary.html` |

### 5. Request help — datum (picker)

| Korak | Fajl | Izmena |
|-------|------|--------|
| Step 1 | `design/lofi/html/s-62-help-request-step-1.html` | Samo **vreme** (Preferred time) |
| Step 2 | `design/lofi/html/s-62-help-request-step-2.html` | **Date picker** UI (popup kalendar, Lo-Fi sivo) |
| Summary | `design/lofi/html/s-62-help-request-summary.html` | Prikaži datum + vreme |
| Greška step 1 | `design/lofi/html/s-62-step-1-error-state.html` | Bez datuma ovde |

Referenca: vežba — datum se bira iz kalendara, ne kuca произvoljno.

### 6. Phone number — konzistentnost

| Opcija | Akcija |
|--------|--------|
| **A (preporučeno)** | Ukloni phone iz `s-101-edit-profile-step-2.html`, `s-101-edit-profile-summary.html`, generator |
| **B** | Dodaj phone u `s-23-registration-step-1.html` + summary + error |

Ne ostavljati phone samo u profilu.

---

## Svi postojeći ekrani — putanje

Koren: `design/lofi/`

| ID | Naziv | HTML | PNG |
|----|-------|------|-----|
| S-00 | Welcome | `html/s-00-welcome.html` | `screenshots/s-00-welcome.png` |
| S-01 | Account | `html/s-01-account-check.html` | `screenshots/s-01-account-check.png` |
| S-10 | Sign in | `html/s-10-sign-in.html` | `screenshots/s-10-sign-in.png` |
| S-20 | Create account (metod) | `html/s-20-registration-method.html` | `screenshots/s-20-registration-method.png` |
| S-23a | Registration step 1 | `html/s-23-registration-step-1.html` | `screenshots/s-23-registration-step-1.png` |
| S-23a-err | Registration error | `html/s-23-step-1-error-state.html` | `screenshots/s-23-step-1-error-state.png` |
| S-23b | Registration step 2 | `html/s-23-registration-step-2.html` | `screenshots/s-23-registration-step-2.png` |
| S-23c | Registration summary | `html/s-23-registration-summary.html` | `screenshots/s-23-registration-summary.png` |
| S-30 | Home | `html/s-30-home-hub.html` | `screenshots/s-30-home-hub.png` |
| S-40 | Scan item | `html/s-40-scan-item.html` | `screenshots/s-40-scan-item.png` |
| S-44 | Describe fault | `html/s-44-describe-fault.html` | `screenshots/s-44-describe-fault.png` |
| S-43e | Not recognized | `html/s-43e-error-not-recognized.html` | `screenshots/s-43e-error-not-recognized.png` |
| S-46 | AI diagnosis | `html/s-46-ai-diagnosis-result.html` | `screenshots/s-46-ai-diagnosis-result.png` |
| S-49 | Repair options | `html/s-49-choose-repair-path.html` | `screenshots/s-49-choose-repair-path.png` |
| S-50 | DIY tutorial | `html/s-50-diy-tutorial.html` | `screenshots/s-50-diy-tutorial.png` |
| S-60 | Community list | `html/s-60-community-list.html` | `screenshots/s-60-community-list.png` |
| S-61 | Café detail | `html/s-61-caf-detail.html` | `screenshots/s-61-caf-detail.png` |
| S-62a | Help step 1 | `html/s-62-help-request-step-1.html` | `screenshots/s-62-help-request-step-1.png` |
| S-62a-err | Help error | `html/s-62-step-1-error-state.html` | `screenshots/s-62-step-1-error-state.png` |
| S-62b | Help step 2 | `html/s-62-help-request-step-2.html` | `screenshots/s-62-help-request-step-2.png` |
| S-62c | Help summary | `html/s-62-help-request-summary.html` | `screenshots/s-62-help-request-summary.png` |
| S-63 | Request sent | `html/s-63-request-sent-confirmation.html` | `screenshots/s-63-request-sent-confirmation.png` |
| S-70 | Not worth repairing | `html/s-70-not-worth-repairing.html` | `screenshots/s-70-not-worth-repairing.png` |
| S-80a | Outcome step 1 | `html/s-80-record-outcome-step-1.html` | `screenshots/s-80-record-outcome-step-1.png` |
| S-80b | Outcome step 2 | `html/s-80-record-outcome-step-2.html` | `screenshots/s-80-record-outcome-step-2.png` |
| S-80c | Outcome summary | `html/s-80-outcome-summary.html` | `screenshots/s-80-outcome-summary.png` |
| S-90 | History | `html/s-90-repair-history-list.html` | `screenshots/s-90-repair-history-list.png` |
| S-100 | Profile | `html/s-100-profile.html` | `screenshots/s-100-profile.png` |
| S-101a | Edit profile step 1 | `html/s-101-edit-profile-step-1.html` | `screenshots/s-101-edit-profile-step-1.png` |
| S-101a-err | Edit profile error | `html/s-101-edit-profile-step-1-error.html` | `screenshots/s-101-edit-profile-step-1-error.png` |
| S-101b | Edit profile step 2 | `html/s-101-edit-profile-step-2.html` | `screenshots/s-101-edit-profile-step-2.png` |
| S-101c | Edit profile summary | `html/s-101-edit-profile-summary.html` | `screenshots/s-101-edit-profile-summary.png` |
| S-110 | Settings | `html/s-110-settings.html` | `screenshots/s-110-settings.png` |

**Novi (ti dodaješ):**

| ID | HTML | PNG |
|----|------|-----|
| S-14 | `html/s-14-forgot-password.html` | `screenshots/s-14-forgot-password.png` |
| S-14a | `html/s-14a-password-reset.html` | `screenshots/s-14a-password-reset.png` |

**Pomoćni fajlovi:**

| Šta | Putanja |
|-----|---------|
| CSS tokeni / komponente | `design/lofi/wireframes/shared.css` |
| Manifest ekrana | `design/lofi/manifest.json` |
| Tok (markdown) | `design/lofi/flow-board-paths.md` |
| Flow board UI | `design/lofi/flow-board.html` |
| Pun app flow (referenca) | `docs/patchup_app_flow.md` |
| HCI pravila | `docs/lofi_compliance.md` |
| Figma import uputstvo | `docs/figma_lofi_import.md` |

---

## Prototip — kompletna lista veza (poveži u Figmi)

Izvor: `design/lofi/flow-board-paths.md`. Za svaku ivicu: **On click** na dugme/link → **Navigate to** frame.

### Glavni tok (solid)

| Od | Akcija / dugme | Do |
|----|----------------|-----|
| S-00 | Continue | S-01 |
| S-01 | I have an account | S-10 |
| S-01 | I don't have an account | S-20 |
| S-10 | Sign in | S-30 |
| S-10 | Continue with Google | S-30 |
| S-10 | Continue with Facebook | S-30 |
| S-10 | Forgot password? | S-14 |
| S-14 | Confirm | S-14a |
| S-14 | Cancel | S-10 |
| S-14a | Send reset link (ili Back) | S-10 |
| S-20 | Sign up with Google | S-30 |
| S-20 | Sign up with Facebook | S-30 |
| S-20 | Email and password | S-23a |
| S-23a | Next (valid) | S-23b |
| S-23b | Next | S-23c |
| S-23c | Create account | S-30 |
| S-30 | Scan item | S-40 |
| S-30 | Repair history | S-90 |
| S-30 | Profile | S-100 |
| S-30 | Settings | S-110 |
| S-40 | Continue / Take photo | S-44 |
| S-44 | Continue | S-46 |
| S-44 | Not recognized | S-43e |
| S-46 | See repair options | S-49 |
| S-49 | Try it yourself | S-50 |
| S-49 | Visit repair café | S-60 |
| S-49 | Not worth repairing | S-70 |
| S-50 | Finish tutorial | S-80a |
| S-60 | (tap café card) | S-61 |
| S-61 | Request help | S-62a |
| S-62a | Next (valid) | S-62b |
| S-62b | Next | S-62c |
| S-62c | Send request | S-63 |
| S-63 | Back to home | S-30 |
| S-63 | Record outcome later | S-80a |
| S-70 | Back to home | S-30 |
| S-70 | Record outcome | S-80a |
| S-80a | Next | S-80b |
| S-80b | Next | S-80c |
| S-80c | Save | S-90 |
| S-80c | (Done / Home) | S-30 |
| S-90 | Back | S-30 |
| S-100 | Edit profile | S-101a |
| S-101a | Next (valid) | S-101b |
| S-101b | Next | S-101c |
| S-101c | Save | S-100 |
| S-110 | Back | S-30 |

### Greške / retry (dashed u flow-board-u)

| Od | Akcija | Do |
|----|--------|-----|
| S-23a | Next (invalid) | S-23a-err |
| S-23a-err | Back / fix → Next | S-23a |
| S-43e | Try again | S-40 |
| S-62a | Next (invalid) | S-62a-err |
| S-62a-err | Back / fix → Next | S-62a |
| S-101a | Next (invalid) | S-101a-err |
| S-101a-err | Back / fix → Next | S-101a |

**NE RADITI:** S-10 → S-20 (sign in ne sme ići na registraciju).

---

## Redosled rada (preporuka)

1. Izmeni `generate_wireframes.py` (S-10 Google/FB, S-14/S-14a, picker, phone, subtitles).
2. `python3 design/lofi/scripts/generate_wireframes.py`
3. `bash design/lofi/scripts/export_screenshots.sh`
4. Ažuriraj `manifest.json`, `flow-board-paths.md`, `flow-board.html` (novi čvorovi + ivice za S-14).
5. Otvori `flow-board.html` u browseru — proveri strelice.
6. U Figmi: import/update frame-ove, pokreni plugin `figma-plugin-prototype`, Present od S-00.
7. `python3 design/lofi/scripts/validate_flow_board_edges.py` (ako postoji).

---

## HCI pravila (ne krši)

- Samo **grayscale**, bez boja i finalnih slika
- Placeholder slike (X u okviru)
- Forme **multi-step** + **summary** pre submit
- Margin **24**, gutter **16**, razmak elemenata **8**
- Bez zvezdica (*) za obavezna polja — napomena "All fields are required"
- Frame **375×812** (mobile)

---

## Checklist pre predaje

- [ ] S-10 ima Google + Facebook sa logotip placeholderima
- [ ] S-20 Google/Facebook imaju logotip placeholdere
- [ ] S-14 i S-14a postoje i povezani sa S-10
- [ ] Bar jedan error ekran očigledno pokazuje poruke greške
- [ ] S-62b ima date picker (ne ručni tekst)
- [ ] Phone uklonjen iz profila ILI dodat u registraciju (konzistentno)
- [ ] Figma Present: ceo happy-path od Welcome do Home radi klikom
- [ ] `flow-board.html` odgovara `flow-board-paths.md`
- [ ] Nema S-10 → S-20 veze

---

## Video (1 min) — kako prototip u Figmi

https://www.youtube.com/watch?v=n7Zoima68uM&list=PLb1LkI2etMb-63rLO22haO1D0w6q9d04u&index=8 — timestamp **1:23:55**

---

*Poslednje ažuriranje: 27.5.2026. Pitanja → Miloš / Vukan.*
