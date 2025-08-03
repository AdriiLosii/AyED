"""
Programa: Class_colas_prioridad_08.py
Propósito:
    Utilizando la clase MonticuloBinario, implementa una nueva clase llamada ColaPrioridad. Esta nueva
    clase ColaPrioridad debe implementar el constructor, además de los métodos agregar y avanzar.
Fecha: 10/05/2022
"""


class ColaPrioridad:
    def __init__(self):
        self.cola=[0]
        self.tamanoActual=0

    def agregar(self,k):
        self.cola.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def maximo(self):
        if self.tamanoActual==0:
            return 'La lista está vacía.'
        else:
            maximo=self.cola[0]
            for elemento in self.cola:
                if elemento>maximo:
                    maximo=elemento
            return maximo

    def extrae_y_borra(self):
        if self.tamanoActual==0:
            return 'La lista está vacía.'
        else:
            indice=0
            for i in range(len(self.cola)):
                if self.cola[i]>self.cola[indice]:
                    indice=i
            aux=self.cola[indice]
            del self.cola[indice]
            return aux
    
    def tamanho(self):
        return self.tamanoActual

    def esta_Vacia(self):
        return self.tamanoActual==0

    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.cola[i] < self.cola[i//2]:
            #los intercambio
             self.cola[i//2],self.cola[i] = self.cola[i],self.cola[i//2]
          i = i // 2

    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.cola[i] > self.cola[hm]:
                #los intercambio
                self.cola[i],self.cola[hm] = self.cola[hm],self.cola[i]
            i = hm

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.cola[i*2] < self.cola[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        if self.tamanoActual == 0:
            return 'La lista está vacía.'
        else:
            valorSacado = self.cola[1]
            self.cola[1] = self.cola[self.tamanoActual]
            self.tamanoActual = self.tamanoActual - 1
            self.cola.pop()
            self.infiltAbajo(1)
            return valorSacado

    def construirMonticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.cola = self.cola + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def avanzar(self):    
        if self.tamanoActual==0:
            print('La lista está vacía')
        else:
            self.eliminarMin()
            x=[str(v) for v in self.cola]
            del x[0]
            print('-'.join(x))