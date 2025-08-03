"""¿Cuál es el resultado de ejecutar en orden inverso los dos pasos del método agregar
de la Lista_No_Ordenada? ¿Qué tipo de referencia resultaría? ¿Qué tipos de
problemas pueden resultar?"""

import timeit
import numpy
import Class_Listas_No_Ordenadas as l1
import Class_Listas_No_Ordenadas_6 as l2

lista1 = l1.ListaNoOrdenada()
lista2 = l2.ListaNoOrdenada()

tiempoLista1 = timeit.Timer("lista1.tamano()", "from __main__ import lista1")
tiempoLista2 = timeit.Timer("lista2.tamano", "from __main__ import lista2")


print("------PRIMER MÉTODO-------")
print("Tamaño lista \t\t Caso mejor \t\t Caso peor \t\t Caso promedio")

for tamano in range (100, 1001, 100):

    tiempos = list()

    for a in range (5):

        for i in range(tamano):

            lista1.agregar(0)

        tiempos.append(tiempoLista1.timeit(number=1000))
    
    print(tamano, '\t\t', min(tiempos), '\t\t', max(tiempos), '\t', numpy.mean(tiempos))



print("------SEGUNDO MÉTODO-------")
print("Tamaño lista \t\t Caso mejor \t\t Caso peor \t\t Caso promedio")

for tamano in range (100, 1001, 100):

    tiempos = list()

    for a in range (5):

        for i in range(tamano):

            lista2.agregar(0)

        tiempos.append(tiempoLista2.timeit(number=1000))
    
    print(tamano, '\t\t', min(tiempos), '\t\t', max(tiempos), '\t', numpy.mean(tiempos))
