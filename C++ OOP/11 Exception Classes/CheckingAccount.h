/* CheckingAccount.h

    A checking account that charges transaction fees.
*/

#pragma once;

#include "BankAccount.h"

const int FREE_TRANSACTIONS = 3;
const double TRANSACTION_FEE = 2.0;

class CheckingAccount : public BankAccount
{
private:
	int transactionCount;      // successful transactions


public:
        /*
            Constructs a checking account with a given balance
            param initialBalance the initial balance
        */
	CheckingAccount(int initialBalance);

    virtual void deposit(double amount);

    void withdraw(double amount);


        /**
            Attempts to deduct the accumulated fees, if any,
            and resets the transaction count if successful.
        */
    void deductFees();


};
