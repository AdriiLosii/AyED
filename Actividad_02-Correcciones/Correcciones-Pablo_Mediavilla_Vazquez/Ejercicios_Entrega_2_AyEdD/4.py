from Class_Estructuras_lineales_P import *

#Creamos  la lista 1, que es una cola, y despues agregamos elementos
lista1 = Cola()

lista1.agregar(2)
lista1.agregar(5)
lista1.agregar(9)
lista1.agregar(6)
lista1.agregar(7)

#La mostramos
print(lista1)

#Ahora repetimos el proceso anterior pero para la lista 2
lista2 = Cola()

lista2.agregar(9)
lista2.agregar(0)
lista2.agregar(2)
lista2.agregar(1)
lista2.agregar(0)

#Tambien la mostramos
print(lista2)

#Creamos la lista final, que tambien es una cola
listafin = Cola()

#Dada la lista final, concatenamos en su interior la lista 1 y la lista 2
print(listafin.concatenar(lista1,lista2))

