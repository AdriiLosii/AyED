from Ej3y4_Clase import Fraccion
try:
    x = Fraccion(1, -2)
    y = Fraccion(2, 3)
    print(x)
    print(y)
    print('Suma de fracciones ', x + y)
    print('Resta de fracciones ', x - y)
    print('Multiplicación de fracciones ', x * y)
    print('División de fracciones ', x / y)

    print('Igualdad de fracciones ', x == y)
    print('Obtener el denominador de x',Fraccion.getDen(x))
    print('Obtener el numerador de x',Fraccion.getNum(x))
    print('Obtener el denominador de y',Fraccion.getDen(y))
    print('Obtener el numerador de y',Fraccion.getNum(y))


    print('x Mayor qué y',Fraccion.__gt__(x,y))
    print('x Menor qué y',Fraccion.__lt__(x,y))
    print('x Mayor o igual qué y',Fraccion.__ge__(x,y))
    print('x Menor o igual qué y',Fraccion.__le__(x,y))
    print('x No igual qué y',Fraccion.__ne__(x,y))
except:
    print("Error, no valen float")
