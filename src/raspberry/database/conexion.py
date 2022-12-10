import psycopg2

from psycopg2 import Error
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PATH_DATABASE = os.environ.get("DATABASE")

def create_connection():
    db_file = PATH_DATABASE
    conn = None
    try:
        conn = psycopg2.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
