# Testaus

### Yksikkötestauksen kattavuusraportti

[Kattavuus](https://app.codecov.io/gh/yuzamonkey/NumeroidenTunnistus)

### Mitä on testattu, miten tämä tehtiin?

Yksikkötesteillä on testattu [KNN](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/services/knn.py)- ja [DataRepository](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/repositories/data_repository.py)-luokka, sekä [Utils](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/utils/utils.py)-tiedoston funktiot. 

Suorituskykytestausta on tehty manuaalisesti ajamalla KNN-luokan metodia [classify_number](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/services/knn.py) eri syötteillä.

### Minkälaisilla syötteillä testaus tehtiin?

Yksikkötestejä varten funktiot on pyritty kirjoittamaan niin, että ne eivät oleta taulukkojen olevan aina pituudeltaan 28*28 tai 784 alkiota. Tällöin on helpompi testata funktiota sellaisilla esimerkkisyötteillä, joista tuloksen oikeellisuuden voi päätellä helposti.

Suorituskykytestauksessa vaihdettiin treenidatan kokoa ja mitattiin aika, mitä yhden numeron tunnistamiseen meni.

### Miten testit voidaan toistaa?

Yksikkötestit ajetaan siirtymällä virtuaaliympäristöön komennolla `poetry shell` ja syöttämällä komento `pytest` tai `invoke test`. Kattavuusraportti generoituu index.html tiedostoon htmlcov-kansion alle komennolla `invoke coverage-report`

### Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.

| trenidatan koko | yhden numeron tunnistamiseen kulunut aika (s) |
|---|---|
| 100 | 0.71 |
| 1000 | 7.22 |
| 10 000 | 77.92 |
| 60 000 | 484.23 (≈8min) |

![graph](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/documentation/images/graph.png)

Tästä voidaan huomata, että numeroiden tunnistus on algoritmille raskas prosessi. Varsinkin jos haluttaisiin tunnistaa kaikki testidatan 10 000 testinumeroa ja verrata jokaista 60 000 treeninumeroon, prosessi kestäisi arviolta 10 000 * 484s ≈ 1344h ≈ 56vrk.