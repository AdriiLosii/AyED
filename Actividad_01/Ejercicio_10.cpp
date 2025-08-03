//Programa: Ejercicio_10.cpp
/*
Propósito:
    Completar la clase Fracción en C++ para que sea como la desarrollada en Python
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 19/02/2022


#include "Clase_Fracciones_10.hpp"
using namespace std;

int main()
{
    Fraccion x(5, 2);
    Fraccion y(2, -4);


    //Mostramos los numeradores y denominadores de las fracciones
    cout << "\nPrimera fracción:" << x << endl;
    cout << "\nSegunda fracción:" << y << "\n" << endl;

    cout << x << " + " << y << " = " << x + y << endl;
    cout << x << " - " << y << " = " << x - y << endl;
    cout << x << " x " << y << " = " << x * y << endl;
    cout << x << " / " << y << " = " << x / y << endl;


    if (x == y)
        cout << "\nx es igual que y" << endl;
    else
        cout << "\nx no es igual que y" << endl;
}