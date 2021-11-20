# Viikon 3 raportti

## [Työaikakirjanpito](./worklog.md)

### Mitä olen tehnyt tällä viikolla?
* Parannellut koodia, kirjoittanut testejä
* Ottanut käyttöön workflown ja codecovin
* UI-kirjaston päättäminen (Tkinter vs PyQt5 vs Curses)
* UI:n suunnittelua kynällä ja paperilla

### Miten ohjelma on edistynyt?
* Ei ollut tehokkain viikko muiden kiireiden takia

### Mitä opin tällä viikolla?

* Joo, etäisyyden määritelmä d(a, B) on ihan simppeli. Jumitin toista viikkoa ajattelemalla jotenkin abstraktimmin kuin mitä asia on käytännössä... Ei se mitään.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?

[Aikaisemman viikon kysymyksen](./weekly2.md) täsmennyksenä: luokka [DataRepository](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/repositories/data_repository.py) käyttää MNIST-nimistä valmista kirjastoa, joka tekee gz-tiedostojen purkaamisen ja antaa datan sopivassa muodossa. Tuskin tietoja olisi kovin vaikea purkaa muuten, mutta kun oli puhetta aloitusluennolla, että valmiit kirjastot tulisi myöhemmin kirjoittaa itse, niin katsotaanko tämä sellaisena tapauksena? 

### Mitä teen seuraavaksi?
* UI:n toteutus PyQt5:lla vertaisarvioitavaan kuntoon
