#Tema3_03
import turtle

miTortuga = turtle.Turtle()
miVentana = turtle.Screen()

def dibujarEspiral(miTortuga, long_linea):
    if long_linea > 0:
        miTortuga.forward(long_linea)
        miTortuga.right(90)
        dibujarEspiral(miTortuga,long_linea-5)

dibujarEspiral(miTortuga,200)
miVentana.exitonclick()
