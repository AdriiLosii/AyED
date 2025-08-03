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
            longitud=0;
        }


        void add(float x)
        {   
            if (cabeza==NULL)
            {   
                Nodo *primero = new Nodo(x);
                cabeza = primero;
                temp = primero;
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
                        temp->next = nuevo;
                        temp = nuevo;         
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


        void del(float x)
        {
            Nodo *actual = cabeza;
            Nodo *previo = NULL;

            while ((actual!=NULL) && actual->valor!=x)
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
                actual->next=NULL;
                longitud--;
            }
            else
            {
                cout<<"ATENCIÓN: el elemento "<<x<<" no se encuentra en la cola. No se realizarán cambios"<<endl;
            }
        }

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
                cout<<"ERROR: el índice "<<x<<" está fuera de límites"<<endl;
                return 0;
            }
            
        }

        float extract()
        {
            return extract(longitud-1);
        }

        bool search(float x)
        {   
            Nodo *actual = cabeza;

            while (actual!=NULL)
            {   
                if (actual->valor==x)
                { 
                    return true;
                }
                actual = actual->next;
            }
            return false;
        }

        bool isEmpty()
        {
            return (cabeza==NULL);
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
        Nodo *temp;
        int longitud;

};

