class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return str.format("({0}, {1})",self.x,self.y)

p1=Punto(11,12)
p2=Punto(5,6)
print("p1: "+ str(p1))
print("p2: "+ str(p2))
