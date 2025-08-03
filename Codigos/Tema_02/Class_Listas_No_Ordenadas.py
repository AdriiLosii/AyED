class ListaNoOrdenada:
    """
        Los valores del TAD Lista son listas de items del tipo tipoelem.
        Las posiciones de los items de la lista y la posición fin de la lista 
        son del tipo int.
        Las listas son mutables: agregar, insertar, anexar, borrar y modificar,
        añaden, eliminan y modifican items en la lista.
    """

    def __init__(self):
        """
            efecto: Crea y devuelve la lista vacía
        """
        self.cabeza = None

    def estaVacia(self):
        """
            requerimientos: Una lista 
            efecto: Devuelve TRUE si es lista vacía, y FALSE en caso contrario
        """
        return self.cabeza == None
    
    def agregar(self,item):
        """
            requerimientos: Una lista y un item
            modifica: La lista
            efecto: Inserta el item en la lista como primer item de la lista.

        """
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

    def tamano(self):
        """
            requerimientos: Una lista
            efecto: devuelve int como numero de items de la lista
        """
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
    
        return contador

    def buscar(self,item):
        """
            requerimientos: Una lista no vacía y el ítem a buscar
            efecto: Devuelve TRUE si esta en la lista y FALSE en caso contrario. 
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
            requerimientos: Una lista no vacía y un item
            modifica: La lista
            efecto: Elimina el item de la lista

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
    
        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())
