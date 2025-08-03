class Pila:
    """ 
    Representa una pila con operaciones de apilar, desapilar y 
    verificar si está vacía.
    """
    def __init__(self):
         """ Crea una pila vacía. """
         # La pila vacía se representa con una lista vacía
         self.items = []

    def __str__(self):
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena

    def estaVacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

    def incluir(self, item):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(item)

    def extraer(self):
        """ Devuelve el elemento tope y lo elimina de la pila. """
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items)-1]

    def tamano(self):
        return len(self.items)

class Cola:
    """ Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """

    
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.items = []

    def __str__(self):
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena
    
    def estaVacia(self):
        """ Devuelve True si la cola esta vacía, False si no."""
        return self.items == []

    def agregar(self, item):
        """ Agrega el elemento x como último de la cola. """
        self.items.insert(0,item)

    def avanzar(self):
        """ Elimina el primer elemento de la cola y devuelve su
        valor. 
        """
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def frente (self):
        return self.items[len(self.items)-1]

    def ultimo (self):
        if len(self.items)>0:
            return self.items[0]


class ColaPrioridad:
    def __init__(self):
        self.cola=[]

    def añade(self,elemento):
        self.cola.append(elemento)

    def primero(self):
        if len(self.cola)==0:
            return None
        maximo=self.cola[0]
        for elemento in self.cola:
            if elemento>maximo:
                maximo=elemento
        return maximo

    def extrae(self):
        if len(self.cola)==0:
            return None
        indice=0
        for i in range(len(self.cola)):
            if self.cola[i]>self.cola[indice]:
                indice=i
        aux=self.cola[indice]
        del self.cola[indice]
        return aux
    
    def tamaño(self):
        return len(self.cola)

    def esta_Vacia(self):
        return len(self.cola)==0

class ColaDoble:
    def __init__(self):
        self.items = []

    def __str__(self):
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena
    
    def estaVacia(self):
        return self.items == []

    def agregarFrente(self, item):
        self.items.append(item)

    def agregarFinal(self, item):
        self.items.insert(0,item)

    def borrarFrente(self):
        return self.items.pop()

    def borrarFinal(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

class Conjunto:
    def __init__(self):
        self.elementos=[]
    def inserta(self,elemento):
        if not (elemento in self.elementos):
            self.elementos.append(elemento)
    def __str__(self):
        cadena='{'
        if len(self.elementos)>0:
            for elemento in self.elementos[:-1]:
                cadena=cadena+str(elemento)+', '
            cadena=cadena+str(self.elementos[-1])
        return cadena+'}'
    def tamaño(self):
        return len(self.elementos)
    def pertenece(self, elemento):
        return elemento in self.elementos
    
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

class ListaNoOrdenada:

    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None
    
    def agregar(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

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
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
    
        return encontrado

    def borrar(self,item):
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

class ListaOrdenada:
    def __init__(self):
        self.cabeza = None

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

    def agregar(self,item):
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

    def estaVacia(self):
        return self.cabeza == None

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador