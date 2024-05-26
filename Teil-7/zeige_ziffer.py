# --------------------------------------------------------------
# zeige_ziffer.py
# Eine Ziffer aus dem MNIST-Datensatz wird als Bild dargestellt.
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 6
# Michael Weigend 19.9.2023
# --------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
stream = open('daten/mnist10_train.csv', 'r')
datenliste = stream.readlines()
stream.close()
datensatz = datenliste[0].split(',')
pixel = datensatz[1:]
bildArray = np.array(pixel, dtype=int).reshape((28, 28))
plt.imshow(bildArray, cmap='Greys')
plt.show()
