#pragma once
#include<string>

using namespace std;

class Distance
{
private:
	long length;

public:
	void setLength(long newLength);

	long getLength();

	double getLengthInFeet();

	int getFeet();

	int getInches();

	void setFeet(int newFeet);

	void setInches(int newInches);

	Distance();

	Distance(long initialLength);

	string toString();
};