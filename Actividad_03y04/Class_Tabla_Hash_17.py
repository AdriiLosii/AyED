"""
Programa: Class_Tabla_Hash_17.py
Propósito:
    En la implementación de Vector Asociativo de las tablas hash, se eligió que el tamaño 
    de la tabla hash fuera 11. Si la tabla se llena, ésta debe agrandarse. Implementa el 
    método agregar para que la tabla se redimensione automáticamente cuando el factor 
    de carga alcance un valor predeterminado (puedes decidir el valor con base en su 
    apreciación de la carga en función del desempeño).
Fecha: 20/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


class TablaHash:
    def __init__(self):
        self.tamano_total = 11
        self.slots = [None] * self.tamano_total
        self.datos = [None] * self.tamano_total
        self.tam = 0
        self.maxima_carga = 0.65 #Valor máximo del factor de carga (tabla llena al 65%).

    def tamaño(self): #Función que devuelve el tamaño de la tabla hash (slots ocupados).
        return self.tam

    def deberia_expandir(self): #Comprueba el factor de carga de la tabla hash y devuelve True si se debería de expandir, False si no.
        return float(self.tam / self.tamano_total) >= self.maxima_carga

    def expande(self): #Función que expande la tabla hash al siguiente número primo.
        slots_antiguos = self.slots #Guardamos las claves de la anterior tabla hash.
        datos_antiguos = self.datos #Guardamos los valores de la anterior tabla hash.

        self.tamano_total = self.siguiente_primo() #Llamamos a la función para obtener el nuevo valor del tamaño total.

        #Creamos la nueva tabla hash.
        self.slots = [None] * self.tamano_total
        self.datos = [None] * self.tamano_total
        self.tam = 0

        self.reposiciona(slots_antiguos, datos_antiguos) #Recolocamos las claves y valores antiguos en la nueva tabla hash.

    def siguiente_primo(self):

        for i in range(2, self.tamano_total*5 + 1):
            es_primo = True
            for j in range(2,i):
                if (i == j):
                    break
                elif (i%j == 0):
                    es_primo = False
                else:
                    continue

            if (i > self.tamano_total and es_primo == True): #Si el primo obtenido es mayor que el primo actual asociado al tamaño total de la tabla hash.
                return i
        
    def reposiciona(self, slots, datos):

        for (slots, datos) in zip(slots, datos):
            if (slots is not None):
                self.agrega(slots, datos)

    def agrega(self, clave, dato):
        valorHash = self.funcionHash(clave, len(self.slots)) #Obtenemos la posición correcta en la tabla hash.

        if (self.deberia_expandir()):
            self.expande()

        if (self.slots[valorHash] == None):
            #Agrego:
            self.slots[valorHash] = clave
            self.datos[valorHash] = dato
            self.tam += 1
        else:
            if (self.slots[valorHash] == clave):
                self.datos[valorHash] = dato  # reemplazo
            else:
                proximaSlot = self.rehash(valorHash, len(self.slots))
                while self.slots[proximaSlot] != None and self.slots[proximaSlot] != clave:
                    proximaSlot = self.rehash(proximaSlot, len(self.slots))

                if (self.slots[proximaSlot] == None):
                    #Agrego:
                    self.slots[proximaSlot] = clave
                    self.datos[proximaSlot] = dato
                    self.tam += 1
                else:
                    self.datos[proximaSlot] = dato  # reemplazo

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
        self.agrega(clave, dato)

    def elimina(self,clave):

        slotInicio = self.funcionHash(clave, len(self.slots))

        #Definimos las variables.
        parar = False
        encontrado = False
        posicion = slotInicio

        #Recorremos la tabla hash mientras no se encuentre o hasta que se termine de recorrer la lista.
        while (not encontrado and not parar):
            if (self.slots[posicion] == clave): #Si el slot actual coincide con la clave.
                encontrado = True
                dato = self.datos[posicion] #Guardamos el valor que se va a eliminar.
                #Eliminamos:
                self.slots[posicion] = None
                self.datos[posicion] = None
                self.tam -= 1

            else:
                posicion = self.rehash(posicion, len(self.slots))
                if (posicion == slotInicio): #Si terminamos de recorrer la tabla hash.
                    parar = True
                    print("La clave que has introducido no se encuentra en la tabla Hash")

        return dato #Devolvemos el valor eliminado.