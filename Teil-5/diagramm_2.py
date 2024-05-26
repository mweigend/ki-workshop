# --------------------------------------------------------------
# diagramm_2.py
# Datenvisualisierung 2
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 2
# Michael Weigend 18.9.2023
# --------------------------------------------------------------
from matplotlib import pyplot
dollarWerte = [9.5, 23.6, 61.99, 81]
euroWerte = [9.0, 20.77, 57.71, 72]
pyplot.plot(dollarWerte, euroWerte)
pyplot.show()
from matplotlib import pyplot
dollarWerte = [9.5, 23.6, 61.99, 81]
euroWerte = [9.0, 20.77, 57.71, 72]
pyplot.plot(dollarWerte, euroWerte, 'or')
pyplot.xlabel('Dollars')
pyplot.ylabel('Euros')
pyplot.grid()
pyplot.show()
