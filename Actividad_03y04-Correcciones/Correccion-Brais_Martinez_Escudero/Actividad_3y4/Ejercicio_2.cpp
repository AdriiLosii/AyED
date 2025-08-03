#include "Class_jarras.hpp"
#include <iostream>
using namespace std;
jarra jarra3(3);
jarra jarra4(4);

int prueba(int litros){
    cout << "Jarra 3: "<<jarra3.volumen()<< endl;
    cout << "Jarra 4: " << jarra4.volumen()<< endl;
    if (jarra4.volumen() == litros){
        printf("Conseguido!");
        return 1;
    }
    else{
        jarra3.llenar();
        jarra3.mover_a(jarra4);
        if(jarra4.volumen()== 4){
            jarra4.vaciar();
            jarra3.mover_a(jarra4);
        }
        return prueba(litros);
    }
}

int main(){
    cout << prueba(2) << endl;
}


