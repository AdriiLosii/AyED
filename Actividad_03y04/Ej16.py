"""
Programa: Ej16.py
Propósito:
    ¿Cómo puedes eliminar ítems de una tabla hash que utiliza encadenamiento para la 
    solución de colisiones? ¿Qué tal si se usa direccionamiento abierto? ¿Cuáles son las 
    circunstancias especiales que deben manejarse? Implementa el método eliminar para 
    la clase TablaHash que utiliza encadenamiento.
Fecha: 19/04/2022
Autores: Gabriel Iglesias Sotelo y Adrián Losada Álvarez 
"""


#Importamos la clase.
from Class_Tabla_Hash_Encadenada_16 import *


#Creamos la tabla hash.
Tabla = TablaHashEncadenada()

#Creamos el menú.
opcion = 0
while (opcion != 5):
    print("\n¿Qué acción quiere realizar?")
    print("\t1) Agregar un elemento a la tabla.")
    print("\t2) Eliminar un elemento de la tabla.")
    print("\t3) Mostrar la tabla.")
    print("\t4) Mostrar la conclusión.")
    print("\t5) Salir.")

    try: #Lectura de datos validada.
        opcion = int(input("\nOpción: "))

        if (opcion == 1):

            clave = int(input("\nIntroduzca la clave del ítem: ")) #Pedimos al ususario la clave del item que quiere agregar a la tabla
            if (clave < 0):
                raise ValueError

            item = input("Introduce el ítem: ")  #Pedimos el item en cuestión

            Tabla[clave] = item #Agregamos el elemento a la tabla.
            input("\nPulse ENTER para continuar.")

        elif (opcion == 2):
            
            clave = int(input("Introduzca la clave del ítem: "))  #Pedimos al ususario la clave del item que quiere eliminar
            if (clave < 0):
                raise ValueError

            print("\nElemento eliminado:",Tabla.eliminar(clave),"\n")  #Mostramos el item elimminado
            input("\nPulse ENTER para continuar.")            

        elif (opcion == 3):
            
            #Mostramos la tabla.
            print("\nLa tabla hash actual es la siguiente:\n{0}".format(Tabla))
            input("\nPulse ENTER para continuar.")
                
        elif (opcion == 4):

            #Mostramos la conclusión.
            print("\nPregunta: ¿Cómo puedes eliminar ítems de una tabla hash que utiliza encadenamiento para la solución de colisiones?")
            print("Respuesta: Para eliminar un elemento en una tabla hash que utiliza encadenamiento, tendremos que eliminar el ítem que está realizando la función de cabeza de la lista enlazada en el slot indicado.")
            print("\nPregunta: ¿Qué tal si se usa direccionamiento abierto?")
            print("Respuesta: Con direccionamiento abierto simplemente nos posicionaremos en el slot con la clave correspondiente y reemplazaremos el valor a eliminar por 'None'.")
            print("\nPregunta: ¿Cuáles son las circunstancias especiales que deben manejarse?")
            print("En el caso de la tabla hash que utiliza encadenamiento habrá un problema, al eliminar la cabeza de la lista, eliminaremos también el resto de elementos posicionados en el mismo slot.")
            input("\nPulse ENTER para continuar.")

        elif (opcion == 5):
            break #Salimos del menú.
        
        else:
            print("\nError, ha ocurrido algo inesperado.")  #Notificamos error en la lectura de datos
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    except ValueError: #Si se introducen datos erróneos.
        print("\nError, ha ocurrido algo inesperado.")   #Notificamos error en la lectura de datos
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

#FIN.
input("\nPulse ENTER para finalizar.")