// CommissionWorker.h

/*  CommissionWorker class derived from Employee

*/

#pragma once;

#include "Employee.h"

class CommissionWorker : public Employee
{
private:
	double salary;                    // base salary per week
	double commission;                // amount per item sold
	int quantity;                     // total items sold for week

public:
      // Constructor for class CommissionWorker

  CommissionWorker( string first, string last,
                    double s, double c, int q);

      // Set CommissionWorker's weekly base salary

  void setSalary( double s );

      // Set CommissionWorker's commission

  void setCommission( double c );

      // Set CommissionWorker's quantity sold

  void setQuantity( int q );

      // Override the base class function
      // Print the CommissionWorker's name

  virtual string toString();

      // Determine CommissionWorker's earnings
      // Must override base class function

  virtual double earnings();

};