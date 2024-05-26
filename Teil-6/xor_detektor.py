# -------------------------------------------------
# nn_2_3_2.py
# Neuronales Netz zur Lösung des XOR-Problems
# 2 Eingabeknoten, 3 verborgene Knoten
# 2 Ausgabeknoten
#
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 5
# Michael Weigend 19.9.2023
# --------------------------------------------------------------

from random import uniform, shuffle
from math import e
W = 0.5  # obere Grenze für Anfangswerte der Gewichte
LR = 0.2


# Initialisierung der Gewichte
wi1h1 = uniform(-W, W)
wi2h1 = uniform(-W, W)
wi1h2 = uniform(-W, W)
wi2h2 = uniform(-W, W)
wi1h3 = uniform(-W, W)
wi2h3 = uniform(-W, W)
wh1o1 = uniform(-W, W)
wh2o1 = uniform(-W, W)
wh3o1 = uniform(-W, W)
wh1o2 = uniform(-W, W)
wh2o2 = uniform(-W, W)
wh3o2 = uniform(-W, W)

def sig(x):
    return 1.0 / (1.0 + e**-x)

def vorhersagen(i1,i2):    
    xh1 = wi1h1 * i1 + wi2h1 * i2 
    xh2 = wi1h2 * i1 + wi2h2 * i2 
    xh3 = wi1h3 * i1 + wi2h3 * i2 
    yh1 = sig(xh1)
    yh2 = sig(xh2)
    yh3 = sig(xh3)
    xo1 = yh1 * wh1o1 + yh2 * wh2o1 + yh3 * wh3o1
    xo2 = yh1 * wh1o2 + yh2 * wh2o2 + yh3 * wh3o2 
    o1 = sig(xo1)
    o2 = sig(xo2)
    return o1, o2

def trainieren(i1, i2, t1, t2):
    global wi1h1, wi2h1, wi1h2, wi2h2, wi1h3, wi2h3 
    global wh1o1, wh2o1, wh3o1, wh1o2, wh2o2, wh3o2

    # Berechnung der Ausgabe (Vorhersage)
    xh1 = wi1h1 * i1 + wi2h1 * i2 
    xh2 = wi1h2 * i1 + wi2h2 * i2 
    xh3 = wi1h3 * i1 + wi2h3 * i2 
    yh1 = sig(xh1)
    yh2 = sig(xh2)
    yh3 = sig(xh3)
    xo1 = yh1 * wh1o1 + yh2 * wh2o1 + yh3 * wh3o1
    xo2 = yh1 * wh1o2 + yh2 * wh2o2 + yh3 * wh3o2 
    o1 = sig(xo1)
    o2 = sig(xo2)
    # Aktualisierung der Gewichte
    # Verborgene Schicht - Ausgabeschicht
    eo1 = t1 - o1
    eo2 = t2 - o2
    wh1o1 += LR * eo1 * o1*(1-o1)*yh1
    wh2o1 += LR * eo1 * o1*(1-o1)*yh2
    wh3o1 += LR * eo1 * o1*(1-o1)*yh3
    wh1o2 += LR * eo2 * o2*(1-o2)*yh1    
    wh2o2 += LR * eo2 * o2*(1-o2)*yh2
    wh3o2 += LR * eo2 * o2*(1-o2)*yh3  
    # Eingabeschicht - verborgene Schicht    
    eh1 = wh1o1 * eo1 + wh1o2 * eo2
    eh2 = wh2o1 * eo1 + wh2o2 * eo2
    eh3 = wh3o1 * eo1 + wh3o2 * eo2
    wi1h1 += LR * eh1 * yh1*(1-yh1)*i1
    wi2h1 += LR * eh1 * yh1*(1-yh1)*i2
    wi1h2 += LR * eh2 * yh2*(1-yh2)*i1
    wi2h2 += LR * eh2 * yh2*(1-yh2)*i2
    wi1h3 += LR * eh3 * yh3*(1-yh3)*i1
    wi2h3 += LR * eh3 * yh3*(1-yh3)*i2
    return eo1, eo2


# Zufällige Trainingsdaten erzeugen
d =[(0, 0, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 1)]
daten = 2000 * d
shuffle(daten)

# Training

for ep in range(10):
    summeFehlerQuadrate = 0
    for i1, i2, t1, t2 in daten:
        eo1, eo2 = trainieren(i1, i2, t1, t2)
        summeFehlerQuadrate += eo1**2 + eo2**2
    mFehlerQuadrate = summeFehlerQuadrate / len(daten)  
    print('Epoche:',ep, 'mittlere Fehlerquadratsumme:',
          mFehlerQuadrate)
# Testen 
for i1, i2, t1, t2 in d:
    o1, o2 = vorhersagen(i1, i2) 
    print('Eingabe:', i1, i2, 'Vorhersage: ', round(o1, 4), round(o2, 4),
          'Target:', t1, t2)
