# --------------------------------------------------------------
# nn_ziffern.py
# Neuronales Netz, das Ziffern erkennen kann.
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 6
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
import numpy as np
import math

EPOCHEN = 1       # Anzahl Trainingsdurchläufe
LR = 0.1          # Lernrate
I_KNOTEN = 784    # Anzahl Eingabeknoten
H_KNOTEN = 100    # Anzahl verborgene Knoten
O_KNOTEN = 10     # Anzahl Ausgabeknoten
PFAD_TRAINING = 'daten/mnist_train.csv'  # Pfad zu Traingsdaten
PFAD_TEST = 'daten/mnist_test.csv'       # Pfad zu Testdaten

# Initialisierung des neuronalen Netzes
wih = np.random.rand(H_KNOTEN, I_KNOTEN) - 0.5
who = np.random.rand(O_KNOTEN, H_KNOTEN) - 0.5

def sig(x):
    return 1 / (1 + math.e **-x)

def datenLesen(pfad):
    """ Etikettierte Daten werden aus der csv-Datei mit dem
        Pfad pfad gelesen. Daraus wird eine Liste
        mit Tupeln aus Numpy-Arrays (i, t)
        erzeugt und zurückgegeben."""
    stream = open(pfad, 'r')
    datenliste = stream.readlines()
    stream.close()
    daten = []   
    for zeile in datenliste:
        zeileListe = zeile.split(',')
        # print(zeileliste)
        # Eingaben aus dem Datensatz extrahieren und skalieren
        eingaben = np.array(zeileListe[1:], dtype=float)
        eingabenSkaliert = (eingaben / 255 * 0.99) + 0.01
        targets = np.zeros(O_KNOTEN) 
        targets[int(zeileListe[0])] = 1
        i = np.array(eingabenSkaliert, ndmin=2).T
        t = np.array(targets, ndmin=2).T
        daten.append((i, t))
    return daten
       
def trainieren(i, t):
    global wih, who      
    xh = np.dot(wih, i)
    yh = sig(xh)      
    xo = np.dot(who, yh)
    o = sig(xo)     
    eo = t - o  
    eh = np.dot(who.T, eo)   
    who += LR * np.dot((eo * o * (1.0 - o)), yh.T)  
    wih += LR * np.dot((eh * yh * (1.0 - yh)), i.T)

def vorhersagen(i):
    xh = np.dot(wih, i)
    yh = sig(xh)        
    xo = np.dot(who, yh)
    o = sig(xo)
    return o

# Neuronales Netz trainieren
for ep in range(EPOCHEN):
    daten = datenLesen(PFAD_TRAINING)
    for i, t in daten:
        trainieren(i, t)
    
# Neuronales Netz testen
testbericht = []    # liste aus 0 (falsches Ergebnis) und 1 (richtiges Ergebnis)
testdaten = datenLesen(PFAD_TRAINING)
for i, t in testdaten:
    o = vorhersagen(i)
    ziffer = np.argmax(o)                                
    erwarteteZiffer = np.argmax(t)                      
    if (ziffer == erwarteteZiffer):                     

        testbericht.append(1)
    else:
        testbericht.append(0)


trefferquote = sum(testbericht) / len(testbericht) 
print ('Trefferquote:',trefferquote * 100, '%')
input()
