#include <iostream>

using namespace std;

int n2(){

    int lista[10] = {12, 2, 36, 45, 20, 8, 9, 8, 7, 1};
    int minimo;
    
    for(int i=0; i<10; i++){
        for(int j=0; j<10; j++){

            if (lista[i] < lista[j]){

                minimo = lista[i];

            }
            
        }
    }

    cout << "El mínimo es: " << minimo << endl;

    return 0;

}

int n(){

    int lista[10] = {12, 2, 36, 45, 20, 8, 9, 8, 7, 1};
    int minimo = lista[0];
    
    for(int i=0; i<10; i++){

        if (minimo > lista[i]){
            minimo = lista[i];
        }
    }

    cout << "El mínimo es: " << minimo << endl;

    return 0;
}

int main(){

    n();
    n2();

}

