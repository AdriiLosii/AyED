#include <list>      //std::list
#include <utility>   //std::pair
#include <algorithm> //std::find
#include <map>       //std::map
#include <iostream>  //std::cout
using namespace std;

class DFSGraph
{
    typedef pair<int, list<int>> vertex_t;
    typedef map<int, vertex_t> graph_t;

public:
    const bool directional;
    DFSGraph(bool directional) : directional(directional) {}

    bool containsVertex(int id)
    {
        return vertices.count(id);
    }

    list<int> &getVertexConnections(int id)
    {
        return vertices[id].second;
    }

    void addVertex(int id)
    {
        if (containsVertex(id))
            vertices[id].second.clear();

        else
            vertices[id] = make_pair(id, list<int>());
    }

    vertex_t &getVertex(int id)
    {
        return vertices[id];
    }

    void addEdge(int fromID, int toID)
    {
        if (!containsVertex(fromID))
            addVertex(fromID);

        if (!containsVertex(toID))
            addVertex(toID);

        getVertexConnections(fromID).push_back(toID);
        if (!directional)
            getVertexConnections(toID).push_back(fromID);
    }

    void dfs()
    {
        list<int> visitedList;

        for (auto &cur : vertices)
            if (find(visitedList.begin(), visitedList.end(), cur.first) == visitedList.end())
                dfsvisit(visitedList, cur.second);
    }

    void dfsvisit(list<int> &visitedList, vertex_t &vertex)
    {
        visitedList.push_back(vertex.first);

        cout << "Visited Vertex With ID#: " << vertex.first << endl;

        for (int neighborID : vertex.second)
            if (find(visitedList.begin(), visitedList.end(), neighborID) != visitedList.end())
                dfsvisit(visitedList, getVertex(neighborID));
    }

private:
    graph_t vertices;
};
