"""
Programa: Class_Colas_04.py
Propósito: 
    Implementa como un nuevo método de la clase, la concatenación de dos colas para 
    constituir una nueva
Fecha: 14/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


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
        """
            requerimientos: Una cola.
            efecto: Devuelve una cadena de como se mostraría la cola.
        """
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '

        return cadena

    def estaVacia(self):
        """
            requerimientos: Una cola.
            efecto: Devuelve True si la cola esta vacía, False si no.
        """
        return self.items == []

    def agregar(self, item):
        """
            requerimientos: Una cola y un item.
            modifica: La cola.
            efecto: Añade el item por el extremo final de la cola.
        """
        self.items.insert(0,item)

    def avanzar(self):
        """
            requerimientos: Una cola no vacía.
            modifica: La cola.
            efecto: Suprime el primer item de la cola y devuelve su
            valor.
        """
        if (self.tamano() == 0):
            print("Error, comprueba que la cola no esté vacía.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

        return self.items.pop()

    def tamano(self):
        """
            requerimientos: Una cola.
            efecto: Devuelve int como numero de items de la cola.
        """
        return len(self.items)
    
    def frente (self):
        """
            requerimientos: Una cola no vacía.
            efecto: Devuelve el primer item de la cola.
        """
        if (self.tamano() == 0):
            print("Error, comprueba que la cola no esté vacía.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa
        else:
            return self.items[len(self.items)-1]
    
    def ultimo (self):
        """
            requerimientos: Una cola no vacía.
            efecto: Devuelve el último item de la cola.
        """
        if (self.tamano() == 0):
            print("Error, comprueba que la cola no esté vacía.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa
        if len(self.items)>0:
            return self.items[0]

    def girarCola(self):
        """
            requerimiento: Una cola no vacía.
            efecto: Devuelve la cola dada en orden opuesto.
        """
        cola_invertida = Cola()

        if (self.tamano() == 0):
            print("Error, comprueba que la cola no esté vacía.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

        for i in range(self.tamano()):
            cola_invertida.agregar(self.items[i])
        
        return cola_invertida

    def concatena(self, cola):
        """
            requerimiento: Dos colas no vacías.
            efecto: Devuelve otra cola formada dada la vuelta a partir de la concatenación de las otras dos.
        """
        cola_concatenada = Cola()

        if (cola.tamano() == 0 or self.tamano() == 0):
            print("Error al concatenar, comprueba que las colas no estén vacías.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa
        else:
            for i in range(cola.tamano()):
                cola_concatenada.agregar(cola.items[i])

            for i in range(self.tamano()):
                cola_concatenada.agregar(self.items[i])

            return cola_concatenada.girarCola()