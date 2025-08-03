
import math
def crea_punto(x,y):
    return (x,y)
def calcula_distancia(p1,p2):
    distancia_x=p1[0]-p2[0]
    distancia_y=p1[1]-p2[1]
    return math.sqrt((distancia_x**2)+(distancia_y**2))
def calcula_distancia_origen(p1):
    return calcula_distancia(p1,(0,0))

if __name__=="__main__":
    p0=crea_punto(0,0)
    p1=crea_punto(3,4)

    print("De", p0, "a", p1, ":", calcula_distancia(p0,p1))
