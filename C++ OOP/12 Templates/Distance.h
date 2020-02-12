// Distance.h

#ifndef INCLUDED_DISTANCE_H
#define INCLUDED_DISTANCE_H

#include<string>
#include<sstream>
using namespace std;

class Distance
{
	private:
		int feet;
		double inches;

	public:
		Distance();
		Distance(int ft, double in);

		int getFeet();
		double getInches();
		void setDist(int ft, double in);
		void setFeet(int ft);
		void setInches(double in);

		bool operator > (const Distance& d);
};

#endif  //  INCLUDED_DISTANCE_H