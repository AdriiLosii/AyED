"""
Programa: Ej19.py
Propósito:
    Utilizando un generador de números aleatorios, crea una lista de 500 enteros. Realiza
    una prueba de referencia usando al menos 3 de los algoritmos de ordenamiento de los
    apuntes. ¿Cuál es la diferencia en la velocidad de ejecución? ¿Cuáles son tus
    conclusiones?
Fecha: 23/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importación de módulos.
from random import randint
import timeit


#Creamos la función.
def crea_lista_aleatoria():

    #Definimos las variables.
    lista = []

    for i in range(500):
        lista.append(randint(0, 500*4))

    return lista

#Creamos la función.
def ordenamiento_seleccion(lista):

    for i in range(len(lista)-1, 0, -1): #Num. recorridos -> Vamos reduciendo el número de comparaciones a medida que ordenamos los valores mayores.
        pos_mayor = 0

        for j in range(1, i+1):
            if (lista[pos_mayor] < lista[j]): #Si el valor de la posición actual es mayor que nuestro valor guardado.
                pos_mayor = j

        lista[pos_mayor], lista[i] = lista[i], lista[pos_mayor] #Intercambiamos los valores, ordenando así el valor más grande lo más a la derecha posible.

    return lista

#Creamos la función.
def ordenamiento_insercion(lista):

    for i in range(1, len(lista)): #Recorremos la lista de izquierda a derecha, saltándonos el primer elemento (sublista ordenada).
        actual = lista[i] #Guardamos el valor de la posición actual.

        #Retrocedemos en la lista hasta encontrar la posición correcta del valor actual.
        while (i > 0 and lista[i-1] > actual):
            lista[i] = lista[i-1]
            i = i-1

        lista[i] = actual #Posicionamos el valor en su lugar correspondiente.
    
    return lista

#Creamos la función.
def ordenamiento_mezcla(lista):

    if (len(lista) > 1): #Si no es caso base.
        mitad = len(lista)//2
        mitad_izq = lista[:mitad]
        mitad_der = lista[mitad:]

        #Llamamos recursivamente a la función hasta llegar a los casos base.
        ordenamiento_mezcla(mitad_izq)
        ordenamiento_mezcla(mitad_der)

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

    return lista


#Programa principal.
#Análisis:

print("\nEn este análisis compararemos los tiempos de ejecución de: ordenamiento por selección, ordenamiento por inserción y ordenamiento por mezcla en una lista de 500 enteros.")
print("Observaremos como aumentan los tiempos de ejecución a medida que se aumenta el número de llamadas a la función.")
input("\nPulse ENTER para comenzar el análisis.")

#Definimos las variables.
ejecuciones = 0
seg_tot_selec = 0
seg_tot_inserc = 0
seg_tot_mezcla = 0

print("\n\t\t\t\t\t * Benchmark: * \n")
print("    N. Ejecuciones       T. ord. selección           T. ord. inserción                T. ord. mezcla")

for i in range(50, 600 + 1, 50): #Llamaremos a las funciones i veces en cada recorrido.

    lista_no_ordenada = crea_lista_aleatoria()

    #Number = i -> Veces que se ejecuta la función.
    t_selec = timeit.Timer("ordenamiento_seleccion(lista_no_ordenada.copy())", "from __main__ import ordenamiento_seleccion, lista_no_ordenada").timeit(number=i)
    t_inserc = timeit.Timer("ordenamiento_insercion(lista_no_ordenada.copy())", "from __main__ import ordenamiento_insercion, lista_no_ordenada").timeit(number=i)
    t_mezcla = timeit.Timer("ordenamiento_mezcla(lista_no_ordenada.copy())", "from __main__ import ordenamiento_mezcla, lista_no_ordenada").timeit(number=i)
    
    #Guardamos los datos en variables.
    ejecuciones += 1
    seg_tot_selec += t_selec
    seg_tot_inserc += t_inserc
    seg_tot_mezcla += t_mezcla

    print("   %10d              %10.4f                  %10.4f                     %10.4f" %(i,t_selec , t_inserc, t_mezcla)) #Mostramos los resultados

#Mostramos los tiempos promedio.
print("\n\nTIEMPOS PROMEDIO:")
print("T. Seleccion      T.  Insercion      T. Mezcla     ")
print("     %10.4f                  %10.4f                    %10.4f" %((seg_tot_selec / ejecuciones), (seg_tot_inserc / ejecuciones), (seg_tot_mezcla / ejecuciones)))

#Conclusión.
print("\nConclusión:")
print("Observando los tiempos de ejecución obtenidos, podemos concluir que el ordenamiento por mezcla es el más rápido de los tres,")
print("debido a que se trata de un algoritmo de orden O(nlogn), pero requiere espacio en memoria adicional para el proceso de mezcla,")
print("mientras que los otros 2 algoritmos trabajan con una complejidad temporal de O(n^2).")

#FIN.
input("\nPulse ENTER para finalizar.")