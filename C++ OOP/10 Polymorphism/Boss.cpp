// Boss.cpp

/*  Boss class derived from Employee.

	A boss' earnings is simply the weeklySalary.

*/

#include "Boss.h"

  // Constructor for class Boss

Boss::Boss( string first, string last, double s)
  : Employee(first, last)             // call base class constructor
{
	setWeeklySalary( s );
}

  // Set the Boss's salary

void Boss::setWeeklySalary( double s )
{
	weeklySalary = ( s > 0 ) ? s : 0;
}

  // Override and modify base class function to
  // print class name along with first and last name

string Boss::toString()
{
	return "Boss: " + Employee::toString();
}

  // Override and hide base class function to
  // return the earnings for a Boss

double Boss::earnings()
{
	return weeklySalary;
}

