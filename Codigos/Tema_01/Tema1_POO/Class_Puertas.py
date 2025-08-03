class PuertaLogica:

    def __init__(self,n):
        self.nombre = n
        self.salida = None

    def obtenerNombre(self):
        return self.nombre

    def obtenerSalida(self):
        self.salida = self.ejecutarLogicaDePuerta()
        return self.salida


class PuertaBinaria(PuertaLogica):

    def __init__(self,n):
        PuertaLogica.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def obtenerPinA(self):
        if self.pinA == None:
            return int(input("Introduzca la entrada del Pin A para la Puerta "+self.obtenerNombre()+"--> "))
        else:
            return self.pinA.obtenerFuente().obtenerSalida()

    def obtenerPinB(self):
        if self.pinB == None:
            return int(input("Introduzca la entrada del Pin B para la Puerta "+self.obtenerNombre()+"--> "))
        else:
            return self.pinB.obtenerFuente().obtenerSalida()

    def asignarProximoPin(self,fuente):
        if self.pinA == None:
            self.pinA = fuente
        else:
            if self.pinB == None:
                self.pinB = fuente
            else:
                print("No se puede conectar: NO HAY PINES DISPONIBLES en esta Puerta")


class PuertaAND(PuertaBinaria):

    def __init__(self,n):
        PuertaBinaria.__init__(self,n)

    def ejecutarLogicaDePuerta(self):

        a = self.obtenerPinA()
        b = self.obtenerPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class PuertaOR(PuertaBinaria):

    def __init__(self,n):
        PuertaBinaria.__init__(self,n)

    def ejecutarLogicaDePuerta(self):

        a = self.obtenerPinA()
        b = self.obtenerPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class PuertaUnaria(PuertaLogica):

    def __init__(self,n):
        PuertaLogica.__init__(self,n)

        self.pin = None

    def obtenerPin(self):
        if self.pin == None:
            return int(input("Introduzca la entrada del Pin para la Puerta "+self.obtenerNombre()+"--> "))
        else:
            return self.pin.obtenerFuente().obtenerSalida()

    def asignarProximoPin(self,fuente):
        if self.pin == None:
            self.pin = fuente
        else:
            print("No se puede conectar: NO HAY PINES DISPONIBLES en esta Puerta")


class PuertaNOT(PuertaUnaria):

    def __init__(self,n):
        PuertaUnaria.__init__(self,n)

    def ejecutarLogicaDePuerta(self):
        if self.obtenerPin():
            return 0
        else:
            return 1


class Conector:

    def __init__(self, deComp, aComp):
        self.dePuerta = deComp
        self.aPuerta = aComp

        aComp.asignarProximoPin(self)

    def obtenerFuente(self):
        return self.dePuerta

    def obtenerDestino(self):
        return self.aPuerta

