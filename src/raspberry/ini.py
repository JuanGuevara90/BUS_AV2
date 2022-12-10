import sys
from .deteccion.detectorRostroVideo import init
from .utiles.const import OPERACION_INGRESO,OPERACION_SALIDA

if __name__ == "__main__":
    try:
        array = sys.argv
        n = len(array)
        if( n == 2 ):
            if( array[1] == OPERACION_INGRESO or array[1] == OPERACION_SALIDA ):
                init(array[1])
            else:
                print("Ingrese como segundo parametro <ingreso> o <salida>")
        else:
            print("Ingrese dos parametros")
    except Exception as e:
            print(e)