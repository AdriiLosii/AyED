#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

class Vertex
{
public:
    int id;
    map<int, float> connectedTo;
    // Added for Breadth-First Algorithm
    char color;
    float dist;
    Vertex *pred;

    Vertex()
    {
        // w for white, g for grey, b for black
        color = 'w';
        dist = 0;
        pred = NULL;
    }

    Vertex(int key)
    {
        id = key;
        color = 'w';
        dist = 0;
        pred = NULL;
    }

    void addNeighbor(int nbr, float weight = 1)
    {
        connectedTo[nbr] = weight;
    }

    vector<int> getConnections()
    {
        vector<int> keys;
        // Use of iterator to find all keys
        for (map<int, float>::iterator it = connectedTo.begin(); it != connectedTo.end(); ++it)
            keys.push_back(it->first);
        return keys;
    }

    int getId()
    {
        return id;
    }

    float getWeight(int nbr)
    {
        return connectedTo[nbr];
    }

    friend ostream &operator<<(ostream &, Vertex &);
};

ostream &operator<<(ostream &stream, Vertex &vert)
{
    vector<int> connects = vert.getConnections();
    stream << vert.id << " -> ";
    for (unsigned int i = 0; i < connects.size(); i++)
        stream << connects[i] << endl
               << "\t";

    return stream;
}

class Graph
{
public:
    map<int, Vertex> vertList;
    int numVertices;
    bool directional;

    Graph(bool directed = true)
    {
        directional = directed;
        numVertices = 0;
    }

    Vertex addVertex(int key)
    {
        numVertices++;
        Vertex newVertex = Vertex(key);
        this->vertList[key] = newVertex;
        return newVertex;
    }

    Vertex *getVertex(int n)
    {
        return &vertList[n];
    }

    bool contains(int n)
    {
        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            if (it->first == n)
                return true;
        return false;
    }

    void addEdge(int f, int t, float cost = 1)
    {
        if (!this->contains(f))
            this->addVertex(f);
        if (!this->contains(t))
            this->addVertex(t);
        vertList[f].addNeighbor(t, cost);

        if (!directional)
            vertList[t].addNeighbor(f, cost);
    }

    vector<int> getVertices()
    {
        vector<int> verts;

        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            verts.push_back(it->first);
        return verts;
    }

    friend ostream &operator<<(ostream &, Graph &);
};

ostream &operator<<(ostream &stream, Graph &grph)
{
    for (map<int, Vertex>::iterator it = grph.vertList.begin(); it != grph.vertList.end(); ++it)
    {
        stream << grph.vertList[it->first];
        cout << endl;
    }

    return stream;
}