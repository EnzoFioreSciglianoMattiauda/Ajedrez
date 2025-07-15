import cv2
import numpy as np # para despues
captura = cv2.VideoCapture(0) #abro la camara
ret, frame_anterior = captura.read() #guardo el primer frame
frame_anterior = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY) # lo convierto a escala de grises
frame_anterior = cv2.GaussianBlur(frame_anterior, (21,21), 0) #aplica un suavizado a la imagen con la funcion gaussiana
# le pasamos el frame anterior, el tamaño del kernel (que es como una ventana que se va moviendo por toda la imagen y en cada posicion 
# toma los pixeles de la zona y calcula el valor de los pixeles con la formula de la campana 2d de gauss )

while (captura.isOpened()): #mientra la camara este abierta
    
    ret, frame_actual = captura.read() #guardo el frame actual
    
    gris = cv2.cvtColor(frame_actual, cv2.COLOR_BGR2GRAY) # lo vuelvo gris
    gris = cv2.GaussianBlur(frame_actual, (21,21), 0) # le aplico el suavizado gaussiano
    
    diferencia = cv2.absdiff(frame_anterior, gris) #crea una imagen en donde el valor de cada pixel = valor_anterior - valor_actual
    #si un pixel no cambio -> diferencia = 0 (negro), si cambio mucho -> diferencia alta (blanco)
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

captura.release()
cv2.destroyAllWindows()