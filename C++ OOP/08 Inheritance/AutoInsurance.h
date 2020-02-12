#pragma once

#include "Insurance.h"

class AutoInsurance : public Insurance
{
private:
	double collisionAmount;
	double liabilityAmount;
	string vinNumber;

public:
	AutoInsurance();
	AutoInsurance(double premium, string name, string policyNo,
		double collision, double liability, string vinNo);
	double getCollisionAmount();
	double getLiabilityAmount();
	string getVinNumber();
	void setCollisionAmount(double collision);
	void setLiabilityAmount(double liability);
	void setVinNumber(string vinNo);
	string toString();
};