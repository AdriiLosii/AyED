"""
Programa: Class_Listas_Ordenadas_12.py
Propósito: 
    Implementar los métodos no desarrollados en el TAD ListaOrdenada, así como los 
    métodos borrar, indice, extraer y extraer(pos)
Fecha: 16/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def __str__(self):
        return str(self.dato)

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente


class ListaOrdenada:
    def __init__(self):
        self.cabeza = None

    def __str__(self): #Salida (print)
        actual = self.cabeza
        cadena = ''

        while(actual != None):
            if (actual.obtenerSiguiente() != None): #Si no es el último nodo
                cadena = cadena + str(actual.obtenerDato()) + " -> "
                actual = actual.obtenerSiguiente()

            else: #Si es el último nodo.
                cadena = cadena + str(actual.obtenerDato())
                actual = actual.obtenerSiguiente()

        return cadena

    def agregar(self,item):
        try: #Validación de datos.
            actual = self.cabeza
            previo = None
            detenerse = False

            while actual != None and not detenerse:
                if actual.obtenerDato() > item:
                    detenerse = True
                else:
                    previo = actual
                    actual = actual.obtenerSiguiente()

            temp = Nodo(item)
            if previo == None:
                temp.asignarSiguiente(self.cabeza)
                self.cabeza = temp
            else:
                temp.asignarSiguiente(actual)
                previo.asignarSiguiente(temp)

        except TypeError: #Si se introduce otra cosa distinta a números.
            print("\nError, revise el tipo de datos introducidos para crear la cola.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    def estaVacia(self):
        return self.cabeza == None

    def tamano(self):
        actual = self.cabeza
        contador = 0

        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        detenerse = False

        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                if actual.obtenerDato() > item:
                    detenerse = True
                else:
                    actual = actual.obtenerSiguiente()

        return encontrado

    def indice(self, elemento): #Devuelve la posición en la lista ordenada del elemento indicado.
        actual = self.cabeza
        encontrado = False
        posicion = 0

        while actual != None and not encontrado:
            if actual.obtenerDato() == elemento:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
                posicion += 1

        if (encontrado == True):
            return posicion
        else:
            return ("Elemento no encontrado.")

    def borrar(self, elemento): #Borra el número indicado de la lista ordenada.
        actual = self.cabeza
        anterior = None
        encontrado = False

        while actual != None and not encontrado:
            if actual.obtenerDato() == elemento:
                encontrado = True
            else:
                anterior = actual
                actual = actual.obtenerSiguiente()
        
        if (encontrado == False): #Si el elemento no esta en la lista ordenada.
            return ("Error al intentar eliminar el elemento -> %f. Compruebe si el elemento introducido pertenece a la lista." % elemento)
        else:
            #Borramos el elemento.
            if (anterior == None): #Si la lista está formada por solo 1 elemento.
                self.cabezaCola = actual.obtenerSiguiente()
                return ("Elemento borrado correctamente.")
            else:
                anterior.asignarSiguiente(actual.obtenerSiguiente()) #Nos "saltamos" el número actual (elemento que queremos borrar).
                return ("Elemento borrado correctamente.")

    def borrarPrimero(self):
        actual = self.cabeza

        if self.tamano() == 0:
            return ("Error, la lista está vacía.")
        else:
            self.cabeza = actual.obtenerSiguiente()
            return ("Primero borrado correctamente.")

    def borrarUltimo(self): #Borra el primer número de la lista ordenada (número más grande).
        actual = self.cabeza
        anterior = None

        if self.tamano() == 0: #Si la cola está vacía.
            return ("Error, la lista está vacía.")

        while(actual.obtenerSiguiente() != None): #Obtenemos el elemento en la última posición (número mayor) y el anterior, como la lista está ordenada de menor a mayor -> último elemento = mayor elemento.
            anterior = actual
            actual = actual.obtenerSiguiente()

        #Borramos el elemento.
        if (anterior == None): #Si la lista está formada por solo 1 elemento.
            self.cabeza = actual.obtenerSiguiente()
            return ("Último borrado correctamente.")
        else:
            anterior.asignarSiguiente(anterior.asignarSiguiente(None))
            return ("Último borrado correctamente.")

    def extraer(self, posicion): #Borra y devuelve el número situado en la posición de la lista ordenada indicada.
        actual = self.cabeza
        anterior = None
        contador = 0

        if (posicion > self.tamano() or posicion < 0): #Si se introduce una posición no válida.
            return ("Error, introduce una posición válida.")

        while(contador != posicion):
            anterior = actual
            actual = actual.obtenerSiguiente()
            contador += 1

        #Borramos el elemento.
        if (anterior == None): #Si el elemento a extraer es el primero de la lista.
            self.cabeza = actual.obtenerSiguiente()
        else:
            anterior.asignarSiguiente(actual.obtenerSiguiente()) #Nos "saltamos" el número actual (elemento que queremos borrar).

        return actual.obtenerDato()

    def extraerPrimero(self):
        actual = self.cabeza

        if self.tamano() == 0:
            return None
        else:
            self.cabeza = actual.obtenerSiguiente()
            return actual.obtenerDato()

    def extraerUltimo(self): #Borra y devuelve el primer número de la lista ordenada (número más grande).
        actual = self.cabeza
        anterior = None

        if self.tamano() == 0: #Si la cola está vacía.
            return ("Error, la lista está vacía.")

        while(actual.obtenerSiguiente() != None): #Obtenemos el elemento en la última posición (número mayor) y el anterior, como la lista está ordenada de menor a mayor -> último elemento = mayor elemento.
            anterior = actual
            actual = actual.obtenerSiguiente()

        #Borramos el elemento.
        if (anterior == None): #Si la lista está formada por solo 1 elemento.
            self.cabeza = actual.obtenerSiguiente()
        else:
            anterior.asignarSiguiente(anterior.asignarSiguiente(None))

        return actual.obtenerDato() #Devolvemos el valor borrado.

    def primero(self):
        if (self.tamano() != 0):
            return self.cabeza.obtenerDato()

    def ultimo(self):
        if (self.tamano() != 0):
            actual = self.cabeza

            #Recorremos la lista hasta llegar al último elemento.
            while (actual.obtenerSiguiente() != None):
                actual = actual.obtenerSiguiente()
            
            return actual.obtenerDato()

    def anterior(self,item):
        actual = self.cabeza
        anterior = None
        encontrado = False

        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                anterior=actual
                actual = actual.obtenerSiguiente()

        if encontrado == False:
            return ("El ítem introducido no esta en la lista.")
        else:
            if (anterior != None): #Si no es el primer elemento de la lista.
                return anterior.obtenerDato()
            else:
                return ("El ítem introducido no tiene elemento anterior.")

    def siguiente(self,item):
        actual = self.cabeza
        encontrado = False

        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        if encontrado == False:
            return("El ítem introducido no esta en la lista.")
        else:
            if (actual.obtenerSiguiente() != None): #Si no es el último elemento de la lista.
                return actual.obtenerSiguiente().obtenerDato()
            else:
                return ("El ítem introducido no tiene elemento siguiente.")