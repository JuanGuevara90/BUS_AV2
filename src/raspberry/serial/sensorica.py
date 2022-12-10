
import RPi.GPIO as GPIO
import time
from os.path import join, dirname
import os
from dotenv import load_dotenv

 

def sensorica(TRIGH,ECHO):
    GPIO.setmode(GPIO.BCM)     #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi            
    GPIO.setup(TRIGH, GPIO.OUT) #Configuramos el pin TRIG como una salida 
    GPIO.setup(ECHO, GPIO.IN) 

        # Ponemos en bajo el pin TRIG y después esperamos 0.5 seg para que el transductor se estabilice
    GPIO.output(TRIGH, GPIO.LOW)
    time.sleep(0.5)

        #Ponemos en alto el pin TRIG esperamos 10 uS antes de ponerlo en bajo
    GPIO.output(TRIGH, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGH, GPIO.LOW)

        # En este momento el sensor envía 8 pulsos ultrasónicos de 40kHz y coloca su pin ECHO en alto
        # Debemos detectar dicho evento para iniciar la medición del tiempo
        
    while True:
        pulso_inicio = time.time()
        if GPIO.input(ECHO) == GPIO.HIGH:
            break

        # El pin ECHO se mantendrá en HIGH hasta recibir el eco rebotado por el obstáculo. 
        # En ese momento el sensor pondrá el pin ECHO en bajo.
	# Prodedemos a detectar dicho evento para terminar la medición del tiempo
        
    while True:
        pulso_fin = time.time()
        if GPIO.input(ECHO) == GPIO.LOW:
           break

        # Tiempo medido en segundos
    duracion = pulso_fin - pulso_inicio

        #Obtenemos la distancia considerando que la señal recorre dos veces la distancia a medir y que la velocidad del sonido es 343m/s
    distancia = (34300 * duracion) / 2

        # Imprimimos resultado
            #print( "Distancia: %.2f cm" % distancia)
    return distancia  
GPIO.cleanup()

    
