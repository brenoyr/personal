/* CheckingAccount.cpp

    A checking account that charges transaction fees.
*/

#include "CheckingAccount.h"

        /*
            Constructs a checking account with a given balance
            param initialBalance the initial balance
        */
CheckingAccount::CheckingAccount(int initialBalance)
	: BankAccount(initialBalance)
{
        // initialize transaction count
    transactionCount = 0;
}

void CheckingAccount::deposit(double amount)
{
        // attempt to add amount to balance
    BankAccount::deposit(amount);

        // now update transaction count
    transactionCount++;
}

void CheckingAccount::withdraw(double amount)
{
        // attempt to subtract amount from balance
    BankAccount::withdraw(amount);

        // now update transaction count
    transactionCount++;
}

    /*
        Attempts to deduct the accumulated fees, if any,
        and resets the transaction count if successful.
    */
void CheckingAccount::deductFees()
{
    if (transactionCount > FREE_TRANSACTIONS)
    {
       double fees = TRANSACTION_FEE *
                    (transactionCount - FREE_TRANSACTIONS);

       BankAccount::withdraw(fees);
    }

    transactionCount = 0;
}

