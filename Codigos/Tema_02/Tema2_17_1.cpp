#include <iostream>
//#include <iterator>
#include <set>
using namespace std;

int main(){
	set<int, greater<int> > s1; // empty set container
	// insert elements in random order
	s1.insert(40);
	s1.insert(30);
	s1.insert(60);
	s1.insert(20);
	s1.insert(50);
	
	// only one 50 will be added to the set
	s1.insert(50); 
	s1.insert(10);

	set<int, greater<int> >::iterator itr;
	cout << "\nThe set s1 is : \n"; 	// printing set s1
	for (itr = s1.begin(); itr != s1.end(); itr++) 
		cout << *itr<<" ";
	cout << endl;

	// remove element with value 50 in s1
	int num;
	num = s1.erase(50);
	cout << "\ns1.erase(50) : ";
	cout << num << " removed\n";
	for (itr = s1.begin(); itr != s1.end(); itr++) 
		cout <<*itr<<" ";
    cout <<endl;
	// lower bound and upper bound for set s1
	cout << "s1.lower_bound(40) : \n"
		<< *s1.lower_bound(40)
		<< endl;
	cout << "s1.upper_bound(40) : \n"
		<< *s1.upper_bound(40)
		<< endl;

	return 0;
}
