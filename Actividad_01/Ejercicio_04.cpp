//Programa: Ejercicio_04.cpp
/*
Propósito:
    En la definición de fracciones asumimos que las fracciones negativas tienen un numerador negativo 
    y un denominador positivo. El uso de un denominador negativo haría que algunos de los operadores 
    relacionales dieran resultados incorrectos. En general, ésta es una restricción innecesaria. Modifique 
    el constructor para permitir que el usuario pase un denominador negativo y que todos los 
    operadores continúen funcionando correctamente.
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 17/02/2022


#include "Clase_Fracciones_04.hpp"
using namespace std;

int main()
{
    //Creamos las fracciones
    Fraction x(-1, 2);
    Fraction y(2, -4);
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