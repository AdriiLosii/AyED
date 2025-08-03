"""
Programa: Class_Listas_No_Ordenadas_14.py
Propósito: 
    Para implementar el método tamano contamos el número de nodos en la lista. Una 
    estrategia alternativa sería almacenar el número de nodos en la lista como una pieza 
    de datos adicional en la cabeza de la lista. Modifica la clase ListaNoOrdenada para 
    incluir esta información y reescribe el método tamano. ¿Qué complejidad tiene el 
    método tamano ahora?
Fecha: 18/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


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
            efecto: Crea la lista vacía
        """
        self.cabeza = None
        self.tamano = 0 #Definimos la nueva variable de la lista.

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
        self.tamano += 1

    def tamano_orden_N(self):
        """
            requerimientos: Una lista.
            efecto: devuelve int del numero de items de la lista.
        """
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
    
        return contador

    def tamano_orden_1(self):
        """
            requerimientos: Una lista.
            efecto: devuelve int del número de items de la lista.
        """
        return self.tamano

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
            self.tamano -= 1
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())
            self.tamano -= 1


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