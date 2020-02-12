// Breno Yamada Riquieri - CSC240-001 Assignment 6

/* AccountTest.cpp

   This program tests the BankAccount class and
   their subclasses.
*/

#include <iostream>
#include <iomanip>
using namespace std;

#include "CheckingAccount.h"
#include "SavingsAccount.h"
#include "TimeDepositAccount.h"
#include "AccountOverdrawnException.h"
#include "InvalidAmountException.h"

int main()
{
  cout << fixed << showpoint << setprecision(2) << endl;

  CheckingAccount harrysChecking(100);
  SavingsAccount  momsSavings(0.5);

// begin try...
  try
  {
	  momsSavings.deposit(10000);

	  // Mom:  10000
	  // Harry:  100

	  momsSavings.transfer(harrysChecking, 2000);

	  harrysChecking.withdraw(1500);
	  harrysChecking.withdraw(80);

	  // Mom:   8000
	  // Harry:  520

	  momsSavings.transfer(harrysChecking, 1000);
	  harrysChecking.withdraw(400);

	  // Mom:   7000
	  // Harry: 1120

	   // simulate end of month
	  momsSavings.addInterest();
	  harrysChecking.deductFees();

	  // 7035
	  cout << "   Mom's savings balance =  "
		  << momsSavings.getBalance() << endl;

	  // 1116
	  cout << "Harry's checking balance =  "
		  << harrysChecking.getBalance() << endl
		  << endl;

	  //harrysChecking.withdraw(5000);       // AccountOverdrawnException
	  //harrysChecking.deposit(-5000);       // InvalidAmountException

		 // -3884
	  cout << "Harry's checking balance =  "
		  << harrysChecking.getBalance() << endl
		  << endl;

	  // ...end try and catch exceptions
  }
  catch (AccountOverdrawnException(ex))
  {
	  cerr << "AccountOverdrawnException: " << ex.getInvalid() << endl << endl;
  }
  catch (InvalidAmountException(in))
  {
	  cerr << "InvalidAmountException: " << in.getInvalid() << endl << endl;
  }



  TimeDepositAccount dadsAccount(5.25, 10);
  dadsAccount.deposit(10000);

  for( int i = 1; i <= 9; i++ )
     dadsAccount.addInterest();


    // 15848.89 after 9 years
  cout << "   Dad's account balance = "
       << dadsAccount.getBalance() << endl << endl;


// begin try...
  try
  {
	  dadsAccount.withdraw(100);     // bal: 15728.89 ($20 penalty)
	  dadsAccount.addInterest();     // bal: 16554.66 (interest: 825.77)
	  dadsAccount.withdraw(100);     // bal: 16454.66 (no penalty)

	 //dadsAccount.transfer(momsSavings, 20000);    // AccountOverdrawnException
  }
// ... end try and catch excpetions.
  catch (AccountOverdrawnException(ex))
  {
	  cerr << "AccountOverdrawnException: " << ex.getInvalid() << endl << endl;
  }


  cout << endl;
  cout << "   Dad's account balance = "
       << dadsAccount.getBalance() << endl;

  cout << "   Mom's savings balance =  "
       << momsSavings.getBalance() << endl;

  cout << "\nEnd Program - ";

  return 0;
}

/*

------------------------------------ No Illegal Transactions:


   Mom's savings balance =  7035.00
Harry's checking balance =  1116.00

Harry's checking balance =  1116.00

   Dad's account balance = 15848.89

   Dad's account balance = 16454.66
   Mom's savings balance =  7035.00

End Program - Press any key to continue . . .


------------------------------------ AccountOverdrawn, Harry


   Mom's savings balance =  7035.00
Harry's checking balance =  1116.00


AccountOverdrawnException: 3884

   Dad's account balance = 15848.89

   Dad's account balance = 16454.66
   Mom's savings balance =  7035.00

End Program - Press any key to continue . . .


------------------------------------ InvalidAmount, Harry


   Mom's savings balance =  7035.00
Harry's checking balance =  1116.00


InvalidAmountException: -5000

   Dad's account balance = 15848.89

   Dad's account balance = 16454.66
   Mom's savings balance =  7035.00

End Program - Press any key to continue . . .


------------------------------------ AmountOverdrawn, Dad


   Mom's savings balance =  7035.00
Harry's checking balance =  1116.00

Harry's checking balance =  1116.00

   Dad's account balance = 15848.89

AccountOverdrawnException: 3545.34


   Dad's account balance = 16454.66
   Mom's savings balance =  7035.00

End Program - Press any key to continue . . .

*/
