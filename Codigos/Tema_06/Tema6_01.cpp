#include <iostream>
#include <map>
#include <vector>
using namespace std;
#include "Class_grafos.hpp"

int main()
{
    Graph g;

    for (int i = 0; i < 6; i++)
    {
        g.addVertex(i);
    }

    g.addEdge(0, 1, 5);
    g.addEdge(0, 5, 2);
    g.addEdge(1, 2, 4);
    g.addEdge(2, 3, 9);
    g.addEdge(3, 4, 7);
    g.addEdge(3, 5, 3);
    g.addEdge(4, 0, 1);
    g.addEdge(5, 4, 8);
    g.addEdge(5, 2, 1);

    cout << g << endl;

    return 0;
}
