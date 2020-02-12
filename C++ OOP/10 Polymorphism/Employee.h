// Employee.h

/*  Base class Employee.

    Declaring contructors using "protected" means that the class
    should be used only as a base class.  You cannot create objects
    of type Employee.  We cannot make it private because derived
	class contructors must be able to access the base class
	contructor when those objects are defined.
*/

#pragma once;

#include<string>
using namespace std;

class Employee
{
private:
	string firstName;
    string lastName;

protected:
      // Constructor
  Employee( string first, string last );

public:

      // Return an Employee's first name

  string getFirstName();

      // Return an Employee's last name

  string getLastName();

      // Return a string representation of an Employee

  virtual string toString();

      // Return an Employee's earnings
	  // Recommended Improvement #3:

  virtual double earnings() = 0;
};