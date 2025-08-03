class Punto:
    num_puntos=0 #num_puntos es un contador estático
    ORIGEN=None #ORIGEN es una variable estática
    @staticmethod #get_origen es un método estático
    def get_origen():
        if Punto.ORIGEN is None:
            Punto.ORIGEN=Punto(0,0)
        return Punto.ORIGEN

    def __init__(self,x,y):
        self.x=x
        self.y=y
        Punto.num_puntos+=1
