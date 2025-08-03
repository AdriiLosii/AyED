"""
Programa: Ej12.py
Propósito: 
    Implementar los métodos no desarrollados en el TAD ListaOrdenada, así como los 
    métodos borrar, indice, extraer y extraer(pos)
Fecha: 16/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos la clase.
from Class_Listas_Ordenadas_12 import ListaOrdenada


#Definimos las variables.
lista = ListaOrdenada()
opcion = 0

while(opcion != 17):
    #Mostramos el menú.
    print("\n¿Qué operación quiere realizar?")
    print("\t1) Agregar.")
    print("\t2) Mostrar.")
    print("\t3) ¿Está vacía?")
    print("\t4) Tamaño.")
    print("\t5) Buscar un elemento.")
    print("\t6) Indice de un elemento.")
    print("\t7) Borrar un elemento.")
    print("\t8) Borrar primer elemento.")
    print("\t9) Borrar último elemento.")
    print("\t10) Extraer un elemento.")
    print("\t11) Extraer el primer elemento.")
    print("\t12) Extraer el último elemento.")
    print("\t13) Primer elemento.")
    print("\t14) Último elemento.")
    print("\t15) Elemento anterior de ítem dado.")
    print("\t16) Elemento siguiente de ítem dado.")
    print("\t17) Salir.")

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
            elemento = float(input("\nIntroduce el elemento del que quieres saber su indice: "))
            print("Índice:",lista.indice(elemento))
            input("Pulse ENTER para continuar.")
        elif (opcion == 7):
            elemento = float(input("\nIntroduce el elemento que quiere borrar: "))
            print(lista.borrar(elemento))
            print("Nueva lista:",lista)
            input("Pulse ENTER para continuar.")
        elif (opcion == 8):
            print("\nBorrando el primer elemento: ")
            print(lista.borrarPrimero())
            print("Nueva lista:",lista)
            input("Pulse ENTER para continuar.")
        elif (opcion == 9):
            print("\nBorrando el ultimo elemento: ")
            print(lista.borrarUltimo())
            print("Nueva lista:",lista)
            input("Pulse ENTER para continuar.")
        elif (opcion == 10):
            elemento = float(input("\nIntroduce la posición del elemento que quieres extraer: "))
            print(lista.extraer(elemento))
            print("Nueva lista:",lista)
            input("Pulse ENTER para continuar.")
        elif (opcion == 11):
            print("\nExtrayendo el primer elemento:",lista.extraerPrimero())
            print("Nueva lista:",lista)
            input("Pulse ENTER para continuar.")
        elif (opcion == 12):
            print("\nExtrayendo el ultimo elemento:",lista.extraerUltimo())
            print("Nueva lista:",lista)
            input("Pulse ENTER para continuar.")
        elif (opcion == 13):
            print("\nPrimer elemento:",lista.primero())
            input("Pulse ENTER para continuar.")
        elif (opcion == 14):
            print("\nÚltimo elemento:",lista.ultimo())
            input("Pulse ENTER para continuar.")
        elif (opcion == 15):
            elemento = float(input("\nIntroduce el elemento del que quiere obtener el anterior: "))
            print("Elemento anterior a",elemento,"->",lista.anterior(elemento))
            input("Pulse ENTER para continuar.")
        elif (opcion == 16):
            elemento = float(input("\nIntroduce el elemento del que quiere obtener el siguiente: "))
            print("Elemento siguiente a",elemento,"->",lista.siguiente(elemento))
            input("Pulse ENTER para continuar.")
        elif (opcion == 17):
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