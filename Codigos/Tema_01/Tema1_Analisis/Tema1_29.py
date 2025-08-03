import timeit
extraerInicio = timeit.Timer("x.pop(0)","from __main__ import x")
extraerFinal = timeit.Timer("x.pop()","from __main__ import x")
print("\t tamaño \t pop(0)     \t  pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = extraerFinal.timeit(number=1000)
    x = list(range(i))
    pz = extraerInicio.timeit(number=1000)
    print("%15d %15.5f %15.5f" %(i,pz,pt))