//ClasesC_03.cpp every number from 0 to 49 uses the reserve operation to save space in memory

#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int> intvector;//declaración del vector de enteros
    intvector.reserve(50);
    for (int i = 0; i < 50; i++)
    {
        intvector.push_back(i * i);
        cout << intvector[i] << endl;
    }
    return 0;
}
