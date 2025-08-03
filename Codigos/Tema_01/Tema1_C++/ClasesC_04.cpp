//ClasesC_04.cpp the english letter to it's spanish equivalent, and outputs the size of the table to the console
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;
int main() {
    unordered_map<string, string> spnumbers;
    spnumbers = { {"one", "uno"}, {"two", "dos"} };
    spnumbers["three"] = "tres";
    spnumbers["four"] = "cuatro";
    cout << "one is ";
    cout << spnumbers["one"] << endl;
    cout << spnumbers.size() << endl;
}

