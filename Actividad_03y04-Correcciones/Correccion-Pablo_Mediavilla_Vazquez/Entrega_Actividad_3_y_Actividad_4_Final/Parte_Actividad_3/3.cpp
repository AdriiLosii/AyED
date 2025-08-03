#include <iostream>
#include <stdlib.h>
#include "conio.h"

using namespace std;

int main() {
    int n, nt;

    cout << "Dame el numero de n: ";
    cin >> n;

    for(int i = 0; i < n; i++ ){
        nt = 1;

        for(int j = 0; j <= i; j++ ){
            cout << nt << " ";
            nt = nt * (i-j)/(j+1);
        }
    
        cout << "\n";
    }

    _getch();


}
