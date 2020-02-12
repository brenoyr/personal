


#pragma once

#include<string>
using namespace std;

class License
{
private:
	int licenseNumber;
	string personName;

public:
	License();
	License(int number, string name);

	int getLicenseNumber() const;
	string getPersonName() const;

	bool operator< (License obj);
	bool operator== (License obj);
	bool operator!= (License obj);
};
