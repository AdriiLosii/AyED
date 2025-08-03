//Programa: Class_Jarras_08.cpp
/*
Propósito:
    Generaliza el programa 2 de esta actividad:
        Tienes dos jarras, una de X litros y otra de Y litros, con X>Y. Ninguna de las jarras
        tiene marcas en ella. Hay una bomba que se puede utilizar para llenar las jarras
        con agua. ¿Cómo se pueden obtener exactamente X/2 litros de agua en la jarra de
        X litros?
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 29/03/2022

//Incluimos las bibliotecas.
#include <iostream>
#include <stack>

using namespace std;

//Creamos la clase de las jarras.
class Jarra
{
    public:
        Jarra(int capacidad_jarra) //Constructor de la jarra.
        {
            capacidad = capacidad_jarra;
        }

        int tamano() //Devuelve la cantidad de litros que hay en la jarra.
        {
            return jarra.size();
        }

        void vierte(int item) //Funcion que apila el elemento dado.
        {
            jarra.push(item);
        }

        void vaciar() //Vacía la jarra.
        {
            //Eliminamos elemento a elemento hasta que su tamaño sea 0.
            while (jarra.size() != 0)
            {
                jarra.pop();
            }
        }

        void llenar() //Llena la jarra.
        {
            //Rellenamos la pila con 1, "tamano_jarra" veces.
            while (jarra.size() < capacidad)
            {
                jarra.push(1);
            }
        }

        void transvasar_a(Jarra &jarra_rellenar) //Transvasa el agua de una jarra a la otra.
        {
            if (jarra.empty()) //Si la jarra que se quiere vaciar ya está vacía.
            {
                std::cout << "La jarra de la que quieres trasvasar el agua está vacía." << endl;
            }

            else
            {
                while (!jarra.empty() and jarra_rellenar.tamano() < jarra_rellenar.capacidad) //Mientras que la jarra que se quiere vaciar no esté vacía y la jarra que se quiere rellenar no esté llena.
                {
                    //Rellenamos la segunda jarra a la vez que vaciamos la primera.
                    jarra_rellenar.vierte(jarra.top());
                    jarra.pop();
                }
            }
        }
    
    private:
        stack<int> jarra;
        int capacidad;
};