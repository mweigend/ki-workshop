# -------------------------------------------------
# nn_xor.py
# Neuronales Netz zur Lösung des XOR-Problems
# mit NumPy-Arrays
#
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 6
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
import numpy as np
from math import e
from random import shuffle
LR = 0.2

def sig(x):
    return 1 / (1 + e**-x)

# Initialisierung der Gewichte
wih = np.random.rand(3, 2) - 0.5
who = np.random.rand(2, 3) - 0.5

def vorhersagen(i):   
    xh = np.dot(wih, i) 
    yh = sig(xh)
    xo = np.dot(who, yh) 
    o = sig(xo)
    return o

def trainieren(i, t):
    global wih, who
    # Berechnung der Ausgabe (Vorhersage)
    xh = np.dot(wih, i)
    yh = sig(xh)
    xo = np.dot(who, yh) 
    o = sig(xo)   
    # Aktualisierung der Gewichte
    eo = t - o
    who += LR * np.dot((eo * o * (1.0 - o)), yh.T)   
    eh = np.dot(who.T, eo)  
    wih += LR * np.dot((eh * yh * (1.0 - yh)), i.T)
    return eo


# Zufällige Trainingsdaten erzeugen
d =[(0, 0, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 1)]
daten = 2000 * d
shuffle(daten)

# Training

for ep in range(10):
    summeFehlerQuadrate = 0
    for i1, i2, t1, t2 in daten:
        i = np.array([i1, i2],ndmin=2).T
        t = np.array([t1, t2], ndmin=2).T
        eo = trainieren(i, t)
        summeFehlerQuadrate += np.sum(eo**2)
    mFehlerQuadrate = summeFehlerQuadrate / len(daten)  
    print('Epoche:',ep, 'mittlere Fehlerquadratsumme:',
          mFehlerQuadrate)

# Testen (dieser Teil steht nicht im Buch)
for i1, i2, t1, t2 in d:
    i = np.array([i1, i2],ndmin=2).T
    t = np.array([t1, t2], ndmin=2).T
    o = vorhersagen(i)
    o1 = round(o[0,0], 4)
    o2 = round(o[1,0], 4)
    
    print('Eingabe:', i1, i2, 'Vorhersage: ', round(o1, 4), round(o2, 4),
          'Target:', t1, t2)
