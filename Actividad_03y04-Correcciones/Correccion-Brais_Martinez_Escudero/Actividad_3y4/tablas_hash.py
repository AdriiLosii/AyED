class TablaHash:
    def __init__(self):
        self.tamano = 11
        self.ocupados=0
        self.slots = [None] * self.tamano
        self.datos = [None] * self.tamano

    def agregar(self, clave, dato):
        
        
        valorHash = self.funcionHash(clave, len(self.slots))

        if self.slots[valorHash] == None:
            self.slots[valorHash] = clave
            self.datos[valorHash] = dato
        else:
            if self.slots[valorHash] == clave:
                self.datos[valorHash] = dato  # reemplazo
            else:
                proximaSlot = self.rehash(valorHash, len(self.slots))
                while self.slots[proximaSlot] != None and self.slots[proximaSlot] != clave:
                    proximaSlot = self.rehash(proximaSlot, len(self.slots))

                if self.slots[proximaSlot] == None:
                    self.slots[proximaSlot] = clave
                    self.datos[proximaSlot] = dato
                else:
                    self.datos[proximaSlot] = dato  # reemplazo
                    
        self.ocupados+=1

    def funcionHash(self, clave, tamano):
        return clave % tamano

    def rehash(self, hashViejo, tamano):
        return (hashViejo+1) % tamano

    def obtener(self, clave):
        slotInicio = self.funcionHash(clave, len(self.slots))

        dato = None
        parar = False
        encontrado = False
        posicion = slotInicio
        while self.slots[posicion] != None and not encontrado and not parar:
            if self.slots[posicion] == clave:
                encontrado = True
                dato = self.datos[posicion]
            else:
                posicion = self.rehash(posicion, len(self.slots))
                if posicion == slotInicio:
                    parar = True
        return dato

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, dato):
        self.agregar(clave, dato)

    def len(self):
        return self.ocupados
