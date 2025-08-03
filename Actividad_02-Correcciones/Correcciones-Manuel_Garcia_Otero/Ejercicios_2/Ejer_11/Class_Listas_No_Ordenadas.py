from Class_Nodos import *

#Métodos: anexar, insertar, modificar, indice, extraer (2 sobrecargas), fin, primero, siguiente, anterior


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

    def __str__(self):

        cadena = "[ "
        actual = self.cabeza

        for i in range (self.tamano()):
            cadena = cadena + str(actual.obtenerDato()) + " "
            actual = actual.obtenerSiguiente()
        
        cadena+="]"

        return str(cadena)

    def primero(self):
        try:
            return self.cabeza
        except:
            print("ERROR: la lista está vacía")

    def ultimo(self):
        try:
            actual = self.cabeza
            for i in range (self.tamano()-1):
                actual = actual.obtenerSiguiente()
            return actual
        except:
            print("ERROR: la lista está vacía")

    def extraer(self, pos):

        try:
            
            if (pos<0):
                raise IndexError


            if (pos==0):
                temp = self.cabeza
                self.cabeza = temp.obtenerSiguiente()
                return temp

            else:
                actual = self.cabeza
                siguiente = actual.obtenerSiguiente()
                

                for i in range (pos-1):
                    actual = actual.obtenerSiguiente()
                    siguiente = siguiente.obtenerSiguiente()
                
                temp = siguiente.obtenerSiguiente()
                siguiente.asignarSiguiente(None)
                actual.asignarSiguiente(temp)
                if (temp!=None):
                    temp.asignarAnterior(actual)
                return siguiente

        except:
            print("ERROR: el índice está fuera de límites")

    def indice(self, valor):

        try:
           contador=0
           actual = self.cabeza

           while (actual.obtenerDato() != valor):
            actual = actual.obtenerSiguiente()
            contador+=1
            
           return contador

        except:
            print("ERROR: el elemento no se encuentra en la lista")


    def modificar(self, pos, valor):

        try:
            
            if (pos<0):
                raise IndexError
            
            actual = self.cabeza

            for i in range (pos):
                actual = actual.obtenerSiguiente()
            
            actual.asignarDato(valor)

        except:
            print("ERROR: el índice está fuera de límites")


    def insertar(self, pos, item):

        try:
            
            if (pos<0):
                raise IndexError

            nuevo = Nodo(item)

            if (pos==0):
                nuevo.asignarSiguiente(self.cabeza)
                nuevo.asignarAnterior(self.cabeza)
                self.cabeza = nuevo

            else:

                actual = self.cabeza
                siguiente = actual.obtenerSiguiente()
                

                for i in range (pos-1):
                    actual = actual.obtenerSiguiente()
                    siguiente = siguiente.obtenerSiguiente()
                
                actual.asignarSiguiente(nuevo)
                nuevo.asignarAnterior(actual)
                nuevo.asignarSiguiente(siguiente)
                siguiente.asignarAnterior(nuevo)

        except:
            print("ERROR: el índice está fuera de límites")

    def anexar(self, item):

        actual = self.cabeza
        nuevo = Nodo(item)
        while (actual.obtenerSiguiente() != None):
            actual = actual.obtenerSiguiente()
        
        actual.asignarSiguiente(nuevo)
        nuevo.asignarAnterior(actual)

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
        if (self.cabeza!=None):
            self.cabeza.asignarAnterior(temp)
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
            self.cabeza.asignarAnterior(None)
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())
            if (actual.obtenerSiguiente()!=None):
                actual.obtenerSiguiente().asignarAnterior(previo)
