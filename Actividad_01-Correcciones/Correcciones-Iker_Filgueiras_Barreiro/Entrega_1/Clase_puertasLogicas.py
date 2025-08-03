class PuertaLogicaBinaria(object):

    def __init__(self,nombre,entradaA,entradaB):
        self.nombre = nombre
        self.entradaA= entradaA
        self.entradaB= entradaB

    def getName(self):
        return self.nombre

    def __str__(self):
        return "Puerta lógica, entradaA: "+str(self.entradaA)+" entradaB: "+str(self.entradaB)

    def salida(self):
        return True


class PuertaLogicaUnaria(object):

    def __init__(self,nombre,entradaA):
        self.nombre = nombre
        self.entradaA= entradaA

    def getName(self):
        return self.nombre

    def __str__(self):
        return "Puerta lógica, entradaA: "+str(self.entradaA)

    def salida(self):
        return True



class PuertaNOT(PuertaLogicaUnaria):

    def __init__(self,n,entradaA):
        PuertaLogicaUnaria.__init__(self,n,entradaA)

    def salida(self):
        return not self.entradaA

class PuertaOR(PuertaLogicaBinaria):

    def __init__(self,n,entradaA,entradaB):
        PuertaLogicaBinaria.__init__(self,n,entradaA,entradaB)

    def salida(self):
        salida = False
        if self.entradaA == 1 or self.entradaB == 1:
            salida = True
        return salida

class PuertaNOR(PuertaOR):

    def __init__(self,n,entradaA,entradaB):
        PuertaOR.__init__(self,n,entradaA,entradaB)
    
    def salida(self):
        return not super().salida()

class PuertaXOR(PuertaLogicaBinaria):

    def __init__(self,n,entradaA,entradaB):
        PuertaLogicaBinaria.__init__(self,n,entradaA,entradaB)
    
    def salida(self):
        salida = True
        if self.entradaA == self.entradaB:
            salida = False
        return salida

class PuertaAND(PuertaLogicaBinaria):

    def __init__(self,n,entradaA,entradaB):
        PuertaLogicaBinaria.__init__(self,n,entradaA,entradaB)
    
    def salida(self):
        salida = True
        if self.entradaA == 0 or  self.entradaB == 0:
            salida = False
        return salida

class PuertaNAND(PuertaAND):

    def __init__(self,n,entradaA,entradaB):
        PuertaAND.__init__(self,n,entradaA,entradaB)
    
    def salida(self):
        return not super().salida()

