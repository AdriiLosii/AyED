from Class_Estructuras_lineales_P import Pila


def calculadora_polaca(elementos):
    """ Dada una lista de elementos que representan las componentes de
        una expresión en notacion polaca inversa, evalúa dicha expresión.
        Si la expresion está mal formada, devuelve ValueError. """

    p = Pila()
    for elemento in elementos:
        print("DEBUG:", elemento)
        #Intenta convertirlo a número
        try:
            numero = float(elemento)
            p.incluir(numero)
            print("Pila: ",p)
            print("DEBUG: apila ", numero)
            #Si no se puede convertir a número, debería ser un operando
        except ValueError:
            #Si no es un operando válido, levanta ValueError
            if elemento not in "+-*/%" or len(elemento) != 1:
                raise ValueError("Operando inválido")
            #Si es un operando válido, intenta extraer y operar
            try:
                a1 = p.extraer()
                print("DEBUG: desapila ", a1)
                a2 = p.extraer()
                print("DEBUG: desapila ", a2)
                #Si hubo problemas al desapilar
            except ValueError:
                #print ("DEBUG: error pila faltan operandos")
                raise ValueError("Faltan operandos")

            if elemento == "+":
                resultado = a2 + a1
            elif elemento == "-":
                resultado = a2 - a1
            elif elemento == "*":
                resultado = a2 * a1
            elif elemento == "/":
                resultado = a2 / a1
            elif elemento == "%":
                resultado = a2 % a1
            print("DEBUG: apila ", resultado)
            p.incluir(resultado)
    #Al final, el resultado debe ser lo único en la Pila
    res = p.extraer()
    if p.estaVacia():
        return res
    else:
        #print ("DEBUG: error pila sobran operandos")
        print("Sobran operandos")


expresion = input("Introduzca la expresion a evaluar: ")
elementos = expresion.split()
print(calculadora_polaca(elementos))