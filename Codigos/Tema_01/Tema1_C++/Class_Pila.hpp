// Pila.hpp: definición de plantilla para pilas


#ifndef TPILA
#define TPILA

// Plantilla para pilas genéricas:
template <class T>
class Pila
{
    // Plantilla para nodos de pila, definición local, sólo accesible para Pila:
    template <class Tn>
    class Nodo
    {
    public:
        Nodo(const Tn &t, Nodo<Tn> *ant) : anterior(ant)
        {
            pT = new Tn(t);
        }
        Nodo(Nodo<Tn> &n)
        { // Constructor copia
            // Invocamos al constructor copia de la clase de Tn
            pT = new Tn(*n.pT);
            anterior = n.anterior;
        }
        ~Nodo() { delete pT; }
        Tn *pT;
        Nodo<Tn> *anterior;
    };
    // Fin de declaración de plantilla de nodo

    // Declaraciones de Pila:
public:
    Pila() : inicio(NULL) {} // Constructor
    ~Pila()
    {
        while (inicio)
            Pop();
    }
    void Push(const T &t)
    {
        Nodo<T> *aux = new Nodo<T>(t, inicio);
        inicio = aux;
    }
    T Pop()
    {
        T temp(*inicio->pT);
        Nodo<T> *aux = inicio;
        inicio = aux->anterior;
        delete aux;
        return temp;
    }
    bool Vacia() { return inicio == NULL; }

private:
    Nodo<T> *inicio;
};

#endif