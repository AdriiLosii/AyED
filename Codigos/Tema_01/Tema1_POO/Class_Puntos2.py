import math


class Punto:
    # Crea una clase llamada Punto con sus dos coordenadas X e Y.
    def __init__(self, x=0, y=0):
        # Añade un método constructor para crear puntos fácilmente. Si no se recibe una de sus coordenadas, su valor será cero.
        self.x = x
        self.y = y

    def __str__(self):
        # Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        # Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que
        # si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} se sitúa sobre el eje X".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} se sitúa sobre el eje Y".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))

    def vector(self, p):
        # Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y))

    def distancia(self, p):
        # Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla.
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print("La distancia entre los puntos {} y {} es {}".format(
            self, p, d))


class Rectangulo:
    # Crea una clase llamada Rectángulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        # Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
        self.pInicial = pInicial
        self.pFinal = pFinal
        # Hago los cálculos, pero no denomino a los atributos igual
        # que los métodos porque sino podríamos sobreescribirlos
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura

    def base(self):
        # Añade al rectángulo un método llamado base que muestre la base.
        print("La base del rectángulo es {}".format(self.vBase))

    def altura(self):
        # Añade al rectángulo un método llamado altura que muestre la altura.
        print("La altura del rectángulo es {}".format(self.vAltura))

    def area(self):
        # Añade al rectángulo un método llamado área que muestre el área.
        print("El área del rectángulo es {}".format(self.vArea))
