
#include "Car.h"
#include "Distance.h"

// Assignment 6
/*	
	This function calculates and returns the 
	distance it will take to stopthe car at its
	current speed if the breaks are slammed.
*/

double Car::breakingDistance()
{
	length = pow(mph, 2) / 12;
}

//------------------------------------------------------------------------------
/*
	The constructor initializes the car's
	year model and make with parameters y and m.
	Initialize the speed to 0.
*/

Car::Car(int y, string m)
{
	yearModel = y;
	make = m;
	speed = 0;
}

//------------------------------------------------------------------------------
/*
	The setYearModel method sets the car's
	year model to parameter y.
*/

void Car::setYearModel(int y)
{
	yearModel = y;
}

//------------------------------------------------------------------------------
/*
	The setMake method sets the car's make to parameter m.
*/

void Car::setMake(string m)
{
	make = m;
}

//------------------------------------------------------------------------------
/*
	The setSpeed method sets the car's current speed to parameter s.
*/

void Car::setSpeed(int s)
{
	speed = s;
}

//------------------------------------------------------------------------------
/*
	The getYearModel method returns the car's
	year model.
*/

int Car::getYearModel()
{
	return yearModel;
}

//------------------------------------------------------------------------------
/*
	The getMake method returns the car's make.
*/
   
string Car::getMake()
{
	return make;
}

//------------------------------------------------------------------------------
/*
	The getSpeed method returns the car's
	current speed.
*/
   
int Car::getSpeed()
{
	return speed;
}

//------------------------------------------------------------------------------
/*
	The accelerate method increases the car's
	speed by 5 MPH.
*/
   
void Car::accelerate()
{
	speed += 5;
}

//------------------------------------------------------------------------------
/*
	The brake method decreases the car's
	speed by 5 MPH.
*/
   
void Car::brake()
{
	speed -= 5;
}

//------------------------------------------------------------------------------
