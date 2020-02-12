#include "Distance.h"
#include<iostream>
#include<sstream>
using namespace std;

void Distance::setLength(long newLength)
{
	length = newLength;
}

long Distance::getLength()
{
	return length;
}

double Distance::getLengthInFeet()
{
	double lengthInFeet;
	lengthInFeet = static_cast<double>(length) / 12;
	return lengthInFeet;
}

int Distance::getFeet()
{
	int feet;
	feet = static_cast<int>(length) / 12;
	return feet;
}

int Distance::getInches()
{
	int inches;
	inches = static_cast<int>(length) % 12;
	return inches;
}

void Distance::setFeet(int newFeet)
{
	newFeet *= 12;
	length = getInches() + newFeet;
}

void Distance::setInches(int newInches)
{
	length = getFeet() * 12;
	length += newInches;
}

Distance::Distance()
{
	length = 1;
}

Distance::Distance(long initialLength)
{
	length = initialLength;
}

string Distance::toString()
{
	ostringstream outStr;

	outStr << static_cast<int>(length) / 12 << "'"
		<< static_cast<int>(length) % 12 << "\"";

	return outStr.str();
}