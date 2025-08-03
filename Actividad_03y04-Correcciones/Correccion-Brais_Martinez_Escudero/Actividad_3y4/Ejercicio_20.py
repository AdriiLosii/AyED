def ordenamientoBurbujaCorto(unaLista):
    intercambios = True
    numPasada = len(unaLista)
    
    while numPasada > 0 and intercambios:
        if (numPasada%2 == 0):
            intercambios = False
            for i in range(0,numPasada-1,+1):
                if unaLista[i]>unaLista[i+1]:
                    intercambios = True
                    unaLista[i],unaLista[i+1] = unaLista[i+1],unaLista[i]
                numPasada = numPasada-1
        else:
            intercambios = False
            for i in range(numPasada-1,0,-1):
                if unaLista[i]<unaLista[i-1]:
                    intercambios = True
                    unaLista[i],unaLista[i-1] = unaLista[i-1],unaLista[i]   
                numPasada = numPasada-1         
    

unaLista=[20,30,40,90,50,60,70,80,110,100]
ordenamientoBurbujaCorto(unaLista)
print(unaLista)