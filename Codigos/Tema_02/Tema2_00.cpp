// CPP program to demonstrate working of STL stack
//#include <bits/stdc++.h> // archivo de encabezado que incluye todas las bibliotecas estándar
#include <iostream>
#include <stack> // Calling Stack from the STL
using namespace std;

void showstack(stack<int> s)
{
    while (!s.empty())
    {
        cout << s.top() << '\t';
        s.pop();
    }
    cout << '\n';
}

int main()
{
    stack<int> s;
    s.push(10);
    s.push(30);
    s.push(20);
    s.push(5);
    s.push(1);

    cout << "The stack is : ";
    showstack(s);

    cout << "\ns.size() : " << s.size();
    cout << "\ns.top() : " << s.top();

    cout << "\ns.pop() : ";
    s.pop();
    showstack(s);

    return 0;
}