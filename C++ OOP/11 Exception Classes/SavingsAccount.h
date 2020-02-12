/* SavingsAccount.h

    An account that earns interest at a fixed rate.
*/

#pragma once;

#include "BankAccount.h"

class SavingsAccount : public BankAccount
{
private:
	double interestRate;

        /*
              Constructs a bank account with a given interest rate
              param rate the interest rate
        */
public:
	SavingsAccount(double rate);

        /*
              Adds the earned interest to the account balance.
        */
    void addInterest();

};
