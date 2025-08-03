"""
Programa: Class_Colas_dobles_07.py
Propósito: 
    Realiza la especificación informal del TAD Cola Doble
Fecha: 15/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


class ColaDoble:
    """
    Especificación informal:
        ColaDoble = TAD con operaciones ColaDoble, estaVacia,
        agregarFrente, agregarFinal, borrarFrente, borrarFinal,
        tamano, frente, ultimo, inspeccionar.

    Descripción:
        Los valores del TAD son colas de items del tipo TIPOELEM.
        Las colas dobles son mutables: agregar(frente y final) y 
        borrar(frente y final), añaden y eliminan ítems (al inicio
        o al final) respectivamente.
        Colas dobles: se pueden añadir y eliminar elementos al inicio
        y al final de la cola doble.

        Representa a una cola doble, con operaciones de encolar y desencolar.
    """

    """
    Operaciones:
    """
    def __init__(self):
        """
            Crea una cola vacía.
            efecto: Devuelve una cola vacía.
        """
        self.items = []

    def __str__(self):
        """
            Muestra la cola doble.
            efecto: Devuelve una cadena de como se muestra la cola doble.
        """
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '

        return cadena
    
    def estaVacia(self):
        """
            Indica a través de una variable booleana si la lista está
            vacía o no.
            requerimientos: Una cola doble.
            efecto: Devuelve booleano: True si la cola doble está vacía, False si no.
        """
        return self.items == []

    def agregarFrente(self, item):
        """
            Añade el ítem dado al inicio de la cola doble.
            requerimientos: Una cola doble y un ítem.
            modifica: La cola doble.
            efecto: Añade el ítem (tipoelem) al inicio de la cola doble.
        """
        self.items.append(item)

    def agregarFinal(self, item):
        """
            Añade el ítem dado al final de la cola doble.
            requerimientos: Una cola doble y un ítem.
            modifica: La cola doble.
            efecto: Añade el ítem (tipoelem) al final de la cola doble.
        """
        self.items.insert(0,item)

    def borrarFrente(self):
        """
            Borra el elemento al inicio de la cola doble.
            requerimientos: Una cola doble.
            modifica: La cola doble.
            efecto: Elimina el primer ítem de la cola doble, si la cola doble está vacía devuelve None.
        """
        if (self.tamano() != 0):
            return self.items.pop()
        else:
            return None

    def borrarFinal(self):
        """
            Borra el elemento al final de la cola doble.
            requerimientos: Una cola doble.
            modifica: La cola doble.
            efecto: Elimina el último ítem de la cola doble, si la cola doble está vacía devuelve None.
        """
        if (self.tamano() != 0):
            return self.items.pop(0)
        else:
            return None

    def tamano(self):
        """
            Devuelve el tamaño de la cola doble.
            requerimientos: Una cola doble.
            efecto: Devuelve un int con el tamaño de la cola.
        """
        return len(self.items)

    def frente (self):
        """
            Devuelve el ítem al inicio de la cola doble.
            requerimientos: Una cola.
            efecto: Devuelve el ítem (tipoelem) en la posición incial de la cola doble.
        """
        return self.items[len(self.items)-1]

    def ultimo (self):
        """
            Devuelve el ítem al final de la cola doble.
            requerimientos: Una cola doble.
            efecto: Devuelve el ítem (tipoelem) en la posición final de la cola doble.
        """
        if len(self.items)>0:
            return self.items[0]
    
    def inspeccionar(self, index):
        """
            Devuelve el ítem situado en la posición indicada de la cola doble.
            requerimientos: Una cola doble y un número (posición).
            efecto: Devuelve el ítem (tipoelem) situado en la posición indicada de la cola doble.
        """
        return self.items[index]
