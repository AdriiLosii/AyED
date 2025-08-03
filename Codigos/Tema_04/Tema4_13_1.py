# Tema4_13_1 Ordenacion por seleccion:
def sort_sel(v):
    n = len(v)
    for i in range(0, n-1):
        minimo = v[i]
        argmin = i
        for j in range(i+1, n):
            if v[j] < minimo:
                minimo = v[j]
                argmin = j
        v[argmin] = v[i]
        v[i] = minimo
