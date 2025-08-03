from numpy import zeros
from random import randint
from statistics import mode
import time


def crear_vectores(MAXEDAD, MAXDATOS):
    edades = zeros(MAXDATOS, dtype=int)
    frecs = zeros(MAXEDAD, dtype=int)
    for i in range(MAXDATOS):
        edades[i] = randint(1, MAXEDAD-1)
        frecs[edades[i]] += 1
    return edades, frecs


def moda1(edades, MAXDATOS):
    # moda1.py: cálculo (ineficiente) de la moda
    # Explora MAXDATOS veces edades[] para determinar cual es la edad que mas se repite (moda)
    maxFrec = 0

    for i in range(MAXDATOS):
        frec = 0
        for j in range(MAXDATOS):
            if edades[i] == edades[j]:
                frec += 1
        if frec > maxFrec:
            maxFrec = frec
            moda = edades[i]
    return moda, maxFrec


def moda2(edades, MAXDATOS, MAXEDAD):
    # moda2.py: cálculo (poco eficiente) de la moda
    # Explora MAXEDAD veces edades[] para determinar cual es la edad que mas se repite (moda)
    maxFrec = 0

    for i in range(MAXEDAD):
        frec = 0
        for j in range(MAXDATOS):
            if edades[j] == i:
                frec += 1
        if frec > maxFrec:
            maxFrec = frec
            moda = i
    return moda, maxFrec


def moda3(frecs, MAXEDAD):
    # moda3.py: cálculo (eficiente) de la moda
    maxFrec = 0

    for edad in range(MAXEDAD):
        if frecs[edad] > maxFrec:
            maxFrec = frecs[edad]
            moda = edad
    return moda, maxFrec


# Inicializa contador de datos (talla)
MAXDATOS = int(input("Dame el tamaño de la muestra "))
MAXEDAD = int(input("Dame la edad máxima "))

edades, frecs = crear_vectores(MAXEDAD, MAXDATOS)

inicio = time.time()
moda, maxFrec = moda1(edades, MAXDATOS)
final = time.time()

print("Moda1: Leídos %d datos; Moda=%d (frecuencia=%d)\n" %
      (MAXDATOS, moda, maxFrec))
print("Este algoritmo requirió %10.7f segundos\n\n" % (final-inicio))

inicio = time.time()
moda, maxFrec = moda2(edades, MAXDATOS, MAXEDAD)
final = time.time()

print("Moda2: Leídos %d datos; Moda=%d (frecuencia=%d)\n" %
      (MAXDATOS, moda, maxFrec))
print("Este algoritmo requirió %10.7f segundos\n\n" % (final-inicio))

inicio = time.time()
moda, maxFrec = moda3(frecs, MAXEDAD)
final = time.time()

print("Moda3: Leídos %d datos; Moda=%d (frecuencia=%d)\n" %
      (MAXEDAD, moda, maxFrec))
print("Este algoritmo requirió %10.7f segundos\n\n" % (final-inicio))

inicio = time.time()
moda = mode(edades)
final = time.time()

print("Mode de statistics: Leídos %d datos; Moda=%d (frecuencia=%d)\n" %
      (MAXDATOS, moda, maxFrec))
print("Este algoritmo requirió %10.7f segundos\n\n" % (final-inicio))
