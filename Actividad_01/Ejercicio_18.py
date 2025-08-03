"""
Programa: Ejercicio_18.py
Propósito:
    Escribir una función que devuelva el número de valores que aparecen dos o más veces en un vector. 
    Calcular la complejidad temporal de dicha función y expresarla en notación asintótica. ¿Lista o 
    diccionario?
Fecha:25/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""

import timeit
import random

def crear_vector_aleatorio(n):

    vector = []

    #Rellenamos la lista con números aleatorios hasta que tenga n elementos.
    for i in range(n):
        vector.append(random.randint(0, n)) #Los números aleatorios estarán comprendidos entre 0 y n.

    return vector #Devolvemos el valor de las variables al programa principal.

def crear_diccionario(vector):

    diccionario = {}

    for i in vector:
        diccionario[i] = vector.count(i)  #Utilizamos count() para ver las apariciones del elemento en el vector.
    
    return diccionario #Devolvemos el valor de las variables al programa principal.

def buscar_apariciones_lista(lista):

    repetidos = []

    for i in range(len(lista)):
        if (lista.count(lista[i]) >= 2): #Utilizamos count() para ver las apariciones del elemento en el vector.
            if (lista[i] not in repetidos): #Comprobamos que el elemento no esté ya en la lista de repetidos para no añadirlo 2 veces.
                repetidos.append(lista[i]) #Añadimos el elemento a la lista de repetidos.

    return len(repetidos) #Devolvemos el valor de las variables al programa principal.

def buscar_apariciones_diccionario(diccionario):

    repetidos = []

    for i in range(len(diccionario)):
        if (list(diccionario.items())[i][1] >= 2): #Si el número que acompaña al elemento (repeticiones) es mayor o igual que 2.
            repetidos.append(list(diccionario.items())[i][0]) #Añadimos el elemento a la lista de repetidos.

    return len(repetidos) #Devolvemos el valor de las variables al programa principal.

ejecuciones = 0
seg_tot_list = 0
seg_tot_dicc = 0
print("          Tamaño            Lista           Diccionario")
for i in range(100, 600 + 1, 50):

    lista = list(range(i)) #Creamos la lista de longitud i.
    diccionario = crear_diccionario(lista) #Llamamos a la función para crear el diccionario.

    #Guardamos los tiempos de ejecución de variables distintas.
    t_lista = timeit.Timer("buscar_apariciones_lista(lista)","from __main__ import buscar_apariciones_lista,lista").timeit(number=1000)
    t_dicc = timeit.Timer("buscar_apariciones_diccionario(diccionario)","from __main__ import buscar_apariciones_diccionario,diccionario").timeit(number=1000)
    ejecuciones += 1
    seg_tot_list += t_lista
    seg_tot_dicc += t_dicc

    print("%15d    %15.5f    %15.5f" %(i,t_lista,t_dicc)) #Mostramos los resultados.

print("\nPromedio de tiempo lista: %1.5f"%(seg_tot_list/ejecuciones))
print("Promedio de tiempo diccionario: %1.5f"%(seg_tot_dicc/ejecuciones))

#Conclusión.
print("\nObservando la tabla se pueden obtener las siguientes conclusiones:")
print("1- El orden de la función que trabaja con listas es O(n)")
print("2- El orden de la función que trabaja con diccionarios es O(n)")
print("\nSin embargo, la función más óptima es la que tabaja con listas")

input("\nPulse ENTER para finalizar.")