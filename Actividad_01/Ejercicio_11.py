"""
Programa: Ejercicio_11.py
Propósito:
    Escribe dos funciones para encontrar el número mínimo en una lista. La primera función debe 
    comparar cada número de una lista con todos los demás de la lista. O(n**2). La segunda función debe 
    ser lineal O(n).
Fecha:22/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import random
import timeit

def crear_lista_aleatoria(n):

    lista = []

    #Rellenamos la lista con números aleatorios hasta que tenga n elementos.
    for i in range(n):
        lista.append(random.randint(0, n))

    return lista

def busca_lista_orden1(lista):

        minimo = lista[0]  #Asignamos un valor cualquiera a la variable "minimo".

        #Recorremos la lista
        for i in lista:
            if i < minimo:  #Si el numero que ocupa la posicion i es menor que la variable, los igualamos
                minimo=i

        return minimo #Devolvemos el valor de la variable al programa principal.

def busca_lista_orden2(lista):

        minimo = lista[0] #Asignamos un valor cualquiera a la variable "minimo".

        #Recorremos la lista
        for i in range(len(lista)):
            for j in range(len(lista)):
                if (minimo > lista[j]):
                    minimo = lista[j]

        return minimo #Devolvemos el valor de las variables al programa principal.


ejecuciones = 0
seg_tot1 = 0
seg_tot2 = 0
print("           Tamaño       Lista O(n)       Lista O(n²)")
for i in range(50, 500 + 1, 50):

    lista = list(crear_lista_aleatoria(i)) #Creamos la lista de longitud i.

    #Guardamos los tiempos de ejecución de variables distintas.
    t1 = timeit.Timer("busca_lista_orden1(lista)","from __main__ import busca_lista_orden1,lista").timeit(number=1000)
    t2 = timeit.Timer("busca_lista_orden2(lista)","from __main__ import busca_lista_orden2,lista").timeit(number=1000)
    seg_tot1 += t1
    seg_tot2 += t2
    ejecuciones += 1

    print("%15d  %15.5f  %15.5f" %(i,t1,t2)) #Mostramos los resultados.

print("\nPromedio de lista O(n):",(seg_tot1/ejecuciones))
print("Promedio de lista O(n²):",(seg_tot2/ejecuciones))

#Conclusión.
print("\nObservando la tabla se pueden obtener las siguientes conclusiones:")
print("1- El orden de la primera función es O(n)")
print("2- El orden de la segunda función es O(n²)")
print("\nPor lo tanto, la función más óptima es la primera, por ser de menor orden.")

input("\nPulse ENTER para finalizar.")