//# Tema2_11.cpp This program creates a simulation of hot potato.

#include <iostream>
#include <queue>
#include <random>
#include <ctime>
#include <string>
using namespace std;

string hotPotato(string nameArray[], int num)
{
    queue<string> simqueue;
    int namelsLenght = nameArray->length();
    for (int i = 0; i < namelsLenght; i++)
        //puts the entire array into a queue.
        simqueue.push(nameArray[i]);

    while (simqueue.size() > 1)
    { //loop continues until there is one remaining item.
        for (int i = 0; i < num; i++)
        {
            simqueue.push(simqueue.front());
            simqueue.pop();
        }
        simqueue.pop();
    }

    return simqueue.front();
}

int main()
{
    string s[] = {"Bill", "David", "Susan", "Jane", "Kent", "Brad"};
    srand(time(NULL));

    cout << hotPotato(s, rand() % 10 + 1) << endl;

    return 0;
}
