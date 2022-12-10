import serial,os
import time 
from os.path import join, dirname
import serial
import os
from dotenv import load_dotenv
from os.path import join, dirname

def sendDatabySerial(msg):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    FRECUENCIA = os.environ.get("FRECUENCIA")
    DISPOSITIVO = os.environ.get("DISPOSITIVO")
    ser=serial.Serial(''+DISPOSITIVO, FRECUENCIA)
    time.sleep(2)
    ser.write(msg.encode("utf-8"))
    ser.close()

def sendDatabySerial2(msg):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    FRECUENCIA2 = os.environ.get("FRECUENCIA2")
    DISPOSITIVO2 = os.environ.get("DISPOSITIVO2")
    ser=serial.Serial(''+DISPOSITIVO2, FRECUENCIA2)
    ser.write(msg.encode("utf-8"))
    ser.close()

def arduino (mnsj):
  arduino = serial.Serial("/dev/ttyACM0", 9600)
  time.sleep(1)
  arduino.write(mnsj.encode("utf-8"))
  arduino.close()

def connection():
    puerto = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 0.2)
    if puerto.isOpen() == False:
        puerto.open()
    puerto.flushInput()
    puerto.flushOutput()
    return puerto




