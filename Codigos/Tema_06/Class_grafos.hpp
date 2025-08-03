#include "Class_vertices.hpp"

class Graph
{
public:
    map<int, Vertex> vertList;
    int numVertices;

    //Empty constructor.
    Graph()
    {
        numVertices = 0;
    }

    //Adds the specified vertex and returns a copy of it.
    Vertex addVertex(int key)
    {
        numVertices++;
        Vertex newVertex = Vertex(key);
        this->vertList[key] = newVertex;
        return newVertex;
    }

    //Returns the vertex with the specified ID.
    //Will return NULl if the vertex doesn't exist.
    Vertex *getVertex(int n)
    {
        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
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
    bool contains(int n)
    {
        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            if (it->first == n)
                return true;
        return false;
    }

    //Adds an edge between vertices F and T with a weight equivalent to cost.
    void addEdge(int f, int t, int cost = 0)
    {
        if (!this->contains(f))
        {
            cout << f << " was not found, adding!" << endl;
            this->addVertex(f);
        }
        if (!this->contains(t))
            cout << t << " was not found, adding!" << endl;
        vertList[f].addNeighbor(t, cost);
    }

    //Returns a vector (e.g, list) of all vertices in this graph.
    vector<int> getVertices()
    {
        vector<int> verts;

        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            verts.push_back(it->first);
        return verts;
    }

    //Overloaded Output stream operator for printing to the screen
    friend ostream &operator<<(ostream &, Graph &);
};

ostream &operator<<(ostream &stream, Graph &grph)
{
    for (unsigned int i = 0; i < grph.vertList.size(); i++)
        stream << grph.vertList[i];

    return stream;
}