
import os
from raspberry.serial.sendData import connection


def agregar(datospantalla):
    puerto = connection()
  
    d1=(datospantalla[1])
    d2=(datospantalla[2])
    d3=(datospantalla[3])
    lblpi=d1
    lblps=d2
    lblpt=d3
    puerto.write(b'n00.val='+str(lblpi).encode()+b'\xFF\xFF\xFF')
    puerto.write(b'n1.val='+str(lblps).encode()+b'\xFF\xFF\xFF')
    puerto.write(b'n2.val='+str(lblpt).encode()+b'\xFF\xFF\xFF')

    #Estado del Bus
    dato=d1
    afverde=(d3*(1/3))
    afnaranja=(d3*(2/3))
    afrojo=d3
    if dato>=0 and dato<=afverde:
       puerto.write(b"t6.bco=GREEN"+b'\xFF\xFF\xFF')
    if dato>afverde and dato<=afnaranja:
       puerto.write(b"t6.bco=64512"+b'\xFF\xFF\xFF')
    if dato>afnaranja and dato<=afrojo:
       puerto.write(b"t6.bco=RED"+b'\xFF\xFF\xFF')
    if dato>=afrojo:
        puerto.write(b'tsw b1,'+str("0").encode()+b'\xFF\xFF\xFF')
        puerto.write(b"b1.bco=RED"+b'\xFF\xFF\xFF')

    
    """output= puerto.readline().hex()
    n= int (output)
    if (n>=0):
        print (n)
        os.system ("sudo shutdown now")"""

        