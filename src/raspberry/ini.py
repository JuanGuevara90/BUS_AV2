import sys
from .deteccion.detectorRostroVideo import init
from .utiles.const import OPERACION_INGRESO, OPERACION_SALIDA
from .hmi.hmi import init_hmi
from .led.led import init_led
from threading import Thread

if __name__ == "__main__":
    try:
        array = sys.argv
        n = len(array)
        if (n == 2):
            if (array[1] == OPERACION_INGRESO or array[1] == OPERACION_SALIDA):
                t1 = Thread(target=init,args=(array[1],))
                t2 = Thread(target=init_hmi)
                t3 = Thread(target=init_led)
                # start the threads
                t1.start()
                t2.start()
                t3.start()
                t1.join()
                t2.join()
                t3.join()


            else:
                print("Ingrese como segundo parametro <ingreso> o <salida>")
        else:
            print("Ingrese dos parametros")
    except Exception as e:
        print(e)
