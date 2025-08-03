from operator import index

from sympy import re


class Conjunto:
    """ 
        Los valores del TAD son Son un tipo de contenedores asociativos en
        los que cada elemento tiene que ser único.
        El valor del elemento es inmutable, aunquees posible eliminarlo y 
        agregarlo modificado.

    """
    def __init__(self):
        
        self.elementos=[]
        
    def inserta(self,elemento):
        """ 
            requerimientos: Un conjunto y un item
            modifica: El conjunto
            efecto: Si el item no está en el conjunto añade el nuevo item
        """
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
        """ 
            requerimientos: Una conjunto 
            efecto: Devuelve el número de items que hay en el conjunto
        """
        return len(self.elementos)
    
    def pertenece(self, elemento):
        """ 
            requerimientos: Un conjunto y un item
            efecto: Si el item no está en el conjunto devuelve False, pero si está en el devuelve True
        """
        return elemento in self.elementos
    
    def elimina(self, elemento):
        """ 
            requerimientos: Un conjunto y un item
             modifica: El conjunto
            efecto: Si el item  está en el conjunto elimina ese item
        """
        if elemento in self.elementos:
           return self.elementos.pop(self.elementos.index(elemento))
    
    def union(self, otroconjunto):
        """ 
            requerimientos: Dos conjuntos
            modifica: Un conjunto nuevo
            efecto: Hace la union de los dos conjuntos, crea un comjuntos 
            nuevo q contenga todos elementos de los dos conjuntos sin que se repitan
        """
        nuevoconjunto=self
        for i in  range (len(otroconjunto.elementos)):
            if otroconjunto.elementos[i] not in nuevoconjunto.elementos:
                nuevoconjunto.inserta(otroconjunto.elementos[i])
        return nuevoconjunto
    
    def interseccion(self, otroconjunto):
        """
            requerimientos: Dos conjuntos
            modifica: Un conjunto nuevo
            efecto: Hace la intersecion de los dos conjuntos, crea un conjunto
            nuevo q contenga los  elementos que estem repetidos en los dos conjuntos 
        """
        nuevoconjunto=Conjunto()
        for i in  range (len(otroconjunto.elementos)):
            if otroconjunto.elementos[i]  in self.elementos and self.elementos[i]  in otroconjunto.elementos:
                nuevoconjunto.inserta(otroconjunto.elementos[i])
        return nuevoconjunto
    
    def diferencia(self, otroconjunto):
        """
            requerimientos: Dos conjuntos
            modifica: Un conjunto nuevo
            efecto: Hace la diferencia de los dos conjuntos, crea un conjunto
            nuevo q contenga los  elementos que están en el primer conjunto
            pero no están en el segundo 
        """
        nuevoconjunto=self
        for i in  range (len(otroconjunto.elementos)):
            if otroconjunto.elementos[i]  in self.elementos :
                nuevoconjunto.elimina(otroconjunto.elementos[i])
        return nuevoconjunto
    
    def incluye(self, otroconjunto):
        """
            requerimientos: Dos conjuntos
            modifica: Un conjunto nuevo
            efecto: Si todos los elementos de el otroconjunto estan en el 
            primer conjunto devuelve Frue, si no devuelve False
        """
        for i in  range (len(otroconjunto.elementos)):
            if otroconjunto.elementos[i] not in self.elementos :
                return False
            else:
                return True
    
    
    
    
    