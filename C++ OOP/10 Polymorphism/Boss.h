// Boss.h

/*  Boss class derived from Employee.

*/

#pragma once;

#include "Employee.h"

class Boss : public Employee
{
private:
	double weeklySalary;

public:
      // Constructor for class Boss

  Boss( string first, string last, double s);

      // Set the Boss's salary

  void setWeeklySalary( double s );

      // Override base class function, and
      // Print the Boss's name

  virtual string toString();

      // Get the Boss's pay
      // Must override base class function

  virtual double earnings();

};