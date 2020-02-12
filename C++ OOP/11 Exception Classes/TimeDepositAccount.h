/*  TimeDepositAccount.h
*/

#pragma once;

#include "SavingsAccount.h"

const double EARLY_WITHDRAWAL_PENALTY = 20;

class TimeDepositAccount : public SavingsAccount
{
private:
	int periodsToMaturity;



public:
	TimeDepositAccount(double rate, int maturity);

    void addInterest();

    void withdraw(double amount);


};
