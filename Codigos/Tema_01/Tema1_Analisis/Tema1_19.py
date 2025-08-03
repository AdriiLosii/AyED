import time


def N2_1(n):
    inicio = time.time()
    m = n*n
    final = time.time()
    return m, final-inicio


def N2_2(n):
    inicio = time.time()
    m = 0.0
    for i in range(n):
        m = m+n
    final = time.time()
    return m, final-inicio


def N2_3(n):
    inicio = time.time()
    m = 0.0
    for i in range(n):
        for j in range(n):
            m += 1.0
    final = time.time()
    return m, final-inicio


n = int(input("Dame un valor para n "))
print("El resultado de1 1 es %10.0f y requirió %10.7f segundos" % N2_1(n))
print("El resultado del 2 es %10.0f y requirió %10.7f segundos" % N2_2(n))
print("El resultado del 3 es %10.0f y requirió %10.7f segundos" % N2_3(n))
