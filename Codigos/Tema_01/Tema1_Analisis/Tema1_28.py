import timeit
def prueba1():
    l = []
    for i in range(1000):
        l = l + [i]

def prueba2():
    l = []
    for i in range(1000):
        l.append(i)

def prueba3():
    l = [i for i in range(1000)]

def prueba4():
    l = list(range(1000))
    
t1 = timeit.Timer("prueba1()", "from __main__ import prueba1")
print("concatenación ",t1.timeit(number=1000), "segundos")
t2 = timeit.Timer("prueba2()", "from __main__ import prueba2")
print("append ",t2.timeit(number=1000), "segundos")
t3 = timeit.Timer("prueba3()", "from __main__ import prueba3")
print("comprensión ",t3.timeit(number=1000), "segundos")
t4 = timeit.Timer("prueba4()", "from __main__ import prueba4")
print("método range ",t4.timeit(number=1000), "segundos")