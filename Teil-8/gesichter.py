# --------------------------------------------------------------
# gesichter.py
# Aus einem Farbbild werden alle Gesichter erfasst und gezählt.
# Das erste erfasste Gesicht wird eingerahmt.
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 8
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
import cv2
FOTO = 'astronauten.png'
XMLDATEI = 'haarcascade_frontalface_default.xml'
bild = cv2.imread(FOTO)
grau = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)
klassifizierer = cv2.CascadeClassifier(XMLDATEI)
rechtecke = klassifizierer.detectMultiScale(grau,
                                            scaleFactor=1.05,
                                            minNeighbors=5)
n = len(rechtecke)
print('Ich habe', n, 'Gesichter gefunden.')
x,y,w,h  = rechtecke[0]
cv2.rectangle(bild, (x, y), (x+w, y+h), (0, 255, 255), 2)
cv2.imshow('Foto mit dem ersten erkannten Gesicht', bild)
cv2.waitKey(0)                 # warte bis Taste gedrückt
cv2.destroyAllWindows()        # Schließe das Viewer-Fenster
