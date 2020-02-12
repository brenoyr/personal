// Distance.cpp

#include "Distance.h"

Distance::Distance() : feet(0), inches(0.0)
{

}

Distance::Distance(int ft, double in) : feet(ft), inches(in)
{

}

int Distance::getFeet()
{
	return feet;
}

double Distance::getInches()
{
	return inches;
}

void Distance::setDist(int ft, double in)
{
	setFeet(ft);
	setInches(in);
}

void Distance::setFeet(int ft)
{
	feet = ft;
}

void Distance::setInches(double in)
{
	inches = in;
}

bool Distance::operator > (const Distance& d)
{
	double thisTotal = feet * 12 + inches;
	double dTotal = d.feet * 12 + d.inches;

	return (thisTotal > dTotal);
}
