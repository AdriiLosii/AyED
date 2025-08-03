# Tema4_06
def FibonacciSearch(vector, val):
    fibM_2 = 0
    fibM_1 = 1
    fibM = fibM_1 + fibM_2
    while (fibM < len(vector)):
        fibM_2 = fibM_1
        fibM_1 = fibM
        fibM = fibM_1 + fibM_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_2, (len(vector)-1))
        if (vector[i] < val):
            fibM = fibM_1
            fibM_1 = fibM_2
            fibM_2 = fibM - fibM_1
            index = i
        elif (vector[i] > val):
            fibM = fibM_2
            fibM_1 = fibM_1 - fibM_2
            fibM_2 = fibM - fibM_1
        else:
            return i
    if(fibM_1 and index < (len(vector)-1) and vector[index+1] == val):
        return index+1
    return False


listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(FibonacciSearch(listaPrueba, 3))
print(FibonacciSearch(listaPrueba, 32))
