#include "WeatherInfo.h"
#include <sstream>
#include <iomanip>
#include<iostream>

using namespace std;

WeatherInfo::WeatherInfo()
{
	weekDay = "";
	highTemp = 0;
	lowTemp = 0;
	rainFall = 0.0;
}

WeatherInfo::WeatherInfo(string day, int hi, int lo, double rain)
{
	weekDay = day;
	highTemp = hi;
	lowTemp = lo;
	rainFall = rain;
}

string WeatherInfo::getWeekDay()
{
	return weekDay;
}

int WeatherInfo::getHighTemp()
{
	return highTemp;
}

int WeatherInfo::getLowTemp()
{
	return lowTemp;
}

double WeatherInfo::getRainFall()
{
	return rainFall;
}

void WeatherInfo::setWeekDay(string day)
{
	weekDay = day;
}

void WeatherInfo::setHighTemp(int degrees)
{
	highTemp = degrees;
}

void WeatherInfo::setLowTemp(int degrees)
{
	lowTemp = degrees;
}

void WeatherInfo::setRainFall(double inches)
{
	rainFall = inches;
}

// This function allows printing values in an instance of the array.
string WeatherInfo::toString()
{
	ostringstream strOut;
	strOut << fixed << showpoint << setprecision(1);

	strOut << setw(20) << weekDay << setw(10) << highTemp
		   << setw(10) << lowTemp << setw(10) << rainFall
		   << ends;

	// Returns the whole string so it can be printed.
	return strOut.str();
}

