/*
Programa: Class_Operators_01.hpp
Propósito:
    Amplía la función construirArbolAnalisis para que pueda manejar expresiones matemáticas que no
    tienen espacios entre cada carácter.
Fecha: 01/05/2022
*/


#include <iostream>
using namespace std;

//Creamos la clase para los operadores.
class Operador {
    public:
    int add(int x, int y)
    {
        return x + y;
    }

    int sub(int x, int y)
    {
        return x - y;
    }

    int mul(int x, int y)
    {
        return x * y;
    }

    int div(int x, int y)
    {
        return x / y;
    }
};