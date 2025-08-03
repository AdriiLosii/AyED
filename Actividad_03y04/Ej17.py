"""
Programa: Ej17.py
Propósito:
    En la implementación de Vector Asociativo de las tablas hash, se eligió que el tamaño 
    de la tabla hash fuera 11. Si la tabla se llena, ésta debe agrandarse. Implementa el 
    método agregar para que la tabla se redimensione automáticamente cuando el factor 
    de carga alcance un valor predeterminado (puedes decidir el valor con base en su 
    apreciación de la carga en función del desempeño).
Fecha: 20/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos la clase.
from Class_Tabla_Hash_17 import *

#Definimos la tabla hash.
Tabla = TablaHash()

#Rellenamos la tabla hash y la mostramos a medida que se expande.
Tabla[22] = "1"
Tabla[23] = "2"
Tabla[24] = "3"
Tabla[25] = "4"
Tabla[26] = "5"
Tabla[27] = "6"
Tabla[28] = "7"
Tabla[29] = "8"
print("Tamaño total de la tabla hash:",Tabla.tamano_total)
print("Claves de la tabla:",Tabla.slots)
print("Datos de la tabla:",Tabla.datos)
print()

#Agrandamiento al siguiente primo automáticamente.
Tabla[30] = "9"
print("Tamaño total de la tabla hash:",Tabla.tamano_total)
print("Claves de la tabla:",Tabla.slots)
print("Datos de la tabla:",Tabla.datos)
print()

#Agrandamiento al siguiente primo automáticamente.
Tabla[31] = "10"
Tabla[32] = "11"
print("Tamaño total de la tabla hash:",Tabla.tamano_total)
print("Claves de la tabla:",Tabla.slots)
print("Datos de la tabla:",Tabla.datos)
print()

#Agrandamiento al siguiente primo automáticamente.
Tabla[17] = "a"
Tabla[18] = "b"
Tabla[19] = "c"
print("Tamaño total de la tabla hash:",Tabla.tamano_total)
print("Claves de la tabla:",Tabla.slots)
print("Datos de la tabla:",Tabla.datos)
print()

#FIN.
input("\nPulse ENTER para finalizar.")