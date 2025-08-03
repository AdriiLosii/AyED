//Programa: Ej01.cpp
/*
Propósito:
    Escribe una función recursiva para invertir una lista enlazada.
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 28/03/2022


//Incluimos la clase.
#include "Class_Listas_No_Ordenadas_01.hpp"


//Programa principal.
int main()
{
    ListaDesordenada lista;

    //Creamos una lista de 20 elementos y la rellenamos con números aleatorios del 0 al 99.
    for (int i = 0; i < 20; i++)
    {
        lista.agrega(rand() % 100);
    }
    
    cout << "Lista inicial: " << lista << endl;

    lista.invierteLista(); //Llamamos a la función para modificar la lista.

    cout << "Lista invertida: " << lista << endl;

    //Finalizamos el programa.
    cout<<("\nPulsa ENTER para finalizar.");
    cin.get();
    return 0;
}