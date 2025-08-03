#include <iostream>
#include <chrono>
#include <vector>
using namespace std;

//Tests the time of the vector "push_back()" operation

void test1(int num)
{
    vector<int> vect;
    for (int i = 0; i < num; i++)
    {
        vect.push_back(i);
    }
}

int main()
{
    int numruns = 10000;
    cout.precision(5); //precision de salida en el cout
    auto t1 = chrono::high_resolution_clock::now();
    for (int i = 0; i < numruns; i++)
        test1(numruns);

    auto t2 = chrono::high_resolution_clock::now();
    chrono::duration<int64_t, nano> elapsed = t2 - t1; //if you want milliseconds you should use: std::chrono::duration<double,milli>

    cout << scientific << endl; //write floating-point values in scientific notation

    cout << "push_back " << elapsed.count() << " nanoseconds" << endl;

    return 0;
}
