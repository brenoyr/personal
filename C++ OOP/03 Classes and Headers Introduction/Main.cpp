#include<iostream>
#include <iomanip>
#include "Distance.h"

using namespace std;

int main()
{
	Distance();

	Distance dist1;
	dist1.setLength(126);

	cout << "Distance: " << fixed << showpoint << setprecision(2)
		<< dist1.getLengthInFeet() << " total feet" << endl
		<< "Length: " << dist1.getLength() << " total inches" << endl
		<< "Feet: " << dist1.getFeet() << endl
		<< "Inches: " << dist1.getInches() << endl
		<< "Formatted: " << dist1.toString() << endl << endl;

	double mph;
	mph = 2 * sqrt(3 * dist1.getLengthInFeet());
	cout << "Approximate speed for this length skid mark:" << endl << endl
		<< mph << " mph" << endl << endl;

	dist1.setFeet(155);

	cout << "After changing just feet to 155..." << endl << endl
		<< "Distance: " << dist1.getLengthInFeet() << " total feet" << endl
		<< "Length: " << dist1.getLength() << " total inches" << endl
		<< "Feet: " << dist1.getFeet() << endl
		<< "Inches: " << dist1.getInches() << endl
		<< "Formatted: " << dist1.toString() << endl << endl;

	dist1.setInches(3);

	cout << "After changing just inches to 3..." << endl << endl
		<< "Distance: " << dist1.getLengthInFeet() << " total feet" << endl
		<< "Length: " << dist1.getLength() << " total inches" << endl
		<< "Feet: " << dist1.getFeet() << endl
		<< "Inches: " << dist1.getInches() << endl
		<< "Formatted: " << dist1.toString()  << endl << endl;

	mph = 2 * sqrt(3 * dist1.getLengthInFeet());
	cout << "Approximate speed for this length skid mark:" << endl << endl
		<< mph << " mph" << endl << endl;

	// Other objects:

	Distance dist2 = Distance(152);
	Distance dist3 = Distance(126);

	cout << "dist1: " << dist1.toString() << endl << endl;

	cout << "dist2: " << dist2.toString() << endl << endl;

	cout << "dist3: " << dist3.toString() << endl << endl;
	
	int sumLength;
	int sumFeet;
	int sumInches;

	sumLength = dist1.getLength() + dist2.getLength() + dist3.getLength();
	
	sumFeet = static_cast<int>(sumLength) / 12;
	
	sumInches = static_cast<int>(sumLength) % 12;

	cout << "sum: " << sumFeet << "'" << sumInches << "\"" << endl << endl;
}
