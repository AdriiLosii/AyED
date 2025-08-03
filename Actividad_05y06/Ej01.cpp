/*
Programa: Ej01.cpp
Propósito:
    Amplía la función construirArbolAnalisis para que pueda manejar expresiones matemáticas que no
    tienen espacios entre cada carácter.
Fecha: 01/05/2022
*/


//Incluimos los módulos.
#include <iostream>
#include <sstream>
#include <stack>
#include "Class_ArbolBinario_01.hpp"
#include "Class_Operators_01.hpp"


//Definimos las funciones creadas.
ArbolBinario *construirArbolAnalisis(string expresion);
void postorden(ArbolBinario *arbol);
string postordereval(ArbolBinario *arbol);
int a_int(string str);
string a_string(int num);


//Programa principal.
int main()
{
    //Definimos la expresión a implementar en forma de arbol.
    ArbolBinario *arbol = construirArbolAnalisis("((10+5)*3)");

    //Mostramos el recorrido postorden del árbol y su resultado.
    cout << "Recorrido postorden del arbol:" << endl;
    postorden(arbol);
    cout << "Resultado: " << postordereval(arbol) << endl;

    //Finalizamos el programa.
    cout << "\nPulse ENTER para finalizar.";
    cin.ignore();
    return 0;
}


//Creamos la función que construye el árbol de análisis a partir de la expresión dada.
ArbolBinario *construirArbolAnalisis(string expresion)
{
    //Rellenamos el array con los caracteres de la expresión (ignorando los posibles espacios introducidos).
    string arr_expr[expresion.size()];
    string digitos = "0123456789.";
    string caracteres_validos = "+-*/^()";
    string numero = "";
    int i = 0;
    int j = 0;

    while (i<expresion.size())
    {
        if (expresion[i] != ' ')
        {
            try //Lectura de datos validada.
            {
                if (digitos.find(expresion[i]) < digitos.length()) //Si es un número.
                {
                    while (digitos.find(expresion[j]) < digitos.length())
                    {
                        numero += expresion[j];
                        j += 1;
                    }

                    arr_expr[i] = numero;
                    i = j;
                    numero = "";
                }

                else if (caracteres_validos.find(expresion[i]) < caracteres_validos.length()) //Si no es un número.
                {
                    arr_expr[i] = expresion[i];
                    i += 1;
                    j = i;
                }

                //Si el caracter actual no es ninguno de los incluidos en las cadenas de caracteres.
                else if (digitos.find(expresion[i]) > digitos.length() or caracteres_validos.find(expresion[i]) > caracteres_validos.length())
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

    stack<ArbolBinario*> pila; //Creamos una pila para guardar los distintos operandos y operadores.

    //Definimos el arbol.
    ArbolBinario *arbol = new ArbolBinario("");
    pila.push(arbol);
    ArbolBinario *arbol_actual = arbol;

    string operadores = "+-*/^";

    //Recorremos el array elemento a elemento
    for (unsigned int i = 0; i < expresion.size(); i++)
    {
        if (arr_expr[i] == "(")
        {
            arbol_actual->insertaIzq("");
            pila.push(arbol_actual);
            arbol_actual = arbol_actual->obtenHijoIzq();
        }

        else if (arr_expr[i] == ")")
        {
            arbol_actual = pila.top();
            pila.pop();
        }

        else if (operadores.find(arr_expr[i]) > operadores.length()) //Si es un operando (es decir, no pertenece al string de los operadores).
        {
            try {
                arbol_actual->estableceRaiz(arr_expr[i]);
                ArbolBinario *padre = pila.top();
                pila.pop();
                arbol_actual = padre;
            }

            catch (string ValueError ){
                cerr <<"El caracter " << arr_expr[i] << " no es un iterador válido."<<endl;
            }
        }

        else if (caracteres_validos.find(expresion[i]) > caracteres_validos.length()) //Si es otro caracter (un espacio en blanco), lo ignoramos.
            continue;

        else if (operadores.find(arr_expr[i]) < operadores.length()) //Si es un operador.
        {
            arbol_actual->estableceRaiz(arr_expr[i]);
            arbol_actual->insertaDer("");
            pila.push(arbol_actual);
            arbol_actual = arbol_actual->obtenHijoDer();
        }
    }

    return arbol;
}

//Función que recorre el arbol postorden.
void postorden(ArbolBinario *arbol)
{
    if (arbol != NULL){
        postorden(arbol->obtenHijoIzq());
        postorden(arbol->obtenHijoDer());
        cout << arbol->obtenRaiz() << endl;
    }
}

//Función que analiza el arbol y realiza la operación.
string postordereval(ArbolBinario *arbol)
{
    Operador Oper;
    ArbolBinario *res1 = arbol->obtenHijoIzq();
    ArbolBinario *res2 = arbol->obtenHijoDer();
    if (arbol) 
    {
        if (res1 && res2) 
        {
            if (arbol->obtenRaiz() == "+")
                return a_string(Oper.add(a_int(postordereval(res1)), a_int(postordereval(res2))));

            else if (arbol->obtenRaiz() == "-")
                return a_string(Oper.sub(a_int(postordereval(res1)), a_int(postordereval(res2))));

            else if (arbol->obtenRaiz() == "*")
                return a_string(Oper.mul(a_int(postordereval(res1)), a_int(postordereval(res2))));

            else
                return a_string(Oper.div(a_int(postordereval(res1)), a_int(postordereval(res2))));
        } 
        else
            return arbol->obtenRaiz();
    }
    else
    {
        return "Error, ha ocurrido algo inesperado."; //Este return es simplemente para que no salte un "warning: control reaches end o non-void function".
    }
}

//Función auxiliar para convertir string en int.
int a_int(string str)
{
    stringstream convierte(str);
    int x = 0;
    convierte >> x;
    return x;
}

//Función auxiliar para convertir int en string.
string a_string(int num)
{
    string str;
    ostringstream convierte;
    convierte << num;
    str = convierte.str();
    return str;
}