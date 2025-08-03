#include <iostream>
#include <string>


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
        Fraction(int top, int bottom)
        {
            try
            {

                if (sizeof(top) == sizeof(int) && sizeof(bottom) == sizeof(int) && bottom != 0){

                    num = top;
                    den = bottom;
                }
                
                else{
                    throw 20;
                }

                if (den < 0){

                    num = num *-1;
                    den = den*-1;
            }

                
            }
            catch(int e)
            {
                cout << "Entrada no valida" << endl;
            }
        }

        Fraction(int top)
        {
           try
            {

                if (sizeof(top) == sizeof(int)){
                    num = top;
                    den = 1;

                }

                else {
                    throw 20;
                }
                
            }
            catch(int e)
            {
                cout << "Entrada no valida" << endl;
            }
        }

        Fraction()
        {
            num = 1;
            den = 1;
        }

        Fraction getNum()
        {
            return num;
        }

        Fraction getDen()
        {
            return den;   

        }

        Fraction operator+(Fraction otherFrac)
        {
            int newnum = num * otherFrac.den + den * otherFrac.num;
            int newden = den * otherFrac.den;
            int common = gcd(newnum, newden);

            return Fraction(newnum / common, newden / common);
        }

        Fraction operator-(Fraction otherFrac)
        {
            
            int newnum = num * otherFrac.den - den * otherFrac.num;
            int newden = den * otherFrac.den;
            int common = gcd(newnum, newden);

            return Fraction(newnum / common, newden / common);
        }
        Fraction operator*(Fraction otherFrac)
        {
            
            int newnum = num * otherFrac.den * num * otherFrac.num;
            int newden = den * otherFrac.den * num * otherFrac.den;
            int common = gcd(newnum, newden);

            return Fraction(newnum / common, newden / common);
        }
        Fraction operator/(Fraction otherFrac)
        {
            
            
            int newnum = den * otherFrac.num / den * otherFrac.num;
            int newden = den * otherFrac.num ;
            int common = gcd(newnum, newden);

            return Fraction(newnum / common, newden / common);
        }

        bool operator==(Fraction &otherFrac)
        {
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum == secondnum;
        }

        bool operator!=(Fraction &otherFrac)
        {
            
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum != secondnum;
        }

        bool operator<=(Fraction &otherFrac)
        {
            
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum <= secondnum;
        }

        bool operator<(Fraction &otherFrac)
        {
            
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum < secondnum;
        }

        bool operator>=(Fraction &otherFrac)
        {
            
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum >= secondnum;
        }

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
    if (fraction.den != 1){
    stream << fraction.num << "/" << fraction.den;
    }
    else{
        stream << fraction.num;
    }
    return stream;
}
