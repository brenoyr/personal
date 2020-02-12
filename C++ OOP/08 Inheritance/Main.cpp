// CSC240-001 Assignment 3 - Breno Yamada Riquieri

#include <iostream>
#include <string>
using namespace std;

#include "Insurance.h"
#include "AutoInsurance.h"
#include "HomeInsurance.h"

int main()
{
	// Variables for member functions
	double premium = 0.0;
	string name = "";
	string policyNo = "";
	string address = "";
	double contents = 0.0;
	double liability = 0.0;
	double collision = 0.0;
	string vinNo = "";

	// hi1 and ai1 are Albert Anderson`s objects;
	// hi2 and ai2 are Mery Merkle`s objects.

	// hi1 and ai2 will demonstrate the default constructors;
	// hi2 and ai1 will demonstrate the constructors that takes parameters.

	HomeInsurance hi1;

	HomeInsurance hi2(600.00, "Mary Merkle", "H-MM-09876",
		"666 Mirkwood Forest Lane", 45000.00, 90000.00);

	AutoInsurance ai1(425.50, "Albert Anderson", "A-AA-12345",
		50000.00, 100000.00, "ABC12345XYZ");

	AutoInsurance ai2;

	// Asking for user input and using the set functions to define variables
	// for Albert Anderson`s default constructor:

	cout << "Input Information about Albert Anderson`s HOME Insurance:"
		<< endl << endl;

	cout << "Annual Premium: ";
	cin >> premium;
	hi1.setAnnualPremium(premium);

	cout << "Name of Insured: ";
	cin.ignore();
	getline(cin, name);
	hi1.setNameOfInsured(name);

	cout << "Policy Number: ";
	cin >> policyNo;
	hi1.setPolicyNumber(policyNo);

	cout << "Location Address: ";
	cin.ignore();
	getline(cin, address);
	hi1.setLocationAddress(address);

	cout << "Contents Amount: ";
	cin >> contents;
	hi1.setContentsAmount(contents);

	cout << "Liability Amount: ";
	cin >> liability;
	hi1.setLiabilityAmount(liability);

	// Asking for user input and using the set functions to define variables
	// for Mary Merkle`s default constructor:

	cout << endl << "Input Information about Mary Merkle`s AUTO Insurance:"
		<< endl << endl;

	cout << "Annual Premium: ";
	cin >> premium;
	ai2.setAnnualPremium(premium);

	cout << "Name of Insured: ";
	cin.ignore();
	getline(cin, name);
	ai2.setNameOfInsured(name);

	cout << "Policy Number: ";
	cin >> policyNo;
	ai2.setPolicyNumber(policyNo);

	cout << "Collision Amount: ";
	cin >> collision;
	ai2.setCollisionAmount(collision);

	cout << "Liability Amount: ";
	cin >> liability;
	ai2.setLiabilityAmount(liability);

	cout << "VIN Number: ";
	cin >> vinNo;
	ai2.setVinNumber(vinNo);

	// Displaying Albert Anderson`s information:
	
	cout << endl << setfill('-') << setw(40) << '-' << endl
		<< "Albert Anderson's Home and Auto Policies" << endl
		<< setw(40) << '-' << endl << endl << "Home Insurance" << endl << endl;

	// Using "Insurance::" to call data from base class:
	cout << hi1.Insurance::toString() << endl << hi1.toString() << endl;

	cout << "Auto Insurance" << endl << endl;

	cout << ai1.Insurance::toString() << endl << ai1.toString() << endl;

	
	// Displaying Mary Merkle`s information:

	cout << setw(40) << '-' << endl
		<< "Mary Merkle's Home and Auto Policies" << endl
		<< setw(40) << '-' << endl << endl << "Home Insurance" << endl << endl;


	cout << hi2.Insurance::toString() << endl << hi2.toString() << endl;

	cout << "Auto Insurance" << endl << endl;

	cout << ai2.Insurance::toString() << endl << ai2.toString() << endl;

	// Sum of all 4 annual premiums:
	double total = 0.0;

	total = hi1.getAnnualPremium() + hi2.getAnnualPremium()
		+ ai1.getAnnualPremium() + ai2.getAnnualPremium();

	cout << setw(40) << '-' << endl
		<< "Total Annual Premiums: " << total << endl
		<< setw(40) << '-' << endl << endl;
}
