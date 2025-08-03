class TablaHash:

    def __init__(self):

        
        self.tamano = 11
        self.slots = [None] * (self.tamano)
        self.datos = [None] * (self.tamano)

            
    def agregar(self, clave, dato):
        n=0
        for elemento in self.slots:
            if elemento==None:
                n=n+1
        if n<2:
            self.slots.append(None)
            self.datos.append(None)
    
        valorHash = self.funcionHash(clave, len(self.slots))
        
        if self.slots[valorHash] == None:
            self.slots[valorHash] = clave
            self.datos[valorHash] = dato
        else:
            if self.slots[valorHash] == clave:
                self.datos[valorHash] = dato  
                
            else:
                proximaSlot = self.rehash(valorHash, len(self.slots))
                while self.slots[proximaSlot] != None and self.slots[proximaSlot] != clave:
                    proximaSlot = self.rehash(proximaSlot, len(self.slots))

                if self.slots[proximaSlot] == None:
            
                    self.slots[proximaSlot] = clave
                    self.datos[proximaSlot] = dato

                    
                else:
                    self.datos[proximaSlot] = dato 


    def funcionHash(self, clave, tamano):
        return clave % tamano

    def rehash(self, hashViejo, tamano):
        return (hashViejo+1) % tamano

    def obtener_2(self, clave):
        slotInicio = self.funcionHash(clave, len(self.slots))

        dato = None
        parar = False
        encontrado = False
        posicion = slotInicio
        n=0
        while self.slots[posicion] != None and not encontrado and not parar:
            n=n+1
            if self.slots[posicion] == clave:
                encontrado = True
                dato = self.datos[posicion]
                
            else:
                
                posicion = self.rehash(posicion, len(self.slots))
                if posicion == slotInicio:
                    parar = True
            
        return print("El dato encontrado en la tabla hash es",dato,"y para encontrarlo repite las comparaciones en total: ",n,"veces")

    def obtener_1(self, clave):
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
        return self.obtener_1(clave)

    def __setitem__(self, clave, dato):
        self.agregar(clave, dato)
    
    def __len__(self,):
        return len(self.slots)

    def Remove(self,clave):
        slotInicio = self.funcionHash(clave, len(self.slots))

        parar = False
        encontrado = False
        posicion = slotInicio
    
        while self.slots[posicion] != None and not encontrado and not parar:
            
            if self.slots[posicion] == clave:
                encontrado = True
                self.datos[posicion]=None
                self.slots[posicion]=None
                
            else:
                
                posicion = self.rehash(posicion, len(self.slots))
                if posicion == slotInicio:
                    parar = True
