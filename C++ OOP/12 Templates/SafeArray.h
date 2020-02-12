// SafeArray.h

#include "ArrayIndexOutOfBoundsException.h"

#pragma once;

const int LIMIT = 100;      //array size

template <class T>
class SafeArray
{
	private:
		T arr[LIMIT];

	public:
		T& operator [](T n);
		T max();
};

/*	NOTE:	Some IDE's will not compile templates that are located in
			separate specification (.h) and implementation (.cpp) files.

			With Microsoft Visual Studio, we "do not" add the .cpp file
			in the Solution Explorer.  Instead, to work around the problem,
			we can #include the .cpp file for a class template
			following the definition of that class as shown below...
*/

#include "SafeArray.cpp"