/* BankAccount.cpp

    A bank account has a balance that can be changed by
    deposits and withdrawals.
*/

#include "BankAccount.h"
#include "AccountOverdrawnException.h"
#include "InvalidAmountException.h"

    /*
    Constructing an account with 0 balance.
    */
BankAccount::BankAccount()
{
	balance = 0.0;
}

    /*
    Constructs a bank account with a given balance
    param initialBalance the initial balance
    */
BankAccount::BankAccount(double initialBalance)
{

    balance = initialBalance;
}

    /*
    Deposits money into the bank account.
    param amount the amount to deposit
    */
void BankAccount::deposit(double amount)
{
	if (amount < 0)
		throw InvalidAmountException(amount);

    balance = balance + amount;
}

    /*
    Withdraws money from the bank account.
    param amount the amount to withdraw
    */
void BankAccount::withdraw(double amount)
{
	// Test for and throw an exception in case balance would be negative
	// Throwing the 1-arg constructor with the difference between the 
	// argument amount and balance, in order to include in the message.
	if (amount > balance)
		throw AccountOverdrawnException(amount - balance);

    balance = balance - amount;
}

    /*
    Gets the current balance of the bank account.
    return the current balance
    */
double BankAccount::getBalance()
{
    return balance;
}

    /*
    Transfers money from the bank account to another account
    param other the other account
    param amount the amount to transfer
    */
void BankAccount::transfer(BankAccount& other, double amount)
{
	// Test for and throw an exception in case balance would be negative
	// Throwing the 1-arg constructor with the difference between the 
	// argument amount and balance, in order to include in the message.
	if (amount > balance)
		throw AccountOverdrawnException(amount - balance);

    withdraw(amount);
    other.deposit(amount);			// polymorphic reference, late binding
}

