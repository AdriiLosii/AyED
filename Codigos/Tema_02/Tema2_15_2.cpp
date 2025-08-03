// CPP program to illustrate Implementation of begin() and end()  function
#include <deque>
#include <iostream>
using namespace std;

int main()
{
    // declaration of deque container
    deque<int> mydeque{1, 2, 3, 4, 5};

    // using begin() to print deque
    for (auto it = mydeque.begin(); it != mydeque.end(); ++it)
        cout << ' ' << *it;
    return 0;
}
