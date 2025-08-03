n = 710
def piramide(n):
    y = 1
    g = 1
    for i in range(1, n+1): 
        l =[]
        C = 1
        x = 1
        for j in range(1, i+1): 
            l.append(C)
            C = C * (i - j) // j 
        
        for k in range(len(l)):
            x = x * l[k]
        
        z = x/y
        r = z/g
        y = x
        g = z
    print('Aproximación del número e: ',r)


piramide(n)