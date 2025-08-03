"""
Programa: Class_Impresion_06.py
Propósito:
    Implementar el TAD Impresión usando Colas de Prioridad.
Fecha: 19/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import random

class Impresora:
    def __init__(self, paginas):
        self.tasaPaginas = paginas  #Velocidad de la impresora.
        self.tareaActual = None
        self.tiempoRestante = 0 #Tiempo restante de impresión (en segundos).

    def tictac(self):
        if self.tareaActual != None: #Si hay una tarea aciva.
            self.tiempoRestante = self.tiempoRestante - 1 #Restamos 1 segundo al tiempo restante.
            if self.tiempoRestante <= 0: #Si termina el tiempo de impresión.
                self.tareaActual = None #Terminamos la tarea actual.

    def ocupada(self): #Comprueba si la impresora está ocupada.
        if self.tareaActual != None: #Si hay una tarea activa.
            return True
        else:
            return False

    def iniciarNueva(self,nuevaTarea): #Inicia una nueva tarea.
        self.tareaActual = nuevaTarea
        self.tiempoRestante = nuevaTarea.obtenerPaginas() * 60/self.tasaPaginas # tiempo = paginas * seg / paginasXsminuto

class Tarea:
    def __init__(self,tiempo):
        self.marcaTiempo = tiempo   #segundoActual
        self.paginas = random.randrange(1,21)   #Número aleatorio entre 1 y 20 de páginas a imprimir.

    def obtenerMarca(self):
        return self.marcaTiempo

    def obtenerPaginas(self):
        return self.paginas

    def tiempoEspera(self, tiempoActual):
        return tiempoActual - self.marcaTiempo

class ColaPrioridad:
    def __init__(self):
        self.cola=[]

    def agregar(self,elemento):
        self.cola.append(elemento)

    def primero(self):
        if len(self.cola)==0:
            return None
        maximo=self.cola[0]
        for elemento in self.cola:
            if elemento>maximo:
                maximo=elemento
        return maximo

    def avanzar(self): #El número más grande de páginas.
        if len(self.cola)==0:
            return None
        indice=0
        for i in range(len(self.cola)):
            if (self.cola[i].obtenerPaginas() > self.cola[indice].obtenerPaginas()):
                indice=i
        aux=self.cola[indice]
        del self.cola[indice]
        return aux

    def tamano(self):
        return len(self.cola)

    def estaVacia(self):
        return len(self.cola)==0