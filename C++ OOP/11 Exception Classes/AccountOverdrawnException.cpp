#include "AccountOverdrawnException.h"

AccountOverdrawnException::AccountOverdrawnException()
{
}

AccountOverdrawnException::AccountOverdrawnException(double ex)
{
	exception = ex;
}

double AccountOverdrawnException::getInvalid()
{
	return exception;
}