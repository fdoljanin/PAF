# PAF seminar - zadatak 17.

Ovaj kod broji zvijezde vidljive ljudskom oku na nebu.
Korišteni su podatci satelita [hipparcos](https://www.cosmos.esa.int/web/hipparcos/hipparcos-2), i to sa [sljedeće poveznice](http://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/txt.gz?I/239/hip_main.dat).

## Koraci za instalaciju

Prije svega, potrebno je imati instaliran [Python 3.x](https://www.python.org/downloads/). Nakon kloniranja ovog repozitorija na računalo, potrebno je preuzeti podatke satelita Hipparcos tako što se uđe u folder [Seminar](/) i pokrene naredba

```
python code/setup/fetcher.py
```

Nakon što se kod izvrši, u mapi `data` pojavit će se datoteke `I_239_hip_main.dat` i `hip_main.csv`.

> **:warning: Napomena:** Preuzimanje može potrajati dugo s obzirom na to da je datoteka veličine 50MB.

Također, ispisat će se poruke pogreške zbog određenih linija Hipparcos kataloga gdje nedostaju neki podatci. One mogu biti zanemarene korištenjem flaga `--iw`.

## Koraci za pokretanje

Brojač se pokreće naredbom

```
python code/counter/main.py
```

Program će korisnika pitati za naziv lokacije za koju želi provjeriti vidljiv broj zvijezda, nakon čega će biti ispisan.
