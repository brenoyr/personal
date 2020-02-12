#include "PieceWorker.h"



PieceWorker::PieceWorker(string first, string last, double wpp, int q)
	: Employee(first, last)
{
	setWagePerPiece(wpp);
	setQuantity(q);
}

void PieceWorker::setQuantity(int q)
{
	quantity = q;
}

void PieceWorker::setWagePerPiece(double wpp)
{
	wagePerPiece = wpp;
}

string PieceWorker::toString()
{
	return "Piece worker: " + Employee::toString();
}

double PieceWorker::earnings()
{
	return quantity * wagePerPiece;
}