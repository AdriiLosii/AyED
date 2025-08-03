//Tema3_07.cpp Simulation of the tower of hanoi.
#include <iostream>
using namespace std;
void moveDisk(char fp, char tp){
    cout << "moving disk from " << fp << " to " << tp << endl;
}

void moveTower(int height, char fromPole, char toPole, char withPole){
    if (height >= 1)
    {
        moveTower(height-1, fromPole, withPole, toPole); //Recursive call
        moveDisk(fromPole, toPole);
        moveTower(height-1, withPole, toPole, fromPole); //Recursive call
    }
}

int main() {
    moveTower(3, 'A', 'B', 'C');
}