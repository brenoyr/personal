// Breno Yamada Riquieri CSC240 - Assignment 5

// TestEmployee.cpp

/*  Driver for Employee hierarchy

    Intended to demonstrate dynamic "late" binding of a function call
    to its definition at run-time.  This can happen when a member function
    declared in a base class is called but a definition in a derived class
    actually runs (executes).

    In other words, calling the same member function may be used to invoke
    member functions defined in different but related classes.
	(That is "true polymorphism").
*/

#include<iostream>
#include<iomanip>
using namespace std;

#include "Employee.h"
#include "Boss.h"
#include "CommissionWorker.h"
#include "HourlyWorker.h"
#include "PieceWorker.h"

void printResults(Employee& emp);

double getTotalEarnings(Employee* ptrEmployee[], int size);

//------------------------------------------------------------------------------

int main()
{
		// Define objects for each derived class

    Boss b("John", "Smith", 800.00);

    CommissionWorker cw("Sue", "Jones", 400.25, 3.05, 150);

    HourlyWorker hw("Karen", "Price", 13.76, 40);

	PieceWorker pw("Bob", "Lewis", 2.52, 204);

	const int ARRAY_SIZE = 10;
	Employee* ptrEmployee[ARRAY_SIZE] = { &b, &cw, &hw, &pw };

		// Print results

    cout << "- Demonstrating Polymorphism -" << endl
		 << endl;

	/*
	  		Call printResult function once for each object
	*/

	printResults(b);

	printResults(cw);

	printResults(hw);

	printResults(pw);

	double average = 0.0;
	double total = 0.0;

	total = getTotalEarnings(ptrEmployee, 4);

	average = total / 4;

	cout << "Total Earnings: " << setw(12) << total
		<< endl
		<< "Average Earnings: " << setw(10) << average
		<< endl << endl;

    cout << "- End Program - " << endl;

	return 0;
}

//------------------------------------------------------------------------------


	/*
	  		Define printResult function to print an employee's
	        class, first and last name, and earnings.
	*/

// "emp.toString()" and "emp.earnings()" will call the function from
// the right class thanks to virtual member functions. Therefore, they are
// doing dynamic binding.
void printResults(Employee& emp)
{
	cout << fixed << setprecision(2);

	cout << emp.toString() << endl
		<< "Earnings: $" << emp.earnings()
		<< endl << endl;
}

// Recommended improvement #2
double getTotalEarnings(Employee* ptrEmployee[], int size)
{
	double sum = 0;

	for (int i = 0; i < size; i++)
	{
		sum += ptrEmployee[i]->earnings();
	}

	return sum;
}


//------------------------------------------------------------------------------
