from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import random

app = Flask(__name__)

# Inizializzazione variabili globali
totale_punti = 100
raccolta = []

# Caricamento dati Pokémon
df = pd.read_csv('pokemon (1).csv')
df_comune = df[df["Rarità"] == "Comune"]
df_non_comune = df[df["Rarità"] == "Non Comune"]
df_raro = df[df["Rarità"] == "Rara"]
df_ultra_raro = df[df["Rarità"] == "Ultra Rara"]

def pesca():
    """Simula l'apertura di un pacchetto di carte."""
    global totale_punti, raccolta
    pacchetto = []
    if totale_punti >= 10:
        totale_punti -= 10
        for _ in range(5):
            numero = random.uniform(0, 1)  # Genera un numero casuale tra 0 e 1
            if numero <= 0.7:  # Comune (70%)
                totale_punti += 1
                pokemon = df_comune.sample().to_dict(orient='records')[0]
            elif numero <= 0.9:  # Non Comune (20%)
                totale_punti += 3
                pokemon = df_non_comune.sample().to_dict(orient='records')[0]
            elif numero <= 0.99:  # Rara (9%)
                totale_punti += 6
                pokemon = df_raro.sample().to_dict(orient='records')[0]
            else:  # Ultra Rara (1%)
                totale_punti += 10
                pokemon = df_ultra_raro.sample().to_dict(orient='records')[0]
            pacchetto.append(pokemon)
        raccolta.extend(pacchetto)
        salva_raccolta_su_file()
    return pacchetto
