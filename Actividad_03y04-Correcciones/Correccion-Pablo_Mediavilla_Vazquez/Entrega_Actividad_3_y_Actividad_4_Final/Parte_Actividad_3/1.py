lista = [1,2,3,4,5]

def invertir(lista):
    if lista == []:
        inversa = lista
    else:
        inversa = [lista[-1]] + invertir(lista[:-1])
    
    return inversa

print(invertir(lista))