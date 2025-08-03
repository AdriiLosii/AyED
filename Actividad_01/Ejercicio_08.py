"""
Programa: Ejercicio_08.py
Propósito:
    Implementar con todos sus componentes la clase Complejo, de manera que se puedan ejecutar 
    todas las operaciones sobre complejos
Fecha: 21/02/2022
Autores: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
"""


from Clase_Complejo_08 import *

real_1 = input("Introduzca la parte real del primer número: ")
imaginario_1 = input("Introduzca la parte imaginaria del primer número: ")

a = Complejo(real_1, imaginario_1)

real_2 = input("Introduzca la parte real del segundo número: ")
imaginario_2 = input("Introduzca la parte imaginaria del segundo número: ")

b = Complejo(real_2, imaginario_2)

print("\nPrimer complejo: {0}".format(a))
print("\nSegundo complejo: {0}".format(b))

#Menu
print("\n¿Que quieres hacer? (Escriba a,b,c,d,e,f,g o h)\n")
print("\ta) Sumar los complejos")
print("\tb) Restar los complejos")
print("\tc) Multiplicar los complejos")
print("\td) Dividir los complejos")
print("\te) Elevar a una potencia los complejos")
print("\tf) Hacer el conjugado")
print("\tg) Ver la parte real")
print("\th) Ver la parte imaginaria")
opcion = str(input())

if opcion == "a" or opcion == "A":

    print("Suma: {0}\n".format(a + b))

if opcion == "b" or opcion == "B":
    
    print("Resta: {0}\n".format(a - b))

if opcion == "c" or opcion == "C":

    print("Multiplicacion: {0}\n".format(a * b))

if opcion == "d" or opcion == "D":

    print("Division: {0}\n".format(a / b))


if opcion == "e" or opcion == "E":

    print("¿A qué complejo le quieres hacer la potencia?")
    print("\ta) Primer complejo")
    print("\tb) Segundo complejo")
    opcion = str(input())

    pot=int(input("Introduce la potencia a la que quieres elevar el complejo: "))

    if opcion == "a" or opcion == "A":
        print("Potencia: {0}".format(a ** pot))

    if opcion == "b" or opcion == "B":
        print("Potencia: {0}".format(b ** pot))



if opcion == "f" or opcion == "F":

    #Menu para el conjugado
    print("¿A qué complejo le quieres aplicar el conjugado?")
    print("\ta) Conjugado del primer complejo")
    print("\tb) Conjugado del segundo complejo")
    print("\tc) Conjugado de ambos complejos")
    opcion = str(input())

    if opcion == "a" or opcion == "A":
        print("Conjugado del primer complejo: ", a.conj())
    if opcion == "b" or opcion == "B":
        print("Conjugado del segundo complejo: ", b.conj())
    if opcion == "c" or opcion == "C":
        print("Conjugado del primer complejo: ", a.conj())
        print("Conjugado del segundo complejo: ", b.conj())
        
if opcion == "g" or opcion == "G":

    #Menu para la parte real
    print("¿De qué conjugado quieres ver la parte real?")
    print("\ta) Parte real del primer complejo")
    print("\tb) Parte real del segundo complejo")
    print("\tc) Parte real de ambos complejos")
    opcion = str(input())

    if opcion == "a" or opcion == "A":
        print("Parte real del primer complejo: ", a.parte_real())
    if opcion == "b" or opcion == "B":
        print("Parte real del segundo complejo: ", b.parte_real())
    if opcion == "c" or opcion == "C":
        print("Parte real del primer complejo: ", a.parte_real())
        print("Parte real del segundo complejo: ", b.parte_real())
        
if opcion == "h" or opcion == "H":

    #Menu para la parte imaginaria
    print("¿De qué conjugado quieres ver la parte imaginaria?")
    print("\ta) Parte imaginaria del primer complejo")
    print("\tb) Parte imaginaria del segundo complejo")
    print("\tc) Parte imaginaria de ambos complejos")
    opcion = str(input())

    if opcion == "a" or opcion == "A":
        print("Parte imaginaria del primer complejo: ", a.parte_imag())
    if opcion == "b" or opcion == "B":
        print("Parte imaginaria del segundo complejo: ", b.parte_imag())
    if opcion == "c" or opcion == "C":
        print("Parte imaginaria del primer complejo: ", a.parte_imag())
        print("Parte imaginaria del segundo complejo: ", b.parte_imag())

input("\nPulse ENTER para finalizar.")