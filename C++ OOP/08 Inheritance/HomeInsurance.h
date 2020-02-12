#pragma once
#include "Insurance.h"

class HomeInsurance : public Insurance
{
private:
	string locationAddress;
	double contentsAmount;
	double liabilityAmount;

public:
	HomeInsurance();
	HomeInsurance(double premium, string name, string policyNo,
		string address, double contents, double liability);
	string getLocationAddress();
	double getContentsAmount();
	double getLiabilityAmount();
	void setLocationAddress(string address);
	void setContentsAmount(double contents);
	void setLiabilityAmount(double liability);
	string toString();
};