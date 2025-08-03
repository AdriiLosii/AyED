class Conjunto:

    def __init__(self):
        self.elementos=[]

    def inserta(self,elemento):
        if not (elemento in self.elementos):
            self.elementos.append(elemento)

    def __str__(self):
        cadena='{'
        if len(self.elementos)>0:
            for elemento in self.elementos[:-1]:
                cadena=cadena+str(elemento)+', '
            cadena=cadena+str(self.elementos[-1])
        return cadena+'}'

    def tamaño(self):
        return len(self.elementos)
        
    def pertenece(self, elemento):
        return elemento in self.elementos

    def borrar(self,posicion):
        self.elementos.pop(posicion)
    
    def union(self,parametro2):
        conjuntofinal={}
        conjunto1 = set(self.elementos)
        conjunto2 = set(parametro2)
        conjuntofinal=conjunto1|conjunto2
        return conjuntofinal

    def interseccion(self,parametro2):
        conjuntofinal={}
        conjunto1 = set(self.elementos)
        conjunto2 = set(parametro2)
        conjuntofinal=conjunto1 & conjunto2
        return conjuntofinal

    def diferencia(self,parametro2):
        sumauno = sum(self.elementos)
        sumados = sum(parametro2)

        diferencia = sumauno - sumados

        return diferencia

    def incluye(self,parametro):
        lista = list(parametro)
        for i in range (len(lista)):
            if lista[i] in self.elementos:
                return True
            else:
                return False