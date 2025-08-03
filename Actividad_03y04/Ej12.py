"""
Programa: Ej12.py
Propósito:
    Genera una pequeña lista aleatoria de números enteros. Muestra paso a paso cómo es 
    ordenada dicha lista por los siguientes algoritmos:
        ordenamiento burbuja, en todas sus variantes
        ordenamiento por selección
        ordenamiento por inserción
        ordenamiento de Shell (con distintos valores de los incrementos)
        ordenamiento por mezcla
        ordenamiento rápido (decide sobre el valor pivote)
Fecha: 21/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importación de módulos.
from random import randint
from math import sqrt


#Creamos la función.
def crea_lista_aleatoria():

    try:
        tam = int(input("\nIntroduzca el tamaño de la lista: "))

    except ValueError: #Si se introducen datos erróneos.
        print("\nError, ha ocurrido algo inesperado.")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

    lista = []

    for i in range(tam):
        lista.append(randint(0, 100))

    return lista

#Creamos la función.
def ordenamiento_burbuja(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy() #Usamos .copy() para que la lista original no se modifique.
    print(lista_ordenada) #Mostramos la lista inicialmente.

    for i in range(len(lista_ordenada)): #Recorremos la lista tantas veces como elementos tenga.
        for j in range(0, len(lista_ordenada)-i-1): #Recorremos la lista de izquierda a derecha pero restandole 1 al tamaño después de cada recorrido.
            if (lista_ordenada[j] > lista_ordenada[j+1]): #Si el primer elemento de la pareja es mayor que el segundo.
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j] #Intercambiamos los valores.
                print(lista_ordenada) #Mostramos la lista a medida que se ordena.

    return lista_ordenada

#Creamos la función.
def ordenamiento_burbuja_bidireccional(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy() #Usamos .copy() para que la lista original no se modifique.
    incompleto = True #True inicial para entrar al bucle.
    direccion = 1
    actual = 0
    inicio = 0
    fin = len(lista_ordenada) - 2 #Le restamos 2: -1 porque las listas empiezan en 0, -1 porque trabajamos con actual y siguiente (actual + 1). De esta forma evitamos salirnos del index de la lista.
    print(lista_ordenada) #Mostramos la lista inicialmente.

    #Mientras no esté ordenada.
    while (incompleto == True):
        incompleto = False

        while (actual < fin and direccion == 1) or (actual > inicio and direccion == -1): #Mientras no se llegue al final (tanto hacia la izquierda como hacia la derecha).            
            if (lista_ordenada[actual] > lista_ordenada[actual + 1]): #Si el valor actual es más grande que el siguiente.
                lista_ordenada[actual], lista_ordenada[actual + 1] = lista_ordenada[actual + 1], lista_ordenada[actual] #Intercambiamos los valores.
                incompleto = True #Mientras esta condición se cumpla significa que el vector aún no está ordenado.
                print(lista_ordenada) #Mostramos la lista a medida que se ordena.

            actual = actual + direccion #Avanzamos/Retrocedemos la posición.

        if direccion == 1: #Si estamos recorriendo la lista hacia la derecha, recortamos la longitud de la lista en 1 por la derecha.
            fin = fin - 1

        else: #Si estamos recorriendo la lista hacia la izquierda, recortamos la longitud de la lista en 1 por la izquierda.
            inicio = inicio + 1

        direccion = -direccion #Cambiamos la dirección en la que recorremos la lista.

    return lista_ordenada

#Creamos la función.
def ordenamiento_seleccion(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy() #Usamos .copy() para que la lista original no se modifique.
    print(lista_ordenada) #Mostramos la lista inicialmente.

    for i in range(len(lista_ordenada)-1, 0, -1): #Num. recorridos -> Vamos reduciendo el número de comparaciones a medida que ordenamos los valores mayores.
        pos_mayor = 0

        for j in range(1, i+1):
            if (lista_ordenada[pos_mayor] < lista_ordenada[j]): #Si el valor de la posición actual es mayor que nuestro valor guardado.
                pos_mayor = j

        lista_ordenada[pos_mayor], lista_ordenada[i] = lista_ordenada[i], lista_ordenada[pos_mayor] #Intercambiamos los valores, ordenando así el valor más grande lo más a la derecha posible.
        print(lista_ordenada) #Mostramos la lista a medida que se ordena.

    return lista_ordenada

#Creamos la función.
def ordenamiento_insercion(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy() #Usamos .copy() para que la lista original no se modifique.
    print(lista_ordenada) #Mostramos la lista inicialmente.

    for i in range(1, len(lista_ordenada)): #Recorremos la lista de izquierda a derecha, saltándonos el primer elemento (sublista ordenada).
        actual = lista_ordenada[i] #Guardamos el valor de la posición actual.

        #Retrocedemos en la lista hasta encontrar la posición correcta del valor actual.
        while (i > 0 and lista_ordenada[i-1] > actual):
            lista_ordenada[i] = lista_ordenada[i-1]
            i = i-1

        lista_ordenada[i] = actual #Posicionamos el valor en su lugar correspondiente.
        print(lista_ordenada) #Mostramos la lista a medida que se ordena.
    
    return lista_ordenada

#Creamos la función.
def ordenamiento_shell_mitad(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy() #Usamos .copy() para que la lista original no se modifique.
    sublistas = len(lista_ordenada)//2 #Número de sublistas = Valor del incremento.
    print(lista_ordenada) #Mostramos la lista inicialmente.

    while (sublistas != 0):
        for i in range(sublistas):
            insercion_sublista_mitad(lista_ordenada, i, sublistas) #Llamamos a la función para ordenar las sublistas mediante inserción.

        #Mostramos el valor de los incrementos y la lista a medida que se ordena.
        print("Valor de los incrementos:",sublistas)
        print(lista_ordenada)

        sublistas = sublistas//2 #Reducimos el número de sublistas a la mitad después de cada recorrido.
    
    return lista_ordenada

#Creamos la función auxiliar al ordenamiento shell.
def insercion_sublista_mitad(lista_ordenada, inicio, incremento):

    for i in range(inicio+incremento, len(lista_ordenada), incremento): #Recorremos los valores de la sublista.
        actual = lista_ordenada[i] #Guardamos el valor de la posición actual.

        while (i >= incremento and lista_ordenada[i-incremento] > actual): #Si el valor anterior (antes del incremento) al actual es mayor que el actual.
            lista_ordenada[i] = lista_ordenada[i-incremento] #Colocamos el valor mayor en su posición.
            i = i-incremento #Obtenemos la posición del valor intercambiado (mayor).
            lista_ordenada[i] = actual #Colocamos el valor guardado previamente (menor) en la posición del intercambiado (mayor).

#Creamos la función.
def ordenamiento_shell_raiz(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy() #Usamos .copy() para que la lista original no se modifique.
    sublistas = int(sqrt(len(lista_desordenada))) #Número de sublistas = Valor del incremento.
    print(lista_ordenada) #Mostramos la lista inicialmente.

    while (sublistas != 1):
        for i in range(sublistas):
            insercion_sublista_raiz(lista_ordenada, i, sublistas)

        sublistas = int(sqrt(sublistas)) #Reducimos el valor del incremento.

        #Mostramos el valor de los incrementos y la lista a medida que se ordena.
        print("Valor de los incrementos:",sublistas)
        print(lista_ordenada)

    insercion_sublista_raiz(lista_ordenada, 0, sublistas) #Llamamos a la función una última vez para realizar la inserción con incremento = 1.

    return lista_ordenada

#Creamos la función auxiliar para el ordenamiento Shell.
def insercion_sublista_raiz(lista_ordenada, inicio, incremento):

    for i in range(inicio, len(lista_ordenada), incremento): #Recorremos los valores de la sublista.
        actual = lista_ordenada[i] #Guardamos el valor de la posición actual.

        #Retrocedemos en la lista hasta encontrar la posición correcta del valor.
        while (i >= incremento and lista_ordenada[i-incremento] > actual):
            lista_ordenada[i] = lista_ordenada[i-incremento]
            i = i-incremento
            lista_ordenada[i] = actual #Colocamos el valor guardado previamente (menor) en la posición del intercambiado (mayor).

#Creamos la función.
def ordenamiento_shell_knuth(lista_desordenada):

    #Definimos las variables.
    lista_ordenada = lista_desordenada.copy()
    secuencia_knuth = []
    h = 1
    print(lista_ordenada) #Mostramos la lista inicialmente.

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
    
        #Mostramos el valor de los incrementos y la lista a medida que se ordena.
        print("Valor de los incrementos:",incremento)
        print(lista_ordenada)

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
    print(lista_ordenada) #Mostramos la lista inicialmente.

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

        #Mostramos el valor de los incrementos y la lista a medida que se ordena.
        print("Valor de los incrementos:",incremento)
        print(lista_ordenada)

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
    print(lista_ordenada) #Mostramos la lista inicialmente.

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

        #Mostramos el valor de los incrementos y la lista a medida que se ordena.
        print("Valor de los incrementos:",incremento)
        print(lista_ordenada)

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

#Creamos la función.
def ordenamiento_mezcla(lista_ordenada):

    print("Dividir:", lista_ordenada) #Mostramos la lista a dividir.

    if (len(lista_ordenada) > 1): #Si no es caso base.
        mitad = len(lista_ordenada)//2
        mitad_izq = lista_ordenada[:mitad]
        mitad_der = lista_ordenada[mitad:]

        #Llamamos recursivamente a la función hasta llegar a los casos base.
        ordenamiento_mezcla(mitad_izq)
        ordenamiento_mezcla(mitad_der)

        i = 0 #Contador para la mitad izquierda.
        j = 0 #Contador para la mitad derecha.
        k = 0 #Contador para la lista final.

        #Fusionamos las listas:
        while (i < len(mitad_izq) and j < len(mitad_der)):
            if (mitad_izq[i] < mitad_der[j]):
                lista_ordenada[k] = mitad_izq[i]
                i += 1
            else:
                lista_ordenada[k] = mitad_der[j]
                j += 1

            k += 1

        #Mezclamos los valores restantes.
        while (i < len(mitad_izq)):
            lista_ordenada[k] = mitad_izq[i]
            i += 1
            k += 1

        while (j < len(mitad_der)):
            lista_ordenada[k] = mitad_der[j]
            j += 1
            k += 1

    print("Mezclar:", lista_ordenada) #Mostramos la lista a mezclar.

    return lista_ordenada

#Creamos la función.
def ordenamiento_rapido_primero(lista_ordenada, primero, ultimo):

    if (primero < ultimo):
        pos_particion = particion(lista_ordenada, primero, ultimo) #Llamamos a la función para ordenar la lista y obtener la posición de la partición.
        print(lista_ordenada) #Mostramos la lista a medida que se ordena.

        #Llamadas recursivas a la función.
        ordenamiento_rapido_primero(lista_ordenada, primero, pos_particion-1) #Quick Sort de parte izquierda.
        ordenamiento_rapido_primero(lista_ordenada, pos_particion+1, ultimo) #Quick Sort de parte derecha.

    return lista_ordenada

#Creamos la función auxiliar al ordenamiento rápido con pivote = primer elemento.
def particion(lista_ordenada, primero, ultimo):

    #Definimos las variables.
    pivote = lista_ordenada[primero]
    marcaIzq = primero + 1 #Sumamos 1 ya el pivote está en la posición 0.
    marcaDer = ultimo
    print("\nPivote:",pivote) #Mostramos el valor del pivote.

    #Mientra que no se crucen las marcas.
    while (marcaIzq <= marcaDer):
        while (marcaIzq <= marcaDer and lista_ordenada[marcaIzq] <= pivote): #Mientras que la marca izq no supere a al derecha y el valor del elemento de la marca izq sea menor o igual que el valor del pivote.
            marcaIzq = marcaIzq + 1 #Avanzamos con la marca izq.

        while (marcaDer >= marcaIzq and lista_ordenada[marcaDer] >= pivote): #Mientras que la marca derecha sea mayor o igual a la izquierda y el valor del elemento de la marca der sea mayor o igual que el valor del pivote.
            marcaDer = marcaDer - 1 #Avanzamos (retrocedemos) con la marca der.

        if (marcaIzq <= marcaDer): #Si las marcas no se han cruzado.
            lista_ordenada[marcaIzq], lista_ordenada[marcaDer] = lista_ordenada[marcaDer], lista_ordenada[marcaIzq] #Intercambiamos los valores encontrados.

    lista_ordenada[primero], lista_ordenada[marcaDer] = lista_ordenada[marcaDer], lista_ordenada[primero] #Colocamos el valor del pivote en su posición.

    return marcaDer #Devolvemos la posición de la partición / posición del pivote.

#Creamos la función.
def ordenamiento_rapido_aleatorio(lista_ordenada, primero, ultimo):

    #Definimos las variables.
    marca_izq = primero
    marca_der = ultimo
    pivote = lista_ordenada[randint(primero, ultimo)]
    print(lista_ordenada) #Mostramos la lista inicialmente.
    print("\nPivote:",pivote) #Mostramos el valor del pivote.

    #Mientras que las marcas no se crucen.
    while (marca_izq <= marca_der):
        #Buscamos valores mayores situados a la izquierda del pivote.
        while (lista_ordenada[marca_izq] < pivote): #Mientras que el valor del elemento de la marca izq. sea menor que el pivote, avanzamos la marca hacia la derecha.
            marca_izq = marca_izq+1

        #Buscamos valores menores situados a la derecha del pivote.
        while (lista_ordenada[marca_der] > pivote): #Mientras que el valor del elemento de la marca der. sea mayor que el pivote, avnazamos la marca hacia la izquierda.
            marca_der = marca_der - 1

        #Una vez finalizada la busqueda de los valores, los intercambiamos si las marcas no se han cruzado.
        if (marca_izq <= marca_der):
            lista_ordenada[marca_izq], lista_ordenada[marca_der] = lista_ordenada[marca_der], lista_ordenada[marca_izq]
            marca_izq = marca_izq+1
            marca_der = marca_der-1

    print(lista_ordenada) #Mostramos la lista a medida que se ordena.

    #Llamadas recursivas.
    if (primero < marca_der):
        ordenamiento_rapido_aleatorio(lista_ordenada, primero, marca_der)
    if (marca_izq < ultimo):
        ordenamiento_rapido_aleatorio(lista_ordenada, marca_izq, ultimo)

    return(lista_ordenada)

#Creamos la función.
def ordenamiento_rapido_mediana(lista_ordenada, primero, ultimo):

    #Definimos las variables.
    marca_izq = primero
    marca_der = ultimo
    pivote = mediana(lista_ordenada[primero], lista_ordenada[ultimo//2], lista_ordenada[ultimo])
    print(lista_ordenada) #Mostramos la lista inicialmente.
    print("\nPivote:",pivote) #Mostramos el valor del pivote.

    #Mientras que las marcas no se crucen.
    while (marca_izq <= marca_der):
        #Buscamos valores mayores situados a la izquierda del pivote.
        while (lista_ordenada[marca_izq] < pivote): #Mientras que el valor del elemento de la marca izq. sea menor que el pivote, avanzamos la marca hacia la derecha.
            marca_izq = marca_izq+1

        #Buscamos valores menores situados a la derecha del pivote.
        while (lista_ordenada[marca_der] > pivote): #Mientras que el valor del elemento de la marca der. sea mayor que el pivote, avnazamos la marca hacia la izquierda.
            marca_der = marca_der - 1

        #Una vez finalizada la busqueda de los valores, los intercambiamos si las marcas no se han cruzado.
        if (marca_izq <= marca_der):
            lista_ordenada[marca_izq], lista_ordenada[marca_der] = lista_ordenada[marca_der], lista_ordenada[marca_izq]
            marca_izq = marca_izq+1
            marca_der = marca_der-1

    print(lista_ordenada) #Mostramos la lista a medida que se ordena.

    #Llamadas recursivas.
    if (primero < marca_der):
        ordenamiento_rapido_aleatorio(lista_ordenada, primero, marca_der)
    if (marca_izq < ultimo):
        ordenamiento_rapido_aleatorio(lista_ordenada, marca_izq, ultimo)

    return lista_ordenada

#Creamos la función auxiliar para obtener el valor de la mediana.
def mediana(primero, medio, ultimo):

    lista_aux = [primero, medio, ultimo]
    lista_aux = sorted(lista_aux)

    return lista_aux[1] #Al haber odernado la lista, la mediana de 3 objetos va a ocupar la posición 1 de la lista.


#Programa principal:

#Definimos las variables.
opcion = 0

#Llamamos a la función para crear la lista aleatoria.
lista_desordenada = crea_lista_aleatoria()

#En las funciones usaremos .copy() para que la lista original no se modifique.
while (opcion != 8):

    #Mostramos el menú.
    print("\n¿Qué tipo de ordenamiento quiere visualizar?")
    print("\t1) Ordenamiento burbuja.")
    print("\t2) Ordenamiento por selección.")
    print("\t3) Ordenamiento por inserción.")
    print("\t4) Ordenamiento de Shell")
    print("\t5) Ordenamiento por mezcla.")
    print("\t6) Ordenamiento rápido.")
    print("\t7) Generar nueva lista aleatoria.")
    print("\t8) Salir.")

    try: #Lectura de datos validada.
        opcion = int(input("Opción: "))

        if (opcion == 1):
            print("\n¿Qué tipo de ordenamiento burbuja quiere visualizar?")
            print("\t1) Ordenamiento burbuja simple.")
            print("\t2) Ordenamiento burbuja bidireccional.")
            opcion = int(input("Opción ordenamiento burbuja: "))

            if (opcion == 1):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante burbuja simple:",ordenamiento_burbuja(lista_desordenada))
                input("Pulse ENTER para continuar.")

            elif (opcion == 2):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante burbuja bidireccional:",ordenamiento_burbuja_bidireccional(lista_desordenada))
                input("Pulse ENTER para continuar.")
            
            else:
                print("\nError, ha ocurrido algo inesperado.")
                input("Pulse ENTER para finalizar.")
                quit() #Salimos del programa

        elif (opcion == 2):
            print("\nLista aleatoria desordenada:",lista_desordenada)
            print("Proceso:")
            print("Lista ordenada mediante seleccion:",ordenamiento_seleccion(lista_desordenada))
            input("Pulse ENTER para continuar.")

        elif (opcion == 3):
            print("\nLista aleatoria desordenada:",lista_desordenada)
            print("Proceso:")
            print("Lista ordenada mediante inserción:",ordenamiento_insercion(lista_desordenada))
            input("Pulse ENTER para continuar.")

        elif (opcion == 4):
            print("\n¿Qué tipo de ordenamiento Shell quiere visualizar?")
            print("\t1) Incremento = mitad del tamaño de la lista.")
            print("\t2) Incremento = raiz cuadrada del tamaño de la lista.")
            print("\t3) Incremento = secuencia de Knuth.")
            print("\t4) Incremento = secuencia de Sedgewick.")
            print("\t5) Incremento = secuencia de Hibbard.")
            opcion = int(input("Opción ordenamiento rápido: "))

            if (opcion == 1):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante Shell (incremento = mitad del tamaño):",ordenamiento_shell_mitad(lista_desordenada))
                input("Pulse ENTER para continuar.")

            elif (opcion == 2):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante Shell (incremento = raiz cuadrada del tamaño):",ordenamiento_shell_raiz(lista_desordenada))
                input("Pulse ENTER para continuar.")

            elif (opcion == 3):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante Knuth (incremento = secuencia de Knuth):",ordenamiento_shell_knuth(lista_desordenada))
                input("Pulse ENTER para continuar.")

            elif (opcion == 4):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante Sedgewick (incremento = secuencia de Sedgewick):",ordenamiento_shell_sedgewick(lista_desordenada))
                input("Pulse ENTER para continuar.")

            elif (opcion == 5):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante Hibbard (incremento = secuencia de Hibbard):",ordenamiento_shell_hibbard(lista_desordenada))
                input("Pulse ENTER para continuar.")
            
            else:
                print("\nError, ha ocurrido algo inesperado.")
                input("Pulse ENTER para finalizar.")
                quit() #Salimos del programa

        elif (opcion == 5):
            print("\nLista aleatoria desordenada:",lista_desordenada)
            print("Proceso:")
            print("Lista ordenada mediante mezcla:",ordenamiento_mezcla(lista_desordenada.copy()))
            input("Pulse ENTER para continuar.")

        elif (opcion == 6):
            print("\n¿Qué tipo de ordenamiento rápido quiere visualizar?")
            print("\t1) Pivote = primer valor.")
            print("\t2) Pivote = valor aleatorio.")
            print("\t3) Pivote = mediana del vector.")
            opcion = int(input("Opción ordenamiento rápido: "))

            if (opcion == 1):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante ordenamiento rápido (pivote = primero):",ordenamiento_rapido_primero(lista_desordenada.copy(), 0, len(lista_desordenada)-1))
                input("Pulse ENTER para continuar.")

            elif (opcion == 2):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante ordenamiento rápido (pivote = aleatorio):",ordenamiento_rapido_aleatorio(lista_desordenada.copy(), 0, len(lista_desordenada)-1))
                input("Pulse ENTER para continuar.")
            
            elif (opcion == 3):
                print("\nLista aleatoria desordenada:",lista_desordenada)
                print("Proceso:")
                print("Lista ordenada mediante ordenamiento rápido (pivote = mediana):",ordenamiento_rapido_mediana(lista_desordenada.copy(), 0, len(lista_desordenada)-1))
                input("Pulse ENTER para continuar.")
            
            else:
                print("\nError, ha ocurrido algo inesperado.")
                input("Pulse ENTER para finalizar.")
                quit() #Salimos del programa

        elif (opcion == 7):
            lista_desordenada = crea_lista_aleatoria()
            print("\nNueva lista aleatoria:",lista_desordenada)
            input("Pulse ENTER para continuar.")

        elif (opcion == 8):
            break #Salimos del bucle.

        else:
            print("\nError, ha ocurrido algo inesperado.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    except ValueError: #Si se introducen datos erróneos.
        print("\nError, ha ocurrido algo inesperado.")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

#FIN.
input("\nPulse ENTER para finalizar.")