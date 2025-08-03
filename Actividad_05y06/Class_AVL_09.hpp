/*
Programa: Class_AVL_09.hpp
Propósito:
    Implementa la eliminación de un nodo y su posterior actualización y reequilibrio en un árbol AVL.
Fecha: 04/05/2022
*/


//Incluimos la clase.
#include "Class_ABB_09.hpp"


//Creamos la clase.
class AVL
{
    private:
        NodoArbol *raiz;
        int tamano;
        int balance;

        //Compara la nueva clave con la almacenada en el nodo actual, si la nueva clave es menor, busca el subarbol izquierdo, sino el derecho.
        //Cuando ya no hay hijo izquierdo (o derecho) que buscar, hemos encontrado la posición correspondiente a la clave dada en el árbol.
        //Para agregar un nodo al arbol, creamos un nuevo objeto "NodoArbol" e insertamos el objeto en la posición descubierta en el paso anterior.
        void _agrega(int clave, string val, NodoArbol *nodoActual)
        {
            if (clave < nodoActual->clave) //Si la clave dada es menor -> hijo izq.
            {
                if (nodoActual->tieneHijoIzq()) //Si ya hay hijo izquierdo en el nodo actual.
                {
                    this->_agrega(clave, val, nodoActual->hijoIzq);
                }
                else
                {
                    nodoActual->hijoIzq = new NodoArbol(clave, val, nodoActual);
                    this->actualizaBalance(nodoActual->hijoIzq);
                }
            }
            else //Si la clave dada es mayor -> hijo der.
            {
                if (nodoActual->tieneHijoDer()) //Si ya hay hijo derecho en el nodo actual.
                {
                    this->_agrega(clave, val, nodoActual->hijoDer);
                }
                else
                {
                    nodoActual->hijoDer = new NodoArbol(clave, val, nodoActual);
                    this->actualizaBalance(nodoActual->hijoDer);
                }
            }
        }

        void _elimina(int clave, NodoArbol *nodoActual)
        {
            if (clave < nodoActual->clave) //Si la clave dada es menor que la clave del nodo actual -> hijo izq.
            {
                this->_elimina(clave, nodoActual->hijoIzq);
            }
            else if (clave > nodoActual->clave) //Si la clave dada es mayor que la clave del nodo actual -> hijo der.
            {
                this->_elimina(clave, nodoActual->hijoDer);
            }
            else if (clave == nodoActual->clave) //Si la clave dada coincide con la clave del nodo actual.
            {
                if (nodoActual->tieneAmbosHijos()) //Si el nodo a borrar tiene ambos hijos.
                {
                    NodoArbol *sucesor = nodoActual->hijoDer->encuentraMin(); //El sucesor será el menor del subárbol derecho.
                    nodoActual->clave = sucesor->clave;
                    this->elimina(sucesor->clave);
                    this->actualizaBalance(nodoActual);
                }
                else //El nodo a borrar tiene uno o ningún hijo.
                {
                    NodoArbol *temp = nodoActual->hijoIzq ? nodoActual->hijoIzq : nodoActual->hijoDer;

                    if (nodoActual->esHoja()) //Si el nodo a borrar no tiene hijos.
                    {
                        temp = nodoActual;
                        nodoActual = NULL;
                        this->actualizaBalance(temp);
                    }
                    else //Si el nodo a borrar tiene solo 1 hijo.
                    {
                        *nodoActual = *temp; //Copiamos el contenido del hijo.
                        this->actualizaBalance(nodoActual);
                    }
                    free(temp);
                }
            }
            else //Si no se encuentra la clave.
            {
                cout << "Error, clave no encontrada en el árbol." << endl;
                return;
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
        AVL()
        {
            this->raiz = NULL;
            this->tamano = 0;
            this->balance = 0;
        }

        //Devuelve el tamaño del arbol.
        int longitud()
        {
            return this->tamano;
        }

        int valorBalance()
        {
            return this->balance;
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

        void elimina(int clave)
        {
            if (this->raiz) //Si el árbol está vacío.
            {
                this->_elimina(clave, this->raiz);
                this->tamano = this->tamano - 1;
            }
            else
            {
                cout << "Error, al eliminar el árbol se encuentra vacío." << endl;
                return;
            }
        }

        //Muestra el valor asociado a la clave dada.
        string obten(int clave)
        {
            if (this->raiz) //Si el árbol no está vacío.
            {
                NodoArbol *res = this->_obten(clave, this->raiz); //Llamamos al método para buscar la clave en el árbol.
                if (res) //Si se encuentra el valor asociado a esa clave.
                {
                    return res->valor;
                }
                else //Si no se encuentra el valor asociado a esa clave.
                {
                    return "Error, clave no encontrada.";
                }
            }
            else //Si el árbol no tiene raiz.
            {
                return "Error, clave no encontrada.";
            }
        }

        void actualizaBalance(NodoArbol *nodo)
        {
            if (nodo->balance > 1 || nodo->balance < -1)
            {
                this->rebalance(nodo);
            }
            if (nodo->padre != NULL)
            {
                if (nodo->esHijoIzq())
                    nodo->padre->balance += 1;

                else if (nodo->esHijoDer())
                    nodo->padre->balance -= 1;

                if (nodo->padre->balance != 0)
                    this->actualizaBalance(nodo->padre);
            }
        }

        void rebalance(NodoArbol *nodo)
        {
            if (nodo->balance < 0) //Nodo actual pesado a la derecha.
            {
                if (nodo->hijoDer->balance > 0) //Hijo derecho del nodo actual pesado a la izquierda.
                {
                    this->rotarDer(nodo->hijoDer);
                    this->rotarIzq(nodo);
                }
                else //Hijo derecho del nodo actual pesado a la derecha.
                {
                    this->rotarIzq(nodo);
                }
            }
            else if (nodo->balance > 0) //Nodo actual pesado a la izquierda.
            {
                if (nodo->hijoIzq->balance < 0) //Hijo izquierdo del nodo actual pesado a la derecha.
                {
                    this->rotarIzq(nodo->hijoIzq);
                    this->rotarDer(nodo);
                }
                else //Hijo izquierdo del nodo actual pesado a la izquierda.
                {
                    this->rotarDer(nodo);
                }
            }
        }

        void rotarIzq(NodoArbol *raizRot)
        {
            NodoArbol *raizNueva = raizRot->hijoDer;
            raizRot->hijoDer = raizNueva->hijoIzq;

            if (raizNueva->hijoIzq != NULL)
            {
                raizNueva->hijoIzq->padre = raizRot;
            }
            raizNueva->padre = raizRot->padre;
            if (raizRot->esRaiz())
            {
                this->raiz = raizNueva;
            }
            else
            {
                if (raizRot->esHijoIzq())
                {
                    raizRot->padre->hijoIzq = raizNueva;
                }
                else
                {
                    raizRot->padre->hijoDer = raizNueva;
                }
            }
            raizNueva->hijoIzq = raizRot;
            raizRot->padre = raizNueva;
            raizRot->balance = raizRot->balance + 1 - min(raizNueva->balance, 0);
            raizNueva->balance = raizNueva->balance + 1 + max(raizRot->balance, 0);
        }

        void rotarDer(NodoArbol *raizRot)
        {
            NodoArbol *raizNueva = raizRot->hijoIzq;
            raizRot->hijoIzq = raizNueva->hijoDer;

            if (raizNueva->hijoDer != NULL)
            {
                raizNueva->hijoDer->padre = raizRot;
            }
            raizNueva->padre = raizRot->padre;
            if (raizRot->esRaiz())
            {
                this->raiz = raizNueva;
            }
            else{
                if (raizRot->esHijoDer())
                {
                    raizRot->padre->hijoDer = raizNueva;
                }
                else
                {
                    raizRot->padre->hijoIzq = raizNueva;
                }
            }
            raizNueva->hijoDer = raizRot;
            raizRot->padre = raizNueva;
            raizRot->balance = raizRot->balance - 1 - min(raizNueva->balance, 0);
            raizNueva->balance = raizNueva->balance - 1 + max(raizRot->balance, 0);
        }
};