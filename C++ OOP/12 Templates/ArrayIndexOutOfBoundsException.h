#pragma once

#include<string>
#include <sstream>
using namespace std;

class ArrayIndexOutOfBoundsException
{
private:
	int invalidIndex;

public:
	ArrayIndexOutOfBoundsException();
	ArrayIndexOutOfBoundsException(int i);
	string getErrorMessage();
};

