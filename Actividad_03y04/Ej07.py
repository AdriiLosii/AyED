"""
Programa: Ej07.py
Propósito:
    Dado un vector V de longitud n, aplicando el esquema de diseño Divide y vencerás
    y sin modificar V, escribir una función que devuelva el valor que ocuparía la 
    posición k (p.e. posición de la mediana) si el vector V estuviera ordenado. Calcular 
    su complejidad temporal en función de n y expresarla en notación asintótica.
Fecha: 02/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos los módulos.
from random import randint


#Creamos la función recursiva que utiliza el esquema de divide y vencerás-
def ordenacion_mezcla(lista, longitud_inicial, k):

    if (len(lista) > 1): #Si no es caso base.
        mitad = len(lista)//2
        mitad_izq = lista[:mitad]
        mitad_der = lista[mitad:]

        #Llamamos recursivamente a la función hasta llegar a los casos base (divide y vencerás).
        ordenacion_mezcla(mitad_izq,  longitud_inicial, k)
        ordenacion_mezcla(mitad_der,  longitud_inicial, k)

        i = 0 #Contador para la mitad izquierda.
        j = 0 #Contador para la mitad derecha.
        k = 0 #Contador para la lista final.

        #Fusionamos las listas:
        while (i < len(mitad_izq) and j < len(mitad_der)):
            if (mitad_izq[i] < mitad_der[j]):
                lista[k] = mitad_izq[i]
                i += 1
            else:
                lista[k] = mitad_der[j]
                j += 1

            k += 1

        #Mezclamos los valores restantes.
        while (i < len(mitad_izq)):
            lista[k] = mitad_izq[i]
            i += 1
            k += 1

        while (j < len(mitad_der)):
            lista[k] = mitad_der[j]
            j += 1
            k += 1

    return lista #Return recursivo.

#Creamos la función para obtener el valor k si la lista estuviera ordenada.
def obten_valor(lista, V):

    #Llamamos a la función para ordenar la lista.
    lista_ord = ordenacion_mezcla(lista, len(lista), k)

    return lista_ord[k] #Return del valor de la posición solicitada.


#Programa principal.
#Definimos las variables.
V = []

#Creamos un vector de 20 elementos aleatorios y lo mostramos.
for i in range(20):
    V.append(randint(0, 100))

print("Vector:",V)

#Petición de datos validada.
try:
    k = int(input("\nIntroduce la posición k del valor que quieres conocer: "))

    if ((k < 0) or (k > (len(V) - 1))): #Valores fuera del rango del vector.
        raise ValueError

except ValueError:
    print("\nError, ha ocurrido algo inesperado.")
    input("Pulse ENTER para finalizar.")
    quit() #Salimos del programa

valor = obten_valor(V.copy(), k) #Llamamos a la función para crear un vector adicional ordenado y obtener el valor de la posición indicada en este.
print("\nValor de la posición",k,"si la lista estuviera ordenada:",valor)
print("(El vector sigue estando desordenada):",V)



######################## Análisis: ########################

input("\nPulse ENTER para comenzar el análisis.")

import timeit

#Creamos la función.
def crear_vector_aleatorio(i):
    vector = []

    for n in range(i):
        vector.append(randint(0, i))

    return vector


#Definimos las variables.
ejecuciones = 0
seg_total = 0

print("\n\t\t * Análisis: * \n")
print("    Tamaño vector       Tiempo")

for i in range(1000, 100000 + 1, 1000):

    vector_analisis = crear_vector_aleatorio(i) #Creamos el vector con números aleatorios de tamaño i.

    t = timeit.Timer("ordenacion_mezcla(vector_analisis, len(vector_analisis), 0)", "from __main__ import ordenacion_mezcla, vector_analisis").timeit(number=1) #Guardamos el tiempo en una variable
    ejecuciones += 1
    seg_total += t

    print("  %10d        %10.6f" % (i, t)) #Mostramos el resultado.

#Mostramos el tiempo promedio.
print("\nTiempo promedio: %1.6f"%(seg_total/ejecuciones))

#Conclusión.
print("\nConclusión:")
print("Como se puede observar, el tiempo de ejecución aumenta a medida que el tamaño del vector aumenta.")
print("En la función debemos considerar los dos procesos distintos que conforman su implementación:")
print("En primer lugar, la lista se divide en mitades, con una complejidad temporal logn, en donde n es igual al tamaño de la lista.")
print("En segundo lugar, cada ítem de la lista se procesará y se colocará en su lugar correspondiente, con una complejidad temporal n.")
print("El resultado de este análisis es de una complejidad temporal O(nlogn).")

#FIN.
input("\nPulse ENTER para finalizar.")