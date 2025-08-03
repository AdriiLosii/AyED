  
numfilas = int(input("Indique el número de filas: "))
print("")

for i in range(1, numfilas+1): 
    for j in range(0, numfilas-i+1): 
        print(' ', end='') 
  
    
    B = 1   #B vale 1 pues es el primer valor de las filas
    for j in range(1, i+1): 
  
        
        print(' ', B, sep='', end='') 
  
        
        B = B * (i - j) // j 
    print()

print(" ")