#include "AutoInsurance.h"

// ": Insurance" used for inheritance
AutoInsurance::AutoInsurance() : Insurance()
{
	collisionAmount = 0.0;
	liabilityAmount = 0.0;
	vinNumber = "";
}

// ": Insurance" used for inheritance
AutoInsurance::AutoInsurance(double premium, string name, string policyNo,
						 double collision, double liability, string vinNo)
									  : Insurance(premium, name, policyNo)
{
	collisionAmount = collision;
	liabilityAmount = liability;
	vinNumber = vinNo;
}

double AutoInsurance::getCollisionAmount()
{
	return collisionAmount;
}

double AutoInsurance::getLiabilityAmount()
{
	return liabilityAmount;
}

string AutoInsurance::getVinNumber()
{
	return vinNumber;
}

void AutoInsurance::setCollisionAmount(double collision)
{
	collisionAmount = collision;
}

void AutoInsurance::setLiabilityAmount(double liability)
{
	liabilityAmount = liability;
}

void AutoInsurance::setVinNumber(string vinNo)
{
	vinNumber = vinNo;
}

string AutoInsurance::toString()
{
	ostringstream strOut;

	strOut << fixed << showpoint << setprecision(2);
	
	strOut << setw(20) << "Collision Amount: " << setw(7) << collisionAmount
		<< endl
		<< setw(20) << "Liability Amount: " << setw(7) << liabilityAmount
		<< endl
		<< setw(20) << "VIN Number: " << setw(7) << vinNumber
		<< endl;

	return strOut.str();
}