#include <iostream>
#include <vector>
using namespace std;

int recDC(vector<int> coinValueList, int change, int knownResults[]) 
{
    int minCoins, numCoins;
    minCoins = change;

    for (unsigned int i = 0; i< coinValueList.size(); i++)

        if (coinValueList[i] == change)
        {
            knownResults[change] = 1;
            return 1;
        }
        else if(knownResults[change] > 0)
            return knownResults[change];

    for (unsigned int y=0; y<coinValueList.size(); y++)
        if (coinValueList[y] <= change)
        {
            numCoins = 1 + recDC(coinValueList, change - coinValueList[y], knownResults);
            if (numCoins < minCoins)
            {
                minCoins = numCoins;
                knownResults[change] = minCoins;
            }
        }
    return minCoins;
}

int main() 
{
    vector<int> coinValueList1 = {1, 5, 8, 10, 20, 25}; 
    int change1 = 33; 
    int knownResults1[34] = {0}; 
    cout << "El número mínimo de monedas a delvolver es: " << recDC(coinValueList1, change1, knownResults1) << endl; 

    vector<int> coinValueList2 = {1, 2, 5, 10, 20, 25};
    int change2 = 67; 
    int knownResults2[68] = {0};
    cout << "El número mínimo de monedas a delvolver es: " << recDC(coinValueList2, change2, knownResults2) << endl;
    vector<int> coinValueList3 = {1, 5, 10, 21, 25}; 
    int change3 = 76; 
    int knownResults3[77] = {0};
    cout << "El número mínimo de monedas a delvolver es: " << recDC(coinValueList3, change3, knownResults3) << endl; 
    vector<int> coinValueList4 = {1, 5, 12, 20, 25}; 
    int change4 = 84; 
    int knownResults4[85] = {0};
    cout << "El número mínimo de monedas a delvolver es: " << recDC(coinValueList4, change4, knownResults4) << endl; 

    vector<int> coinValueList5 = {1, 3, 8, 11, 21}; 
    int change5 = 100; 
    int knownResults5[101] = {0};
    cout << "El número mínimo de monedas a delvolver es: " << recDC(coinValueList5, change5, knownResults5) << endl; 
    
    return 0;
}