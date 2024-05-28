#----------------------------------------------------------------
# Dateiname: kamera_test.py
#
# Das Programm macht mit der angeschlossenen Kamera (Kanal 0)
# und gibt das NumPy-Array auf dem Bildschirm aus
#
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 7
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
import cv2
kamera = cv2.VideoCapture(0)
if not kamera.isOpened():
    print('Kamera nicht geöffnet!')
else:
    input('Drücke ENTER um ein Foto zu machen')
    get, frame = kamera.read()
    graustufen = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(graustufen)
    cv2.imshow('Geste', graustufen)
    cv2.waitKey(0)
kamera.release()

