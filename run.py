"""
CI/CD
"""

import os
import pandas as pd
import random


def main():
    """
    Main
    """
    data = import_data()
    data = rename_columns(data)
    data = random_row(data, 50)
    data = concat_dataset(data)
    data = column_totalsepal(data)
    data = column_totalpetal(data)


def import_data() -> pd.DataFrame:
    """
    Fonction pour importer un fichier CSV en tant que DataFrame.
    Sortie : data [pd.DataFrame]
    """
    data = pd.read_csv("data/iris.csv")
    print(data.shape)
    return data


def rename_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Fonction pour renommer certaines colonnes du DataFrame.
    """
    data_renamed = data.rename(
        columns={
            "sepal.length": "sepal_length",
            "sepal.width": "sepal_width",
            "petal.length": "petal_length",
            "petal.width": "petal_width",
        }
    )
    return data_renamed


def random_row(data: pd.DataFrame, num_rows: int) -> pd.DataFrame:
    """
    Fonction pour sélectionner un nombre spécifié de lignes au hasard à partir du DataFrame.
    Entrées :
    - data : DataFrame
    - num_rows : Nombre de lignes à sélectionner au hasard
    Sortie :
    - DataFrame contenant les lignes sélectionnées
    """
    random_rows = data.sample(n=num_rows, random_state=42)
    return random_rows


def concat_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """
    Fonction pour concaténer les données sélectionnées plusieurs fois.
    """
    data_rows = random_row(data, 50)
    concat_data = pd.concat([data_rows, data_rows, data_rows], ignore_index=True)
    return concat_data


def column_totalsepal(data: pd.DataFrame) -> pd.DataFrame:
    """
    Fonction pour ajouter une nouvelle colonne contenant la somme de 'sepal_length' et 'sepal_width'.
    """
    data["total_sepal"] = data.sepal_length + data.sepal_width
    print(data.head())
    return data


def column_totalpetal(data: pd.DataFrame) -> pd.DataFrame:
    """
    Fonction pour ajouter une nouvelle colonne contenant la somme de 'petal_length' et 'petal_width'.
    """
    data["total_petal"] = data.petal_length + data.petal_width
    print(data.head())
    return data


if __name__ == "__main__":
    """
    Doc
    """
    main()
