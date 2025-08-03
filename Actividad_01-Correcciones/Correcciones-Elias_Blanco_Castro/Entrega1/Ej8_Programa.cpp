#include "Ej8_Clase.cpp"
int main()
{
    Complejo x(7.5, 5);
    Complejo y(2, -7);

    cout << "Conjugado: " << x.conjugado() << endl;
    cout << "(" << x << ") + (" << y << ") = " << x + y << endl;
    cout << "(" << x << ") - (" << y << ") = " << x - y << endl;
    cout << "(" << x << ") * (" << y << ") = " << x * y << endl;
    cout << "(" << x << ") / (" << y << ") = " << x / y << endl;
    return 0;
}
