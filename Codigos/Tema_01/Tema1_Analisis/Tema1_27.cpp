#include <iostream>
#include <string>
using namespace std;

//uses an array to count the number of a ocurrences of the two inputs if the number of occurrences is the same then the input is an anagram

bool anagramSolution4(string s1, string s2)
{
    int c1[26] = {0};
    int c2[26] = {0};
    int x, y;
    int a = 'a';
    int pos, j = 0;

    for (unsigned int i = 0; i < s1.length(); i++)
    {
        x = s1[i] - a;
        pos = x;
        c1[pos] = c1[pos] + 1;
    }

    for (unsigned int i = 0; i < s2.length(); i++)
    {
        y = s2[i] - a;
        int pos = y;
        c2[pos] = c2[pos] + 1;
    }

    bool stillOK = true;
    while (j < 26 && stillOK)
        if (c1[j] == c2[j])
            j = j + 1;
        else
            stillOK = false;
    return stillOK;
}

int main()
{
    bool value = anagramSolution4("apple", "pleap");
    cout << value << endl;
    return 0;
}
