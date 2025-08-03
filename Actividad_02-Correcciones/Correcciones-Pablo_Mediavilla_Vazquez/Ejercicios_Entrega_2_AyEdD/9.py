from Class_Conjuntos_P import *

#Creamos los dos conjuntos
set_uno = Conjunto()
set_uno.inserta(1)
set_uno.inserta(3)
set_uno.inserta(5)
set_uno.inserta(10)
set_uno.inserta(7)

lista2= [9, 3, 7, 12]
set2 = set(lista2)

#Comenzamos a mostrar los resultados del ejercicio
print(set_uno)

#Borramos el elemento que ocupa la posicion dos
set_uno.borrar(2)

print(set_uno)

#Unimos dos conjuntos
Union = set_uno.union(set2)
print(Union)

#Interseccion de dos conjuntos
interseccion = set_uno.interseccion(set2)
print(interseccion)

#Diferencia de los dos conjuntos
print(set_uno.diferencia(set2))


#Creamos un nuevo set y comprobamos si sus elementos se encuentran en el conjunto uno
set3 = {3, 7}
print(set_uno.incluye(set3))