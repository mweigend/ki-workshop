# --------------------------------------------------------------
# sigmoid_plot_starter.py
# Graph der Sigmoid-Funktion (Starterprojekt für Aufgabe 1)
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 5
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
# sigmoid_plot_starter.py
from matplotlib.pyplot import *
from math import e

def sig(x):
    return 1 / (1 + e**-x)

x_ = [x/10 for x in range(-100, 100)]
y_1 = [sig(x) for x in x_]
plot(x_, y_1)
xlabel('x')
grid()
show()
