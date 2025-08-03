"""
Programa: Class_Conjuntos_09.py
Propósito:
    Escribe la especificación informal del TAD Conjunto. Enriquece la clase Conjunto con:
        • Un método elimina que borre del conjunto un elemento dado
        • Un método unión que devuelva el conjunto resultante de unir dos conjuntos
        • Un método intersección que devuelva un conjunto con la intersección de dos 
        conjuntos
        • Un método diferencia que devuelva un conjunto con la diferencia entre dos 
        conjuntos
        • Un método incluye que consulta si un conjunto dado está incluido en el 
        conjunto
Fecha: 16/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


class Conjunto:
    """
    Especificación informal:
        Conjunto = TAD con operaciones Conjunto, inserta,
        tamaño, pertenece, elimina, union, intersección,
        diferencia, incluye.

    Descripción:
        Los valores del TAD son conjuntos de ítems del tipo TIPOELEM.
        Las posiciones de los ítems del conjunto son del tipo int.
        Los conjuntos son mutables: inserta y elimina, añaden, eliminan
        y modifican ítems en la lista.
        Conjuntos: en los conjuntos los elementos son únicos, no se repiten.
        El valor del elemento es inmutable, aunque es posible eliminarlo y agregarlo modificado.
    """

    """
    Operaciones:
    """
    def __init__(self):
        """
            Crea un conjunto vacío.
            efecto: Devuelve un conjunto vacío.
        """
        self.elementos = []

    def __str__(self):
        """
            Muestra el conjunto
            requerimientos: Un conjunto.
            efecto: Devuelve un elemento de tipo string de como se muestra el conjunto.
        """
        cadena = '{'
        if len(self.elementos)>0:
            for elemento in self.elementos[:-1]:
                cadena = cadena + str(elemento) + ', '

            cadena = cadena + str(self.elementos[-1])

        return cadena + '}'

    def inserta(self,elemento):
        """
            Inserta el ítem dado al conjunto.
            requerimientos: Un conjunto y un ítem.
            modifica: El conjunto.
            efecto: Añade el elemento al conjunto.
        """
        if not (elemento in self.elementos):
            self.elementos.append(elemento)

    def tamano(self):
        """
            Indica el tamaño del conjunto.
            requerimientos: Un conjunto.
            efecto: Devuelve un int con el tamaño del conjunto.
        """
        return len(self.elementos)

    def pertenece(self, elemento):
        """
            Indica si el elemento dado pertenece o no al conjunto.
            requerimientos: Un conjunto y un ítem.
            efecto: Devuelve booleano: True si el ítem está en el conjunto, False si no.
        """
        return elemento in self.elementos

    def elimina(self, elemento):
        """
            Elimina del conjunto el elemento indicado.
            requerimientos: Un conjunto y un ítem.
            modifica: El conjunto.
            efecto: Si el elemento no pertenece al conjunto muestra el error,
            si pertenece, lo elimina del conjunto.
        """
        if (self.pertenece(elemento) == False):
            print("Error al intentar eliminar el elemento -> %s. Compruebe si el elemento introducido pertenece al conjunto." % elemento)
        else:
            del self.elementos[self.elementos.index(elemento)]

    def union(self, conjunto):
        """
            Crea un conjunto formado por la unión de 2 conjuntos dados.
            requerimientos: 2 conjuntos.
            efecto: Devuelve un elemento de tipo Conjunto() formado por la unión de 2 conjuntos dados.
        """
        union_conjuntos = Conjunto()

        for i in range(len(self.elementos)):
            union_conjuntos.inserta(self.elementos[i])

        for i in range(len(conjunto.elementos)):
            union_conjuntos.inserta(conjunto.elementos[i])

        return union_conjuntos

    def interseccion(self, conjunto):
        """
            Crea un conjunto formado por la intersección de 2 conjuntos dados.
            requerimientos: 2 conjuntos.
            efecto: Devuelve un elemento de tipo Conjunto() formado por la intersección de 2 conjuntos dados.
        """
        interseccion_conjuntos = Conjunto()

        for i in range(len(self.elementos)):
            for j in range(len(conjunto.elementos)):
                if (self.elementos[i] == conjunto.elementos[j]):
                    interseccion_conjuntos.inserta(self.elementos[i])
        
        return interseccion_conjuntos

    def diferencia(self, conjunto):
        """
            Crea un conjunto formado por la diferencia de 2 conjuntos dados.
            requerimientos: 2 conjuntos.
            efecto: Devuelve un elemento de tipo Conjunto() formado por la diferencia de 2 conjuntos dados.
        """
        diferencia_conjuntos = Conjunto()

        for i in range(len(self.elementos)):
            if (self.elementos[i] not in conjunto.elementos):
                diferencia_conjuntos.inserta(self.elementos[i])
        
        return diferencia_conjuntos

    def incluye(self, conjunto):
        """
            Indica si un conjunto está incluido en otro conjunto dado.
            requerimientos: 2 conjuntos.
            efecto: Devuelve un booleano: True si el conjunto está incluido en el otro, False si no.
        """
        for i in range(len(self.elementos)):
            if (self.elementos[i] not in conjunto.elementos):
                return False

        return True