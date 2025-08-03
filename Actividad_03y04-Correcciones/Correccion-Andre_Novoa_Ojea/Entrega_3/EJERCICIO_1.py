#Ejercicio 1: Escribe una función recursiva para invertir una lista enlazada.
from random import randint

def inversor(lista):
    copia = lista[::-1]

    return copia

longitud = int(input("Indique la longitud de la lista: "))
lista = [0] * longitud

for i in range (len(lista)):
    lista[i] = randint(1, 100)  #Se asignan valores aleatorios entre 1 y 100 a todos los elementos de la lista.

print("Su lista original es", lista)
print(" ")
print("Su lista invertida es", inversor(lista)) #Se llama a la funcion para mostrar el resultado 
print(" ")