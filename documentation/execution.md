# Toteutusdokumentti

## Ohjelman yleisrakenne

Sovellus noudattaa kolmikerrosarkkitehtuuria:

* Käyttöliittymä ([UI](https://github.com/yuzamonkey/NumeroidenTunnistus/tree/main/src/ui))
* Sovelluslogiikka ([Services](https://github.com/yuzamonkey/NumeroidenTunnistus/tree/main/src/services))
* Tiedon talletus ([Repositories](https://github.com/yuzamonkey/NumeroidenTunnistus/tree/main/src/repositories))

![pakkauskaavio](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/documentation/images/packagediagram.png)

Lisäksi sovelluksella on pakkaus [Utils](https://github.com/yuzamonkey/NumeroidenTunnistus/tree/main/src/utils), joka sisältää yleishyödyllisiä funktioita. UI-pakkaus sisältää myös luokat [Params](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/ui/params.py) ja [Results](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/ui/results.py), jotka tallettavat syötteenä annetut parametrit ja tulokset laskennan jälkeen. Nämä luokat ovat sitä varten, ettei UI-luokkien välillä tarvitse antaa suuria määriä parametreja.

## Saavutetut aika- ja tilavaativuudet

K:n lähimmän naapurin menetelmässä yhden numeron tunnistamisen aikavaativuus on O(n^2) tämän pseudokoodin mukaisesti:
```
function classify_number:
    for i to train_data_size:
        distance = compare(selected_image, train_data[i])
        update_k_nearest(distance)
    return result_from_k_nearest(k_nearest)

function compare(img1, img2):
    for each pixel in img1:
        distance += calculate_distance(pixel, img2)
    return distance
```
Kun halutaan tunnistaa useampi numero, aikavaativuus on O(n^3):
```
function classify_set_of_numbers:
    for image in set_of_numbers:
        classify_number(image, training_data)
```
MNIST-luokka palauttaa kuvat 784-alkioisina taulukkoina, mutta ohjelma muuttaa ne 28*28 taulukoiksi. Tämän vuoksi yhden numeron tunnistamisen aikavaativuus voidaan myös tulkita olevan O(n^3) ja useamman numeron tunnistaminen O(n^4).

Funktio [_point_to_set_dist](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/services/knn.py) hakee joukossa A olevan pisteen lähimmän pisteen joukosta B. Usein tämän aikavaativuus on O(1), mutta pahimmassa tapauksessa jokainen joukon B alkio täytyy käydä läpi.

Algoritmin tilavaativuus on O(n), sillä funktio [_point_to_set_dist](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/services/knn.py) käyttää aputaulukkoa lyhimmän etäisyyden etsimiseen.

## Puutteita

* [KNN-luokan](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/services/knn.py) käyttö ei ole UI:n kannalta paras mahdollinen. Esimerkiksi luokittelun reealiaikainen seuranta ei oikein ole mahdollista, ja yksittäisen numeron tunnistamista varten olisi hyvä pystyä antamaan tietty datajoukko. 
* [ProgressWidget](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/ui/result_widgets/progress_widget.py) pyörittää kelloa koko ohjelman ajon ajan, sillä sen pysäyttäminen toisesta luokasta tulostaa konsoliin varoituksen. Varoitus on ilmestynyt välillä, jos luokittelu on mennyt 100% oikein.
* Satunnaisesti ohjelma kaatuu seuraavaan virheeseen: `segmentation fault`. Säännöllisesti ohjelma kaatuu silloin, kun luokittelu aloitetaan treenidatan koon ollessa 1. Virhe ei esiinny, jos funktiota [classify_set_of_numbers](https://github.com/yuzamonkey/NumeroidenTunnistus/blob/main/src/services/knn.py) kutsutaan ohjelman sisällä (esim `index.py`-tiedostossa), vaan pelkästään UI:n kautta syötettynä parametrina.

## Parannusehdotuksia

* Ohjelma on pyritty rakentamaan niin, että uuden luokittelualgoritmin lisääminen olisi sujuvaa. Tällöin voisi lisätä esimerkiksi neuroverkon ohjelman koodiin, joka tunnistaa numeroita testidatasta. 

## Lähteet
[A Modifed Hausdorf Distance for Object Matching](https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf)

[The MNIST Database](http://yann.lecun.com/exdb/mnist/)
