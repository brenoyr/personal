#include "HomeInsurance.h"


// ": Insurance" used for inheritance
HomeInsurance::HomeInsurance() : Insurance()
{
	locationAddress = "";
	contentsAmount = 0.0;
	liabilityAmount = 0.0;
}

// ": Insurance" used for inheritance
HomeInsurance::HomeInsurance(double premium, string name, string policyNo,
						string address, double contents, double liability)
									  : Insurance(premium, name, policyNo)
{
	locationAddress = address;
	contentsAmount = contents;
	liabilityAmount = liability;
}

string HomeInsurance::getLocationAddress()
{
	return locationAddress;
}

double HomeInsurance::getContentsAmount()
{
	return contentsAmount;
}

double HomeInsurance::getLiabilityAmount()
{
	return liabilityAmount;
}

void HomeInsurance::setLocationAddress(string address)
{
	locationAddress = address;
}

void HomeInsurance::setContentsAmount(double contents)
{
	contentsAmount = contents;
}

void HomeInsurance::setLiabilityAmount(double liability)
{
	liabilityAmount = liability;
}

string HomeInsurance::toString()
{
	ostringstream strOut;

	strOut << fixed << showpoint << setprecision(2);

	strOut << setw(20) << "Location Address: " << setw(7) << locationAddress
		<< endl
		<< setw(20) << "Contents Amount: " << setw(7) << contentsAmount
		<< endl
		<< setw(20) << "Liability Amount: " << setw(7) << liabilityAmount
		<< endl;

	return strOut.str();
}