from ..database.operaciones import getDatosActuales
from ..database.conexion import create_connection
from ..serial.sendData import sendDatabySerial
from ..utiles.getDateCurrent import getDate_Current


def init_led():
     
    while (True):
        try:
            conn=create_connection()   
            Sal = getDatosActuales(conn, getDate_Current())
            salard = str(Sal[1])
            sendDatabySerial(salard)
            print(salard)
        except:
            print("error_led")
