# --------------------------------------------------------------
# personen.py
# Lernfähiger Entscheidungsbaum
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 1
# Michael Weigend 18.9.2023
# --------------------------------------------------------------
import pickle

try:
    stream = open('daten.dat', mode='rb')
    baum = pickle.load(stream)
    stream.close()
except:
    baum = [('Ist die Person eine Frau?', 1, 2),
            ('Denkst du an Tina Turner?', -1, -1),
            ('Denkst du an Albert Einstein?', -1, -1)]
aktuell = 0
gefunden = False
print('Denke an eine berühmte Person.')

while not gefunden:
    frage, ja, nein = baum[aktuell]
    eingabe = input(frage + ' (j/n): ')
    if ja == -1:
        if eingabe == 'j':
            gefunden = True
        else:
            print('Wie heißt die Person, an die du denkst?')
            name = input('Name: ')
            print('Denke dir eine Frage aus, mit der man ')
            print('die Person von der Person unterscheiden kann,')
            print('die ich gerade genannt habe. Diese Frage')
            print('muss man bei deiner Person mit "ja" und bei der') 
            print('anderen Person mit "nein" beantworten können.')
            neueFrage = input('Frage: ')
            jaNeu = len(baum)
            neinNeu = jaNeu + 1
            baum[aktuell] = (neueFrage, jaNeu, neinNeu)
            baum += [('Denkst du an ' + name + '?', -1, -1)]
            baum += [(frage, -1, -1)]
    else:
        if eingabe == 'j':
            aktuell = ja
        else:
            aktuell = nein
            
print('Die Person wurde gefunden.')
stream = open('daten.dat', mode='wb')
pickle.dump(baum, stream)
stream.close()
input()
                  
    
