#Tema2_14
from Class_Estructuras_lineales import ListaNoOrdenada
"""todos los Métodos estan en la Clase: Class_Estructuras_lineales 
al lado de cada metodo se indica la linea en la que se encuentra 
la funcion en la clase"""
milista = ListaNoOrdenada()
milista.agregar(31)     #Agregamos numeros a las dos listas
milista.agregar(77)     #linea de la clase 195
milista.agregar(17)
milista.agregar(93)
milista.agregar(26)
milista.agregar(54)
milista.agregar(64)
milista.agregar(55)

print("Este es el tamaño inicial de la primera lista:",milista.tamano())  #linea de la clase 200
print("Esta el numero 93 en la primera lista: ",milista.buscar(93))    #linea de la clase 210
print("Esta el numero 100 en la primera lista: ",milista.buscar(100))   

milista.agregar(100)         #Agregamos al numero 100 a la 2 lista
print("Ahora esta el numero 100 en la primera lista",milista.buscar(100))    



milista.anexar(16)           #linea de la clase 236
print("Ahora comprobamos el tamaño de la lista despùes de añadir al final de la lista el numero 16:  ",milista.tamano())
milista.insertar(2,9)        #linea de la clase 253
print("Ahora comprobamos el tamaño de la lista despùes de añadir en la poscicion 2 el numero 9:  ",milista.tamano())

print("Buscamos el indice del numero 93 en la primera lista",milista.indice(93))    #linea de la clase 266


milista.extaerelemento(17)   #linea de la clase 278
print("Este es el tamaño de la lista despues de extraer el numero 93: ",milista.tamano())

milista.extaerposicion(2)    #linea de la clase 290
print("Este es el tamaño de la lista despues de extraer el numero que estana en la posicion 2: ",milista.tamano())

milista.modificar(2,3)       #linea de la clase 300
print("Comporbamos que el 3 esta en la lista",milista.buscar(3))

print("El final de la lista es: ", milista.fin())         #linea de la clase 308
print("El principio de la lista es: ", milista.primero())     #linea de la clase 315

print("El siguiente en la lista a 77 es: ", milista.siguiente(77)) #linea de la clase 320

print("El anterior en la lista a 77 es: ", milista.anterior(77)) #linea de la clase 278
print("Este es el tamaño final de la primera lista:",milista.tamano())


