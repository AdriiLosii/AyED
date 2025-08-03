/*
Programa: Class_ABB_04.cpp
Propósito:
    Modifica la implementación de árbol binario de búsqueda para que maneje correctamente claves
    duplicadas. Es decir, si una clave ya está en el árbol, entonces la nueva carga útil debería sustituir a la
    antigua en lugar de agregar otro nodo con la misma clave.
Fecha: 02/05/2022
*/


#include "Class_NodoArbol_04.hpp"

class ArbolBusquedaBinario
{
    private:
        NodoArbol *raiz;
        int tamano;

        //Compara la nueva clave con la almacenada en el nodo actual, si la nueva clave es menor, busca el subarbol izquierdo, sino el derecho.
        //Cuando ya no hay hijo izquierdo (o derecho) que buscar, hemos encontrado la posición correspondiente a la clave dada en el árbol.
        //Para agregar un nodo al arbol, creamos un nuevo objeto "NodoArbol" e insertamos el objeto en la posición descubierta en el paso anterior.
        void _agrega(int clave, string val, NodoArbol *nodoActual)
        {
            if (clave == nodoActual->clave) //Si la clave dada coincide con la clave almacenada.
            {
                nodoActual->valor = val; //Modificamos el valor almacenado en el nodo.
            }
            else if (clave < nodoActual->clave) //Si la clave dada es menor -> hijo izq.
            {
                if (nodoActual->tieneHijoIzq())
                {
                    this->_agrega(clave, val, nodoActual->hijoIzq);
                }
                else
                {
                    nodoActual->hijoIzq = new NodoArbol(clave, val, nodoActual);
                }
            }
            else //Si la clave dada es mayor o igual -> hijo der.
            {
                if (nodoActual->tieneHijoDer())
                {
                    this->_agrega(clave, val, nodoActual->hijoDer);
                }
                else
                {
                    nodoActual->hijoDer = new NodoArbol(clave, val, nodoActual);
                }
            }
        }

        //Funciona de la misma manera que "_agrega".
        NodoArbol  *_obten(int clave, NodoArbol *nodoActual){
            if (!nodoActual) //Si llegamos al final del recorrido sin éxito, devolvemos NULL.
            {
                return NULL;
            }
            else if (nodoActual->clave == clave) //Si la clave dada es la actual, devolvemos el valor almacenado en el nodo.
            {
                return nodoActual;
            }
            else if (clave < nodoActual->clave) //Si la clave dada es menor que el valor del nodo actual, nos desplazamos al hijo izquierda (valor menor).
            {
                return this->_obten(clave, nodoActual->hijoIzq);
            }
            else //Si la clave dada es mayor que el valor del nodo actual, nos desplazamos al hijo derecho (valor mayor).
            {
                return this->_obten(clave, nodoActual->hijoDer);
            }
        }

    public:
        //Constructor.
        ArbolBusquedaBinario()
        {
            this->raiz = NULL;
            this->tamano = 0;

        }

        //Devuelve el tamaño del arbol.
        int longitud(){
            return this->tamano;
        }

        //Comprueba si el árbol tiene raiz, si no tiene raiz, crea una nueva y la asigna como raiz del árbol.
        //Si el árbol ya tiene raiz, entonces llama a la función "_agrega", para recorrer el árbol.
        void agrega(int clave, string valor)
        {
            if (this->raiz) //Si ya tiene raiz.
            {
                this->_agrega(clave, valor, this->raiz);
            }
            else //Si no tiene raiz.
            {
                this->raiz = new NodoArbol(clave, valor);
            }
            this->tamano = this->tamano + 1;
        }

        //Muestra el valor asociado a la clave dada.
        string obten(int clave)
        {
            if (this->raiz) //Si el árbol tiene raiz.
            {
                NodoArbol *res = this->_obten(clave, this->raiz); //Llamamos al método para buscar la clave en el árbol.
                if (res) //Si se encuentra el valor asociado a esa clave.
                {
                    return res->valor;
                }
                else //Si no se encuentra el valor asociado a esa clave.
                {
                    return 0;
                }
            }
            else //Si el árbol no tiene raiz.
            {
                return 0;
            }
        }

        //Comprueba que la clave de la raiz coincide con la clave solicitada a borrar.
        //Si la clave no se encuentra, ocurre un error.
        //Si el nodo tiene un solo hijo, el hijo pasa a ser el padre.
        void borra(int clave)
        {
            if (this->tamano > 1) //Si el árbol tiene más nodos además de la raiz.
            {
                NodoArbol *nodoBorrar = this->_obten(clave, this->raiz); //Llamamos a la función para obtener la dirección de memoria del nodo que se quiere borrar.
                if (nodoBorrar) //Si se encuentra el nodo a borrar.
                {
                    this->elimina(nodoBorrar); //Llamamos a la función para eliminar el nodo con la clave solicitada.
                    this->tamano = this->tamano - 1;
                }
                else
                {
                    cerr << "Error, la clave introducida no se encuentra en el árbol." << endl;
                }
            }
            else if (this->tamano == 1 && this->raiz->clave == clave) //Si el árbol solo está formado por el nodo raíz y la clave coincide con la clave de este.
            {
                this->raiz = NULL;
                this->tamano = this->tamano - 1;
            }
            else //Si el árbol solo está formado por el nodo raiz pero la clave no coincide.
            {
                cerr << "Error, la clave introducida no se encuentra en el árbol." << endl;
            }
        }

        void elimina(NodoArbol *nodoActual)
        {
            if (nodoActual->esHoja()) //Si el nodo es un nodo hoja.
            {
                if (nodoActual == nodoActual->padre->hijoIzq)
                {
                    nodoActual->padre->hijoIzq = NULL;
                }
                else
                {
                    nodoActual->padre->hijoDer = NULL;
                }
            }
            else if (nodoActual->tieneAmbosHijos()) //Si el nodo tiene hijo derecho e izquierdo.
            {
                NodoArbol *sucesor = nodoActual->encuentraSucesor(); //Llamamos al método para encontrar el sucesor (que hijo pasará a ser padre).
                sucesor->extraeNodo();
                nodoActual->clave = sucesor->clave;
                nodoActual->valor = sucesor->valor;
            }
            else //Si el nodo tiene solo 1 hijo.
            {
                if (nodoActual->tieneHijoIzq()) //Si el hijo es izquierdo.
                {
                    if (nodoActual->esHijoIzq()) //Caso: El hijo izquierdo tiene un hijo izquierdo.
                    {
                        nodoActual->hijoIzq->padre = nodoActual->padre;
                        nodoActual->padre->hijoIzq = nodoActual->hijoIzq;
                    }
                    else if (nodoActual->esHijoDer()) //Caso: El hijo izquierdo tiene un hijo derecho.
                    {
                        nodoActual->hijoIzq->padre = nodoActual->padre;
                        nodoActual->padre->hijoDer = nodoActual->hijoIzq;
                    }
                    else //Caso: El hijo izquierdo tiene ambos hijos.
                    {
                        nodoActual->cambiarValorNodo(nodoActual->hijoIzq->clave,
                                                     nodoActual->hijoIzq->valor,
                                                     nodoActual->hijoIzq->hijoIzq,
                                                     nodoActual->hijoIzq->hijoDer);

                    }
                }
                else //Si el hijo es derecho.
                {
                    if (nodoActual->esHijoIzq()) //Caso: El hijo derecho tiene un hijo izquierdo.
                    {
                        nodoActual->hijoDer->padre = nodoActual->padre;
                        nodoActual->padre->hijoIzq = nodoActual->hijoDer;
                    }
                    else if (nodoActual->esHijoDer()) //Caso: El hijo derecho tiene un hijo derecho.
                    {
                        nodoActual->hijoDer->padre = nodoActual->padre;
                        nodoActual->padre->hijoDer = nodoActual->hijoDer;
                    }
                    else //Caso: El hijo derecho tiene ambos hijos.
                    {
                        nodoActual->cambiarValorNodo(nodoActual->hijoDer->clave,
                                                     nodoActual->hijoDer->valor,
                                                     nodoActual->hijoDer->hijoIzq,
                                                     nodoActual->hijoDer->hijoDer);
                    }
                }
            }
        }
};