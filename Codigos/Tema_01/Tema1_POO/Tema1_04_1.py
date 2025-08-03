from Class_Puntos import Punto
#Importamos la clase creada y reflejada en la clase puntos (Class_Puntos.py)
if __name__== "__main__":
    p1=Punto(11,12)
    p2=Punto(5,6)
    print("p1: "+str(p1))
    print("p2: "+str(p2))
    print(str.format("Distancia de {0} a {1} - {2}",p1,p2,p1.calcula_distancia(p2)))
