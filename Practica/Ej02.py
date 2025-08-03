#Importamos la clase.
from Class_ListaNoOrdenada_02 import ListaDoblementeEnlazada


#Programa principal:
#Definimos la lista enlazada no ordenada.
lista = ListaDoblementeEnlazada()

#Rellenamos la lista.
for i in range(10):
    lista.agregar(i)

#Mostramos la lista, eliminamos el número 4 y la volvemos a mostrar.
print("Lista inicial:",lista)
lista.borrar(4)
lista.borrar(40)
print("Lista después:",lista)