import cv2
captura = cv2.VideoCapture(0) #abre la camara ('0' para la primera camara conectada, '1' para la segunda, etc)
#captura = cv2.VideoCapture("video.mp4") -> abre un video ya grabado para poder acceder a los fotogramas individuales del video

#captura.isOpened() -> devuelve 'True' si la camara esta abierta
while (captura.isOpened()): #mientras la camara siga abierta
    
    #captura.read() -> devuelve un booleano (indica si se pudo leer) y el frame capturado por la camara
    ret, imagen = captura.read()
    if ret == True: #si se pudo leer el frame capturado
        cv2.imshow("video", imagen) #lo muestro en una ventana llamada 'video'
        
        #cv2.waitKey(1) -> espera un evento de teclado por 1 milisegundo y devuelve el valor ASCII de la tecla presionada
        #pero esto puede devolver un numero superior a un byte (255)
        #& 0xFF -> en caso de que haya un valor superior a un byte, '& 0xFF' lo que hace es quedarse solo con el byte menos significativo,
        #(el de la derecha -> unidades)
        #ord('s') -> devuelve el valor ASCII del carácter que le pasemos
        
        if cv2.waitKey(1) & 0xFF == ord("s"): 
        # si la letra presionada durante 1 ms (recortada a un byte con '& 0xFF') es igual al valor ASCII de la 's':
            break #se rompe el ciclo
        
captura.release() #cierra la camara (por lo que deja de grabar xd)
cv2.destroyAllWindows() #cierra todas las ventanas abiertas por OpenCV