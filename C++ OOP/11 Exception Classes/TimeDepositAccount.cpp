/*  TimeDepositAccount.cpp
*/

#include "TimeDepositAccount.h"

TimeDepositAccount::TimeDepositAccount(double rate, int maturity)
	: SavingsAccount(rate)
{
    periodsToMaturity = maturity;
}

void TimeDepositAccount::addInterest()
{
    periodsToMaturity--;
    SavingsAccount::addInterest();
}

void TimeDepositAccount::withdraw(double amount)
{
    if(periodsToMaturity > 0)
        SavingsAccount::withdraw(EARLY_WITHDRAWAL_PENALTY + amount);
    else
        SavingsAccount::withdraw(amount);
}


