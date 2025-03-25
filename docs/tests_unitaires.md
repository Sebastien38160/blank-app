# Tests unitaires de l'application Streamlit d'analyse de données de jeux vidéo

## Introduction

Les tests unitaires sont essentiels pour assurer la qualité et la fiabilité de l'application. Ils permettent de vérifier que chaque module et fonction fonctionne correctement. Nous utilisons `pytest` pour écrire et exécuter les tests.

## Organisation des tests

Les tests sont organisés dans un dossier `tests` distinct. Les fichiers de test sont nommés `test_nom_du_module.py`. Les tests sont exécutés en utilisant la commande `pytest`.

## Description des tests

### Module `data_processing.py`

* Fonction `load_data(file_path)` :
    * Cas de test : fichier CSV valide.
    * Assertion : vérifie que la fonction renvoie un DataFrame Pandas.
    * Cas de test : fichier CSV invalide.
    * Assertion : vérifie que la fonction lève une exception `FileNotFoundError`.

### Module `visualization.py`

* Fonction `create_bar_chart(data, x, y)` :
    * Cas de test : données valides.
    * Assertion : vérifie que la fonction renvoie un objet `matplotlib.figure.Figure`.
    * Cas de test : données invalides.
    * Assertion : vérifie que la fonction lève une exception `ValueError`.

## Exemples de tests

```python
# tests/test_data_processing.py
import pytest
import pandas as pd
from app import data_processing

def test_load_data_valid_file():
    df = data_processing.load_data("vgsales_cleaned.csv")
    assert isinstance(df, pd.DataFrame)

def test_load_data_invalid_file():
    with pytest.raises(FileNotFoundError):
        data_processing.load_data("invalid_file.csv")

============================= test session starts ==============================
platform linux -- Python 3.9.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /path/to/project
collected 2 items

tests/test_data_processing.py ..                                        [100%]

============================== 2 passed in 0.10s ==============================