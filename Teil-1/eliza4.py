# --------------------------------------------------------------
# eliza1.py
# Beispiel für einen Chat-Bot - Version 4
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 1
# Michael Weigend 18.9.2023
# --------------------------------------------------------------
print('Eliza: Hallo, ich bin Eliza. Was hast du auf dem Herzen?')
eingabe = 'x'                                               #1
while eingabe != '':                                        #2
    eingabe = input('Du: ')                                 #3
    if 'hass' in eingabe:
        print('Eliza: Hass kann Wertvolles zerstören.')
    elif 'liebe' in eingabe:
        print('Eliza: Liebe ist etwas Wunderbares.')
    elif 'schlaf' in eingabe:
        print('Eliza: Schlaf ist wichtig.')
    elif eingabe != '':                                     #4
        print('Eliza: Kannst du mir das Problem näher erklären?')
print('Es war wunderbar, mit dir zu reden. Bis bald!')      #5          
