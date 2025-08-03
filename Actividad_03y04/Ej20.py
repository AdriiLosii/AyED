"""
Programa: Ej20.py
Propósito:
    Un ordenamiento burbuja puede modificarse para que “burbujee” en ambas
    direcciones. La primera pasada mueve la lista hacia “arriba”, y la segunda pasada la
    mueve hacia “abajo”. Este patrón alternante continúa hasta que no son necesarias
    más pasadas. Implementa esta variación y describe en qué circunstancias podría ser
    apropiada.
Fecha: 23/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importación de módulos.
from random import randint


#Creamos la función.
def crea_lista_aleatoria(tamaño):

    #Definimos las variables.
    lista = []

    for i in range(tamaño):
        lista.append(randint(0, tamaño*4))

    return lista

#Creamos la función.
def bubblesort_bidireccional(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy()
    incompleto = True #True inicial para entrar al bucle.
    direccion = 1
    actual = 0
    inicio = 0
    fin = len(lista_ordenada) - 2 #Le restamos 2: -1 porque las listas empiezan en 0, -1 porque trabajamos con actual y siguiente (actual + 1). De esta forma evitamos salirnos del index de la lista.

    #Mientras no esté ordenada.
    while (incompleto == True):
        incompleto = False

        while (actual < fin and direccion == 1) or (actual > inicio and direccion == -1): #Mientras no se llegue al final (tanto hacia la izquierda como hacia la derecha).            
            if (lista_ordenada[actual] > lista_ordenada[actual + 1]): #Si el valor actual es más grande que el siguiente.
                lista_ordenada[actual], lista_ordenada[actual + 1] = lista_ordenada[actual + 1], lista_ordenada[actual] #Intercambiamos los valores.
                print(lista_ordenada)
                incompleto = True #Mientras esta condición se cumpla significa que el vector aún no está ordenado.

            actual = actual + direccion #Avanzamos/Retrocedemos la posición.

        if direccion == 1: #Si estamos recorriendo la lista hacia la derecha, recortamos la longitud de la lista en 1 por la derecha.
            fin = fin - 1
        else: #Si estamos recorriendo la lista hacia la izquierda, recortamos la longitud de la lista en 1 por la izquierda.
            inicio = inicio + 1

        direccion = -direccion #Cambiamos la dirección en la que recorremos la lista.

    return lista_ordenada



#Lectura de datos validada.
try:
    #Petición de datos.
    tamaño = int(input("\nIntroduzca el tamaño de la lista aleatoria: "))

    if (tamaño <= 0):
        raise ValueError()

except ValueError: #Si hay algún problema, el programa realiza las siguientes acciones.
    print("\nError, ha ocurrido algo inesperado.")
    input("Pulse ENTER para finalizar.")
    quit() #Salimos del programa


#Llamamos a las funciones y mostramos las listas.
lista_desordenada = crea_lista_aleatoria(tamaño)
print("\nLista desordenada:", lista_desordenada)
print("Proceso:")
lista_ordenada = bubblesort_bidireccional(lista_desordenada)
print("Lista ordenada:", lista_ordenada)

#Conclusión.
print("\nEste método puede ser útil en una lista semiordenada, ya que la complejidad temporal de este algoritmo es bastante elevada (O(n²)),")
print("y por lo tanto, cuantas más comparaciones tenga que realizar, más lento será.")

#FIN.
input("\nPulse ENTER para finalizar.")