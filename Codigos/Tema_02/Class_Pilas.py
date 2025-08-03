class Pila:
    """ 
        Los valores del TAD pila son pilas de elementos del tipo tipoelem.
        Las pilas son mutables: incluir y extraer, añaden y 
        eliminan elementos de la pila, respectivamente.

        Representa una pila con operaciones de incluir (apilar), 
        extraer (desapilar) y verificar si está vacía.
    """
    def __init__(self):
         """ 
         Crea una pila vacía. 
            efecto: devuelve la pila vacía.
         """
         # La pila vacía se representa con una lista vacía
         self.items = []

    def __str__(self):
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena
    
    def estaVacia(self):
        """ 
            requerimientos: Una pila
            efecto: Devuelve True si es la pila vacía, y False en caso contrario.
        """
        return self.items == []

    def incluir(self, item):
        """ 
            requerimientos: La pila
            modifica: La pila
            efecto: Añade el item a la pila, quedando éste situado en el tope.
        """
        # Apilar es agregar al final de la lista.
        self.items.append(item)

    def extraer(self):
        """ Devuelve el elemento tope y lo elimina de la pila. 
            requerimientos: La pila es no vacía.
            modifica: La pila
            efecto: Suprime el item situado en el tope de la pila.
        """
        return self.items.pop()

    def inspeccionar(self):
        """
            requerimientos: La pila es no vacía.
            efecto: Devuelve el item situado en el tope de la pila.
        """
        return self.items[len(self.items)-1]

    def tamano(self):
        """
            requerimientos: La pila
            efecto: devuelve int como numero de items de la pila.
        """
        return len(self.items)
