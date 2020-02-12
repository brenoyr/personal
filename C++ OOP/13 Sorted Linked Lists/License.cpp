


#include "License.h"

License::License()
{
	licenseNumber = 0;
	personName = "";
}

License::License(int number, string name)
{
	licenseNumber = number;
	personName = name;
}

int License::getLicenseNumber() const
{
	return licenseNumber;
}

string License::getPersonName() const
{
	return personName;
}

bool License::operator< (License obj)
{
	return (this->getLicenseNumber() < obj.getLicenseNumber());
}

bool License::operator== (License obj)
{
	return (this->getLicenseNumber() == obj.getLicenseNumber());
}

bool License::operator!= (License obj)
{
	return (this->getLicenseNumber() != obj.getLicenseNumber());
}