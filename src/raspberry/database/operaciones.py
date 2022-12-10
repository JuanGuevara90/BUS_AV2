from array import array
import datetime 

from conexion import create_connection

conn = create_connection()

def getDate_Current():
    currentDatetime = datetime.datetime.now()
    formatDate = currentDatetime.strftime("%y-%m-%d")
    return formatDate

def getDatosActuales(conn,fechaActual):
    try:
        cur = conn.cursor()
        sql_query= "select Fecha,Total_PasajerosActual,Total_Pasajeros, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"

        cur.execute(sql_query)
        arrayData =[]
        for i in cur.fetchall():
            arrayData.append(i[0])
            arrayData.append(i[1])
            arrayData.append(i[2])
            arrayData.append(i[3])
        conn.close()
        return arrayData
    except:
        conn.close()
        print("Error GetDatos actuales")
    
def getRoutes(conn):
    try:
        cur = conn.cursor()
        sql_query= "select origen,destino from Bus"
        cur.execute(sql_query)
        arrayData =[]
        for i in cur.fetchall():
            arrayData.append(i[0])
            arrayData.append(i[1])
        conn.close()
        return arrayData
    except:
        conn.close()
        print("Error GetRoutes")

def ingresarRegistroPasajeros(conn,fechaActual):
    try:
        cur = conn.cursor()

        sql_insert = "INSERT INTO Registro_Pasajeros (Fecha,Total_PasajerosActual,Total_Pasajeros,Aforo) VALUES ('"+fechaActual+"','1','1','20')"

        cur.execute(sql_insert)
        conn.close()
    except:
        conn.close()
        print("Error ingresarRegistroPasajeros")
        
def ingresarRutaBus(conn):
    try:
        cur = conn.cursor()
        sql_insert = "INSERT INTO Bus (origen,destino) VALUES ('Ibarra','Atuntaqui')"
        cur.execute(sql_insert)
        conn.close()
    except:
        conn.close()
        print("Error ingresarRutaBus")
    
def actualizarRegistroSuma(conn,fechaActual):
    try:
        cur = conn.cursor()
        sql_update ="update  Registro_Pasajeros set Total_PasajerosActual=Total_PasajerosActual+1 ,Total_Pasajeros=Total_Pasajeros+1 where Fecha='"+fechaActual+"'"
        cur.execute(sql_update)
        conn.close()
    except:
        conn.close()
        print("Error actualizarRegistroSuma")

def actualizarRegistroResta(conn,fechaActual):
    try:
        cur = conn.cursor()
        sql_update ="update  Registro_Pasajeros set Total_PasajerosActual=Total_PasajerosActual-1 where Fecha='"+fechaActual+"'"
        cur.execute(sql_update)
        conn.close()
    except:
        conn.close()
        print("Error actualizarRegistroResta")
    
def disponibilidadBus(conn,fechaActual):
    try:
        cur = conn.cursor()
        sql_query= "select Total_PasajerosActual, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cur.execute(sql_query)
        for i in cur.fetchall():
            Total_PasajerosActual=i[0]
            aforo=i[1]
            if (Total_PasajerosActual<aforo):
                conn.close()
                return True
            return False
    except:
        conn.close()
        print("Error disponibilidadBus")
    
def validateLeft(conn,fechaActual):
    try:
        cur = conn.cursor()
        sql_query= "select Total_PasajerosActual, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cur.execute(sql_query)
        for i in cur.fetchall():
            Total_PasajerosActual=i[0]
            if (Total_PasajerosActual>0):
                conn.close()
                return True
            return False
    except:
        conn.close()
        print("Error validateLeft")

def existeRegistrosFechaActual(conn,fechaActual):
    try:
        cur = conn.cursor()
        print(fechaActual)
        sql_query= "SELECT COUNT(*) FROM Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        print(sql_query)
        cur.execute(sql_query)
        for i in cur.fetchall():
            if (i[0]>0):
                conn.close()
                return True
            return False
    except:
        conn.close()
        print("error existeRegistrosFechaActual")


def Asientosdisponibles(array):
    try:
        free =array[3]-array[1]
        return free 
    except:
        print("Error Asientosdisponibles")

print(getRoutes(conn))

existeRegistrosFechaActual(conn,getDate_Current())