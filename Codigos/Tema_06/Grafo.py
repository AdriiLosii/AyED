#Autor: Luis García
#Carrera: Ingeniería en Computación

import os

grafo = {}

opc = 0
while opc != 3:
    os.system("cls")
    print("\n\tGrafo Ponderado no Dirigido")
    opc = input ("\n1.-Ingresar nodos \n2.-Mostrar grafo \n3.-Salir \nElige una opcion-> ")
    opc = int(opc)

    if opc == 1:
        print("\nINGRESE LOS NODOS Y SU PESO \n")
        origen  = input("Ingresa el origen:  ")
        destino = input("Ingresa el destino: ")
        peso    = input("Ingresa el peso:    ")
        peso = int(peso)
        
        ###VERIFICA QUE NO ESTE REPETIDO EL VERTICE ORIGEN Y DESTINO INGRESADO
        repetido = False
        for orig, lista in grafo.items():
            for destin, pesos in grafo[orig]:
                if orig == origen and destin == destino and pesos == peso:
                    print("\nEL VERTICE YA EXISTE\n")
                    repetido = True
        #SI NO ESTÁ REPETIDO INGRESA A VALIDAR SI LOS NODOS ORIGEN Y DESTINO EXISTEN
        if repetido == False:
            if origen in grafo:
                if destino in grafo:
                    lista = grafo[origen]
                    grafo[origen] = lista + [(destino, peso)] 
                    lista = grafo [destino]
                    lista.append((origen, peso))
                    grafo[destino] = lista
                else:
                    grafo[destino] = [(origen, peso)]
                    lista = grafo [origen] 
                    lista.append((destino, peso))
                    grafo[origen] = lista
            elif destino in grafo:
                grafo[origen] = [(destino, peso)]
                lista = grafo [destino]
                lista.append((origen, peso))
                grafo[destino] = lista
            else:
                grafo[destino] = [(origen, peso)]
                grafo[origen] = [(destino, peso)]
    if opc == 2:
        print()
        #SI EL GRAFO TIENE NODOS LO MUESTRA
        if len(grafo) > 0:
            for key, lista in grafo.items():
                print(key)
                print(lista)
        else:
            print("El grafo esta vacio...")
    print()
    os.system("pause")