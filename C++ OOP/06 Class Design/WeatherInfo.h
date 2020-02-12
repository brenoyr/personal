#pragma once
#include <string>
using namespace std;

class WeatherInfo
{
private:
	string weekDay;
	int highTemp;
	int lowTemp;
	double rainFall;

public:
	WeatherInfo();
	WeatherInfo(string day, int hi, int lo, double rain);
	string getWeekDay();
	int getHighTemp();
	int getLowTemp();
	double getRainFall();
	void setWeekDay(string day);
	void setHighTemp(int degrees);
	void setLowTemp(int degrees);
	void setRainFall(double inches);
	string toString();
};