/*
#include <list>      //std::list
#include <utility>   //std::pair
#include <algorithm> //std::find
#include <map>       //std::map
*/
#include <iostream> //std::cout
#include "Class_DFSGrafos.hpp"

int main(int argc, char **argv)
{
    DFSGraph graph(true);

    graph.addEdge(0, 1);
    graph.addEdge(0, 2);
    graph.addEdge(0, 5);

    graph.addEdge(3, 4);
    graph.addEdge(3, 2);

    graph.addEdge(1, 5);
    graph.addEdge(1, 2);

    graph.addEdge(5, 4);
    graph.addEdge(5, 3);

    graph.dfs();

    return 0;
}
