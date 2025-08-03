class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class ListaNoOrdenada:
    
    def __init__(self):
        self.cabeza = None
        self.cont=0
        self.list=[]

    def estaVacia(self):
        return self.cabeza == None
    
    def agregar(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
        if self.cabeza not in self.list:
            self.cont=self.cont+1
            list.append(self.cabeza)
        
    def tamano(self):
        return self.cont
    
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
    
        return encontrado

    def borrar(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())
    
    def anexar(self,item):
        actual = self.cabeza
        while actual.obtenerSiguiente() != None:
            actual = actual.obtenerSiguiente()
            
        else:
            temp=Nodo(item)
            actual.asignarSiguiente(temp)
    
    def anexarlista(self,lista):
        actual = self.cabeza
        while actual.obtenerSiguiente() != None:
            actual = actual.obtenerSiguiente()
        actual.asignarSiguiente(lista.cabeza)
        while actual.obtenerSiguiente() != None:
               actual = actual.obtenerSiguiente()

    def insertar(self,pos,item):
        actual = self.cabeza
        contador = 0
        while contador != pos:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        else:
            temp = Nodo(item)
            temp.asignarSiguiente(actual.obtenerSiguiente())
            actual.asignarSiguiente(temp)
    
        return contador
        
    def indice(self,item):
        actual = self.cabeza
        encontrado=None
        contador=0
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                contador=contador+1
                actual = actual.obtenerSiguiente()
        return contador
    
    def extaerelemento(self,item):
        actual = self.cabeza
        previo=None
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
                previo.asignarSiguiente(actual.obtenerSiguiente())
            else:
                previo=actual
                actual = actual.obtenerSiguiente()
    
    def extaerposicion(self,pos):
        actual = self.cabeza
        previo=None
        contador=0
        while contador != pos:
            contador=contador+1
            previo=actual
            actual = actual.obtenerSiguiente()
        previo.asignarSiguiente(actual.obtenerSiguiente())
    
    def modificar(self,pos,item):
        actual = self.cabeza
        contador=0
        while contador != pos:
            contador=contador+1
            actual = actual.obtenerSiguiente()
        actual.asignarDato(item) 
    
    def fin(self):
        actual = self.cabeza
        while actual.obtenerSiguiente() != None:
            actual = actual.obtenerSiguiente()
        else:
            return actual.obtenerDato()
   
    def primero(self):
        actual=self.cabeza
        return actual.obtenerDato()
    
    
    def siguiente(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
                siguiente=actual.obtenerSiguiente()
            else:
                actual = actual.obtenerSiguiente()
    
        return siguiente.obtenerDato()
    
    def anterior(self,item):
        anterior = self.cabeza
        actual=anterior.obtenerSiguiente()
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
                anterior=anterior.obtenerSiguiente()
        return anterior.obtenerDato()
        