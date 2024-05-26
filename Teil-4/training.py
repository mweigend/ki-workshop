# --------------------------------------------------------------
# training.py
# Lernfähiger Währungsrechner
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 2
# Michael Weigend 18.9.2023
# --------------------------------------------------------------

a = 1

eingabeDollars = input('Betrag in Dollar: ')
while eingabeDollars != '':
    dollars = float(eingabeDollars)
    vorhersageEuros = a * dollars
    print('Vorhersage: ', round(vorhersageEuros, 2), '€')
    eingabeEuros = input('Tatsächlicher Betrag in Euro: ')
    euros = float(eingabeEuros)
    fehler = euros - vorhersageEuros
    print('Fehler:', fehler)
    a += 0.5 * fehler/dollars
    print('Neuer Wechselkurs a:', round(a, 4))
    
    eingabeDollars = input('Betrag in Dollar: ')

print('Auf Wiedersehen!')
input()
