#Tema2_15
from Class_Estructuras_lineales import ListaOrdenada
milista = ListaOrdenada()
milista2 = ListaOrdenada()
milista.agregar(31)
milista.agregar(77)
milista.agregar(17)
milista.agregar(93)
milista.agregar(26)
milista.agregar(54)

print(milista.tamano())
print(milista.buscar(93))
print(milista.buscar(100))
print("Se borrara el siguiente elemento")
milista.borrar(77)
print(milista.tamano())
print("Mostramos el indice del siguiente elemento")
print(milista.indice(54))
print("Ahora extraemos el ultimo elemento y obtenemos que el tamaño y el elemento no estan")
milista.extraer()
print(milista.tamano())
print(milista.buscar(93))
print("Extraemos el elemento en la tercera posicion")
milista.extaerposicion(3)
print(milista.tamano())
print(milista.buscar(54))


