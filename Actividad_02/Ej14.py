"""
Programa: Ej14.py
Propósito: 
     Para implementar el método tamano contamos el número de nodos en la lista. Una 
    estrategia alternativa sería almacenar el número de nodos en la lista como una pieza 
    de datos adicional en la cabeza de la lista. Modifica la clase ListaNoOrdenada para 
    incluir esta información y reescribe el método tamano. ¿Qué complejidad tiene el 
    método tamano ahora?
Fecha: 18/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""

#Importamos la clase.
from Class_Listas_No_Ordenadas_14 import ListaNoOrdenada


#Definimos las variables.
lista = ListaNoOrdenada()

#Agregramos elementos a la lista.
lista.agregar(0)
lista.agregar(76)
lista.agregar(43)
lista.agregar(63)

#Mostramos los resultados.
print("\nLista no ordenada:",lista)
print("Tamaño O(n):",lista.tamano_orden_N())
print("Tamaño O(1):",lista.tamano_orden_1())


######################## Análisis: ########################

import timeit
from random import randint

#Creamos la función.
def crear_lista_aleatoria(i):

    lista = ListaNoOrdenada()

    for n in range(i):
        lista.agregar(randint(-i, i))
    
    return lista


#Definimos las variables.
lista_analisis = ListaNoOrdenada()
ejecuciones = 0
seg_total_orden_n = 0
seg_total_orden_1 = 0

print("\n\t\t * Análisis: * \n")
print("    Tamaño lista       T. O(n)         T. O(1)")

for i in range(10000, 1000000 + 1, 30000):

    lista_analisis = crear_lista_aleatoria(i) #Creamos la lista.

    tn = timeit.Timer("lista_analisis.tamano_orden_N()", "from __main__ import lista_analisis").timeit(number=1) #Guardamos el tiempo en una variable
    t1 = timeit.Timer("lista_analisis.tamano_orden_1()", "from __main__ import lista_analisis").timeit(number=1) #Guardamos el tiempo en una variable
    ejecuciones += 1
    seg_total_orden_n += tn
    seg_total_orden_1 += t1

    print("  %10d        %10.6f       %10.6f" % (i, tn, t1)) #Mostramos el resultado.

#Mostramos los promedios.
print("\nPromedio tamaño O(n): %1.6f"%(seg_total_orden_n/ejecuciones))
print("Promedio tamaño O(1): %1.6f"%(seg_total_orden_1/ejecuciones))

#Conclusión.
print("\nComo se puede observar en los tiempos mostrados anteriormente,\nel tiempo de ejecución del método antiguo es de orden = O(n),\nmientras que el nuevo es de orden = O(1).")

#FIN.
input("\nPulse ENTER para finalizar.")