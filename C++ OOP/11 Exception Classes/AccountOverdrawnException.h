#pragma once

class AccountOverdrawnException
{
private:
	double exception;

public:
	AccountOverdrawnException();
	AccountOverdrawnException(double ex);
	double getInvalid();
};

