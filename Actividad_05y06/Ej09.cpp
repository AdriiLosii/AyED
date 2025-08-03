/*
Programa: Ej09.cpp
Propósito:
    Implementa la eliminación de un nodo y su posterior actualización y reequilibrio en un árbol AVL.
Fecha: 04/05/2022
*/


//Incluimos la clase.
#include "Class_AVL_09.hpp"

//Funcion que recorre el árbol.
void preOrder(NodoArbol *raiz)
{
    if(raiz != NULL)
    {
        cout << raiz->clave << " ";
        preOrder(raiz->hijoIzq);
        preOrder(raiz->hijoDer);
    }
}


//Programa principal.
int main()
{
    //Definimos el árbol AVL.
    AVL *arbolAVL = new AVL();

    //Agregamos ítems al árbol y mostramos su longitud.
    arbolAVL->agrega(3, "rojo");
    arbolAVL->agrega(4, "azul");
    arbolAVL->agrega(6, "amarillo");
    arbolAVL->agrega(2, "verde");
    cout << "Longitud del árbol inicialmente: " << arbolAVL->longitud() << endl;

    //Eliminamos ítems y mostramos la longitud del árbol.
    arbolAVL->elimina(2);
    arbolAVL->elimina(4);
    cout << "Longitud del árbol ahora: " << arbolAVL->longitud() << endl;

    //Intentamos obtener ítems.
    cout << "Ítem con clave 3: " << arbolAVL->obten(3) << endl;
    cout << "Ítem con clave 4: " << arbolAVL->obten(4) << endl;

    //Finalizamos el programa.
    cout << "\nPulsa ENTER para finalizar.";
    cin.get();
    return 0;
}