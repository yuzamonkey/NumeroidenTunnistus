# Testaus

### Yksikkötestauksen kattavuusraportti

[Kattavuus](https://app.codecov.io/gh/yuzamonkey/NumeroidenTunnistus)

### Mitä on testattu, miten tämä tehtiin?

Yksikkötesteillä on testattu [KNN](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/services/knn.py)- ja [DataRepository](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/repositories/data_repository.py)-luokka, sekä [Utils](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/utils/utils.py)-tiedoston funktiot, poislukien tulostavat funktiot.

### Minkälaisilla syötteillä testaus tehtiin?

Funktiot on pyritty kirjoittamaan niin, että ne eivät oleta taulukkojen olevan aina pituudeltaan 28*28 tai 784 alkiota. Tällöin on helpompi testata funktiota sellaisilla esimerkkisyötteillä, joista tuloksen oikeellisuuden voi päätellä helposti.

### Miten testit voidaan toistaa?

Yksikkötestit ajetaan siirtymällä virtuaaliympäristöön komennolla `poetry shell` ja syöttämällä komento `pytest` tai `invoke test`. Kattavuusraportti generoituu index.html tiedostoon htmlcov-kansion alle komennolla `invoke coverage-report`

### Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.


