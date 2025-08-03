/*
Programa: Ej04.cpp
Propósito:
    Modifica la implementación de árbol binario de búsqueda para que maneje correctamente claves
    duplicadas. Es decir, si una clave ya está en el árbol, entonces la nueva carga útil debería sustituir a la
    antigua en lugar de agregar otro nodo con la misma clave.
Fecha: 02/05/2022
*/


//Incluimos la clase.
#include "Class_ABB_04.hpp"


int main()
{
    //Definimos el arbol.
    ArbolBusquedaBinario *arbol = new ArbolBusquedaBinario();

    //Agregamos elementos al arbol.
    arbol->agrega(3, "coche");
    arbol->agrega(4, "moto");
    arbol->agrega(6, "camion");
    arbol->agrega(2, "triciclo");

    cout << "\nElemento en la clave 6 antes: " << arbol->obten(6) << endl;

    //Modificamos el elemento almacenado en la clave 6 y lo mostramos.
    cout << "\n*Modificamos el elemento de la clave 6*" << endl;
    arbol->agrega(6, "trailer");
    
    cout << "\nElemento en la clave 6 ahora: " << arbol->obten(6) << endl;

    //Finalizamos el programa.
    cout << "\nPulsa ENTER para finalizar.";
    cin.ignore();
    return 0;
}