
#include <iostream>
#include <queue>
#include <vector>
#include <random>
#include <time.h>
#include <cstdlib>
#include "Class_Impresion.cpp"
using namespace std;

bool newPrintTask()
{
    
    return (rand() % 180 + 1) == 180;
}

void simulation(int numSeconds, int pagesPerMinute)
{
    Printer labprinter(pagesPerMinute);

    
    queue<Task> printQueue;

    
    vector<int> waitingTimes;

    
    for (int i = 0; i < numSeconds; i++)
    {

        
        if (newPrintTask())
        {
            Task task(i);          
            printQueue.push(task); 
        }

        
        if (!labprinter.busy() && !printQueue.empty())
        {
            Task nextTask = printQueue.front(); 
            printQueue.pop();                   

            
            waitingTimes.push_back(nextTask.waitTime(i));
            labprinter.startNext(nextTask);
        }

        
        labprinter.tick();
    }

    
    float total = 0;
    for (int waitTime : waitingTimes)
        total += waitTime;

    cout << "Average Wait " << total / waitingTimes.size() << " secs " << printQueue.size() << " tasks remaining." << endl;
}

int main()
{
 
    srand(time(NULL));

    for (int i = 0; i < 10; i++)
        simulation(3600, 5);

    return 0;
}
