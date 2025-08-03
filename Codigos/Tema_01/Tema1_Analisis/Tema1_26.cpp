#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// sorts anagrams in order from a-z, and then compares them
bool anagramsolution3(string s1, string s2)
{
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    unsigned int pos = 0;
    bool matches = true;

    while (pos < s1.length() && matches)
        if (s1[pos] == s2[pos])
            pos = pos + 1;
        else
            matches = false;
    return matches;
}

int main()
{
    bool value = anagramsolution3("abcde", "edcba");
    if (value == 1)
        cout << "True" << endl;
    else
        cout << "False" << endl;
    return 0;
}
