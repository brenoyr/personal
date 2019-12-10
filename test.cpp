/************************************************
 * Name:	Breno Yamada Riquieri		*
 * Class:	CSC330 Programming Languages	*
 * Assignment:	Investigations			*
 * Instructor:	Dr. Gourd			*
 * Due Date:	December 16, 2019 		*
 ************************************************/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	cout << endl << setfill('*') << setw(64) << '*'
		<< "\n\t\tInvestigation 1: Goto Statement\n"
		<< setw(64) << '*' << endl << endl;

	cout << "'goto' statements can be utilized in C++.\n"
		<< "'goto' jumps to a specified label,\nwhich has a name followed by a colon.\n\n"
		<< "for example:\n\n"
		<< "goto label;\n\nlabel:\n\t"
		<< "cout << \"now at label where control was transferred to.\"\n\n\n"
		<< "Now this is an example of a goto statement in action:\n\n";

	int times = 1;

	goto label;

	label:
		cout << "Executing 'label' " << times << " time(s)\n";
		times++;
		if (times < 6)
			goto label;
		cout << "\n\n";
	
	cout << setw(64) << '*'
		<< "\n\t\tInvestigation 2: Blocks\n"
		<< setw(64) << '*' << endl << endl;

	cout << "Blocks have their own variable scope.\n"
		<< "If variables are declared with the same name, they\n"
		<< "will have different values in their respective blocks.\n"
		<< "Otherwise, the variables will keep their values\n"
		<< "between blocks' scopes\n\n"
		<< "Examples:\n\n";

	{
		cout << "Entering outer block...\n\n";

		int outerVar = 0;
		int test = 25;

		cout << "outer variable: " << outerVar << endl
			<< "locally declared test variable: " << test << "\n\n";

		{
			cout << "Entering inner block...\n\n";

			int innerVar = 1;
			int test = 30;
			
			cout << "inner variable: " << innerVar << "\n"
				<< "outer variable: " << outerVar << " (still the same value)\n"
			       	<< "locally declared test variable: "
				<< test << " (different than outer block)\n\n";
			
			cout << "Entering loop block:...\n\n";
			for (int c = 1; c < 6; c++)
			{
				cout << "current value of 'c' in loop: " << c
					<< "\ninner variable still: " << innerVar
					<< "\nouter variable still: " << outerVar
					<< endl << endl;
			}
		}
	}

	cout << setw(64) << '*'
		<< "\n\t\tInvestigation 3: |A|r|r|a|y|s|\n"
		<< setw(64) << '*' << endl << endl;


	return 0;
}
