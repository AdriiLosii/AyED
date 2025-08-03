"""
Programa: Class_Monticulo_06.py
Propósito:
    Utilizando el método construirMonticulo, escribe una función de ordenamiento que pueda ordenar una 
    lista en tiempo O(nlogn). (Buscar heapsort)
Fecha: 07/05/2022
"""


class MonticuloBinario:
    def __init__(self): #Constructor
        self.listaMonticulo = [0]
        self.tamanoActual = 0
        self.listaOrdenada = []

    def __len__(self): #Método mágico para len().
        return self.tamanoActual

    def __iter__(self, i): #Método mágico para la iteración.
        return self.listaMonticulo[i]

    def __str__(self): #Método mágico para print().
        return str(self.listaMonticulo)

    def construirMonticulo(self, unaLista): #Construimos el montículo.
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if (self.listaMonticulo[i] > self.listaMonticulo[hm]):
                #los intercambio
                self.listaMonticulo[i], self.listaMonticulo[hm] = self.listaMonticulo[hm], self.listaMonticulo[i]
            i = hm

    def infiltArriba(self,i):
        while (i // 2 > 0):
            if (self.listaMonticulo[i] < self.listaMonticulo[i//2]): #Si el padre es menor que el
                self.listaMonticulo[i//2], self.listaMonticulo[i] = self.listaMonticulo[i], self.listaMonticulo[i//2] #Intercambio.
            i = i // 2

    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def heapSort(self):
        self.listaOrdenada = self.listaMonticulo[1:] #Copiamos la lista del monticulo eliminando el primer "0" auxiliar.

        #Creamos un monticulo max (max heap).
        for i in range(len(self.listaOrdenada)//2-1, -1, -1):
            self.heapify(len(self.listaOrdenada), i)

        #Extraemos los elementos uno a uno.
        for i in range(len(self.listaOrdenada)-1, 0, -1):
            self.listaOrdenada[i], self.listaOrdenada[0] = self.listaOrdenada[0], self.listaOrdenada[i]  #Intercambiamos
            self.heapify(i, 0)

        return self.listaOrdenada

    def heapify(self, n, i):
        mayor = i               #Inicialmente tomamos la raíz/padre como valor mayor (i = raíz/padre)
        izquierda = 2*i + 1     #Hijo izquierdo
        derecha = 2*i + 2       #Hijo derecho

        #Miramos si el hijo izquierdo es mayor que el padre.
        if (izquierda < n and self.listaOrdenada[izquierda] > self.listaOrdenada[mayor]):
            mayor = izquierda

        #Miramos si el hijo derecho es mayor que el padre.
        if (derecha < n and self.listaOrdenada[derecha] > self.listaOrdenada[mayor]):
            mayor = derecha

        #Si se cumplió alguna de las condiciones anteriores.
        if (mayor != i):
            self.listaOrdenada[i], self.listaOrdenada[mayor] = self.listaOrdenada[mayor], self.listaOrdenada[i]  #Intercambiamos los valores.

            #Llamada recursiva a la función.
            self.heapify(n, mayor)