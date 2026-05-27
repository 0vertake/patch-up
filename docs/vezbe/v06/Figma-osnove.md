# Figma — osnove

> Izvor: `Figma-osnove.pdf` (vežbe v06)

---

## Figma

Figma je alat za dizajn interfejsa koji omogućava timovima da zajedno rade na projektima. Koristi se za razmišljanje o idejama, kreiranje prototipa i dobijanje povratne informacije u bilo kojoj fazi kreativnog procesa.

### Prednosti

- Cloud platforma — timski rad u realnom vremenu
- Prototipovi i dizajn interfejsa na jednom mestu
- Jednostavno deljenje projekata i komentarisanje
- Kompatibilnost sa različitim uređajima i OS-ovima

---

## Canvas u Figmi

### Šta je canvas?

Pozadina za dizajn — na nju se dodaju okviri, oblici, tekst i slike. Osnovno radno okruženje za dizajniranje interfejsa.

### Mogućnosti

- Neograničena radna površina
- Organizacija elemenata po želji
- Više frame-ova na istoj površini
- Kretanje i zumiranje
- Grupisanje i logična struktura projekta

> U originalnom PDF-u: slajd sa prikazom canvas-a (slika).

---

## Frame u Figmi

### Definicija

- Osnovni element za organizaciju sadržaja
- Može se posmatrati kao **ekran**
- Podržava **Layout Grids** i **Auto Layout**
- Ima **Constraints** i prototipiranje
- Ugnježdavanje više frame-ova za složene interfejse

> U originalnom PDF-u: primeri frame-a (slike).

---

## Group vs. Frame — ključne razlike

### Group (grupisanje)

- Kombinuje više slojeva u jednu celinu
- Nema sopstvene dimenzije — prilagođava se sadržaju
- Veličina se menja sa sadržajem
- **Ne** podržava constraints ili Auto Layout
- Za brzu organizaciju elemenata

### Frame

- Samostalan sloj — kontejner
- Sopstvene dimenzije (širina, visina)
- Ponaša se kao ekran, artboard ili komponenta
- Podržava **Constraints**, **Auto Layout**, **Layout Grid**
- Kreira novi kontekst za sadržaj

**Kada koristiti:** Group za brzu organizaciju. Frame za ekrane, komponente i responsivan dizajn.

---

## Oblici u Figmi

Osnovni grafički elementi: kvadrat, krug, trougao, linija, itd.

- Kreiranje alatima za crtanje ili bibliotekom
- Prilagođavanje: boja, veličina, ivica
- Grupisanje i kombinovanje oblika
- Osnova za kompleksnije UI elemente (vektorski alati)

---

## Tekst u Figmi

- Alat za tekst: naslovi, paragrafi, navigacija
- Stil: font, veličina, boja, podebljanje
- **Text styles** za konzistentnost u celoj aplikaciji
- Tipografija i skale za čitljivost

---

## Layout grid u Figma-i

Vodič za organizaciju sadržaja u dizajnu.

Omogućava:

- poravnanje elemenata
- doslednost između ekrana
- lakši responzivni dizajn

### Osnovni tipovi layout grida

| Tip | Upotreba |
|-----|----------|
| **Grid (mreža)** | Kvadratna mreža — ikone, tabele |
| **Columns (kolone)** | Najčešće u web/UI dizajnu |
| **Rows (redovi)** | Vertikalno sekcionisanje |

Možeš kombinovati više gridova na jednom frame-u.

> U originalnom PDF-u: slajd 13 je prazan / vizuelni — pogledaj PDF.

---

## 12–8–4 kolonski sistem (responzivni grid)

Pristup za skaliranje dizajna između veličina ekrana:

| Uređaj | Kolone |
|--------|--------|
| Desktop | 12 |
| Tablet | 8 |
| Mobile | 4 |

Elementi se skaliraju proporcionalno prema kolonama.

### Zašto koristiti?

- Konzistentnost na svim uređajima
- Fleksibilnost
- Precizan, ujednačen raspored
- Lakše za developere i dizajnere

### Desktop (≥ 1024px) — 12 kolona

- Standardni desktop layout
- Simetričan dizajn, kombinacije (3+9, 6+6, …)
- Idealno: dashboardi, kompleksni layouti

### Mobile (≤ 599px) — 4 kolone

- Minimalistički raspored
- Često 1–2 kolone za sadržaj i kartice
- Prioritet: čitljivost i vertikalno skrolovanje

---

## Postavljanje gridova za različite uređaje

| Uređaj | Širina frame-a | Kolone | Margin | Gutter |
|--------|----------------|--------|--------|--------|
| Mobile | 375px | 4 | 16px | 16px |
| Tablet | 768px | 8 | 32px | 20px |
| Desktop | 1440px | 12 | 120px | 20px |

---

## Constraints u Figma-i

Određuju kako se elementi ponašaju kada se **veličina frame-a** promeni — odnos objekta prema ivicama frame-a.

**Napomena:** Constraints rade samo u **Frame**, **Auto Layout Frame** ili **Component** — ne u običnim **Group**.

### Horizontalno

| Opcija | Ponašanje |
|--------|-----------|
| **Left** | Zalepljen za levu ivicu; širina se ne menja |
| **Right** | Zalepljen za desnu ivicu |
| **Left & Right (Stretch)** | Širi se sa frame-om (npr. input, background traka) |
| **Center** | Ostaje centriran |
| **Scale** | Proporcionalno skaliranje (retko) |

### Vertikalno

Top · Bottom · Top & Bottom (Stretch) · Center · Scale — ista logika kao horizontalno.

---

## Auto Layout u Figma-i

Automatski raspoređuje elemente bez ručnog poravnavanja.

- Automatski raspored
- Prilagođava razmak i padding
- Reaguje na promenu sadržaja (tekst, veličina)
- Pomaže responzivnom dizajnu

### Kada koristiti?

- Ponavljajuće komponente
- Dugmad, liste, forme, kartice
- Kada dizajn treba da reaguje na sadržaj

### Ključne opcije

| Opcija | Opis |
|--------|------|
| Direction | Horizontalno ili vertikalno |
| Spacing between items | Razmak između elemenata |
| Padding | Unutrašnji razmak |
| Alignment | Gore, centar, itd. |
| Resizing | Hug, Fill, Fixed |

### Hug, Fill i Fixed

| Postavka | Značenje |
|----------|----------|
| **Hug contents** | Frame se prilagođava veličini sadržaja |
| **Fill container** | Frame popunjava prostor roditelja |
| **Fixed** | Fiksna širina/visina |

---

## Razmak između elemenata (spacing)

Prazan prostor između elemenata — aktivni deo dizajna, ne „praznina“.

### Značaj

- Čitljivost
- Grupisanje povezanih elemenata
- Vizuelna hijerarhija
- Lakše skeniranje sadržaja

### Sistemi

Često **4px** ili **8px** mreža — svi razmaci su umnošci (8, 16, 24, 32…).

### Doslednost i responzivnost

Isti sistem na svim uređajima; na mobilnom manji razmaci, ali ista logika proporcija.
