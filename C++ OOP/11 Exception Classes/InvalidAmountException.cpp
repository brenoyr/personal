#include "InvalidAmountException.h"

InvalidAmountException::InvalidAmountException()
{
}

InvalidAmountException::InvalidAmountException(double in)
{
	invalid = in;
}

double InvalidAmountException::getInvalid()
{
	return invalid;
}