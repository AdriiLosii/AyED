"""
Programa: Class_Listas_No_Ordenadas_11.py
Propósito: 
    Implementar el método anexar una nueva lista para ListaNoOrdenada. ¿Cuál es la
    complejidad de tiempo del método que creaste?
Fecha: 17/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


class ListaNoOrdenada:

    def __init__(self):
        """
            efecto: Crea una lista vacía.
        """
        self.cabeza = None

    def __str__(self):
        """
            requerimientos: Una lista.
            efecto: Devuelve un string de como se muestra la lista.
        """
        actual = self.cabeza
        cadena = []

        while(actual != None):
            if (actual.obtenerSiguiente() != None):
                cadena.append(str(actual.obtenerDato()))
                cadena.append("->")
                actual = actual.obtenerSiguiente()

            else:
                cadena.append(str(actual.obtenerDato()))
                actual = actual.obtenerSiguiente()

        
        cadena=" ".join(cadena)

        return str(cadena)

    def estaVacia(self):
        """
            requerimientos: Una lista.
            efecto: Devuelve un booleano: True si está vacía, False si no.
        """
        return self.cabeza == None
    
    def agregar(self,item):
        """
            requerimientos: Una lista y un ítem.
            modifica: La lista.
            efecto: Agrega el ítem dado a la lista.
        """
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

    def tamano(self):
        """
            requerimientos: Una lista.
            efecto: Devuelve un int con el tamaño de la lista.
        """
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
    
        return contador

    def buscar(self,item):
        """
            requerimientos: Una lista y un ítem.
            efecto: Devuelve un booleano: True si el elemento pertenece a la lista, False si no.
        """
        actual = self.cabeza
        encontrado = False  
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
    
        return encontrado

    def borrar(self,item):
        """
            requerimientos: Una lista y un ítem.
            modifica: La lista.
            efecto: Borra el ítem dado de la lista.
        """
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
    
        if (encontrado == False):
            return ("Error al borrar, no ha sido posible encontrar",item)

        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
            return ("Elemento borrado correctamente.")
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())
            return ("Elemento borrado correctamente.")


    def final(self):
        """
            requerimientos: Una lista.
            efecto: Devuelve el elemento del final de la lista.
        """
        actual=self.cabeza
    
        while actual.obtenerSiguiente() != None:

            actual=actual.obtenerSiguiente()

        return actual.obtenerDato()

    def principio(self):
        """
            requerimientos: Una lista.
            efecto: Devuelve el elemento del principio de la lista.
        """
        return self.cabeza.obtenerDato()

    def anterior(self,item):
        """
            requerimientos: Una lista y un ítem.
            efecto: Devuelve el elemento anterior al ítem dado.
        """
        actual = self.cabeza
        anterior= None
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
        """
            requerimientos: Una lista y un ítem.
            efecto: Devuelve el elemento siguiente al ítem dado.
        """
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

            
class Nodo:

    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente