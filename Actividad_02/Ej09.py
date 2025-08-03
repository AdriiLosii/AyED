"""
Programa: Ej09.py
Propósito:
    Escribe la especificación informal del TAD Conjunto. Enriquece la clase Conjunto con:
        • Un método elimina que borre del conjunto un elemento dado
        • Un método unión que devuelva el conjunto resultante de unir dos conjuntos
        • Un método intersección que devuelva un conjunto con la intersección de dos 
        conjuntos
        • Un método diferencia que devuelva un conjunto con la diferencia entre dos 
        conjuntos
        • Un método incluye que consulta si un conjunto dado está incluido en el 
        conjunto
Fecha: 16/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos la clase.
from Class_Conjuntos_09 import Conjunto


#Definimos las variables.
conjunto1 = Conjunto()
conjunto2 = Conjunto()

print("\n\t * Conjunto1 inicial. * \n")
print("Conjunto1:",conjunto1)
print("Tamaño:",conjunto1.tamano())
print("¿Pertenece?",conjunto1.pertenece(4))

#Añadimos elementos a conjunto1.
print("\n\t * Añadimos elementos a conjunto1. * \n")
conjunto1.inserta(4)
conjunto1.inserta('perro')
conjunto1.inserta("gato")
conjunto1.inserta(True)
conjunto1.inserta(-8.4)
conjunto1.inserta(4) #Este elemento no se añadirá ya que en los conjuntos los elementos son únicos, no se repiten.

print("Conjunto1:",conjunto1)
print("Tamaño:",conjunto1.tamano())
print("¿Pertenece?",conjunto1.pertenece(4))

#Borramos elementos
print("\n\t * Borramos elementos del conjunto1. * \n")
conjunto1.elimina(3) #Elemento que no pertenece al conjunto.
conjunto1.elimina('perro')
conjunto1.elimina(-8.4)

print("Conjunto1:",conjunto1)
print("Tamaño:",conjunto1.tamano())
print("¿Pertenece?",conjunto1.pertenece(4))

#Añadimos elementos a conjunto2.
print("\n\t * Añadimos elementos a conjunto2. * \n")
conjunto2.inserta(5)
conjunto2.inserta('elefante')
conjunto2.inserta("loro")
conjunto2.inserta(True)
conjunto2.inserta(4)
conjunto2.inserta(-8.4)

print("Conjunto1:",conjunto1)
print("Conjunto2:",conjunto2)
print("Union conjuntos:",conjunto1.union(conjunto2))
print("Intersección conjuntos:",conjunto1.interseccion(conjunto2))
print("Diferencia conjunto1:",conjunto1.diferencia(conjunto2))
print("Diferencia conjunto2:",conjunto2.diferencia(conjunto1))
print("¿Conjunto1 incluido en conjunto2?",conjunto1.incluye(conjunto2))

#Borramos "gato" del conjunto1.
print("\n\t * Borramos 'gato' del conjunto1. * \n")
conjunto1.elimina("gato")

print("Conjunto1:",conjunto1)
print("Conjunto2:",conjunto2)
print("¿Conjunto1 incluido en conjunto2?",conjunto1.incluye(conjunto2))

#FIN.
input("\nPulse ENTER para finalizar.")