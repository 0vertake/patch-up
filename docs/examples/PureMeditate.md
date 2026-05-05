# Pure Meditate — primer specifikacije (Markdown)

Specifikacija projekta  
Vladimir Popov SV29/2021  
Balša Bulatović SV37/2021  
Momir Milutinović SV39/2021  
Teodor Vidaković SV33/2021  
April, 2024

## Sadržaj

1. Opis aplikacije  
2. Opis problema  
3. Analiza korisnika  
4. Analiza domena  
   - 4.1 Postojeća rešenja  
5. Analiza zahteva  
   - 5.1 Korisnici  
     - 5.1.1 Meditator  
     - 5.1.2 Administrator  
   - 5.2 Funkcionalni zahtevi  
   - 5.3 Nefunkcionalni zahtevi  
6. Limitirajući faktori, ograničenja i preduslovi  
7. Usability  
8. Strategije privlačenja korisnika  
9. Monetizacija aplikacije  
10. Dijagram toka interfejsa (DTI)  
   - 10.1 Meditator  
   - 10.2 Administrator

## 1 Opis aplikacije

Pure Meditate je mobilna aplikacija koja pruža korisnicima alate, tehnike i resurse za praktikovanje meditacije i poboljšanje mentalnog zdravlja. Cilj aplikacije je omogućiti korisnicima pristup različitim vrstama meditativnih praksi, vežbi disanja, meditativnoj muzici i vodičima za poboljšanje koncentracije i mindfulness-a.

Pure Meditate stavlja naglasak na korisničko iskustvo pružajući jednostavan i intuitivan intefejs koji omogućuje korisnicima da lako pronađu željene meditacije. Kroz svoje raznolike funkcionalnosti, aplikacija podržava korisnike u njihovom putovanju ka boljem mentalnom zdravlju, unapređujući njihovu sposobnost upravljanja stresom, fokusiranja uma i postizanja emocionalne ravnoteže.

## 2 Opis problema

U današnjem modernom društvu, ubrzani način života, konstantan pritisak i zahtevi koje postavljaju posao, škola, porodica i društvo često dovode do široko rasprostranjenih problema kao što su stres, anksioznost i nedostatak pažnje. Ovi problemi imaju negativne posledice na mentalno zdravlje pojedinaca i doprinose opštem osećaju nezadovoljstva i disbalansa.

Jedan od ključnih izazova s kojim se ljudi suočavaju jeste nedostatak vremena i resursa da pronađu efikasne tehnike za mentalno i fizičko rasterećenje. Užurban način života često ostavlja malo ili nimalo vremena za brigu o mentalnom zdravlju, što može rezultovati lošim fizičkim i emocionalnim stanjem.

Tradicionalno, meditacija se smatrala složenom praksom koja zahteva puno vremena, stručnost i posvećenost, što čini da mnogi ljudi odustanu pre nego što čak i počnu. Osim toga, neodstatak pristupačnih resursa ili nedovoljno znanje o različitim tehnikama meditacije može dodatno otežati pojedincima da započnu praksu meditacije i da kontinuirano koriste njene benefite.

Sve ovo dovodi do toga da ljudi podležu neadekvatnim, skupim i nezdravim metodatama za oslobađanje stresa, koje loše utiču na njihovo psihičko i fizičko zdravlje.

Aplikacija za meditaciju kao što je Pure Meditate prepoznaje ovaj problem i nudi rešenje. Pruža korisnicima jednostavan i pristupačan način za praktikovanje meditacije, bilo da su početnici ili već iskusni u ovoj praksi. Ova aplikacija omogućava korisnicima da brzo pronađu resurse i tehnike koje odgovaraju njihovim potrebama, pružajući im alate za suočavanje sa stresom, umirenje uma i poboljšanje mentalnog blagostanja. Time se ublažava ovaj problem i omogućava ljudima da aktivno brinu o svom mentalnom zdravlju čak i pod ovakvim okolnostima sveta u kojem živimo.

## 3 Analiza korisnika

Na osnovu sprovedene ankete, koja broji 48 ispitanika, pruženi su važni uvidi u navike, stavove i potrebe potencijalnih korisnika aplikacije za meditaciju. Evo ključnih zaključaka iz ove analize:

1. Niska stopa meditiranja: Većina ispitanika (79%) ne praktikuje meditaciju. Glavni razlozi za to uključuju manjak vremena, religiozne razloge i percepciju meditacije kao dosadne aktivnosti. Ovi rezultati ukazuju na potrebu za alatom koji bi olakšao i učinio privlačnijim praktikovanje meditacije za ljude koji se suočavaju sa ovim preprekama.
2. Nedostatak iskustva na aplikacijama za meditaciju: iako većina ispitanika ne meditira, takođe je značajan broj (81.25%) ljudi koji nije koristio nijednu aplikaciju za meditaciju. To sugeriše da postoji praznina u tržištu za aplikacije koje bi privukle i osposobile ljude da počnu praktikovati meditaciju putem digitalnih alata.
3. Identifikovane potrebe korisnika: Ispitanici su izrazili potrebu za poboljšanjem koncentracije, smanjenjem stresa i kontrolom anksioznosti. Ovi nalazi pokazuju da postoje jasne potrebe za alatima koji bi podržali mentalno blagostanje i emocionalnu stabilnost korisnika.
4. Željene funkcionalnosti aplikacije: Najveći broj ispitanika izrazio je želju za prisustvom pozadinske meditativne muzike u aplikaciji. Osim toga, postojala je potreba za mehanizmom podsetnika koji bi korisnicima pomogao da ostanu dosledni u svojoj praksi meditacije. Ovi zahtevi ukazuju na važnost prisustva funkcionalnosti koje podržavaju opuštanje i kontinuiranu praksu meditacije.

Na osnovu ove analize, jasno je da postoji potreba za razvojem aplikacije za meditaciju koja bi bila prilagođena potrebama korisnika. Ova aplikacija treba da motiviše korisnike da redovno prakikuju meditaciju kroz personalizovane podsetnike i sadržaj koji odgovara njihovim potrebama.

## 4 Analiza domena

Aplikacija za meditaciju ima širok domen koji obuhvata različite aspekte mentalnog zdravlja i tehnike za unapređenje emocionalne ravnoteže. Ovaj domen se sastoji od sledećih ključnih elemenata:

1. Meditacija: Centralni deo aplikacije je meditacija, koja može uključivati različite pristupe kao što su mindfulness meditacija, meditacija mantrama, meditacija pokreta (yoga, tai chi) i druge. Svaka od ovih tehnika ima svoje specifične koristi i ciljeve, te aplikacija treba pružiti raznolikost kako bi korisnici mogli pronaći ono što im najviše odgovara.
2. Mindfulness: Osim tradicionalnih meditativnih praksi, aplikacija bi trebala sadržati i elemente mindfulness-a. To uključuje tehnike za svesno prisustvo u sadašnjem trenutku, posmatranje misli i emocija bez prosuđivanja, kao i razvijanje saosećanja i empatije.
3. Disanje: Tehnike disanja su ključne za smirivanje uma i tela. Aplikacija bi trebalo da sadrži vodiče i vežbe za duboko disanje, ritmičko disanje, dijafragmalno disanje i druge tehnike koje pomažu u opuštanju i smanjenju stresa.
4. Relaksacija: Osim meditativnih praksi, aplikacija može ponuditi i sadržaj za opuštanje tela i uma, kao što su vodiči za progresivnu mišićnu relaksaciju, vizualizacije opuštajućih pejzaža i zvukova prirode, te tehnika za opuštanje uma poput autogenog treninga.
5. Upravljanje stresom i poboljšanje mentalne otpornosti: Aplikacija treba da sadrži alate i tehnike za upravljanje stresom u svakodnevnom životu. To može uključivati tehnike za reagovanje na stresne situacije, kao i vežbe za jačanje mentalne otpornosti i emocionalne stabilnosti.

Kroz integraciju ovih različitih elemenata, aplikacija za meditaciju postaje sveobuhvatan alat za poboljšanje mentalnog zdravlja i dobrobiti korisnika. Ova raznolikost omogućava korisnicima da pronađu pristup koji im najbolje odgovara i da kontinuirano razvijaju svoju praksu u skladu sa svojim potrebama i ciljevima.

### 4.1 Postojeća rešenja

Calm je dobrostojeća aplikacija za meditaciju sa preko 100 miliona preuzimanja. Poznata je po zvucima prirode i opuštajućim pričama pred spavanje. Calm takođe nudi i sistem za praćenje osećanja i kurseve koje predaju vodeći stučnjaci u polju meditacije. Nedostatak ove aplikacije je to što nema sistem za podsećanje korisnika da meditiraju.

Headspace je takođe popularna aplikacija za meditaciju, koja je primarno namenjena početnicima. Ova aplikacija pruža velik broj vođenih meditacija i mindfulness vežbi koje se mogu uraditi za samo par minuta. Iako Headspace ima širok izbor vežbi, one se ne razlikuju puno i ne fokusiraju se na specifične domene mentalnog zdravlja.

## 5 Analiza zahteva

### 5.1 Korisnici

#### 5.1.1 Meditator

Obični korisnici koji rade vežbe u aplikaciji. Poseduju različite nivoe znanja upotrebe telefona. Većinski nisu upoznati sa domenom aplikacije ili su početnici, ali mogu biti i iskusni u domenu. Ukoliko korisnik nikad nije imao dodira sa meditacijom, postoji mogućnost da ima predrasude ili pogrešna ubeđena koja se tiču meditacije. Korisnici mogu imati probleme sa mentalnim zdravljem poput depresije, anksioznosti i poremećaja pažnje, koje žele da reše ili ublaže praktikovanjem raznih tehnika meditacije. Moguće je da je korisnik oštećenog vida ili sluha.

#### 5.1.2 Administrator

Administratori postavljaju meditacije, koje dolaze iz eksternih izvora, na platformu. Meditacije se dostavljaju u vidu audio zapisa i tekstova njihovih transkripata. Ova grupa korisnika poseduje umeren do visok nivo poznavanja rada na računaru, ali ne mora biti upoznata sa domenom aplikacije.

### 5.2 Funkcionalni zahtevi

1. Slušanje meditacije: Meditator vežba meditaciju slušanjem audio zapisa postavljenih od strane administratora. Ukoliko je snimljeno više verzija meditacije, moguće je izabrati naratora i dužinu meditacije.
2. Pregled transkripta meditacije: Korisnik može sam da pročita transkript svake meditacije kojoj ima pristup.
3. Preuzimanje meditacija: Korisnik može da preuzme meditaciju na svoj uređaj kako bi mogao da joj pristupi kada nije povezan na internet.
4. Preuzimanje transkripta: Za svaku meditaciju moguće je preuzeti transkript. Transkripti se čuvaju na korisnikovom uređaju.
5. Tajmer za meditaciju: Korisnik može sam da meditira time što će postaviti tajmer i nakon isteka tajmera će biti zvučno obavešten da mu je meditacija gotova. Moguće je postaviti i periodična obaveštenja u toku meditacije kako bi korisnik znao koliko je vremena prošlo od početka meditacije.
6. Pretraga vežbi: Korisnik može da traži vežbe po njihovom nazivu, tehnici meditiranja ili oblasti mentalnog zdravlja na koju se odnose.
7. Podsetnici: Korisnik može da podesi podsetnike koji će ga svakog dana u isto vreme podsećati da bi trebalo da meditira. Korisnik može da isključi podsetnike kad mu nisu više potrebni.
8. Omiljene meditacije: Korisnik može da označi meditaciju kao omiljenu i može da pogleda listu svojih omiljenih meditacija. Korisnik može da ukloni meditacije sa liste omiljenih. Korisnik mora biti prijavljen da bi mogao da označava meditacije kao omiljene.
9. Meditacija dana: Aplikacija treba svakog dana da korisnicima preporuči meditaciju koju bi mogli da odrade tog dana. Ova meditacija može biti ista za sve korisnike aplikacije. Pojedinačna meditacija ne sme da se pojavi dva dana zaredom.
10. Statistika: Korisnik može da vidi sledeće statistike o svom korišćenju aplikacije:
   - Koliko dana zaredom nije propustio da meditira (streak)
   - Koliko vremena je proveo meditirajući u aplikaciji
   - Broj meditacija koje je odradio
   - Koliko dana je odradio bar jednu meditaciju
11. Korisnički nalozi: Korisnik može da napravi nalog i da se prijavi na svoj nalog u aplikaciji.
12. Online pomoć: Aplikacija bi trebalo da pruži sistem onlajn pomoći koji objašnjava korisnicima kako se koristi aplikacija i daje odgovore na česte nedoumice o meditaciji uopšte (FAQ).
13. Pretplata: Registrovani korisnici mogu da se pretplate na premium nalog kako bi imali pristup većem broju meditacija i uklonili reklame. Korisnik mora da unese informacije o svojoj platnoj kartici kako bi se pretplatio. Naplata se vrši periodično (mesečno, godišnje,...) sa unete platne kartice.

### 5.3 Nefunkcionalni zahtevi

- Aplikacija bi trebalo da se učitava za manje od 5 sekundi.
- Aplikacija bi trebalo da bude dostupna 99% vremena.
- Aplikacija bi trebalo da ima interfejs na engleskom i srpskom jeziku.
- Svi osetljivi podaci korisnika moraju biti šifrovani kako bi se omogućila zaštita podataka o ličnosti.

## 6 Limitirajući faktori, ograničenja i preduslovi

Jedno od glavnih ograničenja koje će uticati na dizajn interfejsa aplikacije jeste da su korisniku najverovatnije zatvorene oči dok meditira. Stoga će sva komunikacija sa korisnikom tokom meditacije morati da bude vršena putem zvuka. Dodatno, meditacija zahteva posvećenost i koncentraciju, te se korisnik ne može prekidati ili ometati u ovom delu aplikacije. Stoga bi bilo nepreporučljivo stavljati reklame u toku same meditacije.

Preduslov za puštanje ovakve aplikacije u upotrebu je dostupnost meditacija u aplikaciji. Za potrebe testiranja, meditacije će biti preuzete sa javno dostupnih izvora na internetu i uvezene u aplikaciju. Da bi aplikacija mogla da uđe u širu upotrebu, neophodno je ostvariti saradnju sa instruktorima meditacije, koji bi snimili meditacije za našu aplikaciju.

## 7 Usability

Razvoj aplikacije za meditaciju zahteva poseban fokus na korisničko iskustvo kako bi se osiguralo da i korisnici sa slabijim tehničkim znanjem mogu koristiti aplikaciju bez poteškoća. Primeri elemenata:

- Intuitivan interfejs: navigacija jasna i logična; prepoznatljive ikone i simboli; minimum suvišnih koraka.
- Personalizacija: izbor omiljenih meditacija, frekvencije i vrste obaveštenja.
- Brzina i performanse: optimizacija za različite uređaje i stabilnost čak i pri sporijoj internet vezi.
- Feedback i navigacija: povratne informacije o uspešnim akcijama (pretplata, podsetnici).
- Pristupačnost: podrška za screen reader-e, veličine fontova i kontrasta, jednostavno rukovanje.

## 8 Strategije privlačenja korisnika

- Besplatan probni period.
- Promotivne akcije i popusti.
- Saradnja sa influenserima i brendovima.
- Program preporuke (nagrade/popusti za dovođenje novih korisnika).

## 9 Monetizacija aplikacije

- Model pretplate (freemium/premium).
- Kupovina unutar aplikacije (specifični sadržaji/paketi).
- Iskustvo bez reklama za premium korisnike.

## 10 Dijagram toka interfejsa (DTI)

U originalnom PDF primeru su detaljno dati tokovi za:

- 10.1 Meditator
- 10.2 Administrator
