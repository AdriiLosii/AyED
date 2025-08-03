// ClasesC_14.cpp: Prueba de plantilla pila
// C con Clase: Marzo de 2002

#include <iostream>
#include "Class_pila.hpp"
#include "Class_Ccadena.hpp"

using namespace std;

// Ejemplo de plantilla de función:
template <class T>
void Intercambia(T &x, T &y)
{
    Pila<T> pila;

    pila.Push(x);
    pila.Push(y);
    x = pila.Pop();
    y = pila.Pop();
}

int main()
{
    Pila<int> PilaInt;
    Pila<Cadena> PilaCad;

    int x = 13, y = 21;
    Cadena cadx("Cadena X");
    Cadena cady("Cadena Y ----");

    cout << "x=" << x << endl;
    cout << "y=" << y << endl;
    Intercambia(x, y);
    cout << "x=" << x << endl;
    cout << "y=" << y << endl;

    cout << "cadx=" << cadx << endl;
    cout << "cady=" << cady << endl;
    Intercambia(cadx, cady);
    cout << "cadx=" << cadx << endl;
    cout << "cady=" << cady << endl;

    PilaInt.Push(32);
    PilaInt.Push(4);
    PilaInt.Push(23);
    PilaInt.Push(12);
    PilaInt.Push(64);
    PilaInt.Push(31);

    PilaCad.Push("uno");
    PilaCad.Push("dos");
    PilaCad.Push("tres");
    PilaCad.Push("cuatro");

    cout << PilaInt.Pop() << endl;
    cout << PilaInt.Pop() << endl;
    cout << PilaInt.Pop() << endl;
    cout << PilaInt.Pop() << endl;
    cout << PilaInt.Pop() << endl;
    cout << PilaInt.Pop() << endl;

    cout << PilaCad.Pop() << endl;
    cout << PilaCad.Pop() << endl;
    cout << PilaCad.Pop() << endl;
    cout << PilaCad.Pop() << endl;

    return 0;
}