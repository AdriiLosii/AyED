class Vertex
{
public:
    int id;
    map<int, int> connectedTo;

    //Empty constructor.
    Vertex()
    {
    }

    //Constructor that defines the key of the vertex.
    Vertex(int key)
    {
        id = key;
    }

    //Adds a neighbor to this vertex with the specified ID and weight.
    void addNeighbor(int nbr, int weight = 0)
    {
        connectedTo[nbr] = weight;
    }
    //Returns a vector (e.g, list) of vertices connected to this one.
    vector<int> getConnections()
    {
        vector<int> keys;
        // Use of iterator to find all keys
        for (map<int, int>::iterator it = connectedTo.begin();
             it != connectedTo.end();
             ++it)
        {
            keys.push_back(it->first);
        }
        return keys;
    }

    //Returns the ID of this vertex.
    int getId()
    {
        return id;
    }

    //Returns the weight of the connection between this vertex and the specified neighbor.
    int getWeight(int nbr)
    {
        return connectedTo[nbr];
    }

    //Output stream overload operator for printing to the screen.
    friend ostream &operator<<(ostream &, Vertex &);
};

ostream &operator<<(ostream &stream, Vertex &vert)
{
    vector<int> connects = vert.getConnections();
    for (unsigned int i = 0; i < connects.size(); i++)
    {
        stream << "( " << vert.id << " , " << connects[i] << " ) \n";
    }

    return stream;
}