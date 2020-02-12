// Employee.cpp

#include "Employee.h"

      // Constructor

Employee::Employee( string first, string last )
{
	firstName = first;
	lastName = last;
}

      // Return an Employee's first name

string Employee::getFirstName()
{
	return firstName;
}

      // Return an Employee's last name

string Employee::getLastName()
{
	return lastName;
}

      // Return a string representation of an Employee

string Employee::toString()
{
	return firstName + ' ' + lastName;
}

      // Deleted original Employee::earnings() for
	  // recommended improvement #3.