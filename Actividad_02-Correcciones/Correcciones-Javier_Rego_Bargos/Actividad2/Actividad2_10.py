from Class_Estructuras_lineales import ListaNoOrdenada

milista = ListaNoOrdenada()
milista2 = ListaNoOrdenada()
milista.agregar(31)     #Agregamos numeros a las dos listas
milista.agregar(77)     #linea de la clase 195
milista.agregar(17)
milista.agregar(93)
milista2.agregar(26)
milista2.agregar(54)
milista2.agregar(64)
milista2.agregar(55)
print("Este es el tamaño de mi lista al principio de todo:",milista.tamano())
milista.anexarlista(milista2)
print("Este es el tamaño de mi lista al anexar la otra:",milista.tamano())