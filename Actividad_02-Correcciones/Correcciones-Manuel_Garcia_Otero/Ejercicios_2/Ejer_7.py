"""Realiza la especificación informal del TAD Cola Doble"""


class ColaDoble:            #inicializa la clase cola doble con una lista vacia
    def __init__(self):         
        self.items = []

    def __str__(self):      #declara el formato que se utilizara para imprimirla por pantalla
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena
    
    def estaVacia(self):        #devuelve si esta vacia o no en un valor booliano
        return self.items == []

    def agregarFrente(self, item):      #inserta un elemento dado al principio de la lista
        self.items.append(item)

    def agregarFinal(self, item):       #inserta un elemento dado al final de la cola
        self.items.insert(0,item)

    def borrarFrente(self):         #borra el primer elemento de la cola
        return self.items.pop()

    def borrarFinal(self):         #borra el ultimo elemento de la cola
        return self.items.pop(0)

    def tamano(self):       #devuelve la longitud de la cola
        return len(self.items)
    
    def frente (self):      #devuleve el elmento al frente de la cola
        return self.items[len(self.items)-1]

    def ultimo (self):      #devuleve el elmento al final de la cola
        if len(self.items)>0:
            return self.items[0]
    
    def inspeccionar(self, index):          #devuelve el elemento que este en la posicion designada
        return self.items[index]
