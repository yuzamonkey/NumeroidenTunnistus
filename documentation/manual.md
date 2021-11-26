# Käyttöohje
<!-- * Miten ohjelma suoritetaan, miten eri toiminnallisuuksia käytetään
* Minkä muotoisia syötteitä ohjelma hyväksyy
* Missä hakemistossa on jar ja ajamiseen tarvittavat testitiedostot.
 -->

Kloonaa [projekti](https://github.com/yuzamonkey/NumeroidenTunnistus)

## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, mene ohjelman juurihakemistoon ja asenna riippuvuudet komennolla:

```bash
poetry install
```

Ohjelma käynnistyy komennolla:
```
python3 src/main.py
```
tai
```
poetry run invoke start
```
Komento `python3 src/main.py` on suositeltava tässä vaiheessa projektia, jotta jotkin tulostukset näkyvät reaaliaikaisesti konsolissa.