from tablas_hash import TablaHash

def main():
    H = TablaHash() 
    H[93] = "azul"
    H[17] = "rojo"
    H[77] = "marron"
    H[22] = "negro"
    H[34] = "blanco"
    H[25] = "gris"
    H[90] = "morado"
    H[1]  = "purpura"
    H[2]  = "verde"
    
    

    print(H.datos)
    print(H.slots)
    H.agregar(3,"Pepe")
    H[0]  = "Francisco"
    H[4]  = "gato"
    H[5]  = "efigie"
    print(H.datos)
    print(H.slots)


main()