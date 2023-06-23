# HandyVol

Este proyecto consiste en la implementación de un control de volumen de audio utilizando la detección de gestos de la mano mediante visión artificial. Se utiliza Python en conjunto con las bibliotecas OpenCV, mediapipe, ctypes, comtypes y pycaw para lograr este objetivo.

Desde el Instituto Politécnico Formosa - Argentina

## Requisitos

- Python 3.x
- OpenCV (cv2)
- Mediapipe
- ctypes
- comtypes
- pycaw

## Cómo utilizar HandyVol

1. Clona este repositorio en tu máquina local.

```
git clone https://github.com/FacundoMajda/HandyVol
```

2. Navega hasta el directorio del proyecto.

```
cd HandyVol
```

3. Asegúrate de tener una cámara conectada a tu computadora.

4. Instala las dependencias requeridas ejecutando el siguiente comando:

```
pip install -r requirements.txt

```

5. Ejecuta el archivo `main.py`:

```
python main.py

```

6. La aplicación abrirá una ventana de video en tiempo real. Coloca tu mano frente a la cámara y utiliza los gestos definidos para controlar el volumen del audio.

## Archivos del proyecto

- `main.py`: Este archivo contiene el código principal para la ejecución del control de volumen mediante gestos de la mano.
- `HandTrackingModule.py`: Este archivo contiene la implementación de la clase `handDetector`, que se utiliza para detectar y rastrear la mano en las imágenes.
- `requirements.txt`: Archivo que lista las bibliotecas y sus versiones necesarias para ejecutar el proyecto.

## Contribuciones

Si deseas contribuir a este proyecto, ¡eres bienvenido! Puedes hacerlo siguiendo estos pasos:

1. Haz un fork de este repositorio y clónalo en tu máquina local.
2. Crea una nueva rama para realizar tus modificaciones:

```
git checkout -b feature/nueva-caracteristica

```

3. Realiza los cambios necesarios y realiza los commits correspondientes:

```
git commit -m "Agrega nueva característica: descripción"
```

4. Sube tus cambios al repositorio remoto:

```
git push origin feature/nueva-caracteristica
```

5. Abre una solicitud de extracción en GitHub y describe los cambios realizados.

Agradezco de antemano cualquier tipo de colaboración.

## Contacto

Si tienes alguna pregunta o consulta adicional, no dudes en contactarme a través de mi correo electrónico [facundomajda14@gmail.com]. Estaré encantado de ayudarte en lo que pueda.
