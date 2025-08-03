#Colas_dobles.py
class ColaDoble:
    def __init__(self):
        self.items = []

    def __str__(self):
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena
    
    def estaVacia(self):
        return self.items == []

    def agregarFrente(self, item):
        self.items.append(item)

    def agregarFinal(self, item):
        self.items.insert(0,item)

    def borrarFrente(self):
        return self.items.pop()

    def borrarFinal(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

    def frente (self):
        return self.items[len(self.items)-1]

    def ultimo (self):
        if len(self.items)>0:
            return self.items[0]
    
    def inspeccionar(self, index):
        return self.items[index]
