# --------------------------------------------------------------
# perzeptron.py
# Rosenblatt-Perzeptron
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 4
# Michael Weigend 19.9.2023
# --------------------------------------------------------------

DATEN = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
LR = 0.1
SW = 0.5
w1 = 0.5
w2 = 0.5

def trainieren(x1, x2, t):
    global w1, w2
    o = vorhersehen(x1, x2)    
    w1 += LR * (t - o) * x1
    w2 += LR * (t - o) * x2

def vorhersehen(x1, x2):
    x = w1 * x1 + w2 * x2
    if x > SW:
        return 1
    else:
        return 0
    
for epoche in range(10):
    for x1, x2, t in DATEN:
        trainieren(x1, x2, t)

for x1, x2, t in DATEN:
    o = vorhersehen(x1, x2)
    print('Eingaben:',x1, x2,
          'Ausgabe:', o, 'Erwartet:', t)

print('w1:', w1, 'w2:', w2)

input()
