# Specifikacija projekta — GastroGuide (LoFi prototip)

> Izvor: `Specifikacija LoFi prototip.pdf` (vežbe v05)  
> **Napomena:** Ovo je **primer specifikacije** sa vežbi (GastroGuide), ne PatchUp. Koristi se kao referenca za strukturu i očekivanja pri LoFi radu.

---

## Zadatak

Osmisliti **LoFi prototip** aplikacije.

Fokus:

- raspored
- hijerarhija
- grupe informacija
- navigacija
- glavne akcije

---

## Pravila LoFi prototipa

- bez boja
- bez finalnih slika
- bez dekoracije
- koristiti **placeholder-e** za slike
- koristiti **realistične naslove**
- dugmad moraju imati **jasne nazive**

---

## 1. Obavezni ekrani

Prototip treba da sadrži **najmanje** sledeće ekrane.

### 1.1 Početna strana

Aplikacija treba da ima početnu stranu koja korisniku odmah objašnjava čemu platforma služi i šta može da uradi.

**Očekivani elementi:**

- naziv aplikacije i glavna navigacija
- kratak uvodni tekst koji objašnjava svrhu aplikacije
- glavni poziv na akciju (npr. *Istraži restorane*)
- sekundarni poziv na akciju (npr. *Rezerviši sto*)
- sekcija sa izdvojenim ili preporučenim restoranima
- kratke informacije ili statistike (npr. broj restorana, recenzija, rezervacija)

### 1.2 Lista restorana

Korisnik pronalazi restoran koji odgovara kriterijumima.

**Očekivani elementi:**

- pretraga po nazivu, tipu kuhinje ili lokaciji
- filteri (kuhinja, lokacija, cena, ocena, dostupnost)
- sortiranje (preporučeno, najbolje ocenjeno, najbliže)
- prikaz restorana: slika, naziv, ocena, lokacija, tip kuhinje, dugme za detalje

### 1.3 Detalji restorana

Dovoljno informacija da korisnik odluči da li želi rezervaciju.

**Očekivani elementi:**

- galerija slika restorana ili hrane
- naziv, ocena, tip kuhinje, lokacija, radno vreme
- kratak opis restorana
- lista popularnih jela ili preporuka
- mapa ili blok sa adresom
- dugmad: *Rezerviši sto*, *Sačuvaj*, *Podeli*, *Kontaktiraj*
- sekcija sa recenzijama ili dodatnim informacijama

### 1.4 Forma za rezervaciju stola

Korisnik jasno i brzo šalje rezervaciju.

**Očekivani elementi:**

- kratak pregled izabranog restorana, datuma i vremena
- polja: ime i prezime, email, telefon, datum, vreme, broj osoba, posebni zahtevi
- potvrda prihvatanja uslova rezervacije
- dugme za potvrdu rezervacije
- poruka o uspešno poslatoj rezervaciji

### 1.5 Dashboard za restoran

Za restoran / administratora — praćenje rezervacija i osnovnih pokazatelja.

**Očekivani elementi:**

- kartice sa ključnim metrikama (rezervacije danas, slobodni stolovi, prosečna ocena)
- grafički prikaz rezervacija po danima
- status rezervacija (potvrđene, na čekanju, otkazane, završene)
- tabela nedavnih rezervacija (datum, vreme, gost, broj gostiju, status, akcije)
- pregled detalja rezervacije (opciono)
- promena statusa rezervacije (opciono)
