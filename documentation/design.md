<!-- 
Mitä ohjelmointikieltä käytät? Kerro myös mitä muita kieliä hallitset siinä määrin, että pystyt tarvittaessa vertaisarvioimaan niillä tehtyjä projekteja.

Mitä algoritmeja ja tietorakenteita toteutat työssäsi?

Mitä ongelmaa ratkaiset ja miksi valitsit kyseiset algoritmit/tietorakenteet?

Mitä syötteitä ohjelma saa ja miten näitä käytetään?

Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)

Lähteet
-->

# Määrittelydokumentti

* Opinto-ohjelma: Tietojenkäsittelytieteen kandi (TKT)
* Ohjelmointikieli: Python
* Dokumentaation kieli: Suomi
* Koodi, tiedostojen nimet ja commitit englanniksi

Pystyn tarvittaessa vertaisarvioimaan myös Javalla, JavaScriptillä tai TypeScriptillä kirjoitettuja ohjelmia.

## Mikä ohjelma

Käsin kirjoitettujen numeroiden tunnistusohjelma tunnistaa numerot 0-9, ja palauttaa NaN, jos syötetteestä ei voida tunnistaa numeroa.

## Algoritmit ja tietorakenteet
* Tekoäly koulutetaan käyttämällä MNIST-tietokantaa, ja (ainakin ensin) k:n lähimmän naapurin menetelmällä

## Aikavaativuus, tilavaativuus

## Input/Output

### Input
* png tai jpg kuvatiedosto

### Output
* kuvaa vastaava numero tai NaN

## Miksi tämä aihe?
Tavoitteenani on, joskus hamassa tulevaisuudessa, kirjoittaa ohjelma, joka ottaa syötteenään käsin kirjoitetun nuotin, ja palauttaa tiedoston, jota nuotinkirjoitusohjelmat voivat lukea. Koska koodaustaitoni ei vielä tätä salli, on aloitettava jostakin... eh... "helposta". Tätä aihetta kohtaan on myös tarve lievälle kostolle; IntroToAI-kurssilla aihetta käsiteltiin yhden viikon laskareissa ohimennen, enkä silloin saanut kunnollista otetta, joten haluan perehtyä paremmin aiheeseen. 

## Tavoitteita/jatkoideoita
Kun kurssin aikana itse "tekoäly" on valmis, niin ohjelmaa tulee laajentaa kurssin aikataulun puitteissa. Tässä muutama ehdotus:
* Käyttöliittymä, johon voi antaa syötteenä kuvatiedoston, jonka ohjelma muuttaa sellaisee muotoon (esim musta-valko, ja resoluution pienennys), josta tekoäly voi tehdä johtopäätöksensä. Ohjelma palauttaa numeron tai tiedon, että syötettä ei voida tunnistaa (NaN, väärän muotoinen tiedosto yms.)
* Muiden kuvioiden tunnistus, kuten reaaliaikainen arvio mitä käyttäjä piirtää. Helppoja piirroksia voivat olla mm. vene, tuulimylly tai auto. Treenidatan hankinta voi olla hankalaa ja harjoitustyön tarkoituksena ei varmastikaan ole piirtää tunteja erilaisia autoja microsoft paintilla tai vastaavalla.
* Jos k:n lähimmän naapurin menetelmä on helppo, tee neuroverkko ja vertaa tuloksia kahden menetelmän välillä.


### Lähteet