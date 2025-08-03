#include "Class_Complejo_02.hpp"

int main()
{
    Complejo a(2, 5);
    Complejo b(1, 2);

    cout << "Suma = " << a + b << endl;
    cout << "Resta = " << a - b << endl;
    cout << "Multiplicación = " << a * b << endl;
    cout << "División = " << a / b << endl;
    cout << "Complejo de a = " << a.conjugado() << endl;
    cout << "Complejo de b = " << b.conjugado() << endl;
}