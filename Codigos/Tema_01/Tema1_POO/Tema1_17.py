from Class_Fracciones1 import Fraccion
try:
    x = Fraccion(1, 2)
    y = Fraccion(2, 3)

    print('Suma de fracciones ', x + y)
    print('Resta de fracciones ', x - y)
    print('Multiplicación de fracciones ', x * y)
    print('División de fracciones ', x / y)

    print('Igualdad de fracciones ', x == y)
except:
    print("Error, no valen float")
