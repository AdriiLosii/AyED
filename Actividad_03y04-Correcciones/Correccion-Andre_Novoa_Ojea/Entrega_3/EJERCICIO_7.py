#EJERCICIO 7: Dado un vector V de longitud n, aplicando el esquema de diseño Divide y vencerás y sin modificar V, 
# escribir una función que devuelva el valor que ocuparía la posición k (p.e. posición de la mediana) si el vector 
# V estuviera ordenado. Calcular su complejidad temporal en función de n y expresarla en notación asintótica.
from random import randint

def div_venc(V, n):
    if n%2 == 0:
        n = float(n)
        valor = V[int((n/2)-0.5)] + V[int((n/2)+0.5)]
        mediana = valor/2
    
        print("El valor de la mediana (k) es:", mediana, ".")
    else:
        n = float(n)
        mediana = V[int((n/2)-0.5)]
        print("El valor de la mediana (k) es:", mediana, ".")

print(" ")
n = int(input("Introduzca la longitud n del vector V: "))
print(" ")
V = [0]*n

for i in range (len(V)):
    V[i] = randint(1, 100)  #Se dan valores aleatorios a las componentes de V.

V = sorted(V)
print("El vector V original es", V, ".")
print(" ")
div_venc(V, n)