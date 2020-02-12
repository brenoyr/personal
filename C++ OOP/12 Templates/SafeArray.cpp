// SafeArray.cpp


#include <process.h>        //for exit()
#include "SafeArray.h"

template <class T>
T& SafeArray<T>::operator [](T n)
{
	// Throwing ArrayIndexOutOfBoundsException
	// with the invalid index as the parameter:
	if (n < 0 || n >= LIMIT)
		throw ArrayIndexOutOfBoundsException(n);	//Recommended Improvement 2

	return arr[n];
}


template<class T>
T SafeArray<T>::max()
{
	T maxvalue = arr[0];				//start with first element

	for (int j = 0; j < LIMIT; j++)
	{										//compare all other elements
		if (arr[j] > maxvalue)				//if one is larger,
			maxvalue = arr[j];
	}										//it becomes largest

	return maxvalue;
}
