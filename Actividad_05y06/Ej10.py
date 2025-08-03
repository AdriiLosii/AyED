"""
Programa: Ej10.py
Propósito:
    Dada la secuencia de claves enteras 20, 10, 30, 5, 25, 12, 3, 35, 22, 11, 6, 2, y la secuencia 100, 29, 71, 82, 48,
    39, 101, 22, 46, 17, 3, 20, 25, 10, representa gráficamente los árboles AVL correspondientes e indica en qué
    momento se efectuó una rotación.
Fecha: 07/05/2022
"""


#Importamos la clase.
from Class_AVL_10 import *


#Programa principal.
opcion = 0
while(opcion != 3):
    #Mostramos el menú con lectura validada
    try:
        print("\n¿Qué árbol quieres visualizar?")
        print("\t1) Visualizar árbol 1")
        print("\t2) Visualizar árbol 2")
        print("\t3) Salir.")
        opcion = int(input("\nOpción: "))

        if (opcion != 1 and opcion != 2 and opcion != 3):
            raise ValueError
    except ValueError:
        print("\nError, ha ocurrido algo inesperado.")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

    if (opcion == 1):
        sec_1 = [20, 10, 30, 5, 25, 12, 3, 35, 22, 11, 6, 2]
        arbol_1 = ArbolBinarioBusquedaAVL()

        #Agregramos las claves al primer arbol y mostramos su recorrido inorden.
        print("\nPrimer árbol:")
        for clave in sec_1:
            print("\nAgregamos la clave:",clave)
            arbol_1.agregar(clave,clave)

        arbol_1.inorden()

        #Representación gráfica del árbol AVL.
        nodos_1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        sec_final_1 = ["20", "10", "30", "5", "25", "12", "3", "35", "22", "11", "6", "2"]
        aristas_1 = ['AB','AC','BD','BE','CG','CF','DI','DH','EJ','FK','HL']
        arbol_1.muestra_graphviz(nodos_1, sec_final_1, aristas_1)

    if (opcion == 2):
        sec_2 = [100, 29, 71, 82, 48, 39, 101, 22, 46, 17, 3, 20, 25, 10]
        arbol_2 = ArbolBinarioBusquedaAVL()

        #Agregamos las claves al segundo arbol y mostramos su recorrido inorden.
        print("\nSegundo árbol:")
        for clave in sec_2:
            print("Agregamos la clave:",clave)
            arbol_2.agregar(clave,clave)

        arbol_2.inorden()

        #Representación gráfica del árbol AVL.
        nodos_2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
        sec_final_2 = ["39", "22", "71", "17", "29", "48", "100", "3", "20", "25", "46", "82", "101", "10"]
        aristas_2 = ['AB','AC','BD','BE','CF','CG','DI','DH','EJ','FK','GL','GM','HN']
        arbol_2.muestra_graphviz(nodos_2, sec_final_2, aristas_2)

    if (opcion == 3):
        break #Salimos del bucle.

#FIN.
input("\nPulse ENTER para finalizar.")