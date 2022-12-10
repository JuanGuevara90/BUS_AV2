import sqlite3
from sqlite3 import Error
import os
from os.path import join, dirname
from dotenv import load_dotenv
from .operaciones import ingresarRutaBus

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PATH_DATABASE = os.environ.get("DATABASE")

def create_connection():
    db_file = PATH_DATABASE
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        print("aeee")
    
def main():
    
    try:
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Registro_Pasajeros (
                                            Fecha TIMESTAMP PRIMARY KEY,
                                            Total_PasajerosActual integer,
                                            Total_Pasajeros integer NOT NULL,
                                            Aforo interger
                                        ); """
        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS Bus (
                                        origen text,
                                        destino text
                                    );"""
        # create a database connection
        conn = create_connection()
        # create tables
        if conn is not None:
            print("Conexion BD correcta")
            # create projects table
            create_table(conn, sql_create_projects_table)

            # create tasks table
            create_table(conn, sql_create_tasks_table)
            ingresarRutaBus(conn)
            print("Ingreso correcto")
            return conn
        else:
            print("Error! cannot create the database connection.")
    except Error as e:
        print(e)
        

def isSqlite3Db():
    if not os.path.isfile(PATH_DATABASE): return False
    sz = os.path.getsize(PATH_DATABASE)

    if sz == 0: return True

    if sz < 100: return False
    
    with open(PATH_DATABASE, 'rb') as fd: header = fd.read(100)    

    return (header[:16] == b'SQLite format 3\x00')    
