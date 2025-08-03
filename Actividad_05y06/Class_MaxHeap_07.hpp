/*
Programa: Class_MaxHeap_07.hpp
Propósito:
    Implementa un montículo binario como un montículo máx.
Fecha: 03/05/2022
*/


//Inlcuimos las librerías.
#include <iostream>
#include <vector>

using namespace std;


//Utiliza un vector para crear un montículo binario.
class MonticuloBinario
{
private:
    vector<int> vector_monticulo;
    int tamano_actual;

public:
    //Constructor.
    MonticuloBinario(vector<int> vector_monticulo)
    {
        this->vector_monticulo = vector_monticulo;
        this->tamano_actual = 0;
    }

    //Construye un montículo a partir de un vector dado.
    void construyeMonticulo(vector<int> vector)
    {
        int i = vector.size() / 2;
        this->tamano_actual = vector.size();
        this->vector_monticulo.insert(this->vector_monticulo.end(), vector.begin(), vector.end());
        while (i > 0)
        {
            this->infiltAbajo(i);
            i = i - 1;
        }
    }

    //Muestra el el vector del montículo.
    void mostrarMonticulo()
    {
        for (unsigned i = 1; i < this->tamano_actual+1; i++) 
            cout<<this->vector_monticulo[i]<<" ";
        cout<<endl;
    }

    //Agrega un número al final del vector.
    void agrega(int num)
    {
        this->vector_monticulo.push_back(num);
        this->tamano_actual = this->tamano_actual + 1;
        this->infiltArriba(this->tamano_actual);
    }

    //Preubica el elemento lo más arriba posible
    //en el árbol para mantener la propiedad de montículo.
    void infiltArriba(int tamano_actual)
    {
        while ((tamano_actual / 2) > 0) //Mientras haya padre (hacia arriba).
        {
            if (this->vector_monticulo[tamano_actual] > this->vector_monticulo[tamano_actual/2]) //Si el valor del hijo izquierdo es mayor que el del padre, los intercambiamos.
            {
                int tmp = this->vector_monticulo[tamano_actual/2];
                this->vector_monticulo[tamano_actual/2] = this->vector_monticulo[tamano_actual];
                this->vector_monticulo[tamano_actual] = tmp;
            }
            tamano_actual = tamano_actual/2; //Pasamos al siguiente nodo padre.
        }
    }

    //Borra el valor máximo del montículo (valor situado en la raíz del montículo),
    //para restablecer el orden del montículo, se coge el último ítem y se posiciona
    //en la raíz, a continuación se reposiciona en su lugar correspondiente.
    void borraMax()
    {
        if (this->estaVacio()) //Si el montículo está vacío.
        {
            cout << "Error al intentar borrar máximo: el montículo se encuentra vacío." << endl;
        }
        else
        {
            int raiz = this->vector_monticulo[1]; //El número con mayor valor siempre será la raíz del montículo.
            this->vector_monticulo[1] = this->vector_monticulo[this->tamano_actual];
            this->vector_monticulo.pop_back();
            this->tamano_actual = this->tamano_actual - 1;
            this->infiltAbajo(1);
            cout << "Número borrado: " << raiz << endl;
        }
    }

    //Preubica el elemento lo más arriba posible
    //en el árbol para mantener la propiedad de montículo.
    void infiltAbajo(int i)
    {
        while ((i*2) <= this->tamano_actual) //Mientras que haya padre (hacia abajo).
        {
            int pos_max_hijo = this->maxHijo(i);
            if (this->vector_monticulo[i] < this->vector_monticulo[pos_max_hijo]) //Si el valor de la raiz es menor que el valor del hijo con máximo valor, los intercambiamos.
            {
                int tmp = this->vector_monticulo[i];
                this->vector_monticulo[i] = this->vector_monticulo[pos_max_hijo];
                this->vector_monticulo[pos_max_hijo] = tmp;
            }
            i = pos_max_hijo;
        }
    }

    //Devuelve la posición del hijo con mayor valor.
    int maxHijo(int i)
    {
        if ((i*2) > this->tamano_actual) //Si la posición del hijo izquierdo es mayor que el tamaño actual.
        {
            return (i * 2) + 1; //Devolvemos el hijo derecho.
        }
        else
        {
            if (this->vector_monticulo[i*2] > this->vector_monticulo[(i*2)+1]) //Si el valor del hijo izquierdo es mayor que el valor del hijo derecho.
            {
                return i * 2; //Devolvemos el hijo izquierdo.
            }
            else
            {
                return (i * 2) + 1; //Devolvemos el hijo derecho.
            }
        }
    }

    //Devuelve un booleano indicando si el montículo está vacío o no.
    bool estaVacio()
    {
        if (this->vector_monticulo.size() == 1) //Ponemos == 1 ya que hay que obviar el valor 0 inicial.
        {
            return true;
        }
        return false;
    }

    //Devuelve el valor máximo del montículo.
    void encuentraMax()
    {
        if (this->estaVacio()) //Si el montículo está vacío.
        {
            cout << "Error al buscar el valor máximo: el montículo se encuentra vacío." << endl;
        }
        else
        {
            cout << "Valor máximo: " << this->vector_monticulo[1] << endl;
        }
    }

    //Devuelve el tamaño del montículo.
    int tamano()
    {
        return this->tamano_actual;
    }
};