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

#Creamos la función.
def junta_y_ordena(lista_mitad_izq, lista_mitad_der):

    #Definimos las variables.
    lista_ordenada = []
    posicion_mitad_izquierda = 0
    posicion_mitad_derecha = 0

    #Recorremos las listas.
    for i in range(len(lista_mitad_izq) + len(lista_mitad_der)):

        if ((posicion_mitad_izquierda < len(lista_mitad_izq)) and (posicion_mitad_derecha < len(lista_mitad_der))): #Si estamos dentro del rango de las dos listas.

            #Comprobamos cual de los 2 elementos de las listas es más pequeño y añadimos este a la lista ordenada.
            if (lista_mitad_izq[posicion_mitad_izquierda] <= lista_mitad_der[posicion_mitad_derecha]): #El de la mitad izquierda es más pequeño.
                lista_ordenada.append(lista_mitad_izq[posicion_mitad_izquierda])
                posicion_mitad_izquierda += 1

            else: #El de la mitad derecha es más pequeño.
                lista_ordenada.append(lista_mitad_der[posicion_mitad_derecha])
                posicion_mitad_derecha += 1

        elif (posicion_mitad_izquierda == len(lista_mitad_izq)): #Si llegamos al final de la mitad izquierda, añadimos los elementos de la mitad derecha.
            lista_ordenada.append(lista_mitad_der[posicion_mitad_derecha])
            posicion_mitad_derecha += 1

        elif (posicion_mitad_derecha == len(lista_mitad_der)): #Si llegamos al final de la mitad derecha, añadimos los elementos de la mitad izquierda.
            lista_ordenada.append(lista_mitad_izq[posicion_mitad_izquierda])
            posicion_mitad_izquierda += 1

    return lista_ordenada #Devolvemos la lista ordenada.

#Creamos la función recursiva.
def ordenacion_mezcla(vector, longitud_inicial, k):

    if (len(vector) <= 1): #Caso base (lista formada por 1 solo elemento).
        return vector

    else:
        mitad = len(vector) // 2 #Obtenemos la posición del elemento situado en la mitad del vector.

        #Llamamos recursivamente a la función para dividir las listas hasta que solo estén formadas por 1 elemento.
        lista_mitad_izq = ordenacion_mezcla(vector[:mitad], longitud_inicial, k)
        lista_mitad_der = ordenacion_mezcla(vector[mitad:], longitud_inicial, k)

        lista_ordenada = junta_y_ordena(lista_mitad_izq, lista_mitad_der) #Llamamos a la función para juntar las listas ordenándolas en una lista nueva.

    #Devolvemos el valor de la posición solicitada.
    if (len(lista_ordenada) == longitud_inicial): #Si la lista ya está ordenada (Longitud de la lista inicial y de la ordenada coinciden).
        return lista_ordenada[k]

    return lista_ordenada #Return recursivo.


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

valor = ordenacion_mezcla(V, len(V), k) #Llamamos a la función para crear un vector adicional ordenado y obtener el valor de la posición indicada en este.
print("Valor solicitado:",valor)


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
print("\nComo se puede observar, el tiempo de ejecución aumenta a medida que el tamaño del vector aumenta,\ncomo la entrada que se repite en 'ordenacion_mezcla' es la mitad de lo que se dio,\nesto hace que el tiempo que se tarda en procesar crezca logarítmicamente hasta n.\nPor lo tanto, orden = O(n*log(n)).")

#FIN.
input("\nPulse ENTER para finalizar.")