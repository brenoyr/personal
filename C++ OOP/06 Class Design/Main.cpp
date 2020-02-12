// CSC240-001 - Assignment 1 - Breno Yamada Riquieri

#include <iostream>
#include <string>
#include <iomanip>
#include "WeatherInfo.h"

using namespace std;

// Main functions:
int userInput(WeatherInfo week[], const int DAYS);
void printWeatherInfo(WeatherInfo week[], int dayCount);
int indexOfHighestTemp(WeatherInfo week[], int dayCount);
int indexOfLowestTemp(WeatherInfo week[], int dayCount);
double totalRainFall(WeatherInfo week[], int dayCount);
double averageHighTemp(WeatherInfo week[], int dayCount, double averageHigh);
double averageLowTemp(WeatherInfo week[], int dayCount, double averageLow);

// Enter main():
int main()
{
	// Define maximum number of days the array can store, then
	// initialize the array with the const amount of days.
	const int DAYS = 7;
	WeatherInfo week[DAYS];

	// Call function that will store values in the week[] array, as well
	// as return the number of days used: dayCount.
	int dayCount = userInput(week, DAYS);

	// Print the user inputs window.
	printWeatherInfo(week, dayCount);

	// Initialize averageRain and call totalRainFall function in order to
	// define the average by dividing total rain fall by the day counter.
	double averageRain = static_cast<double>(totalRainFall(week, dayCount))
						 / dayCount;
	
	// Initialize the variable that will hold the value returned by
	// the averageHighTemp function.
	double averageHigh = 0.0;
	averageHigh = averageHighTemp(week, dayCount, averageHigh);
	
	// Initialize the variable that will hold the value returned by
	// the averageLowTemp function.
	double averageLow = 0.0;
	averageLow = averageLowTemp(week, dayCount, averageLow);

	// Print averages.
	cout << fixed << setprecision(1)
		<< setw(20) << "Averages" << setw(10) << averageHigh
		<< setw(10) << averageLow << setw(10) << averageRain << endl << endl;

	// This cout statement calls a function to find the index of the
	// day with the highest temperature. It then prints the value by
	// calling its get function.
	cout << "Highest reading: " << setw(6)
		<< week[indexOfHighestTemp(week, dayCount)].getHighTemp()
		<< "   [" << week[indexOfHighestTemp(week, dayCount)].getWeekDay()
		<< ']' << endl;

	// This cout statement calls a function to find the index of the
	// day with the lowest temperature. It then prints the value by
	// calling its get function.
	cout << "Lowest reading: " << setw(7)
		<< week[indexOfLowestTemp(week, dayCount)].getLowTemp()
		<< "   [" << week[indexOfLowestTemp(week, dayCount)].getWeekDay()
		<< ']' << endl;

	// Call totalRainFall to get the total rain fall in inches and print it.
	cout << "Total rainfall: " << setw(7)
		<< totalRainFall(week, dayCount) << "\"";

	// End program.
	cout << endl << endl;

	return 0;
}

/************************************************************************
PURPOSE:		Prompt and receive user inputs.							*
*
PRECONDITION:	week[] must have been defined; DAYS must`ve been		*
defined and initialized.								*
*
POSTCONDITION:	week[] will hold values for each day entered;			*
function will return dayCounter.						*
*************************************************************************/
int userInput(WeatherInfo week[], const int DAYS)
{
	char response;
	int dayCounter = 0;
	string day;
	int hi;
	int lo;
	double rain;

	do
	{
		cout << "Enter day of week (eg. Sunday, Monday, etc...): ";
		cin >> day;

		cout << "Enter high temperature in degrees Fahr: ";
		cin >> hi;

		cout << "Enter low temperature in degrees Fahr: ";
		cin >> lo;

		cout << "Enter total rainfall in inches: ";
		cin >> rain;

		cout << endl;

		// Initialize the array instance with the values inputted by the user.
		week[dayCounter] = WeatherInfo(day, hi, lo, rain);

		dayCounter++;	// Increment dayCounter to move on to the next
						// array instance.
		
		// The following if statement will ask the user if the program should
		// continue, but only if the dayCounter is still valid for this array.
		if (dayCounter < DAYS)
		{
			cout << "Another day (y or n): ";
			cin >> response;
			response = tolower(response);
			cout << endl;
		}

	} while (response == 'y' && dayCounter < DAYS);

	// Return the amount of days the user used.
	return dayCounter;
}

/****************************************************************************
	PURPOSE:		Display user inputs window.								*
																			*
	PRECONDITION:	toString (weekDay, highTemp, lowTemp, and rainFall),	*
					week[],	and dayCount must hold values.					*
																			*
	POSTCONDITION:	Program will have printed a window with the information	*
					adquired from the user.									*
****************************************************************************/
void printWeatherInfo(WeatherInfo week[], int dayCount)
{
	cout << setw(20) << "Week Day" << setw(10) << "Hi"
		<< setw(10) << "Low" << setw(10) << "Rain" << endl;

	cout << "            " << setfill('-') << setw(38) << '-' << endl;

	// This for loop is prints the user inputs
	// by calling the toString function for everyday the user used.
	for (int i = 0; i < dayCount; i++)
	{
		cout << week[i].toString() << endl;
	}

	cout << "            " << setw(38) << '-' << setfill(' ') << endl;
}

/************************************************************************
PURPOSE:		Find the total inches of rain fall for the valid days.	*
*
PRECONDITION:	week[] and dayCount must contain values.				*
*
POSTCONDITION:	Function will return total totalRain.					*
*************************************************************************/
double totalRainFall(WeatherInfo week[], int dayCount)
{
	double totalRain = 0.0;

	for (int i = 0; i < dayCount; i++)
		totalRain += week[i].getRainFall();

	return totalRain;
}

/************************************************************************
PURPOSE:		Find the average between the high temperatures.			*
																		*
PRECONDITION:	averageHigh must`ve been defined;						*
				week[] and dayCount must contain values.				*
																		*
POSTCONDITION:	Function will return the average value of high			*
				temperatures between the valid days (totalHigh).		*
*************************************************************************/
double averageHighTemp(WeatherInfo week[], int dayCount, double averageHigh)
{
	int totalHigh = 0;

	for (int i = 0; i < dayCount; i++)
	{
		totalHigh += week[i].getHighTemp();
	}

	averageHigh = static_cast<double>(totalHigh) / dayCount;

	return averageHigh;
}

/************************************************************************
PURPOSE:		Find the average between the low temperatures.			*
																		*
PRECONDITION:	averageLow must`ve been defined;						*
				week[] and dayCount must contain values.				*
																		*
POSTCONDITION:	Function will return the average value of low			*
				temperatures between the valid days (totalLow).			*
*************************************************************************/
double averageLowTemp(WeatherInfo week[], int dayCount, double averageLow)
{
	int totalLow = 0;

	for (int i = 0; i < dayCount; i++)
	{
		totalLow += week[i].getLowTemp();
	}

	averageLow = static_cast<double>(totalLow) / dayCount;

	return averageLow;
}

/************************************************************************
PURPOSE:		Find the highest temperature and which day is it.	*
*
PRECONDITION:	week[] and dayCount must contain values.			*
*
POSTCONDITION:	Function will return the index of the day with the	*
highest temperature (indexHigh).					*
*************************************************************************/
int indexOfHighestTemp(WeatherInfo week[], int dayCount)
{
	int indexHigh = 0;

	// This for loop updates indexHigh everytime it finds a higher value.
	for (int i = 1; i < dayCount; i++)
	{
		if (week[i].getHighTemp() > week[indexHigh].getHighTemp())
			indexHigh = i;
	}

	return indexHigh;
}

/************************************************************************
PURPOSE:		Find the lowest temperature and which day is it.		*
*
PRECONDITION:	week[] and dayCount must contain values.				*
*
POSTCONDITION:	Function will return the index of the day with the		*
lowest temperature (indexLow).							*
*************************************************************************/
int indexOfLowestTemp(WeatherInfo week[], int dayCount)
{
	int indexLow = 0;

	// This for loop updates indexLow everytime it finds a lower value.
	for (int i = 0; i < dayCount; i++)
	{
		if (week[i].getLowTemp() < week[indexLow].getLowTemp())
			indexLow = i;
	}

	return indexLow;
}
