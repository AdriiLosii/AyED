//Programa: Ejercicio_03.cpp
/*
Propósito:
    Modifique el constructor para la clase Fracción de modo que compruebe que el numerador y el 
    denominador sean ambos enteros. Si alguno no es un entero, el constructor debe generar una 
    excepción. Implemente los métodos simples getNum y getDen eso devolverá el numerador y el 
    denominador de una fracción. Implementar los operadores relacionales restantes ( >, >=, <, <=, y !=)
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 17/02/2022


#include "Clase_Fracciones_03.hpp"
using namespace std;

int main()
{
    //Creamos las fracciones
    Fraction x(1, -2);
    Fraction y(2, 3);
    cout << x << " + " << y << " = " << x + y << endl;

    //Mostramos los numeradores y denominadores de las fracciones
    cout << "\nPrimera fracción:" << endl;
    cout << "Numerador: " << x.getNum(x) << "\nDenominador: " << x.getDen(x) << endl;
    cout << "\nSegunda fracción:" << endl;
    cout << "Numerador: " << y.getNum(y) << "\nDenominador: " << y.getDen(y) << endl << endl;

    //Probamos todos los operadores relacionales
    if (x == y)
        cout << "x es igual que y" << endl;
    else
        cout << "x no es igual que y" << endl;

    if (x > y)
        cout << "x es mayor que y" << endl;
    else
        cout << "x no es mayor que y" << endl;

    if (x >= y)
        cout << "x es mayor o igual que y" << endl;
    else
        cout << "x no es mayor o igual que y" << endl;
    
    if (x < y)
        cout << "x es menor que y" << endl;
    else
        cout << "x no es menor que y" << endl;

    if (x <= y)
        cout << "x es menor o igual que y" << endl;
    else
        cout << "x no es menor o igual que y" << endl;

    if (x != y)
        cout << "x es distinto que y" << endl;
    else
        cout << "x no es distinto que y" << endl;

    return 0;
}