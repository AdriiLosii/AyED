#include <iostream>
using namespace std;

class Complejo
{
    private:
        int real;
        int imaginario;

    public:
        Complejo(int r, int i)
        {
            real = r;
            imaginario = i;
        }

        Complejo operator+(Complejo otroComplejo)
        {
            int nuevoReal = real + otroComplejo.real;
            int nuevoImaginario = imaginario + otroComplejo.imaginario;

            return Complejo(nuevoReal, nuevoImaginario);
        }

        Complejo operator-(Complejo otroComplejo)
        {
            int nuevoReal = real - otroComplejo.real;
            int nuevoImaginario = imaginario - otroComplejo.imaginario;

            return Complejo(nuevoReal, nuevoImaginario);
        }

        Complejo operator*(Complejo otroComplejo)
        {
            int nuevoReal = real * otroComplejo.real;
            int nuevoImaginario = imaginario * otroComplejo.imaginario;

            return Complejo(nuevoReal, nuevoImaginario);
        }

        Complejo operator/(Complejo otroComplejo)
        {
            int nuevoReal = real / (otroComplejo.real + 0.0);
            int nuevoImaginario = imaginario / (otroComplejo.imaginario + 0.0);

            return Complejo(nuevoReal, nuevoImaginario);
        }

        Complejo conjugado()
        {
            int nuevoReal = real;
            int nuevoImaginario = imaginario * (-1);

            return Complejo(nuevoReal, nuevoImaginario);
        }

        friend ostream &operator<<(ostream &stream, const Complejo &complejo);
};

ostream &operator<<(ostream &stream, const Complejo &complejo)
{
    stream << complejo.real << " + " << complejo.imaginario << "i";

    return stream;
}