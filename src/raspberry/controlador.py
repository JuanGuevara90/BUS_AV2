from .utiles.getDateCurrent import getDate_Current
import RPi.GPIO as GPIO
from .database.operaciones import Asientosdisponibles, existeRegistrosFechaActual,ingresarRegistroPasajeros,disponibilidadBus,actualizarRegistroSuma,actualizarRegistroResta,validateLeft,getDatosActuales,getRoutes
from .database.conexion import create_connection,main,isSqlite3Db
from .serial.sendData import sendDatabySerial,sendDatabySerial2
from .serial.sensorica import sensorica #sensorica2
import os
from dotenv import load_dotenv
from os.path import join, dirname
from .vista.MostrarDatos import agregar


def controladorIngreso():
    if(controladorSensor):
        if( isSqlite3Db() ): 
            conn = create_connection()
        else:
            conn = main()
        dateCurrent = getDate_Current()
        if( existeRegistrosFechaActual( conn , dateCurrent)  ):
            if( disponibilidadBus( conn , dateCurrent ) ):
                actualizarRegistroSuma( conn , dateCurrent )
                ingreso="Ingeso Pasajeros"
            else:
                bloqueo="Bloqueo de puerta"
                print(bloqueo)
        
            #print(Bloq)
        else:
            """ Enviar al arduino """
            ingresarRegistroPasajeros( conn , dateCurrent )
            A="Ingreso al inicio del dia"
            print(A)

        Ing=getDatosActuales(conn,dateCurrent)
        agregar(Ing)
        enarduin=str(Ing[1])
        sendDatabySerial(enarduin)
        print(enarduin)

def controladorSalida():
    if(controladorSensor()):
        if( isSqlite3Db() ): 
            conn = create_connection()
            dateCurrent = getDate_Current()
            if( existeRegistrosFechaActual( conn , dateCurrent )):
                if( validateLeft( conn , dateCurrent )):
                    actualizarRegistroResta( conn , dateCurrent )
                    """ Actualizar y enviar al arduino"""
                    B="Ingreso un pasajeros"
                
                    print(B)               
                else:
                    print("Enviar al arduino ")   

        Sal=getDatosActuales(conn,dateCurrent)
        agregar(Sal)
        salard=str(Sal[1])
        sendDatabySerial(salard)
        print(salard)
   
        
       

def controladorDatos():
    datospantalla=[]
    if( isSqlite3Db() ): 
        conn = create_connection()
        dateCurrent = getDate_Current()
        datospantalla=(getDatosActuales(conn,dateCurrent))
        print(datospantalla)
    return datospantalla



def SendData(conn,dateCurrent):
    des1=(getRoutes(conn))  
    print(des1)
    Sal=(getDatosActuales(conn,dateCurrent))
    salard=str(Sal[1])
    sendDatabySerial(salard)
    print(salard)
    return Sal



def controladorSensor():

    TRIGH = 23
    ECHO = 24
    distanciaS1=(sensorica(TRIGH,ECHO))
    print(str(distanciaS1))

    if distanciaS1<=30:
        n=True
        return n 
    

