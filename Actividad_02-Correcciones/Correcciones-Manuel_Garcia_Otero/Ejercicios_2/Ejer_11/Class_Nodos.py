class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None

    def obtenerAnterior(self):
        return self.anterior
    
    def asignarAnterior(self, nuevoanterior):
        self.anterior = nuevoanterior

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente
    
    def next(self):
        try:     
            return self.siguiente.obtenerDato()
        except:
            print("ERROR: el último nodo de la lista no tiene siguiente")
    
    def previous(self):
        
        return self.anterior.obtenerDato()
        
    
    


