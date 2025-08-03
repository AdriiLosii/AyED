// C++ program to calculate pow(x,n)
#include<iostream>
using namespace std;

// Function to calculate x raised to the power y

int power(int x, unsigned int y)
{
    if (y == 0)
        return 1;
    else
    {
        float p=power(x,y/2);
        if (y % 2 == 0)
            return p*p;
        else
            return x*p*p;
    }
}

/* Driver code */
int main(){
	int x = 2;
	unsigned int y = 5;

	cout << power(x, y);
	return 0;
}    