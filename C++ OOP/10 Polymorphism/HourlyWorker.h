// HourlyWorker.h

/*  Definition of class HourlyWorker

*/

#pragma once;

#include "Employee.h"

class HourlyWorker : public Employee
{
private:
	double wage;                        // wage per hour
    double hours;                       // hours worked for week

public:
      // Constructor for class HourlyWorker

  HourlyWorker( string first, string last,
                double w, double h );

      // Set the wage

  void setWage( double w );

      // Set the hours worked

  void setHours( double h );

      // Override base class function
      // Print HourlyWorker name

  virtual string toString();

      // Get the HourlyWorker's pay
      // Must override base class function

  virtual double earnings();

};