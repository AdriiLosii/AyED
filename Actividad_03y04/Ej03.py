"""
Programa: Ej03.py
Propósito: 
    El triángulo de Pascal es un triángulo numérico con números dispuestos en filas
    escalonadas de manera que
    Esta ecuación es la ecuación para un coeficiente binomial. Se puede construir el
    triángulo de Pascal agregando los dos números que están, en diagonal, encima de un
    número en el triángulo. A continuación, se muestra un ejemplo del triángulo de Pascal.
                    1
                   1 1
                  1 2 1
                 1 3 3 1
                1 4 6 4 1
    Escribe, siguiendo técnicas descritas en los apuntes, distintas versiones de un
    programa que imprima el triángulo de Pascal. El programa debe aceptar un parámetro
    que indique cuántas filas se imprimirán del triángulo.
Fecha: 04/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Creamos la función.
def Pascal(n):

    triangulo = [[1]]

    for i in range(0, n - 1):   #Lineas
 
        fila = [1] #Principio de la fila.

        for j in range(0, len(triangulo[i])-1):  #Columnas

            fila.extend([ triangulo[i][j] + triangulo[i][j+1] ])

        fila += [1] #Final de la fila.
        
        triangulo.append(fila)

    return triangulo

#Creamos la función recursiva.
def Pascal_recursivo(n):

    for i in range(0, n, 1):

        j = 0
        while (j <= i):
            print(triangulo_recursivo(i, j), end=" ")
            j += 1
        print()

#Creamos la función recursiva para crear las lineas del triángulo.
def triangulo_recursivo(fila, columna):

    if (fila == columna or columna == 0):
        return 1
    else:
        return triangulo_recursivo(fila-1, columna-1) + triangulo_recursivo(fila-1, columna)


#Petición de datos validada.
try:
    n = int(input("Introduce el numero de lineas que quieres que tenga el triangulo de Pascal: "))

    if (n <= 0):
        raise ValueError

    print("\nTriángulo de Pascal sin recursividad:")
    triangulo = Pascal(n) #Llamamos a la función para crear el triángulo de Pascal.

    #Mostramos el triángulo.
    for i in range(len(triangulo)):
        for j in range(len(triangulo[i])):

            print(triangulo[i][j], end=" ") #Mostramos la fila.

        print() #Salto de línea.

    print("\nTriángulo con recursividad:")
    Pascal_recursivo(n) #Llamamos a la función para crear el triángulo de Pascal recursivamente.

except ValueError:
    print ("\nHa ocurrido un error en la lectura de datos, por favor introduce un numero entero mayor que 0.")
    input("Pulse ENTER para finalizar.")
    quit() #Salimos del programa

#FIN.
input("\nPulse ENTER para finalizar.")