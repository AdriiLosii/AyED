#include "Ej10_Clase.cpp"

int main()
{

    Fraction x(2, 17);
    Fraction y(2, -4);

    cout << x.getNum() << endl;
    cout << y.getDen() << endl;


    cout << x << " + " << y << " = " << x + y << endl;
    cout << x << " - " << y << " = " << x - y << endl;
    cout << x << " * " << y << " = " << x * y << endl;
    cout << x << " / " << y << " = " << x / y << endl;
    if (x == y){
        cout << "x es igual a y" << endl;}
    else{
        cout << "x no es igual a y" << endl;}

    if (x != y){
        cout << "x no es igual a y" << endl;}
    else{
        cout << "x es igual a y" << endl;}

    if (x <= y){
        cout << "x es menor igual que y" << endl;}
    else{
        cout << "x no es menor igual que y" << endl;}
    
    if (x < y){
        cout << "x es menor que y" << endl;}
    else{
        cout << "x no es menor que y" << endl;}

    if (x >= y){
        cout << "x es mayor igual que y" << endl;}
    else{
        cout << "x no es mayor igual que y" << endl;}

    if (x > y){
        cout << "x es mayor que y" << endl;}
    else{
        cout << "x no es mayor que y" << endl;}

    return 0;
}
