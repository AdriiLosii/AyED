def piramide(F):
    for i in range(1, F+1): 
        l =[]
        C = 1
        for j in range(1, i+1): 
            l.append(C)
            C = C * (i - j) // j 
        print(l)  

F = int(input("Introduce el número de filas: "))

piramide(F)