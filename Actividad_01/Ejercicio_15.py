"""
Programa: Ejercicio_15.py
Propósito:
    Dada una lista de números en orden aleatorio, escribe un algoritmo que funcione en tiempo 
    O(n*log(n)) para encontrar el k-ésimo número más pequeño de la lista.
Fecha:28/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import random
import timeit

def crear_lista_aleatoria(longitud, rango):

    lista = []
    for i in range(longitud):
        lista.append(random.randint(0, rango)) #Rellenamos la lista con números aleatorios.

    return lista #Devolvemos el valor al programa principal.

def buscar_minimo(lista, numero):

    lista=set(lista) #Eliminamos los elementos repetidos de la lista.
    lista=list(lista)
    lista.sort() #Ordenamos la lista de menor a mayor.

    return lista[numero-1] #Devolvemos el valor al programa principal.


try:
    rango = int(input("Introduce hasta que número aleatorio quieres trabajar: "))
    numero = int(input("Dime el k-ésimo número más pequeño que quieras encontrar en la lista: "))

    if (rango < 0) or (numero < 1):
        print("Error, ha ocurrido algo inesperado.")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

except ValueError:
    print("Error, ha ocurrido algo inesperado.")
    input("Pulse ENTER para finalizar.")
    quit() #Salimos del programa

ejecuciones = 0
seg_tot = 0
print("\n          Tamaño                 Minimo            Tiempo")
for i in range(10000, 300000 + 1, 10000):

    lista = crear_lista_aleatoria(i, rango)

    tiempo = timeit.Timer("buscar_minimo(lista, numero)","from __main__ import buscar_minimo, lista, numero").timeit(number=1000) #Guardamos el tiempo de ejecución en una variable.
    minimo = buscar_minimo(lista, numero) #Guardamos el valor mínimo en una variable.
    ejecuciones += 1
    seg_tot += tiempo

    print("%15d       %15i      %15.5f" %(i, minimo, tiempo)) #Mostramos los resultados.

print("\nPromedio de tiempo: %1.5f"%(seg_tot/ejecuciones))

print("\nComo se puede comprobar, el tiempo de ejecución va aumentando, esto se debe a que el algoritmo funciona en tiempo O(n*log(n)).")

input("\nPulse ENTER para finalizar.")