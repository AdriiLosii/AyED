from tablas_hash_16 import TablaHash

def main():
    H = TablaHash() 
    H[98] = "perro"
    H[33] = "zorro"
    H[25] = "pajaro"
    H[11] = "leon"
    H[22] = "cucaracha"
    H[37] = "macaco"
    H[25] = "anivia"
    H[84] = "tigre"
    H[5]  = "udyr"
    H[2]  = "ballena"


    
    print(H.slots)
    print(H.datos)
    H.Remove(25)
    print(H.slots)
    print(H.datos)
    


main()