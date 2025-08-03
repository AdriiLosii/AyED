import time
import random

def exp():
    print("         %10s    %10s    %10s  %10s   %10s   %10s  %10s" % ("dimensión", "obten. mejor", "asign. mejor", "obtenc. media", "asign. media", "peor obtenc.", "asign. peor"))
    for i in range(1000, 10000, 500):
        x = {j: None for j in range(i)}
        dicc_inicial=time.time()
        x.get(x[0])
        dicc_final=time.time()

        x = {j: None for j in range(i)}
        dicc_inicial2=time.time()
        x.setdefault(1,3)
        dicc_final2=time.time()

        x = {j: None for j in range(i)}
        dicc_medioi=time.time()
        x.get(x[len(x)//2])
        dicc_mediof=time.time()

        x = {j: None for j in range(i)}
        dicc_medioi2=time.time()
        x.setdefault(len(x)//2,3)
        dicc_mediof2=time.time()

        x = {j: None for j in range(i)}
        dicc_peori=time.time()
        x.get(x[len(x)-1])
        dicc_peorf=time.time()

        x = {j: None for j in range(i)}
        dicc_peori2=time.time()
        x.setdefault(len(x)-1,3)
        dicc_peorf2=time.time()

        
        print("%15d %15.5f %15.5f %15.5f %15.5f %15.5f %15.5f" %(i,dicc_final-dicc_inicial,dicc_final2-dicc_inicial2,dicc_mediof-dicc_medioi,dicc_mediof2-dicc_medioi2,dicc_peorf-dicc_peori,dicc_peorf2-dicc_peori2))
exp()