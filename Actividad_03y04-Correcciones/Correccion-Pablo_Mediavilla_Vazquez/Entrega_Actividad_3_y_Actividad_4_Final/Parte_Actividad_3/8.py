from Class_Jarras import Jarra

x = int(input("Volumen de x: "))
y = int(input("Volumen de y: "))


jarraY = Jarra(y)
jarraX = Jarra(x)

if y == x//2:
    jarraY.llenar()
    jarraY.trasladar(jarraX)

    print(jarraX.__str__())


else:
    while jarraX.__str__() != x//2 or jarraY.__str__() != x//2:
        jarraY.llenar()
        print("Llenamos la jarra de YL -->",jarraY.__str__())

        jarraY.trasladar(jarraX)
        print("Jarra de YL -->",jarraY.__str__(),jarraX.__str__(),"<-- Jarra de XL")

        jarraY.llenar()
        print("Llenamos la jarra de YL -->",jarraY.__str__())

        jarraY.trasladar(jarraX)
        print("Jarra de YL -->",jarraY.__str__(),jarraX.__str__(),"<-- Jarra de XL")

        jarraX.vaciar()
        print("Vaciamos la jarra de XL -->",jarraX.__str__())

        jarraY.trasladar(jarraX)
        print("Jarra de YL -->",jarraY.__str__(),jarraX.__str__(),"<-- Jarra de XL")

        

        if int(jarraX.__str__()) == x/2 or int(jarraY.__str__()) == x/2:
            break