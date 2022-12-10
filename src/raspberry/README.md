# Detector de Rostros en un Bus

### Directorios importantes:
* database ->Conexion con la BD , operaciones y archivo de BD.
* deteccion -> detectorRostroVideo.py / Algoritmo de OpenCV
* serial -> Comuncación con arduino
* utiles -> getDateCurrent.py / Fecha actual del sistema ; const.py / Operaciones
* vista -> interfaz gráfica
* ini.py -> Punto de Inicio del programa
* controlador.py -> Archivo que maneja la lógica del programa
* requirements.txt -> Dependencias del proyecto
### Lenguajes usados:

* Python v3.6.13

### Librerias:
* OpenCV
* Sqlite3
* Pyserial
* DotEnv

### Comandos Raspberry Pi 4
> **Nota**: Abrir un terminal y ejecutar cada comando / dentro del raspberry/src.
#### 1. Instalar dependencias
```bash
$ pip install -r requirements.txt
```
#### 2. Ruta del proyecto
#### 2. Ruta del proyecto
```bash
$ cd /home/iw/tensorflow1/models/research/object_detection
```
#### 3. Comando para ejecutar en caso de ingreso de pasajeros
```bash
$ python -m raspberry.ini ingreso     
```
#### 4. Comando para ejecutar en caso de salida de pasajeros
```bash
$ python -m raspberry.ini salida    
```
#### 5. Comando para ejecutar vista
```bash
$ python -m raspberry.vista.VentanaDatos 
```