#Class_Puntos.py
import math
class Punto:
    def __init__(self,x,y):
        """Crea un nuevo punto, dadas las coordenadas.

            :param x: Coordenada x del punto
            :param y: Coordenada y del punto
        """
        self.x=x
        self.y=y

    def calcula_distancia(self,p2):
        """Retorna la distancia entre este punto y otro
            :param p2: El otro punto.
            :return: La distancia entre este punto y p2.
        """
        distancia_x=self.x-p2.x
        distancia_y=self.y-p2.y
        return math.sqrt((distancia_x**2)+(distancia_y**2))

    def calcula_distancia_origen(self):
        """Retorna la distancia desde el origen de coordenadas a este punto
            :return: La distancia entre ambos puntos
        """
        return self.calcula_distancia(Punto(0, 0))
    def __str__(self):
        return str.format("({0}, {1})",self.x,self.y)

