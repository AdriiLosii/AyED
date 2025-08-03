//Programa: Clase_Fracciones_10.hpp
/*
Propósito:
    Completar la clase Fracción en C++ para que sea como la desarrollada en Python
Fecha:19/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
*/


#include <iostream>
using namespace std;

class Fraccion
{
    public:
        Fraccion(int arriba, int abajo)
        {
            try{
                if (arriba - int(arriba) == 0 && abajo - int(abajo) == 0) {
                    num = arriba;
                    den = abajo;
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

        int mcd(int m, int n)
        {
            while (m % n != 0)
            {
                int antiguo_m = m;
                int antiguo_n = n;

                m = antiguo_n;
                n = antiguo_m % antiguo_n;
            }
            return n;
        }

        friend ostream &operator<<(ostream &stream, const Fraccion &fraccion);

        //Suma
        Fraccion operator+(Fraccion fraccion)
        {
            int nuevo_num = num * fraccion.den + den * fraccion.num;
            int nuevo_den = den * fraccion.den;
            int comun_div = mcd(nuevo_num, nuevo_den);

            return Fraccion(nuevo_num / comun_div, nuevo_den / comun_div);
        }

        //Resta
        Fraccion operator-(Fraccion fraccion)
        {
            int nuevo_num = num * fraccion.den - den * fraccion.num;
            int nuevo_den = den * fraccion.den;
            int comun_div = mcd(nuevo_num, nuevo_den);

            return Fraccion(nuevo_num / comun_div, nuevo_den / comun_div);
        }

        //Multiplicación
        Fraccion operator*(Fraccion fraccion)
        {
            int nuevo_num = num * fraccion.num;
            int nuevo_den = den * fraccion.den;
            int comun_div = mcd(nuevo_num, nuevo_den);

            return Fraccion(nuevo_num / comun_div, nuevo_den / comun_div);
        }

        //División entera
        Fraccion operator/(Fraccion fraccion)
        {
            int nuevo_num = num * fraccion.den;
            int nuevo_den = den * fraccion.num;
            int comun_div = mcd(nuevo_num, nuevo_den);

            return Fraccion(nuevo_num / comun_div, nuevo_den / comun_div);
        }

        //Igualdad
        bool operator==(Fraccion fraccion)
        {
            int primer_num = num * fraccion.den;
            int segundo_num = fraccion.num * den;

            return primer_num == segundo_num;
        }

    private:
        int num = 1, den = 1;
};

ostream &operator<<(ostream &stream, const Fraccion &fraccion)
{
    stream << fraccion.num << "/" << fraccion.den;

    return stream;
}