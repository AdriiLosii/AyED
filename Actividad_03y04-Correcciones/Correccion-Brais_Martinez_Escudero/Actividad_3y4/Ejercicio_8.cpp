#include <iostream>
using namespace std;
#include "Class_jarras.hpp"
int X;
int Y;

void prueba(int litros){
    jarra jarrax(X);
    jarra jarray(Y);
    cout << "Jarra"<< jarrax.capacidad() <<": " <<jarrax.volumen()<< endl;
    cout << "Jarra"<< jarray.capacidad() <<": " << jarray.volumen()<< endl;
    while(jarrax.volumen() != litros){
        jarray.llenar();
        jarray.mover_a(jarrax);
        cout << "Jarra"<< jarrax.capacidad() <<": " <<jarrax.volumen()<< endl;
        cout << "Jarra"<< jarray.capacidad() <<": " << jarray.volumen()<< endl;
        if(jarrax.volumen()== jarrax.capacidad()){
            jarrax.vaciar();
            jarray.mover_a(jarrax);
        }
    }
    cout << "Jarra"<< jarrax.capacidad() <<": " <<jarrax.volumen()<< endl;
    cout << "Jarra"<< jarray.capacidad() <<": " << jarray.volumen()<< endl;
}

int main(){
    try{
        cout<< "Introduce la capacidad de la primera jarra: "<< endl;
        cin >> X;
        cout<< "Introduce la capacidad de la segunda jarra: "<< endl;
        cin >> Y;
        if(X< Y){ 
            throw (1);
        }
        if((X/2)%2 != 0){ 
            if(Y%2 == 0){
                throw (2);
            }
        }
        if(X%2 != 0){ 
            throw (3);
        }

        prueba(X/2);

    }
    /*catch (int X){
        cout << "La jarra 1 tiene que ser mayor que la jarra 2."<< endl;
    }*/
    catch (int exc){
        if(exc == 1){
            cout << "La jarra 1 tiene que ser mayor que la jarra 2." << endl;
        }
        if(exc == 2){
            cout << "La jarra 2 tiene que ser impar."<< endl;
        }
        if(exc == 2){
            cout << "La jarra 1 tiene que ser par."<< endl;
        }
    }
    catch(...){
        cout<< "Se ha producido un error" <<endl;
    }
}  



