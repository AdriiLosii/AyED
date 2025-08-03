#include <iostream>
#include <cstring>
#include <typeinfo>
using namespace std;
int main()
{
    string *x;
    char *y;
    y = new char[10];
    strcpy(y,"Prueba");
    cout << y << endl;
    try {
        x = new string; // si no hay memoria, new lanza la excepcion bad_alloc
        *x = "Otra Prueba";
        cout << *x << endl;
        delete x; // Borrar el string
        delete[] y; // Borrar los 10 chars reservados
    }
    catch (bad_alloc &x)
    {
        cerr << "Error de asignación de memoria." << endl;
    }
}
