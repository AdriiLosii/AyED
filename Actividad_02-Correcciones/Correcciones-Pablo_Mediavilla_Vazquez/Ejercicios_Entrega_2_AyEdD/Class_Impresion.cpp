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
        

        if (working) { 
            timeRemaining--;
            if (timeRemaining <= 0)
                working = false; 
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
    int pagerate; 
    Task currentTask = {0};
    bool working; 
    int timeRemaining; 
};
