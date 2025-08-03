"""
Programa: Ej06.py
Propósito:
    Utilizando el método construirMonticulo, escribe una función de ordenamiento que pueda ordenar una 
    lista en tiempo O(nlogn). (Buscar heapsort)
Fecha: 07/05/2022
"""

#Importamos la clase.
from Class_Monticulo_06 import *
from random import randint


#Programa principal.
#Definimos el montículo.
monticulo = MonticuloBinario()

#Llamamos a la función para que construya un montículo con la lista dada.
lista = []
tam = 10

#Creamos una lista de tamaño = tam, con número enteros entre 0 y tam*2.
for i in range(tam):
    lista.append(randint(0, tam*2))

monticulo.construirMonticulo(lista)

#Mostramos el monticulo antes de ser ordenado y después.
print("Monticulo (min heap):",monticulo)
listaOrdenada = monticulo.heapSort()
print("Lista monticulo ordenado:",listaOrdenada)

print("\nConclusión:")
print("La complejidad temporal de la función creada es de O(nlogn) ya que, la complejidad temporal")
print("para construir el monticulo max es de O(n) y la de ordenar el montículo (heapify) es O(nlogn).")

#FIN.
input("\nPulse ENTER para finalizar.")