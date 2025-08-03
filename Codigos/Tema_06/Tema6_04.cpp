#include <fstream>
#include <iostream>
#include <queue>
#include "Class_grafos_int_full.hpp"

using namespace std;

Graph bfs(Graph g, Vertex *start)
{
    start->dist = 0;
    start->pred = NULL;
    queue<Vertex *> vertQueue;
    vertQueue.push(start);
    while (vertQueue.size() > 0)
    {
        Vertex *currentVert = vertQueue.front();
        vertQueue.pop();
        for (unsigned int nbr = 0; nbr < currentVert->getConnections().size();
             nbr++)
        {
            if (g.vertList[currentVert->getConnections()[nbr]].color == 'w')
            {
                g.vertList[currentVert->getConnections()[nbr]].color = 'g';

                g.vertList[currentVert->getConnections()[nbr]].dist =
                    currentVert->dist + 1;
                g.vertList[currentVert->getConnections()[nbr]].pred =
                    currentVert;
                vertQueue.push(&g.vertList[currentVert->getConnections()[nbr]]);
            }
        }
        currentVert->color = 'b';
    }

    return g;
}

void traverse(Vertex *y)
{
    Vertex *x = y;
    int count = 1;

    while (x->pred)
    {
        cout << x->id << " to " << x->pred->id << endl;
        x = x->pred;

        count++;
    }
}

int coordToNum(int x, int y, int bdSize)
{
    // Takes the x y position and returns the id from 0 to (bdSize*2)-1
    int id = 0;
    id += y * bdSize;
    id += x;

    return id;
}

pair<int, int> numToCoord(int id, int bdSize)
{
    int x, y;
    x = id % bdSize;
    y = (id - x) / bdSize;

    return make_pair(x, y);
}

bool legalCoord(int x, int bdSize)
{
    if (x >= 0 && x < bdSize)
    {
        return true;
    }
    else
    {
        return false;
    }
}

vector<int> genLegalMoves(int id, int bdSize)
{
    pair<int, int> coords = numToCoord(id, bdSize);
    int x = coords.first;
    int y = coords.second;

    vector<int> newMoves;
    vector<pair<int, int>> myVec = {
        {-1, -2}, {-1, 2}, {-2, -1}, {-2, 1}, {1, -2}, {1, 2}, {2, -1}, {2, 1}};

    for (unsigned int i = 0; i < myVec.size(); i++)
    {
        int newX = x + myVec[i].first;
        int newY = y + myVec[i].second;
        if (legalCoord(newX, bdSize) && legalCoord(newY, bdSize))
        {
            newMoves.push_back(coordToNum(newX, newY, bdSize));
        }
    }

    return newMoves;
}

Graph knightGraph(int bdSize)
{
    Graph ktGraph(false);

    for (int row = 0; row < bdSize; row++)
    {
        for (int col = 0; col < bdSize; col++)
        {
            int nodeId = coordToNum(row, col, bdSize);
            vector<int> newPositions = genLegalMoves(nodeId, bdSize);
            for (int i = 0; i < newPositions.size(); i++)
            {
                int newId = newPositions[i];
                ktGraph.addEdge(nodeId, newId);
            }
        }
    }

    return ktGraph;
}

int main()
{
    Graph kt = knightGraph(8);

    kt = bfs(kt, kt.getVertex(63));
    traverse(kt.getVertex(0));

    return 0;
}
