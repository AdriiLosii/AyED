"""Implementar el método anexar una nueva lista para ListaNoOrdenada. ¿Cuál es la
complejidad de tiempo del método que creaste?"""

from ClassListasNoOrdenadas import *


lista = ListaNoOrdenada()
lista2 = ListaNoOrdenada()

lista2.agregar(5)
lista2.agregar(9)

print(lista2)

lista.agregar(1)
lista.agregar(-3)
lista.agregar(20)

print(lista)

lista.concatenar(lista2)

print(lista, lista2)

