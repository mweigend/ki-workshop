# --------------------------------------------------------------
# diagramm_4.py
# Datenvisualisierung 4: Nutzung von range()
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 2
# Michael Weigend 18.9.2023
# --------------------------------------------------------------
from matplotlib import pyplot
xWerte = range(-5, 6)
yWerte = []
for x in xWerte:
    yWerte += [x**2]
pyplot.plot(xWerte, yWerte)
pyplot.show()
