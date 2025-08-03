"""
Programa: Class_Nodos_10.py
Propósito:
    Dada la secuencia de claves enteras 20, 10, 30, 5, 25, 12, 3, 35, 22, 11, 6, 2, y la secuencia 100, 29, 71, 82, 48,
    39, 101, 22, 46, 17, 3, 20, 25, 10, representa gráficamente los árboles AVL correspondientes e indica en qué
    momento se efectuó una rotación.
Fecha: 07/05/2022
"""


class NodoArbol:
    def __init__(self, clave, valor,izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.clave
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem

    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual
