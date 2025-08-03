#Colas_dobles.py
class ColaDoble:
    """ 
        Los valores del TAD son colas dobles de items del tipo TIPOELEM.
        Las colas dobles son mutables: agregar y avanzar añaden y 
        eliminan items en la cola respectivamente.

        Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """
    def __init__(self):
        """ 
           efecto: Crea una cola doble nueva que está vacía. 
        """
        self.items = []

    def __str__(self):
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena
    
    def estaVacia(self):
        """ 
            requerimientos: Una cola doble
            efecto: Devuelve True si la cola doble esta vacía, False si no.
        """
        return self.items == []

    def agregarFrente(self, item):
        """ 
            requerimientos: Una cola doble y un item
            modifica: La cola doble
            efecto: Añade el item dado al frente de la cola doble o lo que es lo mismo al final de la lista de python
        """
        self.items.append(item)

    def agregarFinal(self, item):
        """ 
            requerimientos: Una cola doble y un item
            modifica: La cola doble
            efecto: Añade el item dado al final de la cola doble o lo que es lo mismo al final de la lista de python
        """
        self.items.insert(0,item)

    def borrarFrente(self):
        """ 
            requerimientos: Una cola doble y un item
            modifica: La cola doble
            efecto: Borra y devuelve el item dado al principio de la cola doble o lo que es lo mismo al final de la lista de python
        """
        return self.items.pop()

    def borrarFinal(self):
        """ 
            requerimientos: Una cola doble y un item
            modifica: La cola doble
            efecto: Elimina y devuelve  el item dado al final de la cola doble o lo que es lo mismo al final de la lista de python
        """
        return self.items.pop(0)

    def tamano(self):
        """ 
            requerimientos: Una cola doble 
            efecto: Devuelve un numero entero que es el número de items que tiene la cola doble
        """
        return len(self.items)

    def frente (self):
        """ 
            requerimientos: Una cola doble 
            efecto: Devuelve el primer elemento de la cola doble
        """
        return self.items[len(self.items)-1]

    def ultimo (self):
        """ 
            requerimientos: Una cola doble 
            efecto: Devuelve el ultimo elemento  elemento de la cola doble
        """
        if len(self.items)>0:
            return self.items[0]
    
    def inspeccionar(self, index):
        """ 
            requerimientos: Una cola doble 
            efecto:Devuelve el ítem de la posición index de la cola pero no lo elimina.
        """
        return self.items[index]
