# CityBlock — primer specifikacije (Markdown)

## Opis aplikacije

CityBlock je mobilna aplikacija namenjena građanima, koja pruža informacije o zakazanim protestima. Glavni cilj aplikacije je da korisnicima omogući da jednostavno vide gde se protesti dešavaju, informacije o njima, dodaju nove proteste, označe da učestvuju na njima ili dobiju informacije kako bi izbegli zagušenje. Kroz CityBlock, korisnici mogu anonimno pregledati događaje i prijaviti validnost protesta. Na taj način aplikacija ubrzava donošenje odluka kod kretanja gradom i poboljšava sigurnost svih učesnika u saobraćaju.

## Opis problema

Česte blokade saobraćajnica zbog protesta ili skupova u gradu stvaraju nepredvidive zastoje. Trenutno ne postoji centralizovana platforma koja bi ažurno obaveštavala o takvim dešavanjima u realnom vremenu. Ovo može dovesti do toga da korisnik propusti protest na kome bi inače učestvovao ili da ostane zaglavljen u saobraćaju bez znanja o tome kojim putem bi mogao doći do željene destinacije. Anketa među potencijalnim korisnicima pokazuje da bi većina volela da koristi aplikaciju koja rešava ove probleme - učesnici ankete ističu da bi im bio od pomoći prikaz protesta na mapi uz informacije o njihovom trajanju. U tom kontekstu, CityBlock teži da smanji nejasnoće i omogući građanima da unapred budu informisani o dešavanjima na ulicama.

## Analiza korisnika

Ciljna grupa CityBlock aplikacije su svi građani bez obzira na godine, pol ili političko opredeljenje. Posebno je naglašeno da CityBlock nije ni u kakvoj vezi sa političkim pokretima; njena namena je isključivo informativna. Mogućnost anonimnog korišćenja aplikacije je važna većini ispitanika, jer tako mogu prijavljivati dešavanja bez otkrivanja ličnog identiteta (u anketi su mnogi naveli da im je anonimnost “veoma bitna”).

## Analiza domena

CityBlock pripada domenu urbane infrastrukture i javne bezbednosti, sa fokusom na saobraćaj i kretanje kroz grad. Prema podacima ministarstva unutrašnjih poslova, u Srbiji je u toku prethodne godine održano 34.552 javna okupljanja u preko 400 gradova. Takođe, ove godine je u Srbiji održan najveći protest u istoriji zemlje sa procenjenih 300.000 učesnika. Ovi podaci jasno govore o aktuelnosti teme protesta kao i potencijalno velikom broju korisnika koji žele da se informišu o njima. Pored Srbije primećen je porast broja protesta i u ostatku sveta, što govori o potencijalnoj potražnjii u drugim zemljama.

## Analiza zahteva

### Funkcionalni zahtevi

#### Prikaz na mapi

- Glavna funkcija je geografski prikaz trenutnih i zakazanih protesta na interaktivnoj mapi grada.
- Korisnik može da vidi preciznu lokaciju protesta i osnovne informacije o njemu.
- Pregled događaja po danima.

#### Informacije o trajanju i karakteristikama

- Za svaki protest prikazuju se procenjeno vreme trajanja i aktuelni komentari sa opcionim slikama.

#### „Tu sam / učestvujem“ i „Prijavi netačnost“ mehanizam

- Samo korisnici prisutni na licu mesta mogu da potvrde prisustvo („Tu sam / učestvujem“) ili prijave netačnost događaja.
- Broj ucesnika vidljiv je svim korisnicima, što doprinosi proceni verodostojnosti i veličini protesta.

#### Dodavanje novih protesta

- Proteste mogu da dodaju samo korisnici kojima se veruje, što je određeno trust faktorom koji su stekli korišćenjem aplikacije.
- Prilikom kreiranja protesta korisnik unosi predviđeno vreme početka protesta kao i procenjeno vreme završetka, kao i lokaciju odvijanja protesta.

#### Anonimnost i privatnost

- Aplikacija omogućava korišćenje i bez registracije.
- Korisnici mogu da ostanu anonimni.

#### Real-time komentarisanje sa TTL logikom

- Komentarisanje je dozvoljeno samo korisnicima koji su na lokaciji.
- Samo prisutni korisnici mogu da lajkuju komentare.
- Komentar bez lajkova automatski nestaje nakon isteka vremena (TTL).
- Lajkovi produžavaju trajanje komentara i povećavaju njegovu vidljivost i verodostojnost.

#### Trust faktor sistem

- Akcije (prisustvo, prijave netačnosti, lajkovanje komentara) utiču na trust faktor korisnika.
- Algoritam određuje pozitivnu ili negativnu promenu trust faktora u zavisnosti od potvrda zajednice.
- Samo korisnici iznad određenog praga trust faktora mogu kreirati buduće proteste.
- Sistem startuje sa nekoliko pouzdanih profila sa unapred dodeljenim visokom trust faktorom.

#### Administratorske funkcije (CRUD + moderacija)

- Administratori imaju mogućnost CRUD operacija nad korisnicima i protestima (kreiranje, ažuriranje, brisanje, pregled).
- Admini mogu da restore-uju proteste koje je algoritam automatski obrisao, ako smatraju da je došlo do greške.

### Tehnički zahtevi

#### GIS tehnologije

- Aplikacija koristi Google Maps ili OpenStreetMap za prikaz mape i navigaciju.

#### Bezbednost komunikacije

- Svi podaci i komunikacija su šifrovani.

#### Responzivnost i platforme

- CityBlock će biti optimizovan za Android i iOS uređaje različitih rezolucija.

## Usability

Pri dizajnu korisničkog iskustva primenićemo osnovne principe usability-a kako bi aplikacija bila što lakša za korišćenje:

- Pristupačnost: Interfejs će biti jasan i čitljiv, tako da je primenjiv i na osobe sa smanjenom vidnom osetljivošću ili drugim invaliditetom. Navigacija će biti jednostavna i konzistentna na svim stranicama aplikacije.
- Intuitivnost: Elementi interfejsa (dugmad, ikone, meniji) biće postavljeni logički i jasno označeni, kako bi korisnici odmah razumeli funkciju svake opcije bez potrebe za dugim uputstvima. Primarni tok rada (npr. pregled mape i klik na protest) biće minimalan, tako da korisnik brzo pronađe ključne informacije.
- Efikasnost: Aplikacija će omogućiti korisnicima da postignu svoje ciljeve sa što manje koraka. Na primer, od otvaranja aplikacije do prikaza detalja o protestu ne sme proći više nego nekoliko dodira ekrana. Obezbedićemo brzo učitavanje mape i informacija o događajima, kako bi korisnici mogli da reaguju momentalno.
- Pouzdanost: Backend i baze će biti projektovani tako da obezbede stabilan rad bez čestih padova ili grešaka. Korisnici moraju moći da se oslone na to da će aplikacija raditi pravilno čak i pri velikom broju aktivnih događaja ili prijava.
- Zadovoljstvo korisnika: Interfejs će biti moderan i čist, a dobro projektovana korisničko iskustvo i jasne povratne informacije (npr. poruka o uspešnoj prijavi netačnosti) motivisaće korisnike da nastave da koriste aplikaciju.

Primena ovih principa osigurava da CityBlock bude inkluzivan alat prilagođen širokoj publici, što je ključna komponenta uspeha aplikacije.

## Dijagram toka interfejsa (DTI)

U originalnom PDF primeru je prisutan i DTI.
