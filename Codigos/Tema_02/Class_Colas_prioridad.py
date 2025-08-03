#Cola_prioridad.py
class ColaPrioridad:
    def __init__(self):
        self.cola=[]

    def añade(self,elemento):
        self.cola.append(elemento)

    def primero(self):
        if len(self.cola)==0:
            return None
        maximo=self.cola[0]
        for elemento in self.cola:
            if elemento>maximo:
                maximo=elemento
        return maximo

    def extrae(self):
        if len(self.cola)==0:
            return None
        indice=0
        for i in range(len(self.cola)):
            if self.cola[i]>self.cola[indice]:
                indice=i
        aux=self.cola[indice]
        del self.cola[indice]
        return aux
    
    def tamaño(self):
        return len(self.cola)

    def esta_Vacia(self):
        return len(self.cola)==0


