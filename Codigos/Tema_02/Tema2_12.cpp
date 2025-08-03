//Program that simulates printing task management.

#include <iostream>
#include <queue>
#include <vector>
#include <random>
#include <ctime>
#include <cstdlib>
#include "Class_Impresion.hpp"
using namespace std;

bool newPrintTask()
{
    /*uses random to decide if there is a new print task. generates a random number from 1...180, and returns a boolean indicating whether or not it equals 180.*/
    return (rand() % 180 + 1) == 180;
}

void simulation(int numSeconds, int pagesPerMinute)
{
    Printer labprinter(pagesPerMinute);

    //The Queue ADT from the standard container library.
    queue<Task> printQueue;

    //A vector of wait-times for each task.
    vector<int> waitingTimes;

    //For every second in the simulation...
    for (int i = 0; i < numSeconds; i++)
    {

        //If there's a new printing task, add it to the queue.
        if (newPrintTask())
        {
            Task task(i);          //Create it...
            printQueue.push(task); //Push it.
        }

        //If the printer is not busy and the queue is not empty:
        if (!labprinter.busy() && !printQueue.empty())
        {
            Task nextTask = printQueue.front(); // Assign a new task from the queue.
            printQueue.pop();                   // Remove it from the front

            //Add the estimated wait time to our vector.
            waitingTimes.push_back(nextTask.waitTime(i));
            labprinter.startNext(nextTask);
        }

        //Process the current task.
        labprinter.tick();
    }

    //Average out every wait time for the simulation.
    float total = 0;
    for (int waitTime : waitingTimes)
        total += waitTime;

    cout << "Average Wait " << total / waitingTimes.size() << " secs " << printQueue.size() << " tasks remaining." << endl;
}

int main()
{
    //Seed random number generator with the current time
    //This ensures a unique random simulation every time it's ran.
    srand(time(NULL));

    for (int i = 0; i < 10; i++)
        simulation(3600, 5);

    return 0;
}
