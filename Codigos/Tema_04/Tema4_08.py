# Tema4_08
def InterpolacionSearch(vector, val):
    bajo = 0
    alto = (len(vector)-1)
    while bajo <= alto and val >= vector[bajo] and val <= vector[alto]:
        indice = bajo + int(((float(alto-bajo) / (vector[alto]-vector[bajo])) * (val-vector[bajo])))
        if vector[indice] == val:
            return indice
        if vector[indice] < val:
            bajo = indice + 1
        else:
            alto = indice - 1
    return False


listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(InterpolacionSearch(listaPrueba, 3))
print(InterpolacionSearch(listaPrueba, 32))
