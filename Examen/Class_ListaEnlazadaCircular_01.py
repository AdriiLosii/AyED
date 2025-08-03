class ListaCircular:
    """
        Los valores del TAD Lista enlazada circular son listas de items del tipo listas.
        las posiciones de los items de la lista y la posicion fin de la lista son del tipo Nodo().
        Ls listas son mutables: agregar modifican los items de la lista.
    """

    def __init__(self, datoInicio):
        """
            efecto: Crea la lista circular en la que el elemento inicial apunta a la cabeza de la lista (a si mismo en este paso).
        """
        self.nodoUltimo = Nodo(datoInicio)
        self.cabeza = self.nodoUltimo
        self.nodoUltimo.asignarSiguiente(self.cabeza)
        self.tamano = 0

    def __str__(self):
        """
            requerimientos: Una lista.
            efecto: Muestra la lista circular.
        """
        actual = self.cabeza
        cadena = ''

        while(True):
            print(str(actual.obtenerDato()), end = " -> ")
            actual = actual.obtenerSiguiente()

        return cadena

    def estaVacia(self):
        """
            requerimientos: Una lista.
            efecto: Devuelve TRUE si es lista vacía, y FALSE en caso contrario
        """
        return self.cabeza == None

    def agregar(self,item):
        """
            requerimientos: Una lista y un item.
            modifica: La lista
            efecto: Agrega el item dado a la lista, posteriormente le indicamos al "último" nodo que apunte a la cabecera, que en este caso será el nuevo item de la lista.
        """
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
        self.tamano += 1

        self.nodoUltimo.asignarSiguiente(self.cabeza)

    def Coger_pieza(self, accion, pos):
        """
            requerimientos: Una lista, una accion y una posición.
            efecto: Muestra la acción a realizar y devuelve la posición final.
        """
        actual = self.cabeza
        while(True):
            if(pos == actual.obtenerDato()):
                print("Acción:",accion,pos)
                break
            else:
                actual = actual.obtenerSiguiente()

    def Dejar_pieza(self, accion, pos):
        """
            requerimientos: Una lista, una accion y una posición.
            efecto: Muestra la acción a realizar y devuelve la posición final.
        """
        actual = self.cabeza
        while(True):
            if(pos == actual.obtenerDato()):
                print("Acción:",accion,pos)
                break
            else:
                actual = actual.obtenerSiguiente()

    def Go_to(self, accion, pos):
        """
            requerimientos: Una lista, una accion y una posición.
            efecto: Muestra la acción a realizar y devuelve la posición final.
        """
        actual = self.cabeza
        while(True):
            if(pos == actual.obtenerDato()):
                print("Acción:",accion,pos)
                break
            else:
                actual = actual.obtenerSiguiente()

    def tamano_orden_1(self):
        """
            requerimientos: Una lista.
            efecto: Devuelve int del número de items de la lista.
        """
        return self.tamano


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente