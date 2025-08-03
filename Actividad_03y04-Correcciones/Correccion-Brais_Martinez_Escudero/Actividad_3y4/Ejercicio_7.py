import random
import timeit

def posicionk(vector,p,f,k):

    if(f>=p):

        medio=random.randint(p,f)

        if(vector[medio]==k):

            return medio

        if(vector[medio]>k):

            return posicionk(vector,p,medio-1,k)

        return posicionk(vector,medio+1,f,k)

    return None


print("Nº.Elementos   Elemento al principio    Elemento en el medio     Elemento al final")
for i in range(1000,100000+1,1000):

    vector=[random.randint(0,1000) for x in range(i)]
    vector=sorted(vector)
    

    tamano=len(vector)

    posicion_principio=posicionk(vector,0,tamano-1,vector[0])
    posicion_medio=posicionk(vector,0,tamano-1,vector[i-1])  
    posicion_final=posicionk(vector,0,tamano-1,vector[i//2])  

    t_principio=timeit.Timer("posicionk(vector,0,tamano-1,vector[0])","from __main__ import posicionk, vector ,i,tamano").timeit(number=1000)
    t_medio=timeit.Timer("posicionk(vector,0,tamano-1,vector[i-1])","from __main__ import posicionk, vector ,i,tamano").timeit(number=1000)
    t_final=timeit.Timer("posicionk(vector,0,tamano-1,vector[i-1])","from __main__ import posicionk, vector ,i, tamano").timeit(number=1000)

    print("%1d  %10.3f  %9.3f   %10.3f" % (i,t_principio,t_medio,t_final))