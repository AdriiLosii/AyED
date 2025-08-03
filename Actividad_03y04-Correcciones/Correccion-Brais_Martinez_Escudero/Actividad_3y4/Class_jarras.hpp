#include <iostream>
using namespace std;

class jarra
{
    public:
        jarra(float tam){
            vol = 0;
            tamano = tam;
        }
        float capacidad (){
            return tamano;
        }
        float volumen(){
            return vol;
        }
        float llena(){
            return vol == tamano;
        }
        float vacia(){
            return vol == 0;
        }
        void llenar(){
            vol = tamano;
        }
        void vaciar(){
            vol = 0;
        }
        void aumentar_vol(){
            vol = vol + 1;
        }
        void mover_a(jarra &otrajarra)
        {
            while (otrajarra.llena() == false && vacia()== false)
            {
                otrajarra.aumentar_vol();
                vol = vol - 1;
            }
        }
    private:
        float tamano;
        float vol;
        
};
