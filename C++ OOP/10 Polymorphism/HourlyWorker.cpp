// HourlyWorker.cpp

/*  Definition of class HourlyWorker

	An HourlyWorker's earnings is wage * hours
*/

#include "HourlyWorker.h"


  // Constructor for class HourlyWorker

HourlyWorker::HourlyWorker( string first, string last,
              				double w, double h )
  : Employee(first, last)                     // call base class constructor
{
	setWage( w );
	setHours( h );
}

  // Set the wage

void HourlyWorker::setWage( double w )
{
	wage = ( w > 0 ) ? w : 0;
}

  // Set the hours worked

void HourlyWorker::setHours( double h )
{
	hours = ( h >= 0 && h < 168 ) ? h : 0;
}

  // Override base class function
  // Print HourlyWorker name

string HourlyWorker::toString()
{
	return "Hourly worker: " + Employee::toString();
}

  // Get the HourlyWorker's pay
  // Must override base class function

double HourlyWorker::earnings()
{
	return wage * hours;
}

