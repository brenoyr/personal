// Breno Yamada Riquieri - CSC240-001 Assignment 7

// TestTemplates.cpp
// Demonstrate function template that finds maximum value in array.
// Uses Distance class which overloads required operator.

#include <iostream>
#include <fstream>
#include <process.h>        //for exit()
#include "ArrayIndexOutOfBoundsException.h"

using namespace std;

#include "Distance.h"
#include "SafeArray.h"

//*********************************************************
// TODO:   Replace these 5 overloaded function declarations
//         with 1 function template declaration.
//*********************************************************

template <class T>
T amax(T arr[], int size);

// Recommended Improvement #1:
template <class T>
void printArray(T arr[], int size, string fileName);
//--------------------------------------------------------------

int main()
{

	char chrArr[5]   = {'r', 'f', 'z', 'b', 'm'};
	int intArr[7]    = {4500, 7000, 3500, 7500, 2500, 6000, 1001};
	long lonArr[4]   = {5000L, 3000L, 8000L, 15000L};
	double dubArr[6] = {700.9, 700.4, 700.2, 700.3, 700.8, 700.1};

	cout << "\nmax in chrArray = " << amax(chrArr, 5);
	cout << "\nmax in intArray = " << amax(intArr, 7);
	cout << "\nmax in lonArray = " << amax(lonArr, 4);
	cout << "\nmax in dubArray = " << amax(dubArr, 6);

	Distance disArray[3];
	disArray[0].setDist(2, 3.5);
	disArray[1].setDist(5, 10.25);
	disArray[2].setDist(3, 7.75);

	Distance dMax = amax(disArray, 3);

	cout << "\nmax in disArray = "
		 << dMax.getFeet() << "'-"
		 << dMax.getInches() << "\""
		 << endl;

	int j;
	// Recommended Improvement #2:
	SafeArray<Distance> isb;	//demonstrating safe array for Distance objects
	SafeArray<int> isa;			//safe array for ints

	for (j = 0; j < LIMIT; j++)        //insert elements
	{
		isa[j] = j * 10;
	}

	cout << "Max int: " << isa.max() << endl;

	// Recommended Improvement #1:
	printArray(chrArr, 5, "CharOutput.txt");
	printArray(intArr, 7, "IntOutput.txt");

	// Recommended Improvement #2:
	try
	{
		isa[LIMIT] = 123;                 //oops! out of bounds
	}
	catch (ArrayIndexOutOfBoundsException ex)
	{
		// Exception error message includes the invalid index:
		cerr << ex.getErrorMessage() << endl;
	}

	cout << endl;

	return 0;
}

//--------------------------------------------------------------

//*********************************************************
// TODO:    Replace these 5 overloaded function definitions
//          with 1 function template definition
//*********************************************************

template <class T>
T amax(T arr[], int size)
{
	T maxvalue = arr[0];

	for (int j = 1; j < size; j++)		//compare all other elements
		if (arr[j] > maxvalue)		    //if one is larger,
			maxvalue = arr[j];          //it becomes largest

	return maxvalue;
}

// Recommended Improvement #1:
template <class T>
void printArray(T arr[], int size, string fileName)
{
	ofstream OutFile;
	OutFile.open(fileName);
	for (int i = 0; i < size; i++)
	{
		// Printing each value in the array to a separate file:
		OutFile << arr[i] << endl;
	}
	OutFile.close();
}

/*


max in chrArray = z
max in intArray = 7500
max in lonArray = 15000
max in dubArray = 700.9
max in disArray = 5'-10.25"
Max int: 990

Abnormal end of program...Index out of bounds
Press any key to continue . . .
*/
