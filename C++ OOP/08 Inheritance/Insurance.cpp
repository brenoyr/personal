#include "Insurance.h"

Insurance::Insurance()
{
	annualPremium = 0.0;
	nameOfInsured = "";
	policyNumber = "";
}

Insurance::Insurance(double premium, string name, string policyNo)
{
	annualPremium = premium;
	nameOfInsured = name;
	policyNumber = policyNo;
}

double Insurance::getAnnualPremium()
{
	return annualPremium;
}

string Insurance::getNameOfInsured()
{
	return nameOfInsured;
}

string Insurance::getPolicyNumber()
{
	return policyNumber;
}

void Insurance::setAnnualPremium(double premium)
{
	annualPremium = premium;
}

void Insurance::setNameOfInsured(string name)
{
	nameOfInsured = name;
}

void Insurance::setPolicyNumber(string policyNo)
{
	policyNumber = policyNo;
}

string Insurance::toString()
{
	ostringstream strOut;

	strOut << fixed << showpoint << setprecision(2);

	strOut << setw(20) << "Annual Premium: " << setw(7) << annualPremium
		<< endl;
	strOut << setw(20) << "Name of Insured: " << setw(7) << nameOfInsured
		<< endl;
	strOut << setw(20) << "Policy Number: " << setw(7) << policyNumber
		<< endl;

	return strOut.str();
}