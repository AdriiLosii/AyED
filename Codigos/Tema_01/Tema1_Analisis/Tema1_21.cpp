

#include <iostream>
#include <ctime>
using namespace std;
/*Performs same function as listing one, and also list the time it takes to perfrom
the function, and it performs better with larger inputs or (n)*/

double sumOfN3(double n)
{
    clock_t begin = clock();
    double sum_n = (n * (n + 1)) / 2;
    clock_t end = clock();
    double elapsed_secs = double(end - begin)/CLOCKS_PER_SEC;
    cout << fixed << endl; //write floating-point values in fixed-point notation
    cout << "Sum is " << sum_n << " required " << elapsed_secs << " seconds" << endl;
    return sum_n;
}

int main()
{
    for (int i = 0; i < 6; i++)
        sumOfN3(10000000);

    return 0;
}
