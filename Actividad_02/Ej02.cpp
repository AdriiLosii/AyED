//Programa: Ej02.cpp
/*
Propósito:
    Modifica el algoritmo de evaluación en notación sufija para que pueda manejar
    errores y que pueda manejar operandos de más de una cifra int o float
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 12/03/2022

//Incluimos las bibliotecas.
#include <iostream>
#include <stack>
#include <string>
#include <cmath>

using namespace std;

//Definimos las funciones creadas.
float opera_sufijo(string sufijo);
float opera(string operador, float operando1, float operando2);

int main()
{
    string sufijo = "700 -100 + 60.7 -0.7 + /"; //Creamos la expresión sufija.

    cout << sufijo << " = " << opera_sufijo(sufijo) << endl; //Mostramos la expresión y el resultado.

    //Finalizamos el programa.
    cout<<("Pulsa ENTER para finalizar");
    cin.get();
    return 0;
}

//Creamos la función.
float opera_sufijo(string sufijo)
{
    //Definimos las variables.
    stack<string> elementos;
    stack<string> invertida;
    stack<float> pila_operandos;
    string caracteres_validos = "0123456789.+-*/^ ";
    string elemento = "";
    string operadores = "+-*/^";

    for (char caracter : sufijo) //Para cada caracter en la expresión.
    {
        if (caracter == ' ') //Cuando se llega al espacio en blanco añadimos el elemento a la pila.
        {
            elementos.push(elemento);
            elemento = ""; //"Reiniciamos" la variable.
        }
        else
        {
            //Validamos la lectura de datos.
            try
            {
                elemento = elemento + caracter; //Juntamos los caracteres hasta el espacio en blanco para formar los elementos de la expresión.

                if (caracteres_validos.find(caracter) > caracteres_validos.length()) //Si el caracter no es uno de la lista de los elementos válidos.
                {
                    cin.clear();
                    throw 1;
                }
            }
            catch(...)
            {
                printf("\033c"); //Borramos la pantalla
                cout << "\nError, ha ocurrido algo inesperado.\n" << endl;
                exit (-1); //Finalizamos el programa.
            }
        }
    }
    elementos.push(elemento); //Añadimos el último elemento de la expresión.

    //Invertimos el orden de la pila
    while (!elementos.empty())
    {
        invertida.push(elementos.top());
        elementos.pop();
    }

    while (!invertida.empty())
    {
        if (operadores.find(invertida.top()) > operadores.length()) //Si el elemento de la pila no es un operador.
        {
            pila_operandos.push(stof(invertida.top())); //Convertimos el número de string a float y lo añadimos a la pila de operandos.
            invertida.pop();
        }
        else
        {
            //Guardamos el valor del segundo operando en una variable y lo eliminamos de la pila.
            float operando2 = pila_operandos.top();
            pila_operandos.pop();

            //Guardamos el valor del primer operando en una variable y lo eliminamos de la pila.
            float operando1 = pila_operandos.top();
            pila_operandos.pop();

            //Llamamos a la función para que realice la operación correspondiente según el operador encontrado, guardamos el resultado en la pila de resultados y borramos el operador de la expresión.
            float resultado = opera(invertida.top(), operando1, operando2);
            pila_operandos.push(resultado);
            invertida.pop();
        }
    }

    return pila_operandos.top(); //Devolvemos el último valor restante de la pila, es decir, el resultado final.
}

//Creamos la función.
float opera(string operador, float operando1, float operando2)
{
    //Realiza las operaciones dependiendo del operador que se encuentre.
    if (operador == "^")
        return (pow(operando1, operando2));
    else if (operador == "*")
        return (operando1 * operando2);
    else if (operador == "/")
        return (operando1 / operando2);
    else if (operador == "+")
        return (operando1 + operando2);
    else
        return (operando1 - operando2);
}