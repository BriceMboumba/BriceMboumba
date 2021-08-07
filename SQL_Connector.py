import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys
import time
import ast
import requests
import mysql.connector as sql
import sshtunnel

#Connexion à un serveur MySQL

def Connexion():
    db = sql.connect(host='127.0.0.1', user='root', password='*****', database='Data_information', port='3306')

    if db.is_connected() == False: #On aurait bien pu utiliser une Exception
        print("Not connected")

    # db.close()
    # Création d'un curseur se déplaçant dans la BDD
    cur = db.cursor()

    # execution du curseur
    cur.execute("SELECT * FROM Students")

    # récupération de toutes lignes de la dernière instruction exécutée
    res = cur.fetchall()

    # Transformation des tuples en liste
    liste_tuple = [res]

    liste = [i for element in liste_tuple for i in element]
    return liste


def Data_Frame(liste):
    # Création d'un DataFrame avec Pandas partant de la liste
    df = pd.DataFrame(liste)
    print(df)
    print('dimension:', df.shape)
    print(df.info())
    print(df.describe())
    # affichage des noms des colonnes
    df.columns
    # nomination des noms des colonnes
    df.columns = ["stu_id", "stu_name", "stu_age", "stu_genre", "date_of_birth", "city"]
    df.head(13)
    # calcul explicitement la moyenne
    print(df["stu_age"].mean())


if __name__ == "__main__":
    Data_Frame(Connexion())