class Impresora:
    def __init__(self, paginas):
        self.tasaPaginas = paginas
        self.tareaActual = None
        self.tiempoRestante = 0

    def tictac(self):
        if self.tareaActual != None:
            self.tiempoRestante = self.tiempoRestante - 1
            if self.tiempoRestante == 0:
                self.tareaActual = None

    def ocupada(self):
        if self.tareaActual != None:
            return True
        else:
            return False

    def iniciarNueva(self,nuevaTarea):
        self.tareaActual = nuevaTarea
        self.tiempoRestante = nuevaTarea.obtenerPaginas() * 60/self.tasaPaginas

import random

class Tarea:
    def __init__(self,tiempo):
        self.marcaTiempo = tiempo
        self.paginas = random.randrange(1,21)

    def obtenerMarca(self):
        return self.marcaTiempo

    def obtenerPaginas(self):
        return self.paginas

    def tiempoEspera(self, tiempoActual):
        return tiempoActual - self.marcaTiempo
