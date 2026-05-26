# PatchUp — Specifikacija projekta (KT1)

**Predmet:** Interakcija čoveka i računara  
**Akademska godina:** 2025/2026  
**Tim:** Aleksandar Stevanović, Miloš Jovanović, Vukan Radojević, Marko Sladojević

---

## Sadržaj

1. Opis aplikacije
2. Opis problema
3. Analiza korisnika
4. Analiza domena
5. Analiza zahteva
6. Limitirajući faktori i ograničenja
7. Usability
8. User persona
9. HTA dijagram najkompleksnijeg zadatka
10. Dijagram toka interfejsa (DTI)

---

## 1. Opis aplikacije

**PatchUp** je mobilna aplikacija koja korisnicima pomaže da odluče šta da urade sa pokvarenim kućnim predmetima — uz podršku veštačke inteligencije i lokalnih zajednica za popravku.

Korisnik fotografiše pokvareni predmet, ukratko opisuje kvar i u roku od nekoliko sekundi dobija strukturisanu AI procenu: o čemu se verovatno radi, koliko je popravka složena, kolika je verovatnoća uspešnog ishoda i koji je sledeći logičan korak. Na osnovu te procene, aplikacija korisnika usmerava ka jednoj od četiri putanje: uradi sam, potraži lokalnog volontera, poseti repair café ili recikliraj predmet.

PatchUp nije jednostavna mapa servisa niti generički chatbot — to je sistem za donošenje odluka koji spaja AI dijagnozu sa živom lokalnom mrežom volontera i radionica. Aplikacija je dizajnirana pre svega za mobilne uređaje i namenjena je svim korisnicima, bez obzira na tehničko predznanje.

Vizuelni identitet aplikacije je optimistično-pragmatičan: jasne kartice, vidljivi indikatori poverenja u AI preporuku, i jezik koji ohrabruje umesto da zastrašuje.

---

## 2. Opis problema

Svake godine ogromne količine funkcionalno ispravnih ili lako popravljivih kućnih predmeta završe na smetlištu — ne zato što su nepopravljivi, već zato što korisnici ne znaju šta je pokvareno, ne procenjuju da je popravka isplativa ili ne znaju gde da potraže pomoć.

Zajednice za popravku (repair cafési, volonterske radionice, lokalni hobisti) već postoje i nude besplatnu ili simboličnu pomoć. Međutim, put od „imam pokvaren predmet" do „pronašao sam adekvatnu pomoć" i dalje je fragmentisan i nepristupačan prosečnom korisniku. Nema jednostavnog mesta gde bi neko mogao da proceni da li uopšte vredi popravljati predmet, a kamoli da ga poveže sa pravom osobom ili događajem.

Rezultat je jasan: prerano odbacivanje predmeta, nepotrebna potrošnja, propuštene prilike za učenje i slabljenje lokalnih ekosistema popravke.

Sprovedena anketa (28 ispitanika) potvrđuje ovu sliku: 71,4% ispitanika ponekad ili često odlučuje da zameni pokvaren predmet umesto da ga popravi. Najveće barijere su nedostatak znanja (42,9%), nedostatak alata (39,3%) i strah da će kvar pogoršati (32,1%). Istovremeno, čak 89,3% ispitanika izjavilo je da bi sigurno ili verovatno koristilo aplikaciju koja AI-em procenjuje popravljivost predmeta i usmerava ka odgovarajućoj putanji.

PatchUp odgovara upravo na taj jaz — između svesnog odbacivanja i moguće popravke.

---

## 3. Analiza korisnika

Anketa je sprovedena online i prikupljeno je **28 odgovora**. Anketa je obuhvatala pitanja o navikama pri popravci predmeta, stavovima prema AI dijagnozi, iskustvu sa lokalnim zajednicama za popravku i željenim funkcionalnostima aplikacije.

### Demografski profil

Velika većina ispitanika pripada starosnoj grupi **18–25 godina (82,1%)**, što odgovara studentskoj populaciji. Po dvoje ispitanika dolazi iz grupa 26–35 (7,1%) i 50+ (7,1%), dok je jedan ispitanik mlađi od 18 godina (3,6%). Grupa 36–50 nije bila zastupljena. Svi ispitanici svakodnevno koriste mobilne aplikacije (prosečna ocena upotrebe aplikacija: 3,4/5).

### Navike pri popravci predmeta

Kada im se pokvari predmet, **71,4% ispitanika pokušava da ga popravi samo**, a 57,1% traži pomoć od porodice ili prijatelja. Samo 32,1% nosi predmet u servis, dok svega 14,3% predmet odmah baci.

Uprkos tome, **71,4% ispitanika ponekad ili često zamenjuje pokvarene predmete novima** umesto da ih popravlja (ponekad: 53,6%; često: 17,9%). Ovo ukazuje na raskorak između namere i stvarnog ponašanja — korisnici žele da popravljaju, ali nailaze na prepreke.

Najčešće kategorije predmeta koje se kvare:

- Elektronika (telefon, laptop, slušalice): 42,9%
- Nameštaj: 32,1%
- Mali kućni aparati: 25%
- Bicikl i mehanički predmeti: 25%
- Veliki kućni aparati: 21,4%

### Barijere pri popravci

Ispitanici su mogli odabrati više razloga zašto ne pokušavaju popravku:


| Barijera                              | Udio ispitanika |
| ------------------------------------- | --------------- |
| Nedostatak znanja o kvaru             | 42,9%           |
| Nedostatak alata                      | 39,3%           |
| Strah da će pogoršati kvar            | 32,1%           |
| Popravka deluje previše komplikovana  | 35,7%           |
| Nedostatak vremena                    | 32,1%           |
| Radije kupuju novi predmet            | 10,7%           |
| Ništa ih ne sprečava                  | 7,1%            |


Prosečna samoprocena veštine popravke iznosi **3,0/5**, a prosečna sigurnost u izvođenje jednostavnih popravki **3,5/5** — što govori o umerenom, ali nepotpunom samopouzdanju.

### Stavovi prema AI dijagnozi

- **53,6%** ispitanika bi sigurno koristilo AI aplikaciju za procenu kvara; **35,7%** bi je verovatno koristilo → ukupno **89,3% pozitivnog interesa**.
- Prosečno poverenje u preporuke AI sistema: **3,57/5**.
- Prosečna važnost da aplikacija **objasni zašto** daje određenu preporuku: **4,29/5** — ovo je jedan od najviše ocenjenih parametara u čitavoj anketi i direktno potvrđuje potrebu za transparentnom AI dijagnozom.
- Jednostavnost korišćenja aplikacije ocenjena je kao izuzetno važna: **4,39/5**.

### Iskustvo sa lokalnom zajednicom za popravku

Čak **67,9% ispitanika nema nikakvo iskustvo** sa lokalnom zajednicom za popravku (repair café, majstori iz komšiluka i sl.). Od onih koji su imali iskustvo, uglavnom se radi o pomoći iz porodičnog okruženja, a ne o organizovanim repair događajima.

Na pitanje o spremnosti da posete lokalni repair događaj: 32,1% bi definitivno posetilo, 35,7% možda, a 32,1% ne bi. Ovo ukazuje da postoji latentni interes koji može biti aktiviran pravim informacijama i usmeravanjem.

### Motivatori za popravku


| Motivacija               | Udio ispitanika |
| ------------------------ | --------------- |
| Ušteda novca             | 82,1%           |
| Učenje novih veština     | 64,3%           |
| Ekologija (manje otpada) | 21,4%           |


### Željene funkcionalnosti aplikacije


| Funkcionalnost                                    | Udio ispitanika |
| ------------------------------------------------- | --------------- |
| Prepoznavanje kvara putem slike i procena težine  | 75,0%           |
| Preporuka šta dalje (DIY / servis / zajednica)    | 67,9%           |
| Povezivanje sa lokalnim majstorima / volonterima  | 39,3%           |


### Zaključak analize korisnika

Anketa potvrđuje postojanje jasnog jaza između želje za popravkom i stvarne akcije. Korisnici su motivisani (pretežno finansijski), ali ih blokira nedostatak znanja, alata i usmeravanja. Izuzetno visoka ocena važnosti objašnjenja AI preporuke (4,29/5) direktno definiše dizajnerski zahtev: AI mora biti transparentna, a ne samo tačna. Dominantna starosna grupa (18–25) upućuje na korisnika koji je digitalno pismen i spreman da prihvati mobilnu aplikaciju kao primarni alat za donošenje odluka.

---

## 4. Analiza domena

PatchUp se pozicionira u preseku tri oblasti: **veštačke inteligencije za dijagnozu predmeta**, **ekonomije kružnosti i održivosti**, i **lokalnih zajednica za popravku**.

### Zajednice za popravku (repair cafési i slično)

Repair cafési su volonterski eventi na kojima iskusni hobisti i tehničari besplatno pomažu građanima da poprave kućne predmete. Ovaj pokret je počeo u Amsterdamu 2009. godine i danas broji više od 2.500 aktivnih lokacija u preko 35 zemalja. U Srbiji su ovakve inicijative prisutne u nekoliko gradova, ali su slabo vidljive i nedovoljno dostupne prosečnom građaninu.

### AI dijagnoza predmeta

Savremeni modeli računarskog vida (computer vision) sposobni su da identifikuju kategoriju predmeta, uoče vidljiva oštećenja i procenjuju verovatne kvarove na osnovu vizuelnih tragova. U kombinaciji sa korisničkim opisom kvara u prirodnom jeziku, moguće je generisati strukturisane procene bez pozivanja na tačnu tehničku specifikaciju. Ovo je centralni tehnički stub PatchUp platforme.

### Ekonomija kružnosti

Popravka predmeta je direktna materijalizacija principa cirkularne ekonomije. Prema podacima Evropske agencije za životnu sredinu, prosečno evropsko domaćinstvo generiše između 10 i 20 kg e-otpada godišnje. Procenjuje se da bi između 30% i 50% tog otpada moglo biti izbegnuto kvalitetnom popravkom. Ovaj kontekst daje PatchUpu i edukativnu i ekološku dimenziju.

### Postojeća rešenja i tržišna pozicija


| Rešenje               | Snage                         | Slabosti                                           |
| --------------------- | ----------------------------- | -------------------------------------------------- |
| iFixit                | Detaljna uputstva za popravku | Nema AI dijagnozu, nema lokalnu zajednicu          |
| JustFix.nyc           | Fokus na stanarske probleme   | Ograničen domen, bez AI                            |
| Repair Café (website) | Mapa radionica                | Bez dijagnoze, bez digitalne integracije           |
| Generalni chatbotovi  | Fleksibilnost                 | Nema lokalne zajednice, nema strukturisanog ishoda |


PatchUp je jedino rešenje koje integriše sve tri komponente: AI procenu, putanju popravke i lokalnu zajednicu — u jednom mobilnom toku.

---

## 5. Analiza zahteva

### 5.1 Korisnici sistema

#### Krajnji korisnik (građanin)

Osoba koja ima pokvaren kućni predmet i želi brzo i razumljivo da sazna šta može da uradi. Tehničko predznanje nije preduslov. Može biti početnik koji nikad nije popravljao ništa, ali i iskusniji korisnik koji samo treba brzu potvrdu.

#### Volonter

Hobista ili stručnjak koji može da pomogne sa određenim kategorijama predmeta. Nudi svoje usluge kroz aplikaciju, navodi oblasti ekspertize i dostupnost. Prijavljen je u sistemu i vidljiv je krajnjim korisnicima.

#### Organizator radionice

Osoba ili organizacija koja upravlja repair caféom ili sličnim lokalnim događajem. Unosi termine, lokacije i kategorije predmeta koje pokriva, i prima zahteve od korisnika.

### 5.2 Funkcionalni zahtevi

#### Zahtev 1 — Skeniranje predmeta

Korisnik može da fotografiše pokvareni predmet koristeći kameru telefona ili da otpremi sliku iz galerije. Uz fotografiju, korisnik unosi kratak opis kvara (slobodan tekst). Opciono, korisnik može ručno da izabere kategoriju predmeta ako AI nije sigurna u identifikaciju.

#### Zahtev 2 — AI dijagnoza

Na osnovu fotografije i opisa, sistem generiše karticu dijagnoze koja sadrži:

- prepoznati predmet i kategoriju,
- procenjeni kvar (jedan ili više verovatnih uzroka),
- nivo težine popravke (lako / srednje / složeno),
- skor popravljivosti (0–100%),
- indikator pouzdanosti AI procene,
- preporučeni sledeći korak.

Korisnik uvek može da vidi objašnjenje zašto je AI donela određenu preporuku.

#### Zahtev 3 — Preporuka putanje popravke

Sistem na osnovu dijagnoze nudi jednu od četiri putanje:

1. **DIY (uradi sam)** — za jednostavne kvarove, sa osnovnim smernicama,
2. **Lokalni volonter** — za kvarove koji zahtevaju veštinu, ali ne i profesionalni servis,
3. **Repair café / radionica** — za umereno složene kvarove i grupe,
4. **Reciklaža ili donacija delova** — kada popravka nije isplativa.

Korisnik može da istraži sve četiri opcije pre nego što donese odluku.

#### Zahtev 4 — Pretraga i prikaz lokalnih resursa

Aplikacija prikazuje listu repair cafea, radionica i volontera u korisnikovoj blizini. Filteri uključuju: kategoriju predmeta, udaljenost, dostupnost termina, procenu iskustva volontera. Svaki resurs ima svoju stranicu sa detaljima, komentarima i načinom kontakta ili rezervacije.

#### Zahtev 5 — Rezervacija ili zahtev za pomoć

Korisnik može da rezerviše mesto na repair caféu ili da pošalje zahtev odgovarajućem volonteru. Zahtev uključuje dijagnozu predmeta (automatski priloženu), fotografiju i kontakt podatke. Korisnik dobija potvrdu i obaveštenje o statusu zahteva.

#### Zahtev 6 — Praćenje ishoda popravke

Nakon popravke, korisnik beleži ishod: uspešno popravljeno / delimično popravljeno / nije popravljivo / darovano za delove / reciklirano. Ovaj unos ažurira lični profil korisnika i sistem impakt statistike.

#### Zahtev 7 — Impakt statistika

Aplikacija korisnicima prikazuje procenjeni uticaj njihovih odluka:

- ušteda u novcu (procenjena vrednost popravke vs. kupovine novog),
- izbegnuta količina otpada (u kg),
- broj predmeta uspešno popravljenih,
- doprinos lokalnoj zajednici.

Organizatori i volonteri vide agregatne statistike za svoje aktivnosti.

#### Zahtev 8 — Profil korisnika i istorija

Registrovani korisnik ima profil koji čuva istoriju skeniranih predmeta, prethodnih dijagnoza, ishoda i rezervacija. Volonteri i organizatori imaju proširene profile sa prikazom ekspertize, ocenama i aktivnim terminima.

#### Zahtev 9 — Registracija i prijava

Korisnik može da koristi aplikaciju bez registracije za skeniranje i dijagnozu, ali registracija je neophodna za rezervacije, komunikaciju sa volonterima i praćenje istorije. Prijava se vrši putem e-mail adrese ili Google/Apple naloga.

#### Zahtev 10 — Sistem ocenjivanja i povratnih informacija

Korisnici ocenjuju volontere i repair café događaje nakon interakcije (1–5 zvezdica + kratak komentar). Volonteri i organizatori ocenjuju kvalitet zahteva i komunikacije sa korisnicima. Ocene su vidljive na profilima i utiču na vidljivost u pretragama.

### 5.3 Nefunkcionalni zahtevi

- AI dijagnoza treba da bude generisana u manje od 5 sekundi od potvrde unosa.
- Aplikacija mora biti upotrebljiva bez tehničkog predznanja — sve akcije moraju biti razumljive korisniku koji nikad nije popravljao predmete.
- Interfejs mora biti dostupan osobama sa slabijim vidom (podrška za povećanje fonta, dovoljan kontrast).
- Svi lični podaci korisnika moraju biti šifrovani u prenosu i skladištu.
- Aplikacija mora raditi na Android i iOS platformama.

---

## 6. Limitirajući faktori i ograničenja

Razvoj i primena PatchUp aplikacije suočava se sa nekoliko ograničenja koja direktno utiču na dizajn i korisničko iskustvo.

**Tačnost AI dijagnoze** direktno zavisi od kvaliteta fotografije koju korisnik dostavi. Loša osvetljenost, nepogodan ugao ili zamagljena slika mogu dovesti do netačne ili nepouzdane procene. Aplikacija treba da korisnika jasno uputi kako da napravi upotrebljivu fotografiju, ali ne može garantovati tačnost ako ulazni podaci nisu dovoljno kvalitetni.

**AI ne zamenjuje fizički pregled.** Sistem može proceniti verovatne uzroke kvara na osnovu vizuelnih tragova, ali ne može detektovati unutrašnja oštećenja, ismeriti električne vrednosti niti proveriti mehaničke komponente. Korisnik mora biti svestan da je AI preporuka vodič, a ne dijagnoza sa garancijom.

**Dostupnost lokalnih resursa** nije ujednačena. U većim gradovima repair cafési i volonteri postoje u zadovoljavajućem broju, ali u manjim sredinama ova mreža može biti slabo razvijena ili potpuno odsutna. Aplikacija ne može kreirati resurse koji ne postoje — može ih samo prikazati.

**Zavisnost od internet veze.** AI analiza se izvršava na serveru i zahteva aktivnu vezu. Korisnici bez pristupa internetu ili sa sporom vezom neće moći koristiti centralnu funkcionalnost aplikacije.

**Motivacija volontera i organizatora** je preduslov za funkcionisanje zajedničkog sloja platforme. Ako volonteri ne ažuriraju svoju dostupnost ili organizatori ne unose termine radionica, korisnici će dobijati netačne ili zastarele informacije.

**Zaštita podataka.** Fotografije kućnih predmeta i opisi kvarova mogu posredno otkrivati informacije o korisniku (tip doma, imovinska situacija). Svi podaci moraju biti obrađivani u skladu sa važećim propisima o zaštiti ličnih podataka.

---

## 7. Usability

Dizajn PatchUp aplikacije mora odgovoriti na specifične izazove koji proizlaze iz ciljne grupe i prirode zadatka. Korisnici dolaze bez tehničkog predznanja, u situaciji nesigurnosti, i traže jasno usmeravanje — ne informaciono opterećenje.

**Pristupačnost** je primarni usability zahtev. Sve akcije moraju biti razumljive korisniku koji nikad nije popravljao predmete i koji nema iskustva sa sličnim aplikacijama. Navigacija mora biti konzistentna, a terminologija jednostavna i bez žargona. Aplikacija mora podržavati povećanje fonta i dovoljan kontrast za osobe sa oštećenjem vida.

**Transparentnost AI procene** je ključna za izgradnju poverenja. Anketa pokazuje da 89,3% ispitanika želi da razume *zašto* je AI dala određenu preporuku (prosečna ocena važnosti objašnjenja: 4,29/5). Svaka preporuka mora biti praćena kratkim objašnjenjem i indikatorom pouzdanosti. Korisnik nikad ne sme biti u situaciji da sledi preporuku bez razumevanja njene osnove.

**Efikasnost** toka je kritična. Od otvaranja aplikacije do prikaza preporuke ne sme proći više od 4 ekrana. Korisnik koji je u nedoumici ne sme biti blokiran dugim formama ili višestrukim koracima pre nego što dobije vrednost.

**Povratne informacije** moraju biti trenutne i jasne. Svaka važna akcija (fotografija potvrđena, analiza pokrenuta, zahtev poslat, rezervacija potvrđena) mora biti propraćena vidljivim i razumljivim odgovorom sistema — korisnik uvek mora znati šta se dešava i šta je sledeći korak.

**Pouzdanost.** Aplikacija mora stabilno raditi i pri slabijoj internet vezi, uz prikazivanje stanja učitavanja i jasnih poruka o grešci. Korisnik ne sme ostati bez informacije ako nešto ne radi.

**Zadovoljstvo korisnika.** Vizuelni jezik aplikacije treba biti optimistično-pragmatičan — fokus na rešenje, ne na problem. Jezik koji ohrabruje popravku (ne zastrašuje), kratke potvrde pozitivnih ishoda i praćenje impakta treba da ostave korisniku osećaj da je doneo dobru odluku.

---

## 8. User persona

---

### Persona 1 — Krajnji korisnik

**Ime:** Jovana Nikolić  
**Godine:** 34  
**Zanimanje:** Grafički dizajner, radi od kuće  
**Lokacija:** Novi Sad  
**Tehnička pismenost:** Srednja — koristi pametni telefon, poznaje standardne aplikacije, ali ne razume tehničke detalje elektronike

**Biografija:**  
Jovana živi sama u stanu, vodi računa o troškovima i pokušava da živi što održivije. Nedavno joj je prestao da radi blender koji je kupila pre tri godine. Nije sigurna šta je pokvareno, ali smeta joj ideja da ga odmah baci. Čula je za repair café u svom gradu, ali ne zna kako da proceni da li je njen blender uopšte vredan popravke i kakva je procedura.

**Ciljevi:**

- Brzo saznati da li predmet može biti popravljen i ko može da pomogne
- Izbegavati nepotrebne troškove i odbacivanje predmeta koji se mogu popraviti
- Osećati se informisano i sigurno pri donošenju odluke

**Frustracije:**

- Nema tehničkog znanja da proceni kvar
- Ne zna gde da potraži pomoć lokalno
- Boji se da će potrošiti vreme na repair café samo da bi saznala da je predmet nepopravljiv
- AI rešenja često daju odgovore bez objašnjenja, što ne gradi poverenje

**Citat:**  
*„Ne trebaju mi tehničke informacije — samo hoću da znam da li vredi pokušati i kome da se javim."*

**Motivacija za korišćenje PatchUp-a:**  
Jovana traži brzo i jasno usmeravanje. AI dijagnoza sa indikatorom poverenja i direktna veza ka lokalnom repair caféu su tačno ono što je zaustavlja od odbacivanja predmeta bez pokušaja.

---

### Persona 2 — Volonter

**Ime:** Dragan Petrović  
**Godine:** 52  
**Zanimanje:** Elektrotehničar u penziji  
**Lokacija:** Beograd — Zemun  
**Tehnička pismenost:** Visoka u svom domenu (elektronika, mali aparati), umerena u mobilnim aplikacijama

**Biografija:**  
Dragan je radio 25 godina kao elektrotehničar i dalje sa zadovoljstvom popravlja različite uređaje — za sebe, za porodicu, za komšije. Povremeno dolazi na repair café u svom kraju, ali smatra da se vreme ne koristi efikasno jer korisnici dolaze sa predmetima za koje on nije specijalizovan ili koji su nepopravljivi.

**Ciljevi:**

- Pomoći ljudima koji imaju pokvarene predmete u oblasti njegove ekspertize
- Efikasno upravljati dostupnošću i tipovima zahteva koje prima
- Biti vidljiv u zajednici kao pouzdan volonter

**Frustracije:**

- Gubi vreme na repair caféima na predmete izvan njegove ekspertize
- Nema način da unapred vidi kakvi predmeti dolaze
- Korisnici često ne znaju da opišu kvar, što otežava pripremu

**Citat:**  
*„Volim da pomažem, ali je važno da mi neko kaže unapred šta dolazi — da ne trošim vreme ni ja ni oni."*

**Motivacija za korišćenje PatchUp-a:**  
PatchUp mu omogućava da filtrira zahteve po kategoriji, vidi AI dijagnozu pre nego što prihvati slučaj i organizuje svoju dostupnost — čime se vreme bolje koristi za sve strane.

---

## 9. HTA dijagram najkompleksnijeg zadatka

Najkompleksniji zadatak u PatchUp aplikaciji je: **„Proceniti popravljivost predmeta i odabrati putanju popravke"**.

Ovaj zadatak je najsloženiji jer zahteva interakciju korisnika sa AI sistemom, interpretaciju rezultata bez tehničkog predznanja i donošenje odluke sa višestrukim ishodima.

---

**0. Proceniti popravljivost predmeta i odabrati putanju popravke**

**1. Pripremiti predmet i pokrenuti skeniranje**

- 1.1 Otvoriti aplikaciju
- 1.2 Pritisnuti dugme „Skeniraj predmet"
- 1.3 Odabrati između kamere i galerije

**2. Fotografisati predmet**

- 2.1 Uokviriti predmet tako da kvar bude vidljiv
- 2.2 Snimiti fotografiju
- 2.3 Pregledati fotografiju
  - 2.3.1 (Ako fotografija nije jasna) Ponoviti slikanje → vrati se na 2.1
  - 2.3.2 (Ako fotografija je jasna) Potvrditi fotografiju

**3. Opisati kvar**

- 3.1 Uneti kratak opis problema u slobodnom tekstu
- 3.2 (Opciono) Odabrati kategoriju predmeta iz predložene liste
- 3.3 Potvrditi unos i pokrenuti analizu

**4. Čekati i pratiti AI analizu**

- 4.1 Pratiti indikator napretka analize
- 4.2 (Ako analiza traje duže od 10 sekundi) Dobiti obaveštenje o kašnjenju

**5. Pregledati karticu dijagnoze**

- 5.1 Pročitati prepoznati predmet i kategoriju
- 5.2 Pročitati procenjeni uzrok kvara
- 5.3 Uočiti nivo težine popravke (vizuelni indikator)
- 5.4 Pročitati skor popravljivosti
- 5.5 Proveriti indikator pouzdanosti AI procene
  - 5.5.1 (Ako pouzdanost niska) Pročitati objašnjenje nesigurnosti
  - 5.5.2 (Ako pouzdanost visoka) Nastaviti ka preporuci
- 5.6 (Opciono) Pritisnuti „Zašto ova preporuka?" za detaljno objašnjenje

**6. Razmotriti preporučenu putanju popravke**

- 6.1 Pročitati primarnu preporuku sistema
- 6.2 Pregledati alternativne putanje
- 6.3 Doneti odluku o putanji

**7. Realizovati odabranu putanju**

- 7.1 (DIY) Dobiti osnovne smernice i linkove ka resursima
- 7.2 (Volonter) Pregledati profil volontera i poslati zahtev → nastaviti u Zahtevu 5
- 7.3 (Radionica) Pregledati listu radionica i rezervisati mesto → nastaviti u Zahtevu 5
- 7.4 (Reciklaža) Dobiti informacije o reciklažnim centrima u blizini

**Plan izvršavanja:**  
Koraci 1–4 su sekvencijalni. Korak 5 uključuje paralelno razmatranje više informacija na kartici dijagnoze. Korak 6 je korak procene koji ne mora biti linearan. Korak 7 se grana zavisno od odluke korisnika.

---

## 10. Dijagram toka interfejsa (DTI)

DTI opisuje tok kretanja korisnika kroz aplikaciju od početnog ekrana do beleženja ishoda.

### Ekrani aplikacije


| Oznaka | Naziv ekrana                                   |
| ------ | ---------------------------------------------- |
| E1     | Početni ekran (Home)                           |
| E2     | Ekran skeniranja predmeta                      |
| E3     | Ekran unosa opisa kvara                        |
| E4     | Ekran obrade (AI analiza u toku)               |
| E5     | Kartica dijagnoze                              |
| E6     | Ekran objašnjenja AI procene                   |
| E7     | Ekran putanje popravke                         |
| E8     | Lista lokalnih resursa (radionice i volonteri) |
| E9     | Profil radionice / volontera                   |
| E10    | Ekran rezervacije / slanja zahteva             |
| E11    | Potvrda i praćenje statusa                     |
| E12    | Ekran beleženja ishoda                         |
| E13    | Ekran impakt statistike                        |
| E14    | Korisnički profil i istorija                   |
| E15    | Ekran registracije / prijave                   |


### Tok za krajnjeg korisnika (primarni scenario)

```
E1 (Početni ekran)
  │
  ├─[Skeniraj predmet]──► E2 (Skeniranje)
  │                          │
  │                       [Fotografija potvrđena]
  │                          │
  │                          ▼
  │                       E3 (Opis kvara)
  │                          │
  │                       [Potvrdi unos]
  │                          │
  │                          ▼
  │                       E4 (AI obrada...)
  │                          │
  │                       [Analiza završena]
  │                          │
  │                          ▼
  │                       E5 (Kartica dijagnoze)
  │                          │
  │                 ┌────────┴────────┐
  │           [Zašto ova        [Izaberi putanju]
  │           preporuka?]            │
  │                 │                ▼
  │                 ▼             E7 (Putanja popravke)
  │              E6 (Objašnjenje)    │
  │                 │       ┌────────┼────────────┐
  │                 │    [DIY]  [Volonter]  [Radionica]  [Reciklaža]
  │                 │       │       │            │              │
  │                 │       ▼       ▼            ▼              ▼
  │                 │  smernice  E8 (Lista)   E8 (Lista)    info o
  │                 │  i resursi     │            │         recikliranju
  │                 │               ▼            ▼
  │                 │            E9 (Profil)  E9 (Profil)
  │                 │               │            │
  │                 │               ▼            ▼
  │                 │           E10 (Zahtev / Rezervacija)
  │                 │               │
  │                 │               ▼
  │                 │           E11 (Potvrda i status)
  │                 │               │
  │                 └───────────────┘
  │                                 │
  │                         [Popravka završena]
  │                                 │
  │                                 ▼
  │                           E12 (Beleži ishod)
  │                                 │
  │                                 ▼
  │                           E13 (Impakt statistika)
  │
  ├─[Profil]──────────────────► E14 (Profil i istorija)
  │
  └─[Prijava / Registracija]──► E15 (Registracija)
```

### Napomene o navigaciji

- Sa svakog ekrana korisnik može da se vrati na prethodni ekran (standardna navigacija unazad).
- E5 (Kartica dijagnoze) je čvorišni ekran — dostupan je i iz istorije na profilu (E14).
- Korisnik koji nije registrovan može koristiti E1–E7 bez prijave; registracija postaje obavezna pri pokušaju otvaranja E10.
- E13 je dostupan i direktno sa E14, gde korisnik vidi kumulativnu statistiku svih predmeta.

---

*Kraj specifikacije — PatchUp, KT1*