# --------------------------------------------------------------
# eliza1.py
# Beispiel für einen Chat-Bot - Version 3
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 1
# Michael Weigend 18.9.2023
# --------------------------------------------------------------
print('Eliza: Hallo, ich bin Eliza. Was hast du auf dem Herzen?')
eingabe = input('Du: ')
if 'hass' in eingabe:
    print('Eliza: Hass kann Wertvolles zerstören.')
elif 'liebe' in eingabe:
    print('Eliza: Liebe ist etwas Wunderbares.')
elif 'schlaf' in eingabe:
    print('Eliza: Schlaf ist wichtig.')
else:
    print('Eliza: Kannst du mir das Problem näher erklären?')
