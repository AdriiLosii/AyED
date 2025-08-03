# Tema4_14_1 Ordenacion por insercion
def sort_ins(v):
    n = len(v)
    for i in range(1, n):
        x = v[i]
        j = i-1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j = j-1
        v[j+1] = x
