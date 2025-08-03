#include <iostream>
using namespace std;


class Nodo
{   
    public:
        
        Nodo(float a)
        {
            valor=a;
            next = NULL;
        }

    protected:
        float valor;
        Nodo *next;
        friend class Cola;

};




class Cola
{
    public:
        
        Cola()
        {
            cabeza=NULL;
        }


        void add(float x)
        {   
            if (cabeza==NULL)
            {   
                Nodo *primero = new Nodo(x);
                cabeza = primero;
                ultimo = primero;
                longitud=0;
            }
            else
            {   
                Nodo *nuevo = new Nodo(x);

                if (nuevo->valor < cabeza->valor)
                {
                    nuevo->next = cabeza;
                    cabeza = nuevo;               
                }
                else
                {
                    if (longitud<2)
                    {
                        ultimo->next = nuevo;
                        ultimo = nuevo;         
                    }
                    else
                    {
                        Nodo *actual = cabeza;
                        Nodo *siguiente = cabeza->next;

                        while ((siguiente != NULL) && (nuevo->valor > siguiente->valor))
                        {
                            siguiente = siguiente->next;
                            actual = actual->next;
                        }

                        nuevo->next = siguiente;
                        actual->next = nuevo;

                    }
                }
            }
 
            longitud++;
        }

        float extract()
        {
            Nodo *actual;
            actual = cabeza;

            for (int i=0; i<(longitud-2); i++)
            {
                actual = actual->next;
            }
            float valor = (actual->next)->valor;
            actual->next = NULL;
            longitud--;
            return valor;
        }

        float getItemAtIndex(int index)
        {
            Nodo *actual;
            actual = cabeza;

            for (int i=0; i<index; i++)
            {
                actual = actual->next;
 
            }
            return actual->valor;
        }


        Nodo *getCabeza()
        {
            return cabeza;
        }

        int length()
        {
            return longitud;
        }
    
    protected:
        Nodo *cabeza;
        Nodo *ultimo;
        int longitud;

};

