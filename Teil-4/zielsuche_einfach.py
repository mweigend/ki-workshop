#-----------------------------------------------------
# zielsuche_eine_iteration_langsam.py
# Die Turtle zeichnet eine Landschaft mit Start, Ziel und Hindernissen
# Dann sucht sie einen Weg von Start zu Ziel.
# Trufft sie auf ein Hndernis, weicht sie zurück.
# Nach einer Idee von Wilfried Baumann,
# Österreichische Computergesellschaft (OCG)
#
# Michael Weigend 23. 11. 2024
#---------------------------------------------------
from turtle import *
from random import choice, randint
BREITE, HÖHE = 800, 500
S = 25  # Strecke für eine elementare Bewegung
START = (-350, -100, 10)     # x, y, radius
ZIEL = (330, 50, 40)        # x, y, radius
HINDERNISSE = [(-300, 100, 50),
               (-260, -170, 60),
               (-180, 200, 30),
               (-130, -100, 40),
               (-70, 100, 50),
               (50, 180, 40),
               (90, -100, 60),
               (110, 20, 30),
               (150, -200, 40),
               (210, -100, 30),
               (260, 200, 40),]

def zeichne(punkt, farbe):
    up()
    x, y, radius = punkt
    goto(x, y)
    dot(2 * radius, farbe)    # dot() verwendet durchmesser

def kollision():
    x, y = pos()    # Position der Turtle
    if not(-BREITE/2 < x < BREITE/2): 
        return True
    if not(-HÖHE/2 < y < HÖHE/2): 
        return True
    for a, b, h in HINDERNISSE:
        if distance(a, b) < h:
            return True
    return False

def geradeaus(zurück=False):
    if not zurück:
        forward(S)
    else:
        backward(S)

def links(zurück=False):
    if not zurück:
        for i in range(5):
            left(6)
            forward(S/5)
    else:
        for i in range(5):
            forward(-S/5)
            right(6)
        
def scharf_links(zurück=False):
    if not zurück:
        for i in range(5):
            left(12)
            forward(S/5)
    else:
        for i in range(5):
            forward(-S/5)
            right(12)

def rechts(zurück=False):
    if not zurück:
        for i in range(5):
            right(6)
            forward(S/5)
    else:
        for i in range(5):
            forward(-S/5)
            left(6)
        
def scharf_rechts(zurück=False):
    if not zurück:
        for i in range(5):
            right(12)
            forward(S/5)
    else:
        for i in range(5):
            forward(-S/5)
            left(12)

def zeichne_landschaft():
    reset()
    for h in HINDERNISSE:
        zeichne(h, 'lightgrey')
    zeichne(START, 'green')
    zeichne(ZIEL, 'blue')



def suche():
    kommandos = []   
    color('green')
    schritte = 0   
    while distance(ZIEL[0], ZIEL[1]) > ZIEL[2]:
        kommando = choice([scharf_links, links, geradeaus,
                           rechts, scharf_rechts])
        kommandos.append(kommando)
        kommando()
        schritte += 1
        if kollision():
            for i in range(2):
                if kommandos:
                   kommando = kommandos.pop()      
                   kommando(zurück=True)
                   schritte += 1
    return schritte, kommandos

def zeichne_route(kommandos):
    # Zweiter Durchlauf: Ausführung der Kommandofolge (ohne erfolglose Kommandos
    up()
    goto(START[0], START[1])
    setheading(0)
    down()
    color('red')
    width(5)
    for kommando in kommandos:
        kommando()


# Hauptprogramm
Screen().setup(BREITE + 50, HÖHE + 50)
speed(0)
zeichne_landschaft()
up()
goto(START[0], START[1])
down()
schritte, kommaandos = suche()
zeichne_route(kommandos)
print('Schritte vorher:', schritte, 'nachher:', len(kommandos))













