"""
Programa: .py
Propósito:

Fecha: 
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importación de módulos.


while True: #Generamos un bucle en el programa.

    try: #Le pedimos al programa que intente realizar las siguientes órdenes.

        #Petición de datos.

        break #Si no hay problemas al realizar las órdenes, el bucle finaliza.

    except ValueError: #Si hay algún problema, el programa realiza las siguientes acciones.
        print("Error, ha ocurrido algo inesperado.")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

#FIN.
input("\nPulse ENTER para finalizar.")