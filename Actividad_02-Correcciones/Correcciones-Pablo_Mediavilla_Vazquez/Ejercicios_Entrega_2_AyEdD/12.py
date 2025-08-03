from Class_Estructuras_lineales_P import ListaOrdenada

#Creamos la lista ordenada
milista = ListaOrdenada()

milista.agregar(9)
milista.agregar(0)
milista.agregar(2)
milista.agregar(1)
milista.agregar(35)
milista.agregar(3)

"""
A pesar de haber introducido los numeros en un orden aleatorio,
al ser una lista ordenada, el metodo ordena e introduce los numeros
digitados de menor a mayor 
"""
print("Posicion-->",milista.indice(1))
print("Posicion-->",milista.indice(9))
print("Posicion-->",milista.indice(30))

milista.borrar(35)
print("Posicion-->",milista.indice(35))

milista.extraer_pos(9)
print("Posicion-->",milista.indice(9))

milista.extraer()
print("Posicion-->",milista.indice(0))
