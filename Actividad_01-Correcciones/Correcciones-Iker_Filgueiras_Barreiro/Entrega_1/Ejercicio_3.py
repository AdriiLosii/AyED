from Class_Fracciones import *

try:
    f1=Fraccion(8,23)
    f2=Fraccion(4, 5.8)
    print(f1+f2)
except:
    print("El denominador o el numerador no es un numero entero.")