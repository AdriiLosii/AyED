class Task {
public:
    Task(int time) {
        timestamp = time;
        pages=(rand()%20) + 1;
    }

    int getStamp() {
        return timestamp;
    }

    int getPages() {
        return pages;
    }

    int waitTime(int currenttime) {
        return (currenttime - timestamp);
    }
private:
    int timestamp;
    int pages;
};

class Printer {
public:
    Printer(int pagesPerMinute) {
        pagerate = pagesPerMinute;
        timeRemaining=0;
        working = false;
    }

    void tick() {
        //Performed once per second in the simulation.

        if (working) { // If we're working on something...
            timeRemaining--;// Subtract the remaining time.
            if (timeRemaining <= 0)
                working = false; // When finished, stop working.
        }
    }

    bool busy() {
        return working;
    }

    void startNext(Task newtask) {
        currentTask=newtask;
        timeRemaining=newtask.getPages()*60/pagerate;
        working = true;
    }

private:
    int pagerate; // unit is pages per minute.
    Task currentTask = {0};// Current task. default is a dummy value.
    bool working; // Are we working on the current task?
    int timeRemaining; // Time remaining, in "seconds".
};
