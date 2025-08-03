# Tema2_13
from Class_Estructuras_lineales import ColaDoble


def verificarPalindromo(cadena):

    colaDobleCaracteres = ColaDoble()
    for caracter in cadena:
        colaDobleCaracteres.agregarFinal(caracter)

    aunIguales = True

    while colaDobleCaracteres.tamano() > 1 and aunIguales:
        primero = colaDobleCaracteres.borrarFrente()
        ultimo = colaDobleCaracteres.borrarFinal()
        if primero != ultimo:
            aunIguales = False

    return aunIguales


print(verificarPalindromo("lsdkjfskf"))
print(verificarPalindromo("radar"))
