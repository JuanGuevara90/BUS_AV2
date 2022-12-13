from .utiles.getDateCurrent import getDate_Current
import RPi.GPIO as GPIO
from .database.operaciones import Asientosdisponibles, existeRegistrosFechaActual, ingresarRegistroPasajeros, disponibilidadBus, actualizarRegistroSuma, actualizarRegistroResta, validateLeft, getDatosActuales, getRoutes
from .database.conexion import create_connection
from .serial.sendData import sendDatabySerial
from .serial.sensorica import sensorica  # sensorica2
import os
from dotenv import load_dotenv
from os.path import join, dirname
from .vista.MostrarDatos import agregar


def controladorIngreso():
    if (controladorSensor):
        conn = create_connection()
        dateCurrent = getDate_Current()
        print(dateCurrent)
        if (existeRegistrosFechaActual(conn, dateCurrent)):
            if (disponibilidadBus(conn, dateCurrent)):
                actualizarRegistroSuma(conn, dateCurrent)
                ingreso = "Ingeso Pasajeros"
            else:
                bloqueo = "Bloqueo de puerta"
                print(bloqueo)

            # print(Bloq)
        else:
            """ Enviar al arduino """
            ingresarRegistroPasajeros(conn, dateCurrent)
            A = "Ingreso al inicio del dia"
            print(A)




def controladorSalida():
    if (controladorSensor()):
        conn = create_connection()
        dateCurrent = getDate_Current()
        if (existeRegistrosFechaActual(conn, dateCurrent)):
            if (validateLeft(conn, dateCurrent)):
                actualizarRegistroResta(conn, dateCurrent)
                """ Actualizar y enviar al arduino"""
                B = "Salida un pasajeros"

                print(B)
            else:
                print("Enviar al arduino ")

       

def controladorSensor():

    TRIGH = 23
    ECHO = 24
    distanciaS1 = (sensorica(TRIGH, ECHO))
    print(str(distanciaS1))

    if distanciaS1 <= 30:
        n = True
        return n
