def getDatosActuales(conn, fechaActual):
    try:
        cur = conn.cursor()
        sql_query = "select Fecha,Total_PasajerosActual,Total_Pasajeros, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"

        cur.execute(sql_query)
        arrayData = []
        for i in cur.fetchall():
            arrayData.append(i[0])
            arrayData.append(i[1])
            arrayData.append(i[2])
            arrayData.append(i[3])
        return arrayData
    except:
        print("Error GetDatos actuales")


def getRoutes(conn):
    try:
        cur = conn.cursor()
        sql_query = "select origen,destino from Bus"
        cur.execute(sql_query)
        arrayData = []
        for i in cur.fetchall():
            arrayData.append(i[0])
            arrayData.append(i[1])
        return arrayData
    except:
        print("Error GetRoutes")


def ingresarRegistroPasajeros(conn, fechaActual):
    try:
        cur = conn.cursor()

        sql_insert = "INSERT INTO Registro_Pasajeros (Fecha,Total_PasajerosActual,Total_Pasajeros,Aforo) VALUES ('" + \
            fechaActual+"','1','1','20')"

        cur.execute(sql_insert)
        conn.commit()
    except:
        print("Error ingresarRegistroPasajeros")


def ingresarRutaBus(conn):
    try:
        cur = conn.cursor()
        sql_insert = "INSERT INTO Bus (origen,destino) VALUES ('Ibarra','Atuntaqui')"
        cur.execute(sql_insert)
        conn.commit()
    except:
        print("Error ingresarRutaBus")


def actualizarRegistroSuma(conn, fechaActual):
    try:
        cur = conn.cursor()
        sql_update = "update  Registro_Pasajeros set Total_PasajerosActual=Total_PasajerosActual+1 ,Total_Pasajeros=Total_Pasajeros+1 where Fecha='"+fechaActual+"'"
        cur.execute(sql_update)
        conn.commit()
    except:
        print("Error actualizarRegistroSuma")


def actualizarRegistroResta(conn, fechaActual):
    try:
        cur = conn.cursor()
        sql_update = "update  Registro_Pasajeros set Total_PasajerosActual=Total_PasajerosActual-1 where Fecha='"+fechaActual+"'"
        cur.execute(sql_update)
        conn.commit()
    except:
        print("Error actualizarRegistroResta")


def disponibilidadBus(conn, fechaActual):
    try:
        cur = conn.cursor()
        sql_query = "select Total_PasajerosActual, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cur.execute(sql_query)
        for i in cur.fetchall():
            Total_PasajerosActual = i[0]
            aforo = i[1]
            if (Total_PasajerosActual < aforo):
                return True
            return False
    except:
        print("Error disponibilidadBus")


def validateLeft(conn, fechaActual):
    try:
        cur = conn.cursor()
        sql_query = "select Total_PasajerosActual, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cur.execute(sql_query)
        for i in cur.fetchall():
            Total_PasajerosActual = i[0]
            if (Total_PasajerosActual > 0):
                return True
            return False
    except:
        print("Error validateLeft")


def existeRegistrosFechaActual(conn, fechaActual):
    try:
        cur = conn.cursor()
        sql_query = "SELECT COUNT(*) FROM Registro_Pasajeros WHERE Fecha='" + \
            fechaActual+"'"
        cur.execute(sql_query)
        for i in cur.fetchall():
            if (i[0] > 0):
                conn.commit()
                return True
            return False
    except:
        print("error existeRegistrosFechaActual")


def Asientosdisponibles(array):
    try:
        free = array[3]-array[1]
        return free
    except:
        print("Error Asientosdisponibles")
