
#pragma once

#include<string>
using namespace std;

/*
	The Car class stores data about a car.
*/

class Car
{
	private:
		int yearModel;			// The car's year model
		string make;			// The car's make
		int speed;				// The current speed

	public:

		// Constructor
		Car(int y, string m);

		// Transformers
		void setYearModel(int y);
		void setMake(string m);
		void setSpeed(int s);
		void accelerate();
		void brake();

		// Observers
		int getYearModel();
		string getMake();
		int getSpeed();

		// Assignment 6
		double breakingDistance();
};

