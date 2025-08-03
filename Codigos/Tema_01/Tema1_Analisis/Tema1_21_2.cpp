#include <iostream>
#include <chrono>

using namespace std;
/*Performs same function as listing one, and also list the time it takes to perfrom
the function, and it performs better with larger inputs or (n)*/

double sumOfN3(double n)
{
    auto t1 = chrono::high_resolution_clock::now();
    double sum_n = (n * (n + 1)) / 2;
    auto t2 = chrono::high_resolution_clock::now();
    chrono::duration<int64_t, nano> elapsed = t2 - t1; //if you want milliseconds you should use: std::chrono::duration<double,milli>

    cout << fixed << endl; //write floating-point values in fixed-point notation
    cout << "Sum is " << sum_n << " required " << elapsed.count() << " nanoseconds." << endl;
    return sum_n;
}

int main()
{
    for (int i = 0; i < 6; i++)
        sumOfN3(10000000);

    return 0;
}
