//Incluimos la clase.
#include "Class_ABB_03.hpp"

//Programa principal.
int main()
{
    //Definimos el arbol.
    ArbolBusquedaBinario *arbol = new ArbolBusquedaBinario();

    string arr[12] = {"G","B","Q","A","C","K","F","P","D","E","R","H"};

    //Agregamos elementos al arbol.
    for (int i = 0; i < 12; i++)
    {
        arbol->agrega(i, arr[i]); ////////Va dar resultados distintos con respecto al de python ya que va a queda un arbol muy pesado a un lado ya que las claves van aumentando de uno en uno.
    }

    cout << "Número de nodos en el árbol: " << arbol->nodos() << endl;
    cout << "Número de hojas en el árbol: " << arbol->hojas() << endl;
    cout << "Profundidad del árbol: " << arbol->profundidad() << endl;

    //Finalizamos el programa.
    cout << "\nPulsa ENTER para finalizar.";
    cin.ignore();
    return 0;
}