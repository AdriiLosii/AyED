"""
Programa: Clase_Complejo_08.py
Propósito:
    Implementar con todos sus componentes la clase Complejo, de manera que se puedan ejecutar 
    todas las operaciones sobre complejos
Fecha:21/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import numpy as np
from numpy.polynomial import polynomial as P

class Complejo:
    def __init__(self, parte_real, parte_imag):

        try:
            self.complejo = complex(int(parte_real), int(parte_imag))

        except ValueError:
            print("Error, ha ocurrido algo inesperado.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    def __str__(self):
        return str(self.complejo)

    #Suma
    def __add__(self, otro):
        return self.complejo + otro.complejo

    #Resta
    def __sub__(self, otro):
        return self.complejo - otro.complejo

    #Multiplicación
    def __mul__(self, otro):
        return self.complejo * otro.complejo

    #División
    def __truediv__(self, otro):
        return self.complejo / otro.complejo
        
    #Potencia
    def __pow__(self, potencia):
        return self.complejo ** potencia

    #Valor absoluto
    def __abs__(self):
        return abs(self.complejo)

    #Conjugado
    def conj(self):
        return (self.complejo).conjugate()

    #Parte real
    def parte_real(self):
        return (self.complejo).real

    #Parte imaginaria
    def parte_imag(self):
        return (self.complejo).imag