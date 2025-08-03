import random

class Conjunto:

    def __init__(self):
        self.elementos=[]

    def __str__(self):
        cadena='{'
        if len(self.elementos)>0:
            for elemento in self.elementos[:-1]:
                cadena=cadena+str(elemento)+', '
            cadena=cadena+str(self.elementos[-1])
        return cadena+'}'

    def inserta(self,elemento):             #Inserta un elemento a un conjunto si no esta ya  en el
        if not (elemento in self.elementos):
            self.elementos.append(elemento)

    def tamaño(self):               #Devuelve el tamaño del conjunto
        return len(self.elementos)

    def pertenece(self, elemento):          #Devuelve si un elemento esta o no en un conjunto
        return elemento in self.elementos

    def elimina(self, elemento):        #Eliminar un elementode un conjunto
        n=0
        found=False
        while n<len(self.elementos) and found ==False:
            if (elemento==self.elementos[n]):
                self.elementos.remove(elemento)
                found=True
            n=n+1

    def union(self, conjunto2):             #Unir dos conjuntos dados
        c2=conjunto2
        n=0
        while n<len(c2.elementos):
            self.inserta(c2.elementos[n])
            n=n+1
        return self

    def interseccion(self, conjunto2):          #Sacar la interseccion de dos conjuntos dados
        c3=Conjunto()
        c2=conjunto2
        n=0
        while n<len(self.elementos):
            m=0
            while m<len(c2.elementos):
                if self.elementos[n]==c2.elementos[m]:
                    c3.inserta(self.elementos[n])
                m=m+1
            n=n+1
        return c3

    def diferencia(self, conjunto2):        #Sacar la diferencia de dos conjuntos dados
        c2=conjunto2
        n=0
        while n<len(self.elementos):
            m=0
            while m<len(c2.elementos):
                if self.elementos[n]==c2.elementos[m]:
                    self.elimina(self.elementos[n])
                m=m+1
            n=n+1
        return self

    def incluye(self, conjunto2):       #Berificar si un conjunto incluye a otro
        c2=conjunto2
        inc=True
        n=0
        while n<len(c2.elementos) and inc==True:
            if not (self.pertenece(c2.elementos[n])):
                inc=False
            n=n+1
        return inc

    

    def crear_aleatorio(self,NumeroElementos):          #Crea un conjunto con valores aleatorios
        n=NumeroElementos
        m=0
        while m<n:
            x=random.randint(0,100)
            self.inserta(x)
            m=m+1