from Class_Nodos import NodoArbol


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()

    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano = self.tamano + 1

    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol( clave, valor, padre=nodoActual)

    def __setitem__(self, c, v):
        self.agregar(c, v)

    def obtener(self, clave):
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def __getitem__(self, clave):
        res = self.obtener(clave)
        if res:
            return res
        else:
            raise KeyError('Error, la clave no esta en el arbol')

    def __contains__(self, clave):
        if self._obtener(clave, self.raiz):
            return True
        else:
            return False

    def eliminar(self, clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self, clave):
        self.eliminar(clave)

    def remover(self, nodoActual):
        if nodoActual.esHoja():  # hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos():  # interior
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil

        else:  # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, 
                                                    nodoActual.hijoIzquierdo.cargaUtil,
                                                    nodoActual.hijoIzquierdo.hijoIzquierdo, 
                                                    nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, 
                                                    nodoActual.hijoDerecho.cargaUtil,
                                                    nodoActual.hijoDerecho.hijoIzquierdo, 
                                                    nodoActual.hijoDerecho.hijoDerecho)

