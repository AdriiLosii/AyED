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

//creamos la clase Fraction
class Fraction
{

//definimos las dos variables que vamos a tener
public:
    Fraction(int top, int bottom)
    {
        num = top;
        den = bottom;
    }
    Fraction(int top)
    {
        num = top;
        den = 1;
    }
    Fraction()
    {
        num = 1;
        den = 1;
    }

    //definimos la suma de fracciones
    Fraction operator+(Fraction otherFrac)
    {
        int newnum = num * otherFrac.den + den * otherFrac.num;
        int newden = den * otherFrac.den;
        int common = gcd(newnum, newden);

        return Fraction(newnum / common, newden / common);
    }

    //definimos la resta de fracciones
    Fraction operator-(Fraction otherFrac)
    {
        int newnum = num * otherFrac.den - den * otherFrac.num;
        int newden = den * otherFrac.den;
        int common = gcd(newnum, newden);

        return Fraction(newnum / common, newden / common);
    }

    //definimos la multiplicacion de fracciones
    Fraction operator*(Fraction otherFrac)
    {
        int newnum = num * otherFrac.num;
        int newden = den * otherFrac.den;

        return Fraction(newnum, newden);
    }

    //definimos la division de fracciones
    Fraction operator/(Fraction otherFrac)
    {
        int newnum = num * otherFrac.den;
        int newden = den * otherFrac.num;

        return Fraction(newnum, newden);
    }

    //funcion que comprueba si son distintas ambas fracciones
    bool operator!=(Fraction &otherFrac)
    {
        int firstnum = num * otherFrac.den;
        int secondnum = otherFrac.num * den;

        return firstnum != secondnum;
    }

    //funcion que comprueba si la fraccion1 es mayor
    bool operator>(Fraction &otherFrac)
    {
        int firstnum = num * otherFrac.den;
        int secondnum = otherFrac.num * den;

        return firstnum > secondnum;
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
