#Tema2_14
from Class_Estructuras_lineales import ListaNoOrdenada
#from Class_Listas_No_Ordenadas import ListaNoOrdenada
milista = ListaNoOrdenada()

milista.agregar(31)
milista.agregar(77)
milista.agregar(17)
milista.agregar(93)
milista.agregar(26)
milista.agregar(54)

print(milista.tamano())
print(milista.buscar(93))
print(milista.buscar(100))

milista.agregar(100)
print(milista.buscar(100))
print(milista.tamano())

milista.borrar(54)
print(milista.tamano())
milista.borrar(93)
print(milista.tamano())
milista.borrar(31)
print(milista.tamano())
print(milista.buscar(93))
