// Breno Yamada Riquieri - Assignment 2 - CSC240-001

#include <iostream>
#include <iomanip>
#include "PayRoll.h"

using namespace std;

void userInput(PayRoll* const prtEmployee, const int EMP_NUM);
void printInfo(const PayRoll* const ptrEmployee, const int EMP_NUM);

int main()
{
	// Dynamically allocating an array for PayRoll, while making ptrEmployee
	// point to it:
	const int EMP_NUM = 7;
	PayRoll* ptrEmployee = new PayRoll[EMP_NUM];

	userInput(ptrEmployee, EMP_NUM);	// Calling input function.
	printInfo(ptrEmployee, EMP_NUM);	// Calling print function.

	delete [] ptrEmployee;	// Deleting ptrEmployee to avoid inconveniences.

	return 0;
}

// PURPOSE:			Receive input from the user.
//
// PRECONDITION:	ptrEmployee[EMP_NUM] defined.
//
// POSTCONDITION:	Each object will receive hours and payRate from user.

void userInput(PayRoll* const ptrEmployee, const int EMP_NUM)
{
	double h = 0.0;
	double p = 0.0;

	// The following for loop will promp user for hours and pay rate for
	// each employee. It also calls the appropriate set function to assign
	// its value in the array.
	for (int i = 0; i < EMP_NUM; i++)
	{
		cout << "Enter hours for employee #" << i + 1 << ": ";
		cin >> h;
		ptrEmployee[i].setHours(h);

		cout << "Enter pay rate for employee #" << i + 1 << ": ";
		cin >> p;
		ptrEmployee[i].setPayRate(p);

		cout << endl;
	}
}

// PURPOSE:			Print data for each employee.
//
// PRECONDITION:	userInput function called
//					(hours + payRate given to each employee).
//
// POSTCONDITION:	Function will print a table with data from the employees.

void printInfo(const PayRoll* const ptrEmployee, const int EMP_NUM)
{
	cout << fixed << showpoint << setprecision(2);

	cout << "Employee" << setw(12) << "Gross Pay" << endl
		<< setfill('=') << setw(8) << '=' << "   " << setw(9) << '='
		<< setfill(' ') << endl;

	// The following for loop simply prints a line with a single employee`s
	// gross pay, which is provided by calling the getGrossPay member function.
	for (int i = 0; i < EMP_NUM; i++)
	{
		cout << setw(4) << i + 1 << ": " << setw(7) << "$ "
			<< setw(6) << ptrEmployee[i].getGrossPay() << endl;
	}

	cout << endl;
}
