from Class_Puntos import Punto
class Linea:
    """Representa líneas formadas por dos puntos, p1 y p2."""
    def __init__(self,x1,y1,x2,y2):
        """Crea nuevas líneas, dados dos puntos.
            :param x1: Coordenada x del primer punto
            :param y1: Coordenada y del primer punto
            :param x2: Coordenada x del segundo punto
            :param y2: Coordenada y del segundo punto
        """

        self.p1=Punto(x1,y1)
        self.p2=Punto(x2,y2)

    def calcula_longitud(self):
        return self.p1.calcula_distancia(self.p2)

    def __str__(self):
        return "({0}, {1})".format(self.p1,self.p2)
