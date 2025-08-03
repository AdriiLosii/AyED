"""1. Convierte las siguientes expresiones infijas a expresiones prefijas (usa el método de
agrupar completamente) y evaluarlas dando valores a los operandos:
(A+B)*(C+D)*(E+F)
A+((B+C)*(D+E))
A*B*C*D+E+F    """
#Definición de variables


def a_implicita(operacion):
    pilaOperandos = list()
    pilaOperadores = list()
    pilaParentesis = list()

    


    operadores = "+-*/"
    operandos = "ABCDEF"
    valores = [1,2,3,4,5,6]     #Cada valor por defecto corresponde a un operando (letra). Se recomienda cambiar este array para probar distintas ejecuciones del algoritmo


    #Se comprueba que la expresión está bien escrita antes de ejecutar el programa principal

    print(operacion)

    operaciones=0
    operaciones2=0
    operandosSeguidos = False


    for i in operacion:

        if (i in operadores):
            operaciones2+=1

        if (i=='('):
            pilaParentesis.append(i)
            operaciones+=1
        elif (i==')' and len(pilaParentesis)>0):
            pilaParentesis.pop()
        elif (i==')' and len(pilaParentesis)==0):
            pilaParentesis.append("Error")
            break

    if (len(pilaParentesis)==0 and operaciones==operaciones2):      #Si la expresión está totalmente agrupada
        print("La expresión escrita tiene el formato adecuado. Se realizarán", operaciones, "operaciones")
        ejecutar = True
    else:
        print("La expresión escrita no tiene el formato adecuado. Recuerde agrupar completamente todos los términos con paréntesis, de manera que no haya ambigüedad en el orden de operaciones. No se ejecutará el programa principal")
        ejecutar = False


#---------------------------------------------------------------------------------------------- Programa principal ---------------------------------

    if (ejecutar):

        pilaOperadores=list()
        resultado = list()


        for i in range (len(operacion)-1,-1,-1):
        
            if (operacion[i]==')' or operacion[i] in operadores):
                pilaOperadores.append(operacion[i])
            elif (operacion[i] in operandos):
                resultado.append(operacion[i])


            if (operacion[i]=='('):
            
                while (pilaOperadores[len(pilaOperadores)-1] != ')'):

                    resultado.append(pilaOperadores[len(pilaOperadores)-1])
                    pilaOperadores.pop()
                pilaOperadores.pop()
        

        while (len(pilaOperadores)!=0):
            if (pilaOperadores[len(pilaOperadores)-1] in operadores):

                resultado.append(pilaOperadores[len(pilaOperadores)-1])
            pilaOperadores.pop()


        resultado2 = list()

        for i in range (len(resultado)-1,-1,-1):
            resultado2.append(resultado[i])


        print(resultado2)


        for i in range (0,len(resultado2),1):
        
            if (resultado2[i] in operandos):
                resultado2[i] = valores[operandos.index(resultado2[i])]


        print(resultado2)

        for elemento in resultado2:
        


            if (str(elemento) in operadores or type(elemento)==int or type(elemento)==float):
                pilaOperadores.append(elemento)

            print(pilaOperadores)
        

            if (len(pilaOperadores)>2 and (type(pilaOperadores[-1])==int or type(pilaOperadores[-1])==float) and (type(pilaOperadores[-2])==int or type(pilaOperadores[-2])==float)):
            
                if (pilaOperadores[-3]=='+'):
                    variable = pilaOperadores[-1]+pilaOperadores[-2]
                elif (pilaOperadores[-3]=='-'):
                    variable = pilaOperadores[-2]-pilaOperadores[-1]
                elif (pilaOperadores[-3]=='*'):
                    variable = pilaOperadores[-1]*pilaOperadores[-2]
                else:
                    variable = pilaOperadores[-2]/pilaOperadores[-1]

                pilaOperadores.pop()
                pilaOperadores.pop()
                pilaOperadores.pop()
                pilaOperadores.append(variable)

        while (len(pilaOperadores)!=1):

            print(pilaOperadores)

            if ((type(pilaOperadores[-1])==int or type(pilaOperadores[-1])==float) and (type(pilaOperadores[-2])==int or type(pilaOperadores[-2])==float)):
            
                if (pilaOperadores[-3]=='+'):
                    variable = pilaOperadores[-1]+pilaOperadores[-2]
                elif (pilaOperadores[-3]=='-'):
                    variable = pilaOperadores[-2]-pilaOperadores[-1]
                elif (pilaOperadores[-3]=='*'):
                    variable = pilaOperadores[-1]*pilaOperadores[-2]
                else:
                    variable = pilaOperadores[-2]/pilaOperadores[-1]

                pilaOperadores.pop()
                pilaOperadores.pop()
                pilaOperadores.pop()
                pilaOperadores.append(variable)

        res=""
        n=0
        while n<len(resultado):
            res=res+str(resultado[len(resultado)-n-1])+" "
            n=n+1
        print("La ecuacion prefija es " ,res, "y su resultado dados los valores es:" ,pilaOperadores[0])

    

a_implicita("(A+((B+C)*(D+E)))" )    #  **IMPORTANTE**  cada oparacion debe estar encerrada por un parentesis
a_implicita("(((((A*B)*C)*D)+E)+F)")
