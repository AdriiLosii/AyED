#include <fstream>
#include <iostream>
#include <queue>
#include "Class_grafos_string_full.hpp"

using namespace std;

string getBlank(string str, int index)
{
    string blank = str;
    blank[index] = '_'; //
    return blank;
}

Graph buildGraph(vector<string> words)
{
    Graph g(false);

    map<string, vector<string>> d;

    // Go through the words
    for (unsigned int i = 0; i < words.size(); i++)
    {
        // Go through each letter, making it blank
        for (unsigned int j = 0; j < words[i].length(); j++)
        {
            string bucket = getBlank(words[i], j);
            // Add the word to the map at the location of the blank
            d[bucket].push_back(words[i]);
        }
    }

    for (map<string, vector<string>>::iterator iter = d.begin();
         iter != d.end();
         ++iter)
    {
        for (unsigned int i = 0; i < iter->second.size(); i++)
        {
            for (unsigned int j = 0; j < iter->second.size(); j++)
            {
                if (iter->second[i] != iter->second[j])
                {
                    g.addEdge(iter->second[i], iter->second[j]);
                }
            }
        }
    }

    return g;
}

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
        for (unsigned int nbr = 0; nbr < currentVert->getConnections().size(); nbr++)
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

    while (x->pred)
    {
        cout << x->id << endl;
        x = x->pred;
    }
    cout << x->id << endl;
}

int main()
{
    // Vector Initialized with an array
    string arr[] = {"fool",
                    "cool",
                    "pool",
                    "poll",
                    "pole",
                    "pall",
                    "fall",
                    "fail",
                    "foil",
                    "foul",
                    "pope",
                    "pale",
                    "sale",
                    "sage",
                    "page"};

    vector<string> words(arr, arr + (sizeof(arr) / sizeof(arr[0])));

    // Graph g = buildGraph(words);
    Graph g(false);

    g = buildGraph(words);

    g = bfs(g, g.getVertex("fool"));

    traverse(g.getVertex("pall"));

    return 0;
}
