"""Implementar el TAD Impresión usando Colas de Prioridad"""
import random
import numpy
from Class_Estructuras_lineales import ColaPrioridad
from Class_Impresion import Impresora, Tarea


def simulacion(numeroSegundos, paginasPorMinuto):

    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = ColaPrioridad()
    tiemposEspera = []

    for segundoActual in range(numeroSegundos):

        if nuevaTareaImpresion():
            tarea = Tarea(segundoActual)
            colaImpresion.agregar(tarea)

        if (not impresoraLaboratorio.ocupada()) and (not colaImpresion.estaVacia()):
            tareaSiguiente = colaImpresion.extrae()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            impresoraLaboratorio.iniciarNueva(tareaSiguiente)

        impresoraLaboratorio.tictac()

    esperaPromedio = sum(tiemposEspera)/float(len(tiemposEspera))
    print("Tiempo de espera promedio %6.2f segundos  %6.2f minutos  %3d tareas restantes." % (
        esperaPromedio, esperaPromedio/60, colaImpresion.tamano()))

    return esperaPromedio


def nuevaTareaImpresion():
    numero = random.randrange(1, 181)
    if numero == 180:
        return True
    else:
        return False


for j in range (1,10,1):

    promedioTiempos = []


    print("Páginas por minuto: ", j)

    for i in range(10):
        promedioTiempos.append(simulacion(3600, j))
    
    print("CASO MEJOR: ", min(promedioTiempos), "CASO PEOR: ", max(promedioTiempos), "CASO PROMEDIO: ", numpy.mean(promedioTiempos), '\n\n')

