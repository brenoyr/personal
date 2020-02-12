#pragma once
#include <string>
#include <sstream>
#include <iomanip>
using namespace std;

class Insurance
{
private:
	double annualPremium;
	string nameOfInsured;
	string policyNumber;

public:
	Insurance();
	Insurance(double premium, string name, string policyNo);
	double getAnnualPremium();
	string getNameOfInsured();
	string getPolicyNumber();
	void setAnnualPremium(double premium);
	void setNameOfInsured(string name);
	void setPolicyNumber(string policyNo);
	string toString();
};