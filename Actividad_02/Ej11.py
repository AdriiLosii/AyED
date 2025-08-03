"""
Programa: Ej11.py
Propósito: 
    Implementar el método anexar una nueva lista para ListaNoOrdenada. ¿Cuál es la
    complejidad de tiempo del método que creaste?
Fecha: 17/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""

#Importamos la clase.
from Class_Listas_No_Ordenadas_11 import *

#Definimos las variables.
lista = ListaNoOrdenada()
opcion = 0

while(opcion != 11):
    #Mostramos el menú.
    print("\n¿Qué operación quiere realizar?")
    print("\t1) Agregar.")
    print("\t2) Mostrar.")
    print("\t3) ¿Está vacía?")
    print("\t4) Tamaño.")
    print("\t5) Buscar un elemento.")
    print("\t6) Borrar un elemento.")
    print("\t7) Elemento del principio.")
    print("\t8) Elemento del final.")
    print("\t9) Elemento anterior de ítem dado.")
    print("\t10) Elemento siguiente de ítem dado.")
    print("\t11) Salir.")

    try:
        opcion = int(input("Opcion: "))

        if (opcion == 1):
            elemento = float(input("\nIntroduzca un número: "))
            lista.agregar(elemento)
            input("Pulse ENTER para continuar.")
        elif (opcion == 2):
            print("Lista:",lista)
            input("Pulse ENTER para continuar.")
        elif (opcion == 3):
            print("\n¿Está vacía la lista?:",lista.estaVacia())
            input("Pulse ENTER para continuar.")
        elif (opcion == 4):
            print("\nTamaño de la lista:",lista.tamano())
            input("Pulse ENTER para continuar.")
        elif (opcion == 5):
            elemento = float(input("\nIntroduce el elemento que quiere buscar: "))
            print("¿El elemento está en la lista?:",lista.buscar(elemento))
            input("Pulse ENTER para continuar.")
        elif (opcion == 6):
            elemento = float(input("\nIntroduce el elemento que quiere borrar: "))
            print(lista.borrar(elemento))
            input("Pulse ENTER para continuar.")
        elif (opcion == 7):
            print("\nElemento del principio:",lista.principio())
            input("Pulse ENTER para continuar.")
        elif (opcion == 8):
            print("\nElemento del final:",lista.final())
            input("Pulse ENTER para continuar.")
        elif (opcion == 9):
            elemento = float(input("\nIntroduce el elemento del que quiere obtener el anterior: "))
            print("Elemento anterior a",elemento,":",lista.anterior(elemento))
            input("Pulse ENTER para continuar.")
        elif (opcion == 10):
            elemento = float(input("\nIntroduce el elemento del que quiere obtener el siguiente: "))
            print("Elemento siguiente a",elemento,":",lista.siguiente(elemento))
            input("Pulse ENTER para continuar.")
        elif (opcion == 11):
            continue
        else:
            print("\nError, ha ocurrido algo inesperado.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    except ValueError:
        print("\nError, ha ocurrido algo inesperado.")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

#FIN.
input("\nPulse ENTER para finalizar.")