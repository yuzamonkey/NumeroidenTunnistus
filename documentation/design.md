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
* Käyttöliittymä, koodi, tiedostojen nimet ja commitit englanniksi

Pystyn tarvittaessa vertaisarvioimaan myös Javalla, JavaScriptillä tai TypeScriptillä kirjoitettuja ohjelmia.

## Mikä ohjelma

Käsin kirjoitettujen numeroiden tunnistusohjelma tunnistaa numerot 0-9.

## Algoritmit ja tietorakenteet
* Tekoäly koulutetaan käyttämällä MNIST-tietokantaa, ja (ainakin ensin) k:n lähimmän naapurin menetelmällä.

## Aikavaativuus ja tilavaativuus

## Input/Output

<!-- 
## Miksi tämä aihe?
Tavoitteenani on, joskus hamassa tulevaisuudessa, kirjoittaa ohjelma, joka ottaa syötteenään käsin kirjoitetun nuotin, ja palauttaa tiedoston, jota nuotinkirjoitusohjelmat voivat lukea. Koska koodaustaitoni ei vielä tätä salli, on aloitettava jostakin... eh... "helposta".  -->

## Tavoitteita/jatkoideoita
Kun itse "tekoäly" on valmis, ohjelmaa tulisi laajentaa kurssin aikataulun puitteissa. Tässä muutama ehdotus:
* Käyttöliittymä, jossa voi reaaliaikaisesti seurata kouluttamista ja vaihtaa parametreja, kuten k:n arvoa tai treenidatan suuruutta.
* Jos k:n lähimmän naapurin menetelmä tuntuu helpolta, tee neuroverkko tai jokin muu ratkaisutapa, ja vertaa tuloksia menetelmien välillä. Vertailua voi myös tehdä eri etäisyyksien välillä (Euclidian, Chebyshev, Manhattan...).
* Käyttöliittymä, johon voi antaa syötteenä kuvatiedoston, jonka ohjelma muuttaa sellaiseen muotoon (esim. musta-valko, ja resoluution pienennys), jota algoritmi pystyy käsittelemään. Ohjelma palauttaa numeron tai tiedon, että syötettä ei voida tunnistaa (NaN, väärän muotoinen tiedosto yms.)
* Muiden kuvioiden tunnistus, kuten reaaliaikainen arvio mitä käyttäjä piirtää. Helppoja piirroksia voivat olla mm. vene, tuulimylly tai auto. Treenidatan hankinta voi olla hankalaa.

Tkinter on tuttu GUI:n toteutusta varten kurssilta Ohjelmistotekniikka, mutta luulen, että haluan etsiä jonkin muun kirjaston käyttöliittymää varten.


## Lähteet
* [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)
* [https://course.elementsofai.com/fi/4/2](https://course.elementsofai.com/fi/4/2)
* [https://www.youtube.com/watch?v=09mb78oiPkA](https://www.youtube.com/watch?v=09mb78oiPkA)
* [https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf](https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf)