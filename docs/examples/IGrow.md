# IGrow — primer specifikacije (Markdown)

## 1 Opis aplikacije

Aplikacija osmišljena da olakša uzgajanje voća i povrća onima koji žive u stanu i nemaju pristup bašti, tako što pruža podršku kroz praktične savete, praćenje napretka i korisne informacije, kako bi organska hrana bila dostupna svima – čak i na terasi, prozorskoj dasci ili u saksijama u dnevnoj sobi.

IGrow aplikacija je razvijena koristeći moderne Web i Mobilne tehnologije, poput: Flutter okruženja za programiranje mobilnih uređaja nezavisno od platforme; Spring Boot okruženja za server i druge.

Kroz aplikaciju korisnici će dobijati pravovremene podsetnike kada je potrebno zaliti ili prihraniti biljku, čime se olakšava svakodnevna briga i smanjuje rizik od grešaka u uzgoju. Aplikacija omogućava i praćenje rasta biljke, gde korisnici mogu beležiti visinu, izgled listova i veličinu plodova, na osnovu čega će dobijati personalizovane savete o daljoj nezi.

Korisnici mogu pratiti da li njihova biljka dobija optimalnu količinu sunčeve energije na odabranoj lokaciji, zahvaljujući svetlosnom senzoru ugrađenom u aplikaciji. Za početnike, dostupan je jednostavan “starter paket” koji uključuje semena i osnovnu opremu, što proces uzgoja čini dostupnim i onima bez prethodnog iskustva. Pored toga, aplikacija nudi informacije o nutritivnim vrednostima uzgajanih biljaka, omogućavajući korisnicima da bolje razumeju zdravstvene benefite svoje hrane i dodatno ih motiviše da nastave da gaje svoje voće i povrće.

## 2 Opis problema

U savremenom urbanom životu sve je veći problem nedostatak poverenja u hranu koja se plasira kao organska u prodavnicama. Često nije moguće biti siguran da proizvod zaista ne sadrži veštačke materije, hemijska đubriva ili pesticide. Dodatno, etikete i sertifikati nisu uvek transparentni ili lako proverljivi, što izaziva sumnju i kod onih koji žele da se hrane zdravije.

Pored sigurnosti hrane, problem postaje izražen i u urbanim sredinama, poput Beograda, gde veliki broj ljudi nema pristup bašti ili dvorištu, što značajno ograničava mogućnosti za samostalni uzgoj voća i povrća. Ograničen prostor u stanovima, nedostatak zemlje i svetla, kao i gustina urbanih naselja, dodatno komplikuju mogućnost tradicionalnog uzgoja biljaka.

Samostalno uzgajanje organske hrane omogućava stopostotnu kontrolu nad svim aspektima uzgoja: od zemljišta i semena do načina zalivanja i neupotrebe hemijskih sredstava. Time osiguravamo da konzumiramo pravu, sigurnu organsku hranu. Naša aplikacija omogućava korisnicima da uzgajaju povrće i voće i u stanovima, rešavajući problem ograničenog prostora. Iako je količina proizvedene hrane manja, proces uzgoja pruža direktan uvid u trud uložen u hranu, čineći korisnika zahvalnijim za ono što jede.

## 3 Analiza korisnika

Ispitali smo 95 osoba raznih uzrasta o mišljenjima i navikama vezanim za zdravu ishranu, a kasnije specifično za organsko voće i povrće.

Na pitanje „Koliko smatrate da jedete zdravu hranu?” na skali od 1 do 5, većina ispitanika je odabrala 3, što pokazuje da ljudi ocenjuju svoju ishranu kao umereno zdravu. Razlozi za to mogu biti poteškoće u svakodnevnom nabavljanju zdrave hrane ili manjak želje za zdravijom ishranom.

Analiza pokazuje da više od polovine ispitanika smatra da je kontrola nad voćem i povrćem kojim se hrane veoma bitna, dok ukupno 86% ispitanika ocenjuje da je kontrola relevantna makar u određenoj meri. Time saznajemo da korisnici žele da imaju jasnu predstavu o kvalitetu hrane koju konzumiraju i da postoji značajan interes za rešenjima koja im omogućavaju potpunu kontrolu nad uzgojem ili izborom hrane.

Većina ispitanika živi u velikim gradovima, dok manji broj dolazi iz manjih gradova, prigradskih naselja ili sela. Ovi podaci omogućavaju bolje razumevanje urbanih i ruralnih uslova u kojima korisnici trenutno uzgajaju ili planiraju da uzgajaju svoje biljke, što je važno za prilagođavanje rešenja njihovim potrebama.

Najveći deo ispitanih korisnika živi u stanovima, što implicira ograničen prostor za gajenje biljaka i potencijalnu potrebu za rešenjima prilagođenim tim uslovima. Slede kuće sa baštom ili dvorištem, gde prostor za uzgoj nije ograničen, pa korisnici mogu tradicionalno gajiti biljke.

Na osnovu prikupljenih podataka o navikama, interesovanjima i životnim uslovima, moguće je definisati profil korisnika za koje bi rešenja vezana za samostalni uzgoj voća i povrća bila najrelevantnija. Radi se o urbanim korisnicima različitih uzrasta, koji najčešće raspolažu ograničenim prostorom za gajenje biljaka, svesni su važnosti kontrole nad hranom koju konzumiraju i zainteresovani za praktična digitalna rešenja koja olakšavaju uzgoj i praćenje kvaliteta voća i povrća.

## 4 Analiza domena

Aplikacija se nalazi u domenu urbane hortikulture i samostalnog uzgoja hrane, sa fokusom na gajenje voća i povrća u stanovima ili prostorima bez bašte. Ovo uključuje ne samo osnovnu negu biljaka, već i praćenje rasta, personalizovane savete, kao i edukaciju o nutritivnim vrednostima biljaka.

IGrow aplikacija se pozicionira kao digitalno rešenje koje povezuje ove elemente kroz jednu platformu. Na taj način, aplikacija objedinjuje oblast urbane hortikulture sa modernim tehnologijama, pružajući korisnicima intuitivan alat koji olakšava proces uzgoja hrane u savremenim gradskim uslovima, uz istovremeno podizanje svesti o zdravoj ishrani i značaju organske proizvodnje.

## 5 Analiza zahteva

- Briga i informacije o biljci: svaka biljka ima njenu individualnu stranicu na kojoj će pisati glavne informacije o toj biljci i kako se brinuti o njoj, ali i koliko ju je teško gajiti. Korisnik može da je doda u svoj katalog klikom na dugme na toj stranici.
- Slikovita polica sa svim biljkama: stranica na kojoj korisnik lako može da vidi koje sve biljke gaji i njihovo ime.
- Stranica za dnevnik svake biljke koju gajimo: možemo unositi statističke podatke o svakoj biljci koju gajimo (visina i boja lista), ali možemo unositi i proizvoljan tekst koji opisuje biljku. Moguće je slikati biljku svakim unosom u dnevnik.
- Grafikonski prikaz statistike: ako korisnik redovno unosi podatke u dnevnik biljke, moći će da pregledno vidi promenu boje lista i visine i eventualno primeti neke anomalije.
- Registracija i login: kreiranje naloga (korisničko ime, email, lozinka) radi čuvanja statistke rasta biljaka i istorije kupovine, na serveru.
- Tehnička bezbednost: zaštita privatnosti i sigurnost podataka.
- Notifikacije o statusu: korisniku će biti slane notifikacije (podsetnik zalivanja, podsetnik stavljanja đubriva, kada je biljka gotova sa rastom, kada kupovina uspešno prođe, podsetnik da se popuni dnevnik) i te notifikacije će moći kasnije da se otvore ponovo na posebnoj stranici za notifikacije, da korisnik ne bi morao sve da radi u trenutku i da ne bi morao da pamti. Notifikacije za zalivanje i đubrenje biljke će imati tri nivoa hitnosti koji pokazuju koliko korisnik dugo nije uradio datu akciju i meriće se u odnosu na to kad je notifikacija poslata i koliko je bitno toj biljci da dobije vodu ili đubrivo.
- Praćenje intenziteta svetlosti: stranica sa softverski implementiranim senzorom jačine svetlosti (koji koristi kameru telefona), da bi korisnik lakše udovoljio biljci.
- Preporuka biljaka na osnovu lokacije korisnika: pošto će korisnici živeti pod različitim klimama, neće sve biljke moći idealno da rastu kod svih korisnika. Informacije o klimatskim ograničenjima se nalaze na stranici osnovnih informacija o biljci, ali će postojati i dugme realizovano kao filter da se biljke nepogodne za korisnikovu lokaciju ni ne prikazuju.
- Laka nabavka alata i biljaka: u okviru aplikacije moguće je naručivanje „starter paketa“ u kojima se nalazi kombinacija svih potrebnih stvari za uzgajanje jedne biljke ili za uzgajanje jedne vrste biljaka (na primer „Starter Paket Paradajz“ koji uključuje 100 semena paradajza, mini lopatu, saksiju, kvalitetnu zemlju i štap koji će služiti paradajzu kao potpora ili „Starter Paket Salate“ koji uključuje sve potrebno za paradajz, luk, zelenu salatu, ...). Takođe, moguće je i naručivanje svih alata i biljaka posebno, u slučaju da korisnik već ima nešto svoje.

## 6 Limitirajući faktori i ograničenja

Razvoj aplikacije zahteva resurse: vreme, tim ljudi i budžet. Pored tehničkih izazova, neophodno je obezbediti tačne i relevantne informacije iz oblasti botanike i nutricionizma. Dodatni faktori uključuju:

- Zaštita podataka: sigurnost ličnih podataka i očuvanje privatnosti korisnika.
- Ograničena interakcija sa stvarnim biljkama: aplikacija može pružiti samo digitalnu pomoć; fizičko uzgajanje biljaka zavisi od veština korisnika i spoljašnjih faktora (svetlost, temperatura, voda).
- Zavisnost od uređaja i senzora: praćenje intenziteta svetlosti koristi kameru telefona, što može biti nepouzdano ili varirati između uređaja - stariji telefoni ili oni sa slabijom kamerom mogu davati netačne podatke.

## 7 Usability

Usability predstavlja ključni aspekt dizajna aplikacije za urbani uzgoj hrane.

1. Pristupačnost: aplikacija je prilagođena korisnicima sa različitim nivoima iskustva u gajenju biljaka, uključujući potpune početnike.
2. Intuitivni interfejs: funkcionalnosti poput podsetnika, praćenja rasta i unosa podataka jasno su istaknute i lako dostupne.
3. Efikasnost: proces dodavanja biljke, praćenja napretka i dobijanja saveta brz je i jednostavan.
4. Pouzdanost: aplikacija konzistentno daje tačne podsetnike i preporuke zasnovane na podacima korisnika.
5. Zadovoljstvo korisnika: aplikacija pruža pozitivno iskustvo, motiviše korisnike da nastave sa uzgojem i podstiče ih da postignu bolje rezultate u gajenju sopstvene hrane.
6. Text-to-speech podrška: sekcije koje sadrže veće količine teksta mogu se slušati umesto čitati, čime se aplikacija dodatno prilagođava korisnicima i povećava dostupnost informacija.

## 8 Monetizacija

Monetizacija aplikacije se bazira na kupovini fizičkih proizvoda od nas (izdavača aplikacije), a ne na pretplaćivanje na aplikaciju ili na reklamama. Mi ne moramo biti proizvođači tih fizičkih proizvoda, već možemo imati ugovore sa poljoapotekama ili lokalnim poljoprivrednicima.

1. Prodaja starter paketa: korisnici mogu kupiti fizičke pakete sa semenom i osnovnom opremom za uzgoj biljaka, što predstavlja dodatni prihod i olakšava početak uzgoja.
2. Prodaja individualne opreme: korisnici mogu kupiti i sve što se nalazi u starter paketu, posebno. To uključuje još kvalitetne zemlje, alate za kućno baštovanstvo i još semenki specifične za tog korisnika, ne nužno u paketu sa ostalim semenkama.

## 9 Dijagram toka interfejsa

U originalnom PDF primeru su navedeni ekrani i dijagram toka interfejsa (DTI) uz slike.
