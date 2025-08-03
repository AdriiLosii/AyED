"""
Programa: Ej09.py
Propósito:
    A partir del programa del triángulo de Pascal desarrollado en el ejercicio 3, vamos a
    multiplicar los elementos de cada una de las filas:
                    1        ........1
                   1 1       ........1
                  1 2 1      ........2
                 1 3 3 1     ........9
                1 4 6 4 1    .......96
    Si ahora dividimos cada resultado obtenido al multiplicar entre el obtenido en la fila
    anterior obtenemos los siguientes valores:
            {1, 2, 4.5, 10.666, …, 26.0417, 64.8}
    Y ahora volvamos a dividir cada uno de los resultados de esa lista entre el anterior.
    Llegamos a los siguientes datos:
            {2, 2.25, 2.370370, … , 2.44140625, 2.48832}
    Parece que después de comenzar en 2 los números van subiendo poco a poco. Si
    avanzamos un poco, por ejemplo, por la zona del n = 1000, el dato de la lista sería ya
    2.71692, que ya está más cerca del número e = 2.71818281
    Modifica el programa realizado en el ejercicio 3 para que calcule una aproximación del
    número e tal y como se explica en este enunciado. Aplicar alguna de las técnicas descritas
    en el tema...
Fecha: 04/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos los módulos.
from math import *

#Creamos la función.
def Pascal(n):

    triangulo = [[1]]

    for i in range(0, n - 1):   #Lineas
 
        fila = [1] #Principio de la fila.

        for j in range(0, len(triangulo[i])-1):
            fila.extend([ triangulo[i][j] + triangulo[i][j+1] ])

        fila += [1] #Final de la fila.
        
        triangulo.append(fila)

    return triangulo[-3], triangulo[-2], triangulo[-1] #Devolvemos las 3 últimas filas del triángulo.

def aproxima_e(n, error, aproximacion):

    #Definimos las variables.
    mult_linea1 = 1
    mult_linea2 = 1
    mult_linea3 = 1

    #Realizamos los cálculos.
    linea1, linea2, linea3 = Pascal(n) #Llamamos a la función para crear el triángulo de Pascal.

    #Multiplicamos los elementos de las lineas.
    for i in range(len(linea1)):
        mult_linea1 *= linea1[i]

    for i in range(len(linea2)):
        mult_linea2 *= linea2[i]
        
    for i in range(len(linea3)):
        mult_linea3 *= linea3[i]

    aproximacion = (mult_linea3/mult_linea2) / (mult_linea2/mult_linea1) #Dividimos la 3º y la 2º fila entre la división de la 2º entre la 1º (hacemos los 2 pasos de las divisiones en 1).

    #Hacemos la comparación mientras que n sea igual a 714, ya que, al trabajar en un ordenador de 64 bits, no es posible trabajar con floats de 128 bits (en este ejercicio saltaría la excepción de overflow).
    if (n != 714): #e - aproximacion >= error
        n += 1
        aproximacion, n = aproxima_e(n, error, aproximacion) #Llamamos recursivamente a la función.
        return aproximacion, n

    else:
        return aproximacion, n #Devolvemos el valor de la aproximación y el número de n.


#Programa principal.
#Definimos las variables.
error = 0.001
n = 3 #Valor inicial para las filas del triángulo (necesitamos 3 filas para realizar la aproximación).

aproximacion, n = aproxima_e(n, error, 0) #Llamamos a la función para aproximar el valor de e.

#Mostramos los resultados.
print("\nValor de e:",e)
print("Aproximación del número 'e' con un error menor a:",error,"aproximación =",aproximacion)
print("Número de filas requeridas:",n)
print("La aproximación solo es posible realizarla hasta n == 714 ya que si seguimos aumentando el valor de n saltará la excepción de overflow.")

#FIN.
input("\nPulse ENTER para finalizar.")