class ArbolBinario:
    def __init__(self,objetoRaiz):
        self.clave = objetoRaiz
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.tamano = 1
        self.numeroNodos = 0
        self.numeroHojas = 0
        self.prof = 0
        self.listaProf = []

    def inorden(self, nodoActual):
        if (nodoActual != None):
            self.inorden(nodoActual.obtenerHijoIzquierdo())
            print(nodoActual.obtenerValorRaiz(), end = " ")
            self.inorden(nodoActual.obtenerHijoDerecho())

    def numNodos(self, nodoActual):
        if (nodoActual != None):
            if (nodoActual.tieneHijoIzquierdo() or nodoActual.tieneHijoDerecho()):
                self.numeroNodos += 1

            self.numNodos(nodoActual.obtenerHijoIzquierdo())
            self.numNodos(nodoActual.obtenerHijoDerecho())

        return self.numeroNodos

    def numHojas(self, nodoActual):
        if (nodoActual != None):
            if (not nodoActual.tieneHijoIzquierdo() and not nodoActual.tieneHijoDerecho()):
                self.numeroHojas += 1

            self.numHojas(nodoActual.obtenerHijoIzquierdo())
            self.numHojas(nodoActual.obtenerHijoDerecho())

        return self.numeroHojas

    def profundidad(self, nodoActual):
        if (nodoActual != None):
            if (not nodoActual.tieneHijoIzquierdo() and not nodoActual.tieneHijoDerecho()):
                self.listaProf.append(self.prof)

            self.prof += 1
            self.profundidad(nodoActual.obtenerHijoIzquierdo())
            self.prof -= 1
            self.prof += 1
            self.profundidad(nodoActual.obtenerHijoDerecho())
            self.prof -= 1

        return max(self.listaProf)

    def espejo(self, nodoActual):
        if (nodoActual != None):
            self.espejo(nodoActual.obtenerHijoIzquierdo())
            self.espejo(nodoActual.obtenerHijoDerecho())

            if (nodoActual.tieneHijoIzquierdo() or nodoActual.tieneHijoDerecho()):
                auxIzq = nodoActual.obtenerHijoIzquierdo()
                auxDer = nodoActual.obtenerHijoDerecho()
                nodoActual.hijoIzquierdo = auxDer
                nodoActual.hijoDerecho = auxIzq

        return self

    def insertarIzquierdo(self,nuevoNodo):
        self.tamano += 1
        if self.hijoIzquierdo == None:
            self.hijoIzquierdo = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.hijoIzquierdo = self.hijoIzquierdo
            self.hijoIzquierdo = t

    def insertarDerecho(self,nuevoNodo):
        self.tamano += 1
        if self.hijoDerecho == None:
            self.hijoDerecho = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.hijoDerecho = self.hijoDerecho
            self.hijoDerecho = t

    def obtenerHijoDerecho(self):
        return self.hijoDerecho

    def obtenerHijoIzquierdo(self):
        return self.hijoIzquierdo

    def asignarValorRaiz(self,obj):
        self.clave = obj

    def obtenerValorRaiz(self):
        return self.clave

    def tieneHijoIzquierdo(self):
        if (self.hijoIzquierdo == None):
            return False
        else:
            return True

    def tieneHijoDerecho(self):
        if (self.hijoDerecho == None):
            return False
        else:
            return True