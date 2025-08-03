"""Problema de Simulación: Tareas de impresión Disponemos en un laboratorio de una
impresora antigua capaz de procesar 10 páginas por minuto en calidad de borrador.
Suele haber 10 usuarios por hora, imprimiendo hasta 2 veces en ese tiempo, y la
extensión de estas tareas oscila entre 1 y 20 páginas. ¿Podrá la impresora actual
manejar la carga de tareas si fuera ajustada para imprimir con una mejor calidad, pero
con una tasa de página más lenta? (Tema2_12.py y Tema2_12.cpp) Simular distintas
situaciones de la impresora"""

import random
import numpy
from Class_Estructuras_lineales import Cola
from Class_Impresion import Impresora, Tarea


def simulacion(numeroSegundos, paginasPorMinuto):

    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = Cola()
    tiemposEspera = []

    for segundoActual in range(numeroSegundos):

        if nuevaTareaImpresion():
            tarea = Tarea(segundoActual)
            colaImpresion.agregar(tarea)

        if (not impresoraLaboratorio.ocupada()) and (not colaImpresion.estaVacia()):
            tareaSiguiente = colaImpresion.avanzar()
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



