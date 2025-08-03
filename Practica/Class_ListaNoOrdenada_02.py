class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def obtenerAnterior(self):
        return self.anterior

    def asignarDato(self, nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self, nuevoSiguiente):
        self.siguiente = nuevoSiguiente

    def asignarAnterior(self, nuevoAnterior):
        self.anterior = nuevoAnterior


class ListaDoblementeEnlazada:
    """
    Especificación informal:
        ListaDoblementeEnlazada = TAD con operaciones estaVacia, agregar,
        len, buscar y borrar.

    Descripción:
        Los valores del TAD son listas no ordenada de ítems del tipo TIPOELEM.
        Las listas doblemente enlazadas con mutables: agregar y borrar modifican la lista.
    """

    """
    Operaciones:
    """
    def __init__(self):
        """
            Crea una lista vacía.
            efecto: Crea una lista vacía.
        """
        self.cabeza = None
        self.tamano = 0

    def __str__(self):
        """
            Muestra la lista.
            requerimientos: Una lista.
            efecto: Devuelve la cadena de como se muestra la lista.
        """
        actual = self.cabeza
        cadena = ''

        while(actual != None):
            if (actual.obtenerSiguiente() != None):
                cadena = cadena + str(actual.obtenerDato()) + " <-> "
                actual = actual.obtenerSiguiente()

            else:
                cadena = cadena + str(actual.obtenerDato())
                actual = actual.obtenerSiguiente()

        return cadena

    def estaVacia(self):
        """
            Indica si la lista está vacía o no.
            requerimientos: Una lista.
            efecto: Devuelve un booleano: True si la lista está vacía, False si no.
        """
        return self.cabeza == None
    
    def agregar(self,item):
        """
            Añade el ítem dado a la lista.
            requerimientos: Una lista y un ítem.
            modifica: La lista doblemente enlazada.
            efecto: Agrega el ítem dado a la lista.
        """
        if (len(self) == 0):
            temp = Nodo(item)
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp = Nodo(item)
            temp.asignarSiguiente(self.cabeza)
            self.cabeza.asignarAnterior(temp)
            self.cabeza = temp

        self.tamano += 1

    def __len__(self):
        """
            Indica el tamaño de la lista.
            requerimientos: Una lista.
            efecto: Devuelve un entero con la cantidad de ítems en la lista.
        """
        return self.tamano

    def buscar(self,item):
        """
            Busca un ítem dado en la lista.
            requerimientos: Una lista y un ítem.
            efecto: Devuelve un booleano: True si el ítem dado se encuentra en la lista, False si no.
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
            Borra el ítem dado en la lista (si se encuentra en ella).
            requerimientos: Una lista y un ítem.
            modifica: La lista doblemente enlazada.
            efecto: Borra el ítem dado en la lista si se encuentra, si no se encuentra, imprime el error en pantalla.
        """
        actual = self.cabeza
        previo = None
        encontrado = False
        try:
            while not encontrado:
                if actual.obtenerDato() == item:
                    encontrado = True
                else:
                    previo = actual
                    actual = actual.obtenerSiguiente()

            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())
        except AttributeError:
            print("Error, no ha sido posible encontrar en la lista el ítem:",item)