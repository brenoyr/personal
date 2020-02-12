#pragma once

class InvalidAmountException
{
private:
	double invalid;

public:
	InvalidAmountException();
	InvalidAmountException(double in);
	double getInvalid();
};

