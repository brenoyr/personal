#include "PayRoll.h"



PayRoll::PayRoll()
{
	// Recommended Improvement #3:
	hours = new double;
	payRate = new double;
}

PayRoll::~PayRoll()
{
	// Recommended Improvement #3:
	delete hours;
	delete payRate;
}

void PayRoll::setHours(double h)
{
	*hours = h;
}

void PayRoll::setPayRate(double p)
{
	*payRate = p;
}

double PayRoll::getGrossPay() const
{
	double grossPay = 0.0;
	double overtime = 0.0;

	grossPay = *hours * *payRate;

	// The following if statement calculates overtime bonus if 
	// applicable (more than 40 hours), and adds it to  grossPay.
	if (*hours > 40.0)
	{
		overtime = (*hours - 40.0) * (0.5 * *payRate);

		grossPay += overtime;
	}

	return grossPay;
}