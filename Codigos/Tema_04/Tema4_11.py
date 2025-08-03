#Tema4_11
def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                unaLista[i],unaLista[i+1]=unaLista[i+1],unaLista[i]


unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoBurbuja(unaLista)
print(unaLista)
