/*
Programa: Class_NodoArbol_09.hpp
Propósito:
    Implementa la eliminación de un nodo y su posterior actualización y reequilibrio en un árbol AVL.
Fecha: 04/05/2022
*/


//Incluimos los módulos.
#include <iostream>
#include <cstdlib>
#include <cstddef>
#include <string>

using namespace std;

//Creamos la clase.
class NodoArbol
{
    public:
        int clave;
        int balance;
        string valor;
        NodoArbol *hijoIzq;
        NodoArbol *hijoDer;
        NodoArbol *padre;

        //Constructor (con parámetros opcionales).
        NodoArbol(int clave, string valor, NodoArbol *padre = NULL, NodoArbol *izq = NULL, NodoArbol *der = NULL){
            this->clave = clave;
            this->valor = valor;
            this->hijoIzq = izq;
            this->hijoDer = der;
            this->padre = padre;
        }

        //Devuelve un puntero al hijo izquierdo del nodo, si no tiene, devuelve null.
        NodoArbol *tieneHijoIzq(){
            return this->hijoIzq;
        }

        //Devuelve un puntero al hijo derecho del nodo, si no tiene, devuelve null.
        NodoArbol *tieneHijoDer(){
            return this->hijoDer;
        }

        //Devuelve un booleando indicando si este nodo es el hijo izquierdo del nodo o no.
        bool esHijoIzq(){
            return this->padre && this->padre->hijoIzq == this;
        }

        //Devuelve un booleando indicando si este nodo es el hijo derecho del nodo o no.
        bool esHijoDer(){
            return this->padre && this->padre->hijoDer == this;
        }

        //Devuelve un booleando indicando si este nodo es un nodo raiz (no tiene padre).
        bool esRaiz(){
            return !this->padre;
        }

        //Devuelve un booleando indicando si este nodo es un nodo hoja (no tiene hijo izquierdo ni derecho).
        bool esHoja(){
            return !(this->hijoDer || this->hijoIzq);
        }

        //Devuelve un booleando indicando si este nodo tiene algún hijo.
        bool tieneAlgunHijo(){
            return this->hijoDer || this->hijoIzq;
        }

        //Devuelve un booleando indicando si este nodo tiene los dos hijos.
        bool tieneAmbosHijos(){
            return this->hijoDer && this->hijoIzq;
        }

        //Elimina el nodo del árbol en el que está, convirtiéndolo en el nodo raíz de su propio árbol.
        void extraeNodo()
        {
            if (this->esHoja()){
                if (this->esHijoIzq()){
                    this->padre->hijoIzq = NULL;
                }
                else{
                    this->padre->hijoDer = NULL;
                }
            }
            else if (this->tieneAlgunHijo()){
                if (this->tieneHijoIzq()){
                    if (this->esHijoIzq()){
                        this->padre->hijoIzq = this->hijoIzq;
                    }
                    else{
                        this->padre->hijoDer = this->hijoDer;
                    }
                    this->hijoIzq->padre = this->padre;
                }
                else{
                    if (this->esHijoIzq()){
                        this->padre->hijoIzq = this->hijoDer;
                    }
                    else{
                        this->padre->hijoDer = this->hijoDer;
                    }
                    this->hijoDer->padre = this->padre;
                }
            }
        }

        //Devuelve el nodo sucesor a la hora de eliminar un nodo con dos hijos.
        NodoArbol *encuentraSucesor()
        {
            NodoArbol *sucesor = NULL;

            if (this->tieneHijoDer()) //Caso: El nodo tiene un hijo derecho.
            {
                sucesor = this->hijoDer->encuentraMin(); //Sucesor = clave más pequeña en subárbol derecho.
            }
            else
            {
                if (this->padre)
                {
                    if (this->esHijoIzq()) //Caso: El nodo no tiene hijo derecho y es el hijo izquierdo de su padre.
                    {
                        sucesor = this->padre; //Sucesor = padre.
                    }
                    else //Caso: El nodo es hijo derecho de su padre, y éste no tiene hijo derecho.
                    {
                        this->padre->hijoDer = NULL;
                        sucesor = this->padre->encuentraSucesor(); //Sucesor = sucesor de su padre.
                        cout << "This = " << this << endl;
                        this->padre->hijoDer = this;
                    }
                }
            }
            return sucesor;
        }

        //Devuelve el valor minimo del árbol (el valor hoja más a la izquierda).
        NodoArbol *encuentraMin()
        {
            NodoArbol *current = this;

            while (current->tieneHijoIzq()){
                current = current->hijoIzq;
            }
            return current;
        }

        //Modifica las variables del nodo.
        void cambiarValorNodo(int clave, string value, NodoArbol *hijoIzq = NULL, NodoArbol *hijoDer = NULL)
        {
            this->clave = clave;
            this->valor = value;
            this->hijoIzq = hijoIzq;
            this->hijoDer = hijoDer;

            if (this->tieneHijoIzq()){
                this->hijoIzq->padre = this;
            }

            if (this->tieneHijoDer()){
                this->hijoDer->padre = this;
            }
        }
};

