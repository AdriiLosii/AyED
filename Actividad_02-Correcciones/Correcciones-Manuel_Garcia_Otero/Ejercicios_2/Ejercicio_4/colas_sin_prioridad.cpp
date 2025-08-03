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
        friend class ColaSinPrioridad;

};




class ColaSinPrioridad
{
    public:
        
        ColaSinPrioridad()
        {
            cabeza=NULL;
            longitud=0;
        }

        void concatenate(ColaSinPrioridad x)
        {   
            Nodo *primero = x.cabeza;
            x.cabeza = NULL;

            Nodo *actual = cabeza;

            while (actual->next!=NULL)
            {
                actual = actual->next;
            }

            actual->next = primero;

            longitud += x.length();
        }

        void add(float x)
        {   
            
            if (cabeza==NULL)
            {   
                Nodo *primero = new Nodo(x);
                cabeza = primero;
            }
            else
            {
                Nodo *nuevo = new Nodo(x);
                Nodo *actual = cabeza;

                while (actual->next!=NULL)
                {
                    actual = actual->next;
                }

                actual->next = nuevo;

            }
    
            longitud++;
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

        float advance()
        {
            return extract(0);
        }

        float front()
        {
            return getItemAtIndex(0);
        }

        float back()
        {
            return getItemAtIndex(longitud-1);
        }

        bool isEmpty()
        {
            return (cabeza==NULL);
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
        int longitud;
    
    private: 

        float extract(float x)
        {
            try
            {
                Nodo *actual = cabeza;
                Nodo *previo = NULL;

                if (x>=longitud)
                    throw 1;

                for (int i=0; i<x; i++)
                {   
                    previo = actual;
                    actual = actual->next;
                }

                if (previo==NULL)
                {
                    cabeza = actual->next;
                    actual->next=NULL;
                    longitud--;
                }

                else if (actual!=NULL)
                {
                    previo->next = actual->next;
                    actual->next = NULL;   
                    longitud--;
                }
                return actual->valor;
            }
            catch(...)
            {
                cout<<"ATENCIÓN: la cola está vacía"<<endl;
                return 0;
            }
        }


};

