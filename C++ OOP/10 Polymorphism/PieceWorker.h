#pragma once

#include "Employee.h"

class PieceWorker : public Employee
{
private:
	int quantity;
	double wagePerPiece;

public:
	PieceWorker(string first, string last, double wpp, int q);

	void setQuantity(int q);

	void setWagePerPiece(double wpp);

	virtual string toString();

	virtual double earnings();
};