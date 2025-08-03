"""
Programa: Ej06.py
Propósito:
    Escribir un algoritmo que obtenga de manera recursiva el valor máximo del tramo 
    [izq; der] de un vector V. Expresar el coste temporal del algoritmo.
Fecha: 01/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos los módulos.
from random import randint

#Creamos la función.
def parte_y_ordena(vector, izq, der):
    pivote = vector[(izq + der) // 2] #Usamos de pivote el valor situado en la mitad del tramo.
    #Restamos uno a la posición izq para compensar la suma posteriormente y no saltarnos ningún elemento, (lo mismo pasa con la posición der pero sumando).
    i = izq - 1
    j = der + 1

    while True:

        i += 1
        while (vector[i] < pivote): #Obtenemos la posición del último valor (de izquierda a derecha) menor que el pivote.
            i += 1

        j -= 1
        while (vector[j] > pivote): #Obtenemos la posición del primer valor (de izquierda a derecha) mayor que el pivote.
            j -= 1

        if (i >= j): #Cuando la posición i y la j se topan, finaliza el bucle.
            return j #Devolvemos la posición de la partición.

        #Como la posición i va a estar situado en un valor menor al pivote y la posición j en uno mayor,
        #intercambiamos las posiciones de los valores, dejando los valores menores al pivote a al izquierda
        #y los mayores a la derecha.
        vector[i], vector[j] = vector[j], vector[i]


#Creamos la función recursiva.
def QuickSort(vector, izq, der):
    if (izq < der): #Comprobamos que la posición del limite izquierdo sea menor que la del derecho.
        posicion_particion = parte_y_ordena(vector, izq, der) #Guardamos la posición de donde se hizo la partición, ya que nos servirá para delimitar el final de la mitad izquierda y el principio de la derecha.

        #Llamamos recursivamente a la función.
        QuickSort(vector, izq, posicion_particion) #Mitad izquierda.
        QuickSort(vector, posicion_particion + 1, der) #Mitad derecha.


#Programa principal.
#Definimos las variables.
V = []

#Rellenamos el vector con 20 números    aleatorios (desde 0 hasta 100).
while(len(V) < 20):
    num_aleatorio = randint(0, 100)
    if (num_aleatorio not in V): #Evitamos números repetidos.
        V.append(num_aleatorio)

print("V inicial:",V) #Mostramos el vector.

#Petición y validación de datos.
try:
    izq = int(input("\nIntroduce el número que limita al tramo por la izquierda: "))
    der = int(input("Introduce el número que limita al tramo por la derecha: "))

    if (V.index(izq) >= V.index(der)): #Evitamos que la posición del límite izquierdo del tramo sea mayor o igual que la del derecho.
        raise ValueError

    aux = V.index(der) #Creamos una variable auxiliar para guardar la posición del límite derecho (ya que posteriormente esta posición la ocupará el valor máximo del tramo).
    QuickSort(V, V.index(izq), V.index(der)) #LLamamos a la función recursiva para ordenar el tramo indicado.

    #Mostramos los resultados.
    print("\nV con tramo ordenado:",V)
    print("Valor máximo del tramo:",V[aux])

except ValueError:
    print("\nError, ha ocurrido algo inesperado.")
    input("Pulse ENTER para finalizar.")
    quit() #Salimos del programa.


######################## Análisis: ########################

input("\nPulse ENTER para comenzar el análisis.")

import timeit

#Creamos la función.
def crear_vector_aleatorio(i):
    vector = []

    for n in range(i):
        num_aleatorio = randint(0, i)
        if (num_aleatorio not in vector): #Evitamos números repetidos.
            vector.append(num_aleatorio)

    return vector


#Definimos las variables.
ejecuciones = 0
seg_total = 0

print("\n\t\t * Análisis: * \n")
print("INFORMACIÓN: El tamaño del tramo será aproximadamente el mismo que la longitud del vector (apróximadamente: ya que se pueden repetir números, los cuales no se añadirán al vector).")
print("    Tamaño tramo       Tiempo")

for i in range(1000, 50000 + 1, 1000):

    vector_analisis = crear_vector_aleatorio(i) #Creamos el vector con números aleatorios de tamaño i.
    t = timeit.Timer("QuickSort(vector_analisis, vector_analisis.index(vector_analisis[0]), vector_analisis.index(vector_analisis[-1]))", "from __main__ import QuickSort, parte_y_ordena, vector_analisis, i").timeit(number=1) #Guardamos el tiempo en una variable
    ejecuciones += 1
    seg_total += t

    print("  %10d        %10.6f" % (i, t)) #Mostramos el resultado.

#Mostramos el tiempo promedio.
print("\nTiempo promedio: %1.6f"%(seg_total/ejecuciones))

#Conclusión.
print("\nComo se puede observar, el tiempo de ejecución aumenta a medida que el tamaño del tramo aumenta,\nesto se debe a que es un algoritmo de orden = O(n) en los casos promedio,\nen los peores casos (cuando se escoje el número más grande o más pequeño como pivote)\nel tiempo de ejecución es de O(n²) ya que se estarían creando particiones del vector de tamaño n-1.")

#FIN.
input("\nPulse ENTER para finalizar.")