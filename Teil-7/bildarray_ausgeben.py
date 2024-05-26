# --------------------------------------------------------------
# bildarray_ausgaben.py
# Aus den MNIST-Trainingsdaten wird ein Bild als Array ausgegeben.
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 6
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
PFAD = 'daten/mnist10_train.csv'
NR = 0

stream = open(PFAD, 'r')
datenliste = stream.readlines()
stream.close()

datensatz = datenliste[0].split(',')
pixel = datensatz[1:]
bildArray = np.array(pixel, dtype=int).reshape((28, 28))
print(bildArray)
