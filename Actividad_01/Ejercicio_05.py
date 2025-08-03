"""
Programa: Ejercicio_05.py
Propósito: Reescribir la clase común Clase Fecha, de manera que sea robusta y completarla con métodos
necesarios
Fecha:19/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""

from Clase_Fecha_05 import *
from datetime import *

hoy=str(datetime.now()).split()
hoy=hoy[0].split('-')
hoy=hoy[::-1] #Le damos la vuelta a la lista
fecha_hoy = Fecha(hoy)

fecha_int = input('Dime el dia,mes,año o bien dia/mes/año: ').strip()  #Pedimos al usuario la fecha

#Cambiamos los símbolos ',' y '/' por espacios y creamos una lista con la fecha
fecha_int = fecha_int.replace(',', ' ')
fecha_int = fecha_int.replace('/', ' ')
fecha_int = fecha_int.split()

fecha_int = Fecha(fecha_int)

print('\nTu fecha: ', fecha_int)

if fecha_int.comprueba_fecha():    #Si la fecha introducida es correcta mostramos los datos en pantalla
    print("La fecha con la que comparamos:", fecha_hoy)
    print("¿Año Bisiesto?", fecha_int.bisiesto())
    print("¿Menor que la fecha actual?", fecha_int.es_menor(fecha_hoy))
    print("¿Mayor que la fecha actual?", fecha_int.es_mayor(fecha_hoy))
    print("¿La fecha es distinta?", fecha_int.es_distinto(fecha_hoy))
    print("¿La fecha es igual?", fecha_int.es_igual(fecha_hoy))
else:
    print("La fecha que has introducido no es correcta, por favor revisala")  #Si la fecha es incorrecta lo notificamos

input("\nPulse ENTER para finalizar.")