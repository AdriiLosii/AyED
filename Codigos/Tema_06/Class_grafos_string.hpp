/*
#include <fstream>
#include <iostream>
#include <map>
*/
#include <string>
#include <vector>
using namespace std;

class Vertex
{
public:
    string id;
    map<string, float> connectedTo;

    //Empty constructor.
    Vertex()
    {
    }

    //Constructor that defines the key of the vertex.
    Vertex(string key)
    {
        id = key;
    }

    //Adds a neighbor to this vertex with the specified ID and weight.
    void addNeighbor(string nbr, float weight = 1)
    {
        connectedTo[nbr] = weight;
    }
    //Returns a vector (e.g, list) of vertices connected to this one.
    vector<string> getConnections()
    {
        vector<string> keys;
        // Use of iterator to find all keys
        for (map<string, float>::iterator it = connectedTo.begin(); it != connectedTo.end(); ++it)
            keys.push_back(it->first);
        return keys;
    }
    //Returns the ID of this vertex.
    string getId()
    {
        return id;
    }

    //Returns the weight of the connection between this vertex and the specified neighbor.
    float getWeight(string nbr)
    {
        return connectedTo[nbr];
    }

    //Output stream overload operator for printing to the screen.
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

    //Adds the specified vertex and returns a copy of it.
    Vertex addVertex(string key)
    {
        numVertices++;
        Vertex newVertex = Vertex(key);
        this->vertList[key] = newVertex;
        return newVertex;
    }
    //Returns the vertex with the specified ID.
    //Will return NULl if the vertex doesn't exist.
    Vertex *getVertex(string n)
    {
        for (map<string, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            if (it->first == n)
            {
                // Forced to use pntr due to possibility of returning NULL
                Vertex *vpntr = &vertList[n];
                return vpntr;
            }
            else
                return NULL;
    }

    //Returns a boolean indicating if an index with the specified ID exists.
    bool contains(string n)
    {
        for (map<string, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            if (it->first == n)
                return true;
        return false;
    }

    //Adds an edge between vertices F and T with a weight equivalent to cost.
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

    //Returns a vector (e.g, list) of all vertices in this graph.
    vector<string> getVertices()
    {
        vector<string> verts;

        for (map<string, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            verts.push_back(it->first);
        return verts;
    }

    //Overloaded Output stream operator for printing to the screen
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