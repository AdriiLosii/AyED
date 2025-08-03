
#include <iostream>
#include<stdlib.h>
#include<time.h>
#include <unistd.h>
using namespace std;
int random(int minimo, int maximo);
int main(){
    srand(getpid());
    int turnos , puntuacion1 , puntuacion2 , numero , numero2, lados;

   puntuacion1=0;
   puntuacion2=0;

   cout << "Numero de turnos" << endl;
   cin >> turnos;
   cout << "Numero de lados"<< endl;
   cin >> lados;
   for (int i = 1; i <= turnos; i ++){
      numero = random(1,lados);
      puntuacion1 = numero + puntuacion1;
   }
   for (int i = 1; i <= turnos; i ++){
      numero2 = random(1,lados);
      puntuacion2 = numero2 + puntuacion2;
   }
   
   cout << "Jugador 1 :" << puntuacion1<<endl;
   cout << "Jugador 2 :" << puntuacion2<<endl;

   if (puntuacion1 == puntuacion2) {
        cout << "Draw" ;
    }
   if (puntuacion1 > puntuacion2) {
        cout << "Gana jugador 1" ;
    }
   if (puntuacion1 < puntuacion2) {
        cout << "Gana jugador 2" ;
    }
    

}


int random(int minimo, int maximo){
   return minimo + rand() / (RAND_MAX / (maximo - minimo + 1) + 1);
}
