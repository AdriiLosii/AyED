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