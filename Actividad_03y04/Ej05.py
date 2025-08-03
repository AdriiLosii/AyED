"""
Programa: Ej05.py
Propósito: 
    Supón que eres un científico de la computación/ladrón de arte que se ha colado en
    una galería de arte importante. Dispones sólo de una mochila para sacar las obras de
    arte robadas, que sólo puede contener W “kilos de arte”; no obstante, para cada pieza
    de arte conoces su valor y su peso. Escribe una función de programación dinámica
    para maximizar tus ganancias, con distintas capacidades de la mochila y distintos
    valores/pesos de los ítems.
Fecha: 04/04/2022
Autores: Gabriel Iglesias Sotelo y Adrián Losada Álvarez 
"""


#Creamos la función para obtener el máximo beneficio.
def mochila(peso, valores, W):
    n = len(peso)
    ant = [0 for m in range(W+1)]  #Anterior
    act = [0 for m in range(W+1)]  #Actual

    d = [[0 for m in range(W+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for m in range(1, W+1) :
            if (peso[i-1] <= m and valores[i-1] + ant[m-peso[i-1]] > ant[m]):
                act[m] = valores[i-1] + ant[m-peso[i-1]]
                d[i][m] = 1
            else:
                act[m] = ant[m]
                d[i][m] = 0

        ant = act[:]

    lista_cuadros = []
    m = W
    for i in range(n,0,-1):

        lista_cuadros.insert(0,d[i][m])
        if (d[i][m] == 1):
            m = m-peso[i-1]

    return lista_cuadros, act[W]

#Creamos la función para solicitar el número de objetos/cuadros.
def num_cuadros():
    cuadro = int(input("Dime cuantos objetos hay en la galería de arte: "))
    if (cuadro <= 0):
        raise ValueError()
    else:
        return cuadro

#Creamos la función para rellenar la columna de los valores de los cuadros.
def introducir_valor(num):

    valores = []

    for i in range (0,num):

        valor = int(input("Dame el valor de tu objeto numero {0}:  ".format(i+1)))   #Pedimos el valor de cada objeto
        if (valor <= 0):
            raise ValueError

        valores.append(valor)

    return valores

#Creamos la función para rellenar la columna de los pesos de los cuadros.
def introducir_peso(num):

    pesos = []

    for i in range (0,num):

        peso = int(input("Dame el peso de tu objeto numero {0}:  ".format(i+1)))  #Pedimos el peso de cada objeto
        if (peso <= 0):
            raise ValueError

        pesos.append(peso)

    return pesos

#Creamos la función para solicitar la capacidad de la mochila.
def solicitar_peso():
    capacidad = int(input("\n¿Cuál será la capacidad de la mochila?\n"))
    if (capacidad <= 0):
        raise ValueError()
    else:
        return capacidad


#Programa principal.
try: #Lectura validada.

    num = num_cuadros() #Llamamos a la función para solicitar el número de cuadros a robar.
    valores = introducir_valor(num) #Llamamos a la función para rellenar la columna de los valores
    pesos = introducir_peso(num)
    W = solicitar_peso() #Llamamos a la función para solicitar la capacidad de la mochila (kilos).
    lista_cuadros, max_beneficio = mochila(pesos, valores, W) #Llamamos a la función para calcular el máximo beneficio.

    #Mostramos los resultados.
    print("\nMaximo beneficio:", max_beneficio)
    print("Lista de escogidos:", lista_cuadros)

    #FIN.
    input("\nPulse ENTER para finalizar.")

except ValueError:  
    print("\nError, ha ocurrido algo inesperado.")   #Notificamos error en la lectura de datos
    input("Pulse ENTER para finalizar.")
    quit() #Salimos del programa