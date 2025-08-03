/*
Programa: Class_ArbolBinario_01.hpp
Propósito:
    Amplía la función construirArbolAnalisis para que pueda manejar expresiones matemáticas que no
    tienen espacios entre cada carácter.
Fecha: 01/05/2022
*/


#include <iostream>
#include <string>
using namespace std;


//Crea un arbol binario.
class ArbolBinario
{
private:
    string clave;
    ArbolBinario *hijoIzq;
    ArbolBinario *hijoDer;

public:
    ArbolBinario(string raiz) //Constructor, necesita un valor inicial como valor raiz.
    {
        this->clave = raiz;
        this->hijoIzq = NULL;
        this->hijoDer = NULL;
    }

    void estableceRaiz(string valorRaiz) //Función que asigna el valor dado como raiz del arbol.
    {
        this->clave = valorRaiz;
    }

    void insertaIzq(string valor) //Inserta el valor dado como hijo izquierdo.
    {
        if (this->hijoIzq == NULL) //Si no hay hijo izquierdo, crea uno.
            this->hijoIzq = new ArbolBinario(valor);

        else //Si ya hay hijo izquierdo, lo inserta.
        {
            ArbolBinario *aux = new ArbolBinario(valor);
            aux->hijoIzq = this->hijoIzq;
            this->hijoIzq = aux;
        }
    }

    void insertaDer(string valor) //Inserta el valor dado como hijo derecho.
    {
        if (this->hijoDer == NULL) //Si no hay hijo derecho, crea uno.
            this->hijoDer = new ArbolBinario(valor);

        else //Si ya hay hijo derecho, lo inserta
        {
            ArbolBinario *aux = new ArbolBinario(valor);
            aux->hijoDer = this->hijoDer;
            this->hijoDer = aux;
        }
    }

    string obtenRaiz() //Devuelve el valor de la raiz.
    {
        return this->clave;
    }

    ArbolBinario *obtenHijoIzq() //Devuelve el valor del hijo izquierdo.
    {
        return this->hijoIzq;
    }

    ArbolBinario *obtenHijoDer() //Devuelve el valor del hijo derecho.
    {
        return this->hijoDer;
    }
};

