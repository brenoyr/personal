#include "ArrayIndexOutOfBoundsException.h"
#include <iostream>


ArrayIndexOutOfBoundsException::ArrayIndexOutOfBoundsException()
{
}

ArrayIndexOutOfBoundsException::ArrayIndexOutOfBoundsException(int i)
{
	invalidIndex = i;
}

string ArrayIndexOutOfBoundsException::getErrorMessage()
{
	ostringstream outStr;

	outStr << "\nAbnormal end of program..."
		<< "Index out of bounds." << endl
		<< "Invalid index: " << invalidIndex;

	return outStr.str();
}