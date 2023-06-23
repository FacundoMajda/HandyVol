import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


################################
wCam, hCam = 640, 480
################################

cap = cv2.VideoCapture(0)  # Inicializar la captura de video
cap.set(3, wCam)  # Establecer el ancho de la cámara
cap.set(4, hCam)  # Establecer el alto de la cámara
pTime = 0

detector = htm.handDetector(detectionCon=1, maxHands=1)  # Inicializar el detector de manos

# Obtener el control de volumen
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange = volume.GetVolumeRange()  # Obtener el rango de volumen
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
area = 0
colorVol = (255, 0, 0)

while True:
    success, img = cap.read()  # Leer una imagen de la cámara

    if not success:
        print("Error: no se pudo leer la imagen de la cámara")
        continue

    # Encontrar la mano
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)
    if len(lmList) != 0:

        # Filtrar basado en el tamaño del área de la mano
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
        if 250 < area < 1000:

            # Encontrar la distancia entre el índice y el pulgar
            length, img, lineInfo = detector.findDistance(4, 8, img)

            # Convertir la longitud en volumen
            volBar = np.interp(length, [50, 200], [400, 150])
            volPer = np.interp(length, [50, 200], [0, 100])

            # Reducir la resolución para que sea más suave
            smoothness = 10
            volPer = smoothness * round(volPer / smoothness)

            # Verificar qué dedos están levantados
            fingers = detector.fingersUp()

            # Si el meñique está abajo, establecer el volumen
            if not fingers[4]:
                volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                colorVol = (0, 255, 0)
            else:
                colorVol = (255, 0, 0)

    # Dibujar elementos en la imagen
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)  # Rectángulo del volumen
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)  # Barra de volumen
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)  # Porcentaje de volumen
    cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
    cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX, 1, colorVol, 3)  # Volumen establecido

    # Mostrar la tasa de cuadros por segundo
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)  # Mostrar la imagen
    cv2.waitKey(1)

# "Facundo Majda - Desde Formosa ARG"
