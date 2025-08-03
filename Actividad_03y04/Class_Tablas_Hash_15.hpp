//Programa: Class_Tablas_Hash_15.hpp
/*
Propósito:
    Implementa el método tamano (__len__) para la implementación del TAD Vector
    Asociativo o mapa de las tablas hash, de manera que sea O(1).
*/
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 19/04/2022


#include <iostream>
#include <string>
using namespace std;

class TablaHash{
public:
    static const int tamano_total = 11; //Tamaño inicial de la tabla hash.
    int slots[tamano_total]; //Lista que almacena las claves de los ítems.
    string items[tamano_total]; //Lista que almacena los ítems.
    int tamano = 0;

    //Método que devuelve la posición del slot que le corresponde al ítem con la clave dada.
    int funcionHash(int clave)
    {
        return clave % tamano_total;
    }

    //Avanza un slot.
    int rehash(int slot_anterior)
    {
        return (slot_anterior + 1) % tamano_total;
    }

    //Agrega el ítem dado en la posición que corresponde a la clave dada,
    //si esta está ocupada, recorrerá la tabla hasta encontrar un slot vacío,
    //y si la clave ya está presente en la tabla, sobreescribe el valor de dicho slot.
    void agrega(int clave, string item){
        int pos_slot = funcionHash(clave);
        int contador = 0;

        if (items[pos_slot] == "") //Si el slot que le corresponde está vacío.
        {
            //Asignamos la clave y el item dados.
            slots[pos_slot] = clave;
            items[pos_slot] = item;
            tamano += 1;
        }

        else
        {
            if (slots[pos_slot] == clave) //Si la clave almacenada anteriormente en la posición del slot correspondiente actual coincide con la clave dada.
            {
                items[pos_slot] = item; //Se sobreescribe el ítem almacenado.
            }

            else
            {
                int siguiente_slot = rehash(pos_slot); //Avanzamos al siguiente slot.

                //Avanzamos slot a slot mientras que la posición en la lista de los valores no esté vacía o la clave almacenada en esa posición sea distinta a la dada.
                while (items[siguiente_slot] != "" && slots[siguiente_slot] != clave)
                {
                    siguiente_slot = rehash(siguiente_slot); 

                    contador++;
                    if (contador > tamano_total) //Si el contador alcanza un valor mayor que el tamaño total de la lista.
                    {
                        //Indicamos el problema y volvemos al programa principal.
                        cout<<"Tabla hash llena."<<endl;
                        return;
                    }
                }

                //Cuando se encuentra una posición en la tabla hash válida.
                if (items[siguiente_slot] == "") //Si el slot que le corresponde está vacío.
                {
                    //Asignamos la clave y el item dados.
                    slots[siguiente_slot] = clave;
                    items[siguiente_slot] = item;
                    tamano += 1;
                }
                else //(Si la clave almacenada anteriormente en la posición del slot correspondiente actual coincide con la clave dada)
                {
                    items[siguiente_slot] = item; //Se sobreescribe el ítem almacenado.
                }
            }
        }
    }

    //Devuelve el ítem asociado a la clave dada.
    string obten(int clave)
    {
        int slot_inicial = funcionHash(clave);

        string valor;
        bool encontrado = false;
        bool fin = false;
        int posicion = slot_inicial;

        //Mientras que el slot contenga algo, no se haya encontrado el slot con la clave indicada o no se llegue al final de la tabla.
        while (items[posicion] != "" && !encontrado && !fin)
        {
            if (slots[posicion] == clave) //Si encontramos el slot con la clave dada.
            {
                encontrado = true;
                valor = items[posicion];
            }
            else
            {
                posicion = rehash(posicion); //Avanzamos un slot.

                if (posicion == slot_inicial) //Si ya hemos recorrido toda la tabla (volvemos al slot inicial), volvemos al programa principal.
                    fin = true;
            }
        }

        if (encontrado == false)
            return "No encontrado.";
        else
            return items[posicion];
    }

    //Implementamos el método que devuelva el tamaño de la tabla (número de slots ocupados).
    int __len__()
    {
        return tamano;
    }

    friend ostream& operator<<(ostream& stream, TablaHash& hash);
};



ostream& operator<<(ostream& stream, TablaHash& hash)
{
    for (int i=0; i < hash.tamano_total; i++)
    {
        if (hash.items[i] == "")
            stream << "Posicion " << i << ": Slot vacio." << endl;
        else
            stream << hash.slots[i] << ": " << hash.items[i] << endl;
    }

    return stream;
}