from array import array
from ast import Try
from sqlite3 import Error

def getDatosActuales(conn,fechaActual):
    try:
        sql_query= "select Fecha,Total_PasajerosActual,Total_Pasajeros, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"

        cursor=conn.execute(sql_query)
        arrayData =[]
        for i in cursor:
            arrayData.append(i[0])
            arrayData.append(i[1])
            arrayData.append(i[2])
            arrayData.append(i[3])
        return arrayData
    except Error as e:
        print(e)
    
def getRoutes(conn):
    try:
        sql_query= "select origen,destino from Bus"
        cursor=conn.execute(sql_query)
        arrayData =[]
        for i in cursor:
            arrayData.append(i[0])
            arrayData.append(i[1])
        return arrayData
    except Error as e:
        print(e)

def ingresarRegistroPasajeros(conn,fechaActual):
    try:

        sql_insert = "INSERT INTO Registro_Pasajeros (Fecha,Total_PasajerosActual,Total_Pasajeros,Aforo) VALUES ('"+fechaActual+"','1','1','20')"

        conn.execute(sql_insert)
        conn.commit()
    except Error as e:
        print(e)
        
def ingresarRutaBus(conn):
    try:
        sql_insert = "INSERT INTO Bus (origen,destino) VALUES ('Ibarra','Atuntaqui')"
        conn.execute(sql_insert)
        conn.commit()
    except Error as e:
        print(e)
    
def actualizarRegistroSuma(conn,fechaActual):
    try:
        sql_update ="update  Registro_Pasajeros set Total_PasajerosActual=Total_PasajerosActual+1 ,Total_Pasajeros=Total_Pasajeros+1 where Fecha='"+fechaActual+"'"
        conn.execute(sql_update)
        conn.commit()
    except Error as e:
        print(e)

def actualizarRegistroResta(conn,fechaActual):
    try:
        sql_update ="update  Registro_Pasajeros set Total_PasajerosActual=Total_PasajerosActual-1 where Fecha='"+fechaActual+"'"
        conn.execute(sql_update)
        conn.commit()
    except Error as e:
        print(e)
    
def disponibilidadBus(conn,fechaActual):
    try:
        sql_query= "select Total_PasajerosActual, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cursor=conn.execute(sql_query)
        for i in cursor:
            Total_PasajerosActual=i[0]
            aforo=i[1]
            if (Total_PasajerosActual<aforo):
                return True
            return False
    except Error as e:
        print(e)
    
def validateLeft(conn,fechaActual):
    try:
        sql_query= "select Total_PasajerosActual, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cursor=conn.execute(sql_query)
        for i in cursor:
            Total_PasajerosActual=i[0]
            if (Total_PasajerosActual>0):
                return True
            return False
    except Error as e:
        print(e)

def existeRegistrosFechaActual(conn,fechaActual):
    try:
        sql_query= "select count(*) from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cursor=conn.execute(sql_query)
        for i in cursor:
            if (i[0]>0):
                return True
            return False
    except Error as e:
        print(e)


def Asientosdisponibles(array):
    try:
        free =array[3]-array[1]
        return free 
    except Error as e:
        print(e)
