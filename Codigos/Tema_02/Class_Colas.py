class Cola:
    """ 
        Los valores del TAD son colas de items del tipo TIPOELEM.
        Las colas son mutables: agregar y avanzar añaden y 
        eliminan items en la cola respectivamente.

        Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """
    
    def __init__(self):
        """ 
            efecto: Crea una cola vacía. 
        """
        # La cola vacía se representa por una lista vacía
        self.items = []

    def __str__(self):
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena

    def estaVacia(self):
        """ 
            requerimientos: Una cola
            efecto: Devuelve True si la cola esta vacía, False si no.
        """
        return self.items == []

    def agregar(self, item):
        """ 
            requerimientos: Una cola y un item
            modifica: La cola
            efecto: Añade el item por el extremo final de la cola
        """
        self.items.insert(0,item)

    def avanzar(self):
        """ 
            requerimientos: Una cola no vacía
            modifica: La cola
            efecto: Suprime el primer item de la cola y devuelve su
            valor.
        """
        return self.items.pop()

    def tamano(self):
        """
            requerimientos: Una cola
            efecto: devuelve int como numero de items de la cola
        """
        return len(self.items)
    
    def frente (self):
        """
            requerimientos: Una cola no vacía
            efecto: Devuelve el primer item de la cola
        """
        return self.items[len(self.items)-1]
    
    def ultimo (self):
        """
            requerimientos: Una cola no vacía
            efecto: Devuelve el último item de la cola
        """
        if len(self.items)>0:
            return self.items[0]