/*
Programa: Ej05.cpp
Propósito:
    Modifica la función imprimirExpresion para que no incluya un par de paréntesis ‘extra’ alrededor de
    cada número.
Fecha: 02/05/2022
*/

//Incluimos las bibliotecas.
#include "Class_ArbolBinario_05.hpp"

//Definimos las funciones creadas.
string imprimirExpresion(ArbolBinario *arbol);


int main()
{
    //Definimos el arbol.
    ArbolBinario *arbol = new ArbolBinario("raiz");

    //Agregamos elementos al arbol.
    arbol->insertaIzq("hijoIzq");
    arbol->insertaDer("hijoDer");
    arbol->insertaIzq("padreIzq");
    arbol->insertaDer("padreDer");

    cout << imprimirExpresion(arbol) << endl;

    //Finalizamos el programa.
    cout << "\nPulsa ENTER para finalizar.";
    cin.get();
    return 0;
}


//Creamos la función para mostrar la expresión.
string imprimirExpresion(ArbolBinario *arbol)
{
    string cadena;

    if (arbol)
    {
        cadena = " " + imprimirExpresion(arbol->obtenHijoIzq());
        cadena += arbol->obtenRaiz();
        cadena += imprimirExpresion(arbol->obtenHijoDer()) + " ";
    }

    return cadena;
}