from ..database.operaciones import getDatosActuales
from ..database.conexion import create_connection
from ..vista.MostrarDatos import agregar
from ..utiles.getDateCurrent import getDate_Current


def init_hmi():
    
    while (True):
        try:            
            conn= create_connection()
            Sal = getDatosActuales(conn, getDate_Current())
            agregar(Sal)
            print(Sal)
        except:
            print("error_hmi")
