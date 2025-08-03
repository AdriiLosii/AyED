"""
Programa: Class_Impresion_05.py
Propósito:
    Problema de Simulación: Tareas de impresión Disponemos en un laboratorio de una 
    impresora antigua capaz de procesar 10 páginas por minuto en calidad de borrador. 
    Suele haber 10 usuarios por hora, imprimiendo hasta 2 veces en ese tiempo, y la 
    extensión de estas tareas oscila entre 1 y 20 páginas. ¿Podrá la impresora actual 
    manejar la carga de tareas si fuera ajustada para imprimir con una mejor calidad, pero 
    con una tasa de página más lenta? (Tema2_12.py y Tema2_12.cpp) Simular distintas 
    situaciones de la impresora.
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

class Cola:
    """
        Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """

    def __init__(self):
        """
            Crea una cola vacía.
        """
        # La cola vacía se representa por una lista vacía
        self.items = []
    
    def estaVacia(self):
        """
            Devuelve True si la cola esta vacía, False si no.
        """
        return self.items == []

    def agregar(self, item):
        """
            Agrega el elemento x como último de la cola.
        """
        self.items.insert(0,item)

    def avanzar(self):
        """
            Elimina el primer elemento de la cola y devuelve su
            valor.
        """
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def frente (self):
        return self.items[len(self.items)-1]

    def ultimo (self):
        if len(self.items)>0:
            return self.items[0]