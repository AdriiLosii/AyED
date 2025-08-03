#include <iostream>
#include <vector>
#include <ctime>
#include <cmath>
using namespace std;

double value = 0;

// print the sorted vector
void printl(vector<int> avector) 
{
    for (unsigned int i=0; i<avector.size(); i++) 
        cout << avector[i] << " ";
    cout << endl;
}
// function returns sorted subvector
vector<int> gapInsertionSort(vector<int> avector, int start, int gap) 
{
    for (unsigned int i = start + gap; i < avector.size(); i += gap) 
    {
        int currentvalue = avector[i];
        int position = i;

        while (position >= gap && avector[position - gap] > currentvalue) 
        {
            avector[position] = avector[position - gap];
            position -= gap;
        }
        avector[position] = currentvalue;
    }
    return avector;
}

//function shellsorts through the vector
vector<int> shellSort(vector<int> avector, double value) 
{
    unsigned t0, t1;
    t0 = clock();

    int subvectorcount = avector.size() / value ; //cuts vector by half
    while (subvectorcount > 0) 
    {
        for (int startposition = 0; startposition < subvectorcount; startposition++) 
            avector = gapInsertionSort(avector, startposition, subvectorcount);
            //runs avector through gapInsertionSort function

        cout << "Tras los incrementos de tamanho " << subvectorcount
             << " El vector es: " << endl;
        printl(avector);

        subvectorcount = subvectorcount / 2; //cuts vector in half
    }

    t1 = clock();

    double time = (double(t1-t0)/CLOCKS_PER_SEC);
    cout << "Tiempo de ejecucion: " << time << endl;

    return avector;
}

int main() {
    // Vector initialized using a static array
    static const int arr[] = {54, 26, 93, 17, 77, 31, 44, 55, 20};
    
    vector<int> avector (arr, arr + sizeof(arr) / sizeof(arr[0]));

    int size = sizeof(arr)/sizeof(*arr);

    cout << "Conjunto de incremento 1 (numero dos)" << endl;
    printl(shellSort(avector, 2));
    cout << "\n" << endl;

    cout << "Conjunto de incremento 2 (raiz cuadrada del tamanho del vector)" << endl;
    printl(shellSort(avector, sqrt(size)));
    cout << "\n" << endl;

    cout << "Conjunto de incremento 3 (log base 10 de el tamanho del vector)" << endl;
    printl(shellSort(avector, log10(size)));
    cout << "\n" << endl;

    return 0;
}


