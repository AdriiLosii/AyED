//Programa: Clase_Fracciones_04.hpp
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


#include <iostream>
using namespace std;

int gcd(int m, int n)
{
    while (m % n != 0)
    {
        int oldm = m;
        int oldn = n;

        m = oldn;
        n = oldm % oldn;
    }
    return n;
}

class Fraction
{
    public:
        Fraction(float top, float bottom)
        {
            try{
                if (top - int(top) == 0 && bottom - int(bottom) == 0) {
                    num = top;

                    //Si introducen un den negativo lo pasamos a positivo.
                    if (den > 0)
                        den = bottom;
                    else
                        den = bottom*(-1);
                }
                else
                    throw 1;
            }
            catch (...){
                cout << "\nError, introduzca números enteros." << endl;
                cout << "Pulse ENTER para finalizar." << endl;
                cin.ignore();
                exit(-1); //Finalizamos el programa
            }
        }
        Fraction(float top)
        {
            try{
                if (top - int(top) == 0) {
                    num = top;
                    den = 1;
                }
                else
                    throw 1;
            }
            catch (...){
                cout << "\nError, introduzca números enteros." << endl;
                cout << "Pulse ENTER para finalizar." << endl;
                cin.ignore();
                exit(-1); //Finalizamos el programa
            }
        }
        Fraction()
        {
            num = 1;
            den = 1;
        }

        int getNum(Fraction &fraccion)
        {
            int nuevo_num = fraccion.num;

            return nuevo_num;
        }

        int getDen(Fraction &fraccion)
        {
            int nuevo_den = fraccion.den;

            return nuevo_den;
        }

        Fraction operator+(Fraction otherFrac)
        {
            int newnum = num * otherFrac.den + den * otherFrac.num;
            int newden = den * otherFrac.den;
            int common = gcd(newnum, newden);

            return Fraction(newnum / common, newden / common);
        }

        bool operator==(Fraction &otherFrac)
        {
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum == secondnum;
        }

        //Creamos los operadores.

        //Para poder obtener los resultados decimales, al trabajar en C++, necesitaremos que uno de los 
        //valores de la división sea un número decimal, para conseguir esto multiplicamos el numerador por 0.1. 
        //Después de esto multiplicamos el resultado por 10 para obtener el valor correcto de la división inicial.
        bool operator>(Fraction &segundaFraccion)
        {
            float valor1 = (num*0.1 / den)*10;
            float valor2 = (segundaFraccion.num*0.1 / segundaFraccion.den)*10;

            return valor1 > valor2;
        }

        bool operator>=(Fraction &segundaFraccion)
        {
            float valor1 = (num*0.1 / den)*10;
            float valor2 = (segundaFraccion.num*0.1 / segundaFraccion.den)*10;

            return valor1 >= valor2;
        }

        bool operator<(Fraction &segundaFraccion)
        {
            float valor1 = (num*0.1 / den)*10;
            float valor2 = (segundaFraccion.num*0.1 / segundaFraccion.den)*10;

            return valor1 < valor2;
        }

        bool operator<=(Fraction &segundaFraccion)
        {
            float valor1 = (num*0.1 / den)*10;
            float valor2 = (segundaFraccion.num*0.1 / segundaFraccion.den)*10;

            return valor1 <= valor2;
        }

        bool operator!=(Fraction &segundaFraccion)
        {
            float valor1 = (num*0.1 / den)*10;
            float valor2 = (segundaFraccion.num*0.1 / segundaFraccion.den)*10;

            return valor1 != valor2;
        }

        friend ostream &operator<<(ostream &stream, const Fraction &fraction);

    private:
        int num, den;
};

ostream &operator<<(ostream &stream, const Fraction &fraction)
{
    stream << fraction.num << "/" << fraction.den;

    return stream;
}