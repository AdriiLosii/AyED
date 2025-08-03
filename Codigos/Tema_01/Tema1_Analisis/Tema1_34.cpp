#include <iostream>
#include <ctime>
#include <vector>
#include <unordered_map>
using namespace std;

int main()
{
    //system("cls");
    cout << "Tamanho\t"
         << "Vector\t"
         << "Tabla hash\t" << endl;
    for (int a = 10000; a < 1000001; a = a + 20000)
    {
        // vector Part
        clock_t begin = clock();
        vector<int> avector;
        for (int i = 0; i < a; i++)
            avector.push_back(i);
        clock_t end = clock();
        double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;

        // Hash Table Part
        clock_t begin_ht = clock();
        unordered_map<int, int> y;
        for (int j = 0; j < a; j++)
            y[j] = j;
        clock_t end_ht = clock();
        double elapsed_secs_ht = double(end_ht - begin_ht) / CLOCKS_PER_SEC;

        // Printing final output
        cout << a << "\t " << elapsed_secs << "\t  " << elapsed_secs_ht << endl;
    }

    return 0;
}