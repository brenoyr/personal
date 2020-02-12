/* BankAccount.h

    A bank account has a balance that can be changed by
    deposits and withdrawals.
*/

#pragma once;


class BankAccount
{
private:
    double balance;

public:
        /*
        Constructing an account with 0 balance.
        */
    BankAccount();

        /*
        Constructs a bank account with a given balance
        param initialBalance the initial balance
        */
    BankAccount(double initialBalance);

        /*
        Deposits money into the bank account.
        param amount the amount to deposit

        Must be virtual for BankAccount& param in trasfer()
        */
    virtual void deposit(double amount);

        /*
        Withdraws money from the bank account.
        param amount the amount to withdraw
        */
    void withdraw(double amount);

        /*
        Gets the current balance of the bank account.
        return the current balance
        */
    double getBalance();

        /*
        Transfers money from the bank account to another account
        param other the other account
        param amount the amount to transfer
        */
    void transfer(BankAccount& other, double amount);

};
