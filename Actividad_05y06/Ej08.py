"""
Programa: Ej08.py
Propósito:
    Utilizando la clase MonticuloBinario, implementa una nueva clase llamada ColaPrioridad. Esta nueva
    clase ColaPrioridad debe implementar el constructor, además de los métodos agregar y avanzar.
Fecha: 10/05/2022
"""


#Importamos la clase.
from Class_colas_prioridad_08 import *


#Programa principal.
def main():

    #Definimos las variables.
    miMonticulo = ColaPrioridad()
    opcion = 0

    #Mostramos el menú.
    while (opcion != 8):
        print('\n\t***ELIGE UNA OPCIÓN***')
        print('\t1) Introducir un valor.')
        print('\t2) Introducir un conjunto de valores.')
        print('\t3) Verificar si la lista está vacía.')
        print('\t4) Verificar el máximo del montículo')
        print('\t5) Extraer el valor máximo del montículo')
        print('\t6) Extraer el valor mínimo del montículo')
        print('\t7) Recorrer la lista.')
        print('\t8) Salir.')

        try: #Lectura de datos validada.
            opcion = int(input('\t'))

            if opcion==1:
                try:
                    valor=int(input('\nIntroduce el valor a añadir en el montículo:\n'))
                    miMonticulo.agregar(valor)

                except ValueError:
                    print('\nHas cometido un error, inténtalo de nuevo.')
                    input("Pulse ENTER para continuar.")
        
            elif opcion==2:
                try:
                    valor=input('\nIntroduce los valores a añadir en el montículo separados por comas:\n')
                    valor=valor.replace(" ","") #Eliminamos espacios en blanco.
                    valor=valor.split(',') #Creamos una lista con los valores introducidos.
                    valor=[int(v) for v in valor] #Transformamos los números en formado de string a tipo int.
                    miMonticulo.construirMonticulo(valor)

                except ValueError:
                    print('\nHas cometido un error, inténtalo de nuevo.')
                    input("Pulse ENTER para continuar.")

            elif opcion==3:
                if miMonticulo.esta_Vacia():
                    print('La lista está vacía.\n')
                else:
                    print('La lista tiene valores dentro.')

            elif opcion==4:
                if miMonticulo.esta_Vacia():
                    print('La lista está vacía.')
                else:
                    print('El valor máximo de la lista es: ',miMonticulo.maximo())

            elif opcion==5:
                if miMonticulo.esta_Vacia():
                    print('La lista está vacía.')
                else:
                    print('El valor máximo de la lista es: ',miMonticulo.extrae_y_borra(),' el cuál acaba de ser eliminado.')

            elif opcion==6:
                if miMonticulo.esta_Vacia():
                    print('La lista está vacía.')
                else:
                    print('El valor mínimo de la lista es: ',miMonticulo.eliminarMin(),' el cuál acaba de ser eliminado.')

            elif opcion==7:
                if miMonticulo.esta_Vacia():
                    print('La lista está vacía.')
                else:
                    print('La lista en un recorrido preorden, avanzando y dejando atrás el valor más pequeño es:')
                    miMonticulo.avanzar()

            elif opcion==8:
                break #Salimos del bucle

            else: #Si se introduce un número distinto a los mostrados.
                print("\nError, ha ocurrido algo inesperado.")
                input("Pulse ENTER para finalizar.")
                quit() #Salimos del programa

        except ValueError: #Si se introducen datos erróneos.
            print("\nError, ha ocurrido algo inesperado.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa


#Llamamos al programa principal.
main()

#FIN.
input("\nPulse ENTER para finalizar.")