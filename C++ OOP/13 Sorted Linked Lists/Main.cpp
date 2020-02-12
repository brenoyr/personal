/*
	Name: Breno Yamada Riquieri

	CSC 240, Assignment 8

*/

#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include "SortedList.h"
using namespace std;

int main()
{
	ifstream inData;
	ofstream outDataDuplicates;
	
	License license;
	SortedList list;
	int licenseNo;
	string name;

	inData.open("licensesa.txt");
	outDataDuplicates.open("ducplicates.txt");

	inData >> licenseNo;
	while (!inData.eof())
	{
		inData.ignore(1);
		getline(inData, name);

		license = License(licenseNo, name);

		if (list.IsThere(license))
		{
			outDataDuplicates << licenseNo << ' ' << name << endl;
			
			cout << licenseNo << ' ' << name << endl;
		}
		else
		{
			list.Insert(license);
		}

		inData >> licenseNo;
	}
	
	inData.close();
	outDataDuplicates.close();

	ofstream outDataSorted;
	outDataSorted.open("licenselist.txt");
	
	list.ResetList();

	while (list.HasNext())		// infinite loop
	{
		license = list.GetNextItem();
		outDataSorted << license.getLicenseNumber() << ' '
					  << license.getPersonName() << endl;
	}

	cout << endl;
	return 0;
}
