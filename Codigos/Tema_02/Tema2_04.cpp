//Tema2_04.cpp converts a given decimal number into binary.

#include <iostream>
#include <stack> // Calling Stack from the STL
#include <string>

using namespace std;

string divideBy2(int decNumber)
{
    //performs the conversion process.
    stack<int> remstack;

    while (decNumber > 0)
    {
        //gets the remainder of division by 2
        //and adds the remainder to a stack.
        int rem = decNumber % 2;
        remstack.push(rem);
        decNumber = decNumber / 2;
    }

    string binString = "";
    while (!remstack.empty())
    {
        //adds the remainder numbers in the stack into a string.
        binString.append(to_string(remstack.top()));
        remstack.pop();
    }

    return binString;
}

int main()
{
    cout << divideBy2(421) << endl;

    return 0;
}
