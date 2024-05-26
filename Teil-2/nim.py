#---------------------------------------------
# nim.py
# Nim-Spiel, klassische Version
# Wer das letzte Streichholz nimmt, hat gewonnen.
#
# Version 2 (verbesserte Eingabe)
#
# Michael Weigend
# 15.04.2024
#----------------------------------------------
from random import randint
streichhölzer = [1, 2, 3, 4, 7]

def ausgabe():
    for i in streichhölzer:
        print(i)

def mensch_zieht(streichhölzer):
    ok = False
    while not ok:
        reihe = int(input("Reihe (1-5): ")) - 1
        anzahl = int(input("Wieviele Streichhölzer nimmst du? "))
        if 0 <= reihe <= 4:
            if anzahl <= streichhölzer[reihe]:
                streichhölzer[reihe] -= anzahl
                ok = True

def ki_zieht(streichhölzer):
    ok = False
    while not ok:
        reihe = randint(0, 4)
        if streichhölzer[reihe] > 0:
            streichhölzer[reihe] -= 1
            ok = True
        print("Ich nehme 1 Streichholz aus Reihe", reihe + 1)

ausgabe()
while sum(streichhölzer) != 0:
    mensch_zieht(streichhölzer)
    ausgabe()
    if sum(streichhölzer) == 0:
        print("Du hast gewonnen!")
    else:
        ki_zieht(streichhölzer)
        ausgabe()
        if sum(streichhölzer) == 0:
            print("Du hast verloren!")

        
    

            
        
    
