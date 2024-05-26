# --------------------------------------------------------------
# eliza1.py
# Beispiel für einen Chat-Bot - Version 5
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 1
# Michael Weigend 18.9.2023
# --------------------------------------------------------------
import random
PHRASEN = ['Eliza: Kannst du mir das Problem näher erklären?',
           'Eliza: Erzähle mir mehr darüber!',
           'Eliza: Warum ist das wichtig für dich?']
           

print('Eliza: Hallo, ich bin Eliza. Was hast du auf dem Herzen?')
eingabe = 'x'
while eingabe != '':
    eingabe = input('Du: ')
    if 'hass' in eingabe:
        print('Eliza: Hass kann Wertvolles zerstören.')
    elif 'liebe' in eingabe:
        print('Eliza: Liebe ist etwas Wunderbares.')
    elif 'schlaf' in eingabe:
        print('Eliza: Schlaf ist wichtig.')
    elif eingabe != '':
        text = random.choice(PHRASEN) 
        print(text)
        
print('Eliza: Es war wunderbar, mit dir zu reden. Bis bald!')
input()
