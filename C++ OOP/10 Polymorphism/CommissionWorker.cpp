// CommissionWorker.cpp

/*  CommissionWorker class derived from Employee

	A CommissionWorker's earnings is

	salary + (commission * quantity)

*/

#include "CommissionWorker.h"


  // Constructor for class CommissionWorker

CommissionWorker::CommissionWorker( string first, string last,
			                        double s, double c, int q)
	: Employee(first, last)                 // call base class constructor
{
	setSalary( s );
	setCommission( c );
	setQuantity( q );
}

  // Set CommissionWorker's weekly base salary

void CommissionWorker::setSalary( double s )
{
	salary = ( s > 0 ) ? s : 0;
}

  // Set CommissionWorker's commission

void CommissionWorker::setCommission( double c )
{
	commission = ( c > 0 ) ? c : 0;
}

  // Set CommissionWorker's quantity sold

void CommissionWorker::setQuantity( int q )
{
	quantity = ( q > 0 ) ? q : 0;
}

  // Determine CommissionWorker's earnings
  // Must override base class function

double CommissionWorker::earnings()
{
	return salary + (commission * quantity);
}

  // Override the base class function
  // Print the CommissionWorker's name

string CommissionWorker::toString()
{
	return "Commission worker: " + Employee::toString();
}

