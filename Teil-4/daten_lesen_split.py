# --------------------------------------------------------------
# daten_lesen_split.py
# Text aus einer Datei auslesen und als Folge von Listen ausgeben
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 3
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
stream = open('trainingsdaten.csv', mode='r')

for zeile in stream: #1
    datenliste = zeile.split(',') #2
    print(datenliste) #3

stream.close()

