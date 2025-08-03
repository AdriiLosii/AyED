#include <iostream>
#include <string>
using namespace std;

class Complejo
{
    public:
        Complejo(float re, float imaginario)
        {
            real = re;
            complejo = imaginario;
        }
        Complejo(int re)
        {
            real = re;
            complejo = 0;
        }
        Complejo()
        {
            real = 0;
            complejo = 0;
        }

        Complejo conjugado()
        {

            return Complejo(real, -complejo);
        }

        Complejo operator+(Complejo complex2)
        {
            float nuevoreal = real + complex2.real;
            float nuevoimag = complejo + complex2.complejo;

            return Complejo(nuevoreal, nuevoimag);
        }

        Complejo operator-(Complejo complex2)
        {
            float nuevoreal = real - complex2.real;
            float nuevoimag = complejo - complex2.complejo;

            return Complejo(nuevoreal, nuevoimag);
        }

        Complejo operator*(Complejo complex2)
        {
            float nuevoreal = (real * complex2.real)-(complejo * complex2.complejo);
            float nuevoimag = (real * complex2.complejo)+(complex2.real * complejo);

            return Complejo(nuevoreal, nuevoimag);
        }

        Complejo operator/(Complejo complex2)
        {
            float denominador = (complex2.real * complex2.real)+(complex2.complejo * complex2.complejo);
            float nuevoreal = ((real * complex2.real)+(complejo * (complex2.complejo)))/denominador;
            float nuevoimag = ((real * -(complex2.complejo))+(complex2.real * complejo))/denominador;

            return Complejo(nuevoreal, nuevoimag);
        }

        friend ostream &operator<<(ostream &stream, const Complejo &complex);

    private:
        float real;
        float complejo;
};

ostream &operator<<(ostream &stream, const Complejo &complex)
{
    if (complex.complejo >= 0){

        stream << complex.real << "+" << complex.complejo << "i";
    }

    else{

        stream << complex.real << complex.complejo << "i";
    }
    

    return stream;
}
