class PuertaLogica:

    def __init__(self,n):
        self.nombre = n
        self.salida = None

    def obtenerNombre(self):
        return self.nombre

    def obtenerSalida(self,datos):
        self.salida = self.ejecutarLogicaDePuerta(datos)
        return self.salida



class PuertaBinaria(PuertaLogica):

    def __init__(self,n):
        PuertaLogica.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def obtenerPinA(self,datos):
        if self.pinA == None:

            while 1:

                try:

                    #pinA = int(input("Introduzca la entrada del Pin A para la Puerta "+self.obtenerNombre()+"--> "))
                    if self.obtenerNombre() == "C1" or self.obtenerNombre() == "C4":

                        pinA = int(datos[0])

                    if self.obtenerNombre() == "C2" or self.obtenerNombre() == "C5":

                        pinA = int(datos[1])


                    if pinA == 0 or pinA == 1:

                        break

                    else:
                        1/0
                except:
                    print ("\nHa habido un error\n")

            return pinA
        else:

            return self.pinA.obtenerFuente().obtenerSalida(datos)

    def obtenerPinB(self,datos):
        if self.pinB == None:

            while 1:

                try:
                    #pinB = int(input("Introduzca la entrada del Pin B para la Puerta "+self.obtenerNombre()+"--> "))

                    if self.obtenerNombre() == "C1" or self.obtenerNombre() == "C4":

                        pinB = int(datos[2])

                    if self.obtenerNombre() == "C2" or self.obtenerNombre() == "C5":

                        pinB = int(datos[3])
                
                    if pinB == 0 or pinB == 1:

                        break

                    else:
                        1/0
                except:
                    print ("\nHa habido un error\n")

            return pinB
        else:
 
            return self.pinB.obtenerFuente().obtenerSalida(datos)

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

    def ejecutarLogicaDePuerta(self,datos):

        a = self.obtenerPinA(datos)
        b = self.obtenerPinB(datos)
        if a==1 and b==1:
            return 1
        else:
            return 0

class PuertaOR(PuertaBinaria):

    def __init__(self,n):
        PuertaBinaria.__init__(self,n)

    def ejecutarLogicaDePuerta(self,datos):

        a = self.obtenerPinA(datos)
        b = self.obtenerPinB(datos)
        if a ==1 or b==1:
            return 1
        else:
            return 0

class PuertaNAND(PuertaBinaria):

    def __init__(self,n):
        PuertaBinaria.__init__(self,n)

    def ejecutarLogicaDePuerta(self,datos):

        a = self.obtenerPinA(datos)
        b = self.obtenerPinB(datos)
        if a ==1 and b==1:
            return 0
        else:
            return 1

class PuertaNOR(PuertaBinaria):

    def __init__(self,n):
        PuertaBinaria.__init__(self,n)

    def ejecutarLogicaDePuerta(self,datos):

        a = self.obtenerPinA(datos)
        b = self.obtenerPinB(datos)
        if a==1 or b==1:
            return 0
        else:
            return 1

class PuertaXOR(PuertaBinaria):

    def __init__(self,n):
        PuertaBinaria.__init__(self,n)

    def ejecutarLogicaDePuerta(self,datos):

        a = self.obtenerPinA(datos)
        b = self.obtenerPinB(datos)
        if a + b == 1:
            return 1
        else:
            return 0

class PuertaUnaria(PuertaLogica):

    def __init__(self,n):
        PuertaLogica.__init__(self,n)

        self.pin = None

    def obtenerPin(self):
        if self.pin == None:

            while 1:

                try:
                    pin = int(input("Introduzca la entrada del Pin para la Puerta "+self.obtenerNombre()+"--> "))
                    
                    if pin == 0 or pin == 1:
                        break

                    else:
                        1/0
                except:
                    print ("\nSolo se permite 0 o 1\n")

            return pin
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