/* SavingsAccount.cpp

    An account that earns interest at a fixed rate.
*/

#include "SavingsAccount.h"

    /*
          Constructs a bank account with a given interest rate
          param rate the interest rate
    */
SavingsAccount::SavingsAccount(double rate)
{
    interestRate = rate;
}

    /*
          Adds the earned interest to the account balance.
    */
void SavingsAccount::addInterest()
{
    double interest = getBalance() * interestRate / 100;

    deposit(interest);
}


