"""
Programa: Ej21.py
Propósito:
    Realiza una prueba de referencia (Benchmark ) para un ordenamiento de Shell,
    utilizando diferentes conjuntos de incrementos en la misma lista (los expresados en
    los apuntes y dos más…).
Fecha: 23/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importacion de modulos 
from math import *
import timeit
from random import randint


#Creamos la función para generar la lista aleatoria.
def crea_lista_aleatoria(tamaño):

    #Definimos las variables.
    lista = []

    for i in range(tamaño):
        lista.append(randint(0, tamaño*4)) #Rellenamos la lista con número aleatorios desde 0 hasta 200*4.

    return lista

#Creamos la función.
def ordenamiento_shell_mitad(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy() #Usamos .copy() para que la lista original no se modifique.
    sublistas = len(lista_ordenada)//2 #Número de sublistas = Valor del incremento.

    while (sublistas != 0):
        for i in range(sublistas):
            insercion_sublista_mitad(lista_ordenada, i, sublistas) #Llamamos a la función para ordenar las sublistas mediante inserción.

        sublistas = sublistas//2 #Reducimos el número de sublistas a la mitad después de cada recorrido.
    
    return lista_ordenada

#Creamos la función auxiliar al ordenamiento shell.
def insercion_sublista_mitad(lista_ordenada, inicio, incremento):

    for i in range(inicio+incremento, len(lista_ordenada), incremento): #Recorremos los valores de la sublista.
        actual = lista_ordenada[i] #Guardamos el valor de la posición actual.

        #Cuando el valor del incremento inicial (donde se inicia el salto), es mayor que el siguiente (donde cae el salto), los valores se intercambian.
        while (i >= incremento and lista_ordenada[i-incremento] > actual):
            lista_ordenada[i] = lista_ordenada[i-incremento]
            i = i-incremento
            lista_ordenada[i] = actual

#Creamos la función.
def ordenamiento_shell_raiz(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy() #Usamos .copy() para que la lista original no se modifique.
    sublistas = int(sqrt(len(lista_desordenada))) #Número de sublistas = Valor del incremento.

    while (sublistas != 1):
        for i in range(sublistas):
            insercion_sublista_raiz(lista_ordenada, i, sublistas)

        sublistas = int(sqrt(sublistas)) #Reducimos el valor del incremento.

    insercion_sublista_raiz(lista_ordenada, 0, sublistas) #Llamamos a la función una última vez para realizar la inserción con incremento = 1.

    return lista_ordenada

#Creamos la función auxiliar para el ordenamiento Shell.
def insercion_sublista_raiz(lista_ordenada, inicio, incremento):

    for i in range(inicio, len(lista_ordenada), incremento): #Recorremos los valores de la sublista.
        actual = lista_ordenada[i] #Guardamos el valor de la posición actual.

        #Cuando el valor del incremento inicial (donde se inicia el salto), es mayor que el siguiente (donde cae el salto), los valores se intercambian.
        while (i >= incremento and lista_ordenada[i-incremento] > actual):
            lista_ordenada[i] = lista_ordenada[i-incremento]
            i = i-incremento
            lista_ordenada[i] = actual

#Creamos la función.
def ordenamiento_shell_knuth(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy()
    secuencia_knuth = []
    h = 1

    #Obtenemos la secuencia de Knuth.
    while (int((3**h-1)/2) <= len(lista_ordenada)):
        secuencia_knuth.append(int((3**h-1)/2))
        h += 1

    secuencia_knuth = secuencia_knuth[::-1] #Giramos el orden (de incremento mayor a incremento menor).
    sublistas = len(secuencia_knuth) #Obtenemos el número de sublistas.

    #Ordenamos la lista con cada valor de incremento.
    for incremento in secuencia_knuth:
        for i in range(sublistas):
            insercion_sublista_knuth(lista_ordenada, i, incremento)

    return lista_ordenada

#Creamos la función auxiliar para el ordenamiento shell con secuencia Knuth.
def insercion_sublista_knuth(lista_ordenada, inicio, incremento):

    for i in range(inicio+incremento, len(lista_ordenada), incremento): #Recorremos los valores de la sublista.
        actual = lista_ordenada[i] #Guardamos el valor de la posición actual.

        #Cuando el valor del incremento inicial (donde se inicia el salto), es mayor que el siguiente (donde cae el salto), los valores se intercambian.
        while (i >= incremento and lista_ordenada[i-incremento] > actual):
            lista_ordenada[i] = lista_ordenada[i-incremento]
            i = i-incremento
            lista_ordenada[i] = actual

#Creamos la función.
def ordenamiento_shell_sedgewick(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy()
    secuencia_sedgewick = [1]
    k = 1

    #Obtenemos la secuencia de Knuth.
    while (int(pow(4, k)+3*pow(2, k-1)+1) <= len(lista_ordenada)):
        secuencia_sedgewick.append(int(pow(4, k)+3*pow(2, k-1)+1))
        k += 1

    secuencia_sedgewick = secuencia_sedgewick[::-1] #Giramos el orden (de incremento mayor a incremento menor).
    sublistas = len(secuencia_sedgewick) #Obtenemos el número de sublistas.

    #Ordenamos la lista con cada valor de incremento.
    for incremento in secuencia_sedgewick:
        for i in range(sublistas):
            insercion_sublista_sedgewick(lista_ordenada, i, incremento)

    return lista_ordenada

#Creamos la función auxiliar para el ordenamiento shell con secuencia Sedgewick.
def insercion_sublista_sedgewick(lista_ordenada, inicio, incremento):

    for i in range(inicio+incremento, len(lista_ordenada), incremento): #Recorremos los valores de la sublista.
        actual = lista_ordenada[i] #Guardamos el valor de la posición actual.

        #Cuando el valor del incremento inicial (donde se inicia el salto), es mayor que el siguiente (donde cae el salto), los valores se intercambian.
        while (i >= incremento and lista_ordenada[i-incremento] > actual):
            lista_ordenada[i] = lista_ordenada[i-incremento]
            i = i-incremento
            lista_ordenada[i] = actual

#Creamos la función.
def ordenamiento_shell_hibbard(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy()
    secuencia_hibbard = []
    i = 1

    #Obtenemos la secuencia de Knuth.
    while (int(pow(2, i)-1) <= len(lista_ordenada)):
        secuencia_hibbard.append(int(pow(2, i)-1))
        i += 1

    secuencia_hibbard = secuencia_hibbard[::-1] #Giramos el orden (de incremento mayor a incremento menor).
    sublistas = len(secuencia_hibbard) #Obtenemos el número de sublistas.

    #Ordenamos la lista con cada valor de incremento.
    for incremento in secuencia_hibbard:
        for i in range(sublistas):
            insercion_sublista_hibbard(lista_ordenada, i, incremento)

    return lista_ordenada

#Creamos la función auxiliar para el ordenamiento shell con secuencia Hibbard.
def insercion_sublista_hibbard(lista_ordenada, inicio, incremento):

    for i in range(inicio+incremento, len(lista_ordenada), incremento): #Recorremos los valores de la sublista.
        actual = lista_ordenada[i] #Guardamos el valor de la posición actual.

        #Cuando el valor del incremento inicial (donde se inicia el salto), es mayor que el siguiente (donde cae el salto), los valores se intercambian.
        while (i >= incremento and lista_ordenada[i-incremento] > actual):
            lista_ordenada[i] = lista_ordenada[i-incremento]
            i = i-incremento
            lista_ordenada[i] = actual


#Análisis:
#Definimos las variables.
ejecuciones = 0
seg_tot_mitad = 0
seg_tot_raiz = 0
seg_tot_knuth = 0
seg_tot_sedgewick = 0
seg_tot_hibbard = 0

input("\nPulse ENTER para comenzar el análisis.")
print("\n\t\t\t\t\t\t\t\t * Benchmark: * \n")
print("     Tamaño            T. Shell original            T. Shell raíz           T. Shell Knuth        T. Shell Sedgewick       T. Shell Hibbard")

for i in range(250, 10000 + 1, 250): #Aumentamos el tamaño de la lista a ordenar con cada llamada.

    lista_no_ordenada = crea_lista_aleatoria(i) #Creamos la lista aleatoria.

    #Llamamos a las funciones de ordenación y guardamos el tiempo en una variables.
    t_mitad = timeit.Timer("ordenamiento_shell_mitad(lista_no_ordenada)", "from __main__ import ordenamiento_shell_mitad, lista_no_ordenada").timeit(number=1)
    t_raiz = timeit.Timer("ordenamiento_shell_raiz(lista_no_ordenada)", "from __main__ import ordenamiento_shell_raiz, lista_no_ordenada").timeit(number=1)
    t_knuth = timeit.Timer("ordenamiento_shell_knuth(lista_no_ordenada)", "from __main__ import ordenamiento_shell_knuth, lista_no_ordenada").timeit(number=1)
    t_sedgewick = timeit.Timer("ordenamiento_shell_sedgewick(lista_no_ordenada)", "from __main__ import ordenamiento_shell_sedgewick, lista_no_ordenada").timeit(number=1)
    t_hibbard = timeit.Timer("ordenamiento_shell_hibbard(lista_no_ordenada)", "from __main__ import ordenamiento_shell_hibbard, lista_no_ordenada").timeit(number=1)
    
    #Guardamos los datos en variables.
    ejecuciones += 1
    seg_tot_mitad += t_mitad
    seg_tot_raiz += t_raiz
    seg_tot_knuth += t_knuth
    seg_tot_sedgewick += t_sedgewick
    seg_tot_hibbard += t_hibbard

    print("%10d              %10.4f                  %10.4f              %10.4f              %10.4f              %10.4f" %(i, t_mitad, t_raiz, t_knuth, t_sedgewick, t_hibbard)) #Mostramos los resultados

#Mostramos los tiempos promedio.
print("\n\nTIEMPOS PROMEDIO:")
print("T. Shell original      T. Shell raíz               T. Shell Knuth               T. Shell Sedgewick               T. Shell Hibbard")
print("  %10.4f           %10.4f                  %10.4f                     %10.4f                       %10.4f" %((seg_tot_mitad/ejecuciones), (seg_tot_raiz/ejecuciones), (seg_tot_knuth/ejecuciones), (seg_tot_sedgewick/ejecuciones), (seg_tot_hibbard/ejecuciones)))

#Conclusión.
print("\nConclusión:")
print("Como se puede comprobar, los tiempos de ejecución para cada tipo de ordenamiento Shell, del más rápido al más lento, son: Shell original, Shell raíz cuadrada, Shell Hibbard, Shell Knuth, Shell Sedgewick.")
print("Con complejidad temporal cada uno:")
print("Shell original = entre O(n) y O(n^2)")
print("Shell raíz = entre O(n) y O(n^2)")
print("Shell Knuth = O(n^(3/2)))")
print("Shell Sedgewick = O(n^(4/3))")
print("Shell Hibbard = O(n^(3/2))")

#FIN.
input("\nPulse ENTER para finalizar.")