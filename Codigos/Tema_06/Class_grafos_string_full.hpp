#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

class Vertex
{
public:
    string id;
    map<string, float> connectedTo;
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

    Vertex(string key)
    {
        id = key;
        color = 'w';
        dist = 0;
        pred = NULL;
    }

    void addNeighbor(string nbr, float weight = 1)
    {
        connectedTo[nbr] = weight;
    }

    vector<string> getConnections()
    {
        vector<string> keys;
        // Use of iterator to find all keys
        for (map<string, float>::iterator it = connectedTo.begin(); it != connectedTo.end(); ++it)
            keys.push_back(it->first);
        return keys;
    }

    string getId()
    {
        return id;
    }

    float getWeight(string nbr)
    {
        return connectedTo[nbr];
    }

    friend ostream &operator<<(ostream &, Vertex &);
};

ostream &operator<<(ostream &stream, Vertex &vert)
{
    vector<string> connects = vert.getConnections();
    stream << vert.id << " -> ";
    for (unsigned int i = 0; i < connects.size(); i++)
        stream << connects[i] << endl
               << "\t";

    return stream;
}

class Graph
{
public:
    map<string, Vertex> vertList;
    int numVertices;
    bool directional;

    Graph(bool directed = true)
    {
        directional = directed;
        numVertices = 0;
    }

    Vertex addVertex(string key)
    {
        numVertices++;
        Vertex newVertex = Vertex(key);
        this->vertList[key] = newVertex;
        return newVertex;
    }

    Vertex *getVertex(string n)
    {
        return &vertList[n];
    }

    bool contains(string n)
    {
        for (map<string, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            if (it->first == n)
                return true;
        return false;
    }

    void addEdge(string f, string t, float cost = 1)
    {
        if (!this->contains(f))
            this->addVertex(f);
        if (!this->contains(t))
            this->addVertex(t);
        vertList[f].addNeighbor(t, cost);

        if (!directional)
            vertList[t].addNeighbor(f, cost);
    }

    vector<string> getVertices()
    {
        vector<string> verts;

        for (map<string, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            verts.push_back(it->first);
        return verts;
    }

    friend ostream &operator<<(ostream &, Graph &);
};

ostream &operator<<(ostream &stream, Graph &grph)
{
    for (map<string, Vertex>::iterator it = grph.vertList.begin(); it != grph.vertList.end(); ++it)
    {
        stream << grph.vertList[it->first];
        cout << endl;
    }

    return stream;
}