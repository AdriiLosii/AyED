#include <fstream>
#include <iostream>
#include <map>
#include "Class_grafos_string.hpp"
using namespace std;

string getBlank(string str, int index)
{
    string blank = str;
    blank[index] = '_';
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

    for (map<string, vector<string>>::iterator iter = d.begin(); iter != d.end(); ++iter)
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

int main()
{
    // Vector Initialized with an array
    string arr[] = {"fool", "cool", "pool", "poll", "pole", "pall", "fall", "fail", "foil", "foul", "pope", "pale", "sale", "sage", "page"};
    vector<string> words(arr, arr + (sizeof(arr) / sizeof(arr[0])));

    Graph g = buildGraph(words);

    cout << g << endl;

    return 0;
}
