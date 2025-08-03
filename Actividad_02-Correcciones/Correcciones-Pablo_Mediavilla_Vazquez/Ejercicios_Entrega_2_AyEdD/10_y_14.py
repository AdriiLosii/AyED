from Class_Estructuras_lineales_P import ListaNoOrdenada

#Creamos la lista no ordenada
milista = ListaNoOrdenada()

milista.agregar(9)
milista.agregar(0)
milista.agregar(2)
milista.agregar(1)
milista.agregar(35)
milista.agregar(3)
milista.agregar(5)

#Buscamos tres elementos que no se encuentan en la lista, por lo que se devuelve None
print(milista.buscar(4))
print(milista.buscar(6))
print(milista.buscar(8))

#Ahora indexamos la lista a la lista no ordenada
lista=[4,8,6]
milista.anexar(lista)

#Ahora volvemos a buscar los elementos anteriores que acaban de ser introducidos en la lista no ordenada y si que encontramos su posicion
print(milista.buscar(4))
print(milista.buscar(6))
print(milista.buscar(8))

#Borrar comentario de abajo para devolver el tamaño para el ejercicio 14
#print(milista.tamano())