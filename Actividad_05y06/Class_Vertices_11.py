"""
Programa: Class_Vertices_11.py
Propósito:
    Crea el grafo correspondiente a la siguiente lista de aristas:
        de   a   costo
        1    2    10
        1    3    15
        1    6    5
        2    3    7
        3    4    7
        3    6    10
        4    5    7
        6    4    5
        5    6    13
Fecha: 10/05/2022
"""


import sys

class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.color ='white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0
    
    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + \
            "; color = " + self.color + \
            "; disc = " + str(self.disc) + \
            "; fin = " + str(self.fin) + \
            "; dist = " + str(self.dist) + \
            "; pred = [" + str(self.pred)+ "]\t" + \
            "; conectadoA = " + str([x.id for x in self.conectadoA])

    def asignarColor(self,color):
        self.color = color
        
    def asignarDistancia(self,d):
        self.dist = d

    def asignarPredecesor(self,p):
        self.pred = p

    def asignarDescubrimiento(self,dtime):
        self.disc = dtime
        
    def asignarFinalizacion(self,ftime):
        self.fin = ftime
        
    def obtenerFinalizacion(self):
        return self.fin
        
    def obtenerDescubrimiento(self):
        return self.disc
        
    def obtenerPredecesor(self):
        return self.pred
        
    def obtenerDistancia(self):
        return self.dist
        
    def obtenerColor(self):
        return self.color

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]