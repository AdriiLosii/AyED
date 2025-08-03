"""
Programa: Ej13.py
Propósito:
    Diseña un experimento aleatorio (Benchmark ) para probar la diferencia entre una 
    búsqueda secuencial y una búsqueda binaria, en todas sus variantes, en una lista de 
    200 enteros.
Fecha: 22/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importación de módulos.
import timeit
from random import randint


#Creamos la función para generar la lista aleatoria.
def crea_lista_aleatoria():

    #Definimos las variables.
    lista = []
    tam = 200

    for i in range(tam):
        lista.append(randint(0, tam*4)) #Rellenamos la lista con número aleatorios desde 0 hasta 200*4.

    return lista

#Creamos la función para ordenar la lista.
def ordena(lista):
    return sorted(lista)

#Creamos la función no óptima de búsqueda secuencial.
def secuencial_no_optima(lista_desordenada, numero):

    #Definimos las variables.
    i = 0
    encontrado = False

    while (i < len(lista_desordenada) and not encontrado): #Recorremos la lista hasta que se acabe o hasta que lo encontremos.
        if (lista_desordenada[i] == numero):
            encontrado = True
        else:
            i += 1

    return encontrado

#Creamos la función no óptima de búsqueda binaria.
def binaria_no_optima(lista_desordenada, numero):

    #Definimos las variables.
    lista = ordena(lista_desordenada)
    primero = 0
    ultimo = len(lista)-1
    encontrado = False

    while (primero <= ultimo and not encontrado):
        puntoMedio = (primero + ultimo)//2
        if (lista[puntoMedio] == numero):
            encontrado = True
        else:
            if (numero < lista[puntoMedio]):
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1

    return encontrado

#Creamos la función no óptima de búsqueda binaria recursiva.
def binaria_recursiva_no_optima(lista_desordenada, primero, ultimo, numero):

    #Definimos las variables.
    lista = ordena(lista_desordenada)

    if (primero == ultimo):
        return False
    else:
        puntoMedio = (primero+ultimo)//2

        if (lista[puntoMedio] == numero):
            return True
        else:
            if (numero < lista[puntoMedio]):
                return binaria_recursiva_no_optima(lista, primero, puntoMedio, numero)
            else:
                return binaria_recursiva_no_optima(lista, puntoMedio+1, ultimo, numero)

#Creamos la función óptima de búsqueda secuencial.
def secuencial_optima(lista_ordenada, numero):

    #Definimos las variables.
    i = 0
    encontrado = False
    parar = False

    while (i < len(lista_ordenada) and not encontrado and not parar):
        if (lista_ordenada[i] == numero):
            encontrado = True
        else:
            if (lista_ordenada[i] > numero):
                parar = True
            else:
                i += 1

    return encontrado

#Creamos la función no óptima de búsqueda binaria.
def binaria_optima(lista_ordenada, numero):

    #Definimos las variables.
    primero = 0
    ultimo = len(lista_ordenada)-1
    encontrado = False

    while (primero <= ultimo and not encontrado):
        puntoMedio = (primero + ultimo)//2
        if (lista_ordenada[puntoMedio] == numero):
            encontrado = True
        else:
            if (numero < lista_ordenada[puntoMedio]):
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1

    return encontrado

#Creamos la función no óptima de búsqueda binaria recursiva.
def binaria_recursiva_optima(lista_ordenada, primero, ultimo, numero):

    if (primero == ultimo):
        return False
    else:
        puntoMedio = (primero+ultimo)//2

        if (lista_ordenada[puntoMedio] == numero):
            return True
        else:
            if (numero < lista_ordenada[puntoMedio]):
                return binaria_recursiva_optima(lista_ordenada, primero, puntoMedio, numero)
            else:
                return binaria_recursiva_optima(lista_ordenada, puntoMedio+1, ultimo, numero)


#Programa principal:
#Análisis:

print("\nEn este análisis se tendrán en cuenta 2 cosas para cada búsqueda:")
print("En la búsqueda secuencial, por una parte se observará el comportamiento cuando la lista está desordenada y por otra, el comportamiento de ésta con una lista ordenada.")
print("En el caso de búsqueda binaria, será algo distinto, primero observaremos el comportamiento de ésta con una lista ya ordenada previamente. En la segunda parte, añadiremos al tiempo de búsqueda el tiempo de ordenación de la lista.")
input("\nPulse ENTER para comenzar el análisis.")

#Definimos las variables.
ejecuciones = 0
seg_tot_sec_desordenada = 0 #Tiempo de búsqueda secuencial en una lista desordenada.
seg_tot_bin_y_ordenacion = 0 #Tiempo de búsqueda binaria + tiempo de ordenación de la lista.
seg_tot_bin_recur_y_ordenacion = 0 #Tiempo de búsqueda binaria con algoritmo recursivo + tiempo de ordenación de la lista.
seg_tot_sec_ordenada = 0 #Tiempo de búsqueda secuencial en una lista ordenada previamente.
seg_tot_bin_sin_ordenacion = 0 #Tiempo de búsqueda binaria en una lista ordenada previamente.
seg_tot_bin_recur_sin_ordenacion = 0 #Tiempo de búsqueda binaria en una lista ordenada previamente.

print("\n\t\t\t\t\t\t\t\t\t\t * Análisis: * \n")
print("      Ejecuciones      T. secuencial no óptima      T. binaria no óptima      T. binaria recursiva no óptima      T. secuencial óptima      T. binaria óptima      T. binaria recursiva óptima")

for i in range(100, 10000 + 1, 100): #Llamaremos a las funciones i veces en cada recorrido.

    lista_no_ordenada = crea_lista_aleatoria()
    lista_ordenada = ordena(lista_no_ordenada)
    num_aleatorio = randint(0, 200*4) #Número aleatorio a buscar entre 0 y 200*4.

    #Number = i -> Veces que se ejecuta la función.
    #Casos no óptimos (listas no ordenadas).
    t_sec_no_opt = timeit.Timer("secuencial_no_optima(lista_no_ordenada, num_aleatorio)", "from __main__ import secuencial_no_optima, lista_no_ordenada, num_aleatorio").timeit(number=i)
    t_bin_no_opt = timeit.Timer("binaria_no_optima(lista_no_ordenada, num_aleatorio)", "from __main__ import binaria_no_optima, lista_no_ordenada, num_aleatorio").timeit(number=i)
    t_bin_rec_no_opt = timeit.Timer("binaria_recursiva_no_optima(lista_no_ordenada, 0, len(lista_no_ordenada)-1, num_aleatorio)", "from __main__ import binaria_recursiva_no_optima, lista_no_ordenada, num_aleatorio").timeit(number=i)

    #Casos óptimos (listas ordenadas).
    t_sec_opt = timeit.Timer("secuencial_optima(lista_ordenada, num_aleatorio)", "from __main__ import secuencial_optima, lista_ordenada, num_aleatorio").timeit(number=i)
    t_bin_opt = timeit.Timer("binaria_optima(lista_ordenada, num_aleatorio)", "from __main__ import binaria_optima, lista_ordenada, num_aleatorio").timeit(number=i)
    t_bin_rec_opt = timeit.Timer("binaria_recursiva_optima(lista_ordenada, 0, len(lista_ordenada)-1, num_aleatorio)", "from __main__ import binaria_recursiva_optima, lista_ordenada, num_aleatorio").timeit(number=i)

    #Guardamos los datos en variables.
    ejecuciones += 1
    seg_tot_sec_desordenada += t_sec_no_opt
    seg_tot_bin_y_ordenacion += t_bin_no_opt
    seg_tot_bin_recur_y_ordenacion += t_bin_rec_no_opt
    seg_tot_sec_ordenada += t_sec_opt
    seg_tot_bin_sin_ordenacion += t_bin_opt
    seg_tot_bin_recur_sin_ordenacion += t_bin_rec_opt

    print("   %10d              %10.4f                  %10.4f                     %10.4f                      %10.4f              %10.4f                 %10.4f" %(i, t_sec_no_opt, t_bin_no_opt, t_bin_rec_no_opt, t_sec_opt, t_bin_opt, t_bin_rec_opt)) #Mostramos los resultados

#Mostramos los tiempos promedio.
print("\n\nTIEMPOS PROMEDIO:")
print("T. secuencial no óptima      T. binaria no óptima      T. binaria recursiva no óptima      T. secuencial óptima      T. binaria óptima      T. binaria recursiva óptima")
print("     %10.4f                  %10.4f                    %10.4f                     %10.4f               %10.4f                  %10.4f" %((seg_tot_sec_desordenada / ejecuciones), (seg_tot_bin_y_ordenacion / ejecuciones), (seg_tot_bin_recur_y_ordenacion / ejecuciones), (seg_tot_sec_ordenada / ejecuciones), (seg_tot_bin_sin_ordenacion / ejecuciones), (seg_tot_bin_recur_sin_ordenacion / ejecuciones)))

#Conclusión.
print("\nObservando los tiempos de ejecución anteriores se pueden sacar las siguiente conclusiones:")
print("En las pruebas no óptimas, en donde la lista no estaba ordenada (búsqueda secuencial) o había que ordenarla previamente (búsqueda binaria),")
print("se ven unos tiempos de ejecución mayores con respecto a los de los casos óptimos, en donde las listas ya estaban ordenadas, debido a que,")
print("en el caso del ordenamiento secuencial, si el número a buscar no se encuentra en la lista, este lo recorrerá de todas formas,")
print("y en el caso de la búsqueda binaria, puede que compense usar este método o no, ya que al necesitar ordenación previa, en listas grandes, esto retrasará la ejecución.")
print("En cuanto a los distintos algorítmos de búsqueda, se puede observar que el más rápido es el binario no recursivo, después el binario recursivo y por último el secuencial.")

#FIN.
input("\nPulse ENTER para finalizar.")