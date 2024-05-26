# --------------------------------------------------------------
# klassifizierer.py
# Unterscheidung von Menschen und Hunden 
# Künstliche Intelligenz kapieren und programmieren
# 
# Michael Weigend 18.9.2023
# --------------------------------------------------------------
LR = 0.2  # Lernrate
# etikettierte Daten
DATEN = [(77, 135, 'M'), (88, 55, 'H'), (70, 115, 'M'),
        (50, 85, 'M'), (80, 140, 'M'), (45, 27, 'H'),
        (79, 132, 'M'), (50, 91, 'M'), (45, 80, 'M'), (67, 45, 'H')]

# Training
a = 0.2    # Anfangswert    
for breite, höhe, label in DATEN:
    if label == 'H':
        t = höhe + 1
    else:
        t = höhe - 1
    e = t - a * breite
    da = LR * e/breite    # Änderung der Steigung a
    a += da   

# Vorhersagen
eingabe_breite = input('Breite: ')
while eingabe_breite != '':
    eingabe_höhe = input('Höhe: ')
    breite = float(eingabe_breite)
    höhe = float(eingabe_höhe)
    if höhe < a * breite:
        print('Hund')  # unter der Trennlinie
    else:
        print('Mensch')
    eingabe_breite = input('Breite: ')
print('Auf Wiedersehen')
input()  # Warten bis Eingabetaste gedrückt
    
