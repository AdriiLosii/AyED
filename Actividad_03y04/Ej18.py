"""
Programa: Ej18.py
Propósito:
    Implementa la prueba cuadrática como una técnica de rehash.
Fecha: 23/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos la clase.
from Class_Tabla_Hash_18 import *

#Definimos las variables.
Tabla = TablaHash()

#Añadimos items a la tabla (tamaño 11).
Tabla[44] = "cabra" #Posición: 44%11 = 0.
Tabla[55] = "cerdo" #Posición: 55%11 = 0 -> rehash cuadrado perfecto 1*1 = 1.
Tabla[66] = "elefante" #Posición: 66%11 = 0 -> rehash cuadrado perfecto 2*2 = 4.
Tabla[11] = "zebra" #Posición: 11%11 = 0 -> rehash cuadrado perfecto 3*3 = 9.
Tabla[40] = "pollo" #Posición: 40%11 = 7.

#Mostramos los slots y los datos de la tabla hash.
print(Tabla.slots)
print(Tabla.datos)

#FIN.
input("\nPulse ENTER para finalizar.")