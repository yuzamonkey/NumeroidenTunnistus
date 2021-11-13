# Viikon 2 raportti

## [Työaikakirjanpito](./worklog.md)

### Mitä olen tehnyt tällä viikolla?

* Ottanut tarvittavia konfiguraatioita käyttöön
* Käsitellyt MNIST-tietokantaa koodissa
* Rakentanut/sandboxannut naiivin ratkaisun

### Miten ohjelma on edistynyt?

* Ihan ok. Tällä viikolla koodaus oli enemmänkin luonnostelua ja kokeilua, mikä mielestäni on vaadittua aiheeseen perehtymisen kannalta.

### Mitä opin tällä viikolla?

Menee paljon aikaa, jos haluaa käydä nykyisellä algoritmilla 10_000 testikuvaa läpi suhteessa 60_000 treenikuvaan. Käytännön sovellusta varten ratkaisua täytyy optimoida huomattavasti, tai rakentaa se toisesta näkökulmasta, jos haluaa hyödyntää treeni- ja testidataa kokonaisuudessaan.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Vaativuuksien parantaminen tulee olemaan haaste. En ole myöskään täysin varma, ymmärsinkö etäisyysmitan d(a, B) = min(b∈B)||a-b|| oikein. Siis d(a, B) on alkion a etäisyys joukon B alkioon b, joka on lähimpänä alkio a:ta. Siis tässä työssä voidaan valita a = A[i]. Tällöin lähimpänä on b = B[i]? Kaadunko vain siihen, että asia on yksinkertaisempi mitä luulen? Saan tällä tavalla kuitenkin tarkkuuden jo 90% kieppeille suhteellisen pienellä treenijoukolla.

Onko MNIST kirjaston käyttäminen ok, vai kuuluuko työhön myös lukea gz-tiedostot?

### Mitä teen seuraavaksi?
* Optimointia
* Parametreja ja luokkia helpottamaan testausta ja UI:n käsittelyä
* Ehkä komentorivikäyttöliittymän aloittaminen