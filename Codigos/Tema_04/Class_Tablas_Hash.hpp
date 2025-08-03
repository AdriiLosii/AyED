#include <iostream>
#include <string>
using namespace std;

class HashTable{
    public:
    static const int size=11; // initial size of hash table is prime to help with collision resolution
    int slots[size]; // list to hold key items
    string data[size]; // list to hold data values

    int hashfunction(int key) { // implements remainder method
        return key%size;
    }

      // Computes original hashvalue, and if slot is
      // not empty iterates until empty slot is found
    int rehash(int oldhash) {
        return (oldhash+1)%size;
    }

    // Function that assumes there will eventually be
    // an empty slot unless the key is alread present in the slot
    void put(int key, string val){
        int hashvalue = hashfunction(key);
        int count = 0;

        if (data[hashvalue]=="") {
            slots[hashvalue] = key;
            data[hashvalue] = val;
        } else {
            if (slots[hashvalue] == key) {
                data[hashvalue] = val;
            } else {
                int nextslot = rehash(hashvalue);

                while (data[nextslot]!="" && slots[nextslot] != key) {
                    nextslot = rehash(nextslot);

                    count++;
                    if (count>size) {
                        cout<<"TABLE FULL"<<endl;
                        return;
                    }
                }
                if (data[nextslot]=="") {
                    slots[nextslot]=key;
                    data[nextslot]=val;
                } else {
                    data[nextslot] = val;
                }
            }
        }
    }

    // computes the initial hash value
    // if value is not in the initial slot, uses
    // rehash to locate the next position
    string get(int key) {
        int startslot = hashfunction(key);

        string val;
        bool stop=false;
        bool found=false;
        int position = startslot;
        while(data[position]!="" && !found && !stop) {
            if (slots[position]==key) {
                found = true;
                val = data[position];
            } else {
                position=rehash(position);
                if (position==startslot) {
                    stop=true;
                }
            }

        }
        return val;
    }

    friend ostream& operator<<(ostream& stream, HashTable& hash);
};



ostream& operator<<(ostream& stream, HashTable& hash) {
    for (int i=0; i<hash.size; i++) {
        stream<<hash.slots[i]<<": "<<hash.data[i]<<endl;
    }

    return stream;
}