#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int recMC_greedy(vector<int> coinValueList, int change)
{
    if (change == 0)
    //base case if, change is 0, then the number of coins have been finalized
        return 0;
    else
    {
        int cur_max = *max_element(coinValueList.begin(), coinValueList.end()); 
        //use the maximum in the list to see how many of these can be used to form the sum                                    
        
        int count = int(change / cur_max);  
        //find how many of the max is needed to make the change so that the number of coins used is minimum
        
        coinValueList.erase(std::remove(coinValueList.begin(), coinValueList.end(), cur_max), coinValueList.end()); 
        //erasing the current max so that a different max can be used in next recursion and continue the greedy process
        cout<<count<<", ";
        return count + recMC_greedy(coinValueList, change - cur_max * count); 
        //returns the counts of the coins using recursion
    }
}

int main()
{
    int arr2[] = {1, 5, 10, 21, 25};
    vector<int> coinValueList(arr2, arr2 + (sizeof(arr2) / sizeof(arr2[0]))); 
    //Initializing vector using the greedy algorithm for the edge case 63 whose optimal solution is 3 coins of 21, but greedy algorithm gives 6 coins which is not the most optimum solution
    cout << "\nTotal coins: "<<recMC_greedy(coinValueList, 63) << endl;                          
    return 0;                                                                 
}
