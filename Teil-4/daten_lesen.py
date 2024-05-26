# --------------------------------------------------------------
# daten_lesen.py
# Text aus einer Datei auslesen und ausgeben
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 3
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
stream = open('trainingsdaten.csv')

for zeile in stream:
    print(zeile)
stream.close()

