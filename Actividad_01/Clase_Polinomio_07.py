"""
Programa: Clase_Polinomio_07.py
Propósito:
    Implementar con todos sus componentes la clase Polinomio, de manera que se puedan ejecutar 
    todas las operaciones sobre polinomios
Fecha:20/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import numpy as np
from numpy.polynomial import polynomial as P

class Polinomio:
    def __init__(self, polinomio):

        try:

            polinomio = polinomio.split() #Creamos una lista con los valores introducidos

            #Comprobamos que todos los elementos de la lista sean de tipo float.
            for i in range(len(polinomio)):
                polinomio[i] = float(polinomio[i])

            self.polinomio = polinomio

        except ValueError:
            print("Error, ha ocurrido algo inesperado.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    def __str__(self):
        return str(np.poly1d(self.polinomio))

    #Suma
    def __add__(self, otro):
        return np.poly1d(np.polyadd(self.polinomio, otro.polinomio))

    #Resta
    def __sub__(self, otro):
        return np.poly1d(np.polysub(self.polinomio, otro.polinomio))

    #Multiplicación
    def __mul__(self, otro):
        return np.poly1d(np.polymul(self.polinomio, otro.polinomio))

    #División
    def __truediv__(self, otro):
        cociente, resto = P.polydiv(self.polinomio, otro.polinomio)
        return np.poly1d(cociente), np.poly1d(resto)

    #Potencia
    def __pow__(self, potencia):
        return np.poly1d(P.polypow(self.polinomio, potencia))