#include "Class_Fracciones.hpp"
int main()
{
    Fraction x(1, 2);
    Fraction y(2, 4);
    cout << x << " + " << y << " = " << x + y << endl;
    if (x == y)
        cout << "x is equal y" << endl;
    else
        cout << "x is not equal y" << endl;
    return 0;
}
