"""
Programa: Class_Tabla_Hash_16.py
Propósito:
    ¿Cómo puedes eliminar ítems de una tabla hash que utiliza encadenamiento para la 
    solución de colisiones? ¿Qué tal si se usa direccionamiento abierto? ¿Cuáles son las 
    circunstancias especiales que deben manejarse? Implementa el método eliminar para 
    la clase TablaHash que utiliza encadenamiento.
Fecha: 19/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


class Nodo:
    def __init__(self, datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def __str__(self):
        return str(self.dato)

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente


#Creamos la clase de la tabla hash encadenada.
class TablaHashEncadenada:
    def __init__(self):
        self.tamano_total = 11
        self.slots = [None] * self.tamano_total
        self.datos = [Nodo(None)] * self.tamano_total
        self.tam = 0
        self.maxima_carga = 0.7 #Valor máximo del factor de carga (tabla llena al 70%).

    def __str__(self):  #Definimos el str para poder mostrar los datos de la clase

        string = ""

        for slot in range(self.tamano_total):
            string += "Pos. " + str(slot) + " = " + "Clave " + str(self.slots[slot]) + ": "

            actual = self.datos[slot]
            while(actual != None):
                if (actual.obtenerSiguiente() != None):
                    string += str(actual.obtenerDato())+" -> "
                    actual = actual.obtenerSiguiente()

                else:
                    string += str(actual.obtenerDato())+"\n"
                    actual = actual.obtenerSiguiente()

        return string #Devolvemos la cadena de como se mostraría la tabla al programa principal.

    def agrega(self, clave, dato):
        valorHash = self.funcionHash(clave, len(self.slots))

        #Comprobamos si tenemos que expandir la tabla hash.
        if (self.deberia_expandir()):
            self.expande()

        #Agregamos:
        self.slots[valorHash] = clave #Añadimos la clave la lista de los slots.

        #Añadimos el dato a la lista enlazada del slot.
        temp = Nodo(dato)
        temp.asignarSiguiente(self.datos[valorHash])
        self.datos[valorHash] = temp

        self.tam += 1

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
        self.datos = [Nodo(None)] * self.tamano_total
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

    def funcionHash(self, clave, tamano):
        return clave % tamano

    def rehash(self, hashViejo, tamano):
        return (hashViejo+1) % tamano

    def obtener(self, clave):  #Definimos la funcion para agregar elementos a la tabla
        slotInicio = self.funcionHash(clave, len(self.slots))

        #Definimos las variables.
        dato = None
        parar = False
        encontrado = False
        posicion = slotInicio
        while self.slots[posicion] != None and not encontrado and not parar:
            if self.slots[posicion] == clave:  #Si el elemento coincide con la clave, es decir, si se encuentra en la tabla Hash entonces:
                encontrado = True
                dato = self.datos[posicion]    #Guardamos el valor
            else:
                posicion = self.rehash(posicion, len(self.slots))
                if posicion == slotInicio:
                    parar = True
        return dato  #Devolvemos el valor

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, dato):
        self.agrega(clave, dato)

    def eliminar(self, clave):  #Definimos la funcion que elimina elementos de la tabla Hash

        slotInicio = self.funcionHash(clave, len(self.slots))

        #Definimos las variables.
        parar = False
        encontrado = False
        posicion = slotInicio

        #Recorremos la tabla hash mientras no se encuentre o hasta que se termine de recorrer la lista.
        while (not encontrado and not parar):
            if (self.slots[posicion] == clave): #Si el slot actual coincide con la clave entonces: 
                encontrado = True
                dato = self.datos[posicion] #Guardamos el valor que se va a eliminar.

                #Eliminamos:
                self.slots[posicion] = None
                self.datos[posicion] = Nodo(None)
                self.tam -= 1
                return dato #Devolvemos el valor eliminado.

            else:
                posicion = self.rehash(posicion, len(self.slots))
                if (posicion == slotInicio): #Si terminamos de recorrer la tabla hash.
                    parar = True
                    print("La clave que has introducido no se encuentra en la tabla Hash.")