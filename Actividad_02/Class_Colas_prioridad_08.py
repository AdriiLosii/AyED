"""
Programa: Class_Colas_prioridad_08.py
Propósito: 
    Implementar el TAD Colas de Prioridad, usando listas enlazadas ordenadas
Fecha: 15/03/2022
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


class ColaPrioridad:
    def __init__(self): #Constructor
        """
            efecto: Crea una cola de prioridad vacía.
        """
        self.cabezaCola = None

    def __str__(self): #Salida (print)
        actual = self.cabezaCola
        cadena = ''

        while(actual != None):
            if (actual.obtenerSiguiente() != None): #Si no es el último nodo
                cadena = cadena + str(actual.obtenerDato()) + " -> "
                actual = actual.obtenerSiguiente()

            else: #Si es el último nodo.
                cadena = cadena + str(actual.obtenerDato())
                actual = actual.obtenerSiguiente()

        return cadena

    def agregar(self,elemento):
        """
            requerimientos: Una cola y un elemento.
            modifica: La cola.
            efecto: Añade el elemento dado a la cola de prioridad, ordenándolos de menor a mayor.
        """
        actual = self.cabezaCola
        previo = None
        detenerse = False

        try: #Validación de datos.
            while actual != None and not detenerse:
                if actual.obtenerDato() > elemento:
                    detenerse = True
                else:
                    previo = actual
                    actual = actual.obtenerSiguiente()

            temp = Nodo(elemento)
            if previo == None:
                temp.asignarSiguiente(self.cabezaCola)
                self.cabezaCola = temp
            else:
                temp.asignarSiguiente(actual)
                previo.asignarSiguiente(temp)

        except TypeError: #Si se introduce otra cosa distinta a números.
            print("\nError, revise el tipo de datos introducidos para crear la cola.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    def primero(self):
        """
            Devuelve el primero de la cola.
            requerimientos: Una cola no vacía.
            efecto: Devuelve el primer elemento de la cola de prioridad (el número más grande).
        """
        if (self.cabezaCola == None):
            return None

        actual = self.cabezaCola
        maximo = self.cabezaCola.obtenerDato()

        for i in range(self.tamano()):
            if (actual.obtenerDato() >= maximo):
                maximo = actual.obtenerDato()
                actual = actual.obtenerSiguiente()

        return maximo

    def avanzar(self):
        """
            Extrae de la cola el primero (número más grande)
            requerimientos: Una cola no vacía.
            modifica: La cola de prioridad.
            efecto: Elimina el elemento más grande de la lista y lo devuelve.
        """
        actual = self.cabezaCola
        anterior = None

        if self.tamano() == 0: #Si la cola está vacía.
            return None

        while(actual.obtenerSiguiente() != None): #Obtenemos el elemento en la última posición (número mayor) y el anterior, como la lista está ordenada de menor a mayor -> último elemento = mayor elemento.
            anterior = actual
            actual = actual.obtenerSiguiente()

        #Borramos el elemento.
        if (anterior == None): #Si la lista está formada por solo 1 elemento.
            self.cabezaCola = actual.obtenerSiguiente()
        else:
            anterior.asignarSiguiente(anterior.asignarSiguiente(None))

        return actual.obtenerDato() #Devolvemos el valor borrado.

    def tamano(self):
        """
            Devuelve el tamaño de la cola.
            requerimientos: Una cola de prioridad.
            efecto: Devuelve un int con el tamaño de la cola de prioridad.
        """
        actual = self.cabezaCola
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador

    def esta_Vacia(self):
        """
            Devuelve true/false dependiendo de si la lista está vacía/no vacía.
            requerimientos: Una cola de prioridad.
            efecto: Devuelve un booleano: True si está vacía, false si no.
        """
        return self.cabezaCola == None