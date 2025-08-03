// Tema2_22.cpp C++ code to demonstrate working of push_front(), emplace_front() and pop_front()
#include <iostream>
#include <forward_list> 
using namespace std;

int main()
{
	// Initializing forward list
	forward_list<int> flist = {10, 20, 30, 40, 50};

	// Inserting value using push_front()
	// Inserts 60 at front
	flist.push_front(60);
	
	// Displaying the forward list
	cout << "The forward list after push_front operation : ";
	for (int&c : flist) 
		cout << c << " ";
	cout << endl;
	
	// Deleting first value using pop_front()
	// Pops 60
	flist.pop_front();
	
	// Displaying the forward list
	cout << "The forward list after pop_front operation : ";
	for (int&c : flist) 
		cout << c << " ";
	cout << endl;
	// Declaring a forward list iterator
	forward_list<int>::iterator ptr;

	// Inserting value using insert_after()
	// starts insertion from second position
	ptr = flist.insert_after(flist.begin(), {1, 2, 3});
	
	// Displaying the forward list
	cout << "The forward list after insert_after operation : ";
	for (int&c : flist) 
		cout << c << " ";
	cout << endl;

    	// Deleting value using erase.after Deleted 2
	// after ptr
	ptr = flist.erase_after(ptr);
	
	// Displaying the forward list
	cout << "The forward list after erase_after operation : ";
	for (int&c : flist) 
		cout << c << " ";
	cout << endl;

	return 0;
}
