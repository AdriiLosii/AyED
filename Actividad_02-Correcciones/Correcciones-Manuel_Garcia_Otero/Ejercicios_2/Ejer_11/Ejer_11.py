"""Implementar los métodos no desarrollados en el TAD Lista_No_Ordenada, así como
los métodos fin, primero, siguiente y anterior"""

from typing import List
from Class_Listas_No_Ordenadas import *
from Class_Nodos import *


lista = ListaNoOrdenada()
lista2 = ListaNoOrdenada()
lista2.agregar(3)

lista.agregar(2)
lista.agregar(7)
lista.agregar(-1)
lista.agregar(-23)
lista.agregar(77)

print(lista, lista.tamano())

lista.anexar(78)
print(lista, lista.tamano())

lista.insertar(3,5)
print(lista, lista.tamano())

lista.modificar(6,-888)
print(lista, lista.tamano())

print(lista.indice(77))
print(lista.indice('1'))

print(lista.extraer(1).obtenerDato(), lista, lista.tamano())

print(lista2.ultimo().obtenerDato(), lista2, lista2.tamano())
print(lista.ultimo().obtenerDato(), lista, lista.tamano())

print(lista2.primero().obtenerDato(), lista2, lista2.tamano())
print(lista.primero().obtenerDato(), lista, lista.tamano())

print("anterior del ultimo: ", lista.ultimo().obtenerAnterior().obtenerDato())
lista.borrar(77)
print(lista)
print("anterior del ultimo: ", lista.ultimo().obtenerAnterior().obtenerDato())
lista.insertar(4,555)
print(lista)
print("anterior del ultimo: ", lista.ultimo().previous())
print("siguiente al primero: ", lista.primero().next())



objeto = lista.extraer(3)
print(lista)
print(objeto.previous())
