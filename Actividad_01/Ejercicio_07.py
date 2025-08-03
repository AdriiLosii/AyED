"""
Programa: Ejercicio_07.py
Propósito:
    Implementar con todos sus componentes la clase Polinomio, de manera que se puedan ejecutar 
    todas las operaciones sobre polinomios
Fecha: 19/02/2022
Autores: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
"""

from Clase_Polinomio_07 import *

#Petición de datos.
print("El primer número será el que acompañe a x^n y el último el término independiente")
pol1 = Polinomio(str(input("Introduce los valores del primer polinomio separados por espacios: ")))
pol2 = Polinomio(str(input("Introduce los valores del segundo polinomio separados por espacios: ")))

#Mostramos  los polinomios introducidos
print("\nPolinomio 1:\n",pol1)
print("\nPolinomio 2:\n",pol2)

#Realizamos las operaciones con los polinomios
print("\nSuma:\n",pol1 + pol2)

print("\nResta:\n",pol1 - pol2)

print("\nMultiplicación:\n",pol1 * pol2)

cociente, resto = pol1 / pol2
print("\nDivisión:\n",cociente, "\ncon resto:\n",resto)

print("¿A qué polinomio quiere aplicar la potencia? (Escriba a o b)\n")
print("\ta) Polinomio 1")
print("\tb) Polinomio 2")
opcion = str(input())

try:
    potencia = int(input("Introduce la potencia a la que quiere elevar el polinomio: "))
    
except ValueError:
    print("Error, ha ocurrido algo inesperado.")
    input("Pulse ENTER para finalizar.")
    quit() #Salimos del programa

if (opcion == "a" or opcion == "A" and potencia >= 0):
    print("\nPotencia:\n", pow(pol1, potencia))
elif (opcion == "b" or opcion == "B" and potencia >= 0):
    print("\nPotencia:\n", pow(pol2, potencia))
else:
    print("Error, introduzca una opción válida.")

input("\nPulse ENTER para finalizar.")