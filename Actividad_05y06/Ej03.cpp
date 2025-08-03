/*
Programa: Ej03.cpp
Propósito:
    Utilizando el método encontrarSucesor, escribe un recorrido inorden no recursivo para un árbol
    binario de búsqueda.
Fecha: 02/05/2022
*/


//Incluimos la clase.
#include "Class_ABB_03.hpp"


//Programa principal.
int main()
{
    //Definimos el arbol.
    ArbolBusquedaBinario *arbol = new ArbolBusquedaBinario();

    //Agregamos elementos al arbol.
    arbol->agrega(5, "gato");
    arbol->agrega(1, "leon");
    arbol->agrega(3, "perro");
    arbol->agrega(2, "cerdo");
    arbol->agrega(4, "elefante");

    //Mostramos el arbol utilizando recorrido inorden.
    cout << "Recorrido inorden: " << endl; arbol->inorden();

    //Finalizamos el programa.
    cout << "\nPulsa ENTER para finalizar.";
    cin.ignore();
    return 0;
}