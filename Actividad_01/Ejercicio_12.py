"""
Programa: Ejercicio_12.py
Propósito:
    Diseña un experimento para verificar que el operador indexación para listas es O(1).
Fecha:26/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import timeit
import random

def indexacion(i):
    elemento = [random.randint(0, i)] #Indexación de un número aleatorio.

ejecuciones = 0
seg_tot = 0
print("        Tamaño:      T. indexación:")
for i in range(1000000, 100000000 + 1, 1000000):

    tiempo = timeit.Timer("indexacion(i)", "from __main__ import indexacion,i").timeit(number=1000) #Guardamos el tiempo en una variable.
    seg_tot += tiempo
    ejecuciones += 1

    print("%15d %15.3f" %(i, tiempo)) #Mostramos los resultados.

print("\nPromedio tiempo de indexación: %1.3f"%(seg_tot/ejecuciones))

#Conclusión.
print("\nObservando la tabla de arriba se puede comprobar que los resultados para el tiempo \nson un número constante (%1.3f segundos), por lo tanto el orden de la indexación = O(1)\n"%(seg_tot/ejecuciones))

input("Pulse ENTER para finalizar.")