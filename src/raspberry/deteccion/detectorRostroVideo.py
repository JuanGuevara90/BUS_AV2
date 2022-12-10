import cv2                # Importar librería de open cv
import time               # Importar librería de tiempo
import os
from dotenv import load_dotenv
from os.path import join, dirname
from ..utiles.const import OPERACION_INGRESO,OPERACION_SALIDA
from ..controlador import controladorIngreso,controladorSalida


def init(operation):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    PATH_CASCADE = os.environ.get("PATH_CASCADE")
    
    cap = cv2.VideoCapture(0)
    """ Todo """
    """ if( operation == OPERACION_INGRESO ):
        cap = cv2.VideoCapture(0)     #Captura la imagen con la cámara
    else:
        cap = cv2.VideoCapture(1)   """ 
        
    faceClassif = cv2.CascadeClassifier(''+PATH_CASCADE)
    while True:              # Ciclo repetitivo hasta que la condición se vuelva verdadero
        try:
            ret,frame = cap.read()  # Bucle infinito hastan llegar a la instrucción brake
            #imAux = frame.copy()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Se define una nueva variable gray (marco)
            faces = faceClassif.detectMultiScale(gray, 1.3, 5)
            #cropped = frame.copy()
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)   

                cropped = frame[y:y+h, x:x+w]
                if( operation == OPERACION_INGRESO ):
                    print("Ingreso Pasajero")
                    controladorIngreso()
                
                if( operation == OPERACION_SALIDA ):
                    print("Salida Pasajero")
                    controladorSalida()
                    
                #cv2.imshow('CORTE1',cropped)
            cv2.imshow('frame',frame)         # Muestra una ventana
            #cv2.imshow('GRISS',gray)          #Muentra ventana en gris
            time.sleep(3)       # 
            k= cv2.waitKey(1)
            if k== 27:
                break
        except Exception as e:
            print(e)
    cap.release()         # Librera la imagen
    cv2.destroyAllWindows()  # Cierra todas las ventanas del imshow