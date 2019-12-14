/************************************************
 * Name:	Breno Yamada Riquieri		*
 * Class:	CSC330 Programming Languages	*
 * Assignment:	Investigations			*
 * Instructor:	Dr. Gourd			*
 * Due Date:	December 18, 2019 		*
 ************************************************/

#include <iostream>
#include <iomanip>
using namespace std;

// Function to test pass by reference:
void testByRef(int arr[])
{
	arr[0] = 10;

	cout << "changed value in arr[0] inside testByRef: " <<  arr[0] << endl;
}

// Struct to work around passing arrays by value:
struct valueWrap
{
	int arrWrap[5] = {1,2,3,4,5};
};

// Function to test pass by value:
void testByVal(struct valueWrap arrByVal)
{

	int *ptr = arrByVal.arrWrap; // Pointer will make pass by value work

	ptr[1] = 20;

	cout << "changed value in arrByVal[1] inside testByVal: " << ptr[1] << endl;
}

int main()
{
	// Investigation 1:
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

	goto label;	// executes 'label.' 

	label:
		cout << "Executing 'label' " << times << " time(s)\n";
		times++;
		if (times < 6)
			goto label; // loops back to label until times >= 6
		cout << "\n\n";
	
	// Investigation 2:
	cout << setw(64) << '*'
		<< "\n\t\tInvestigation 2: Blocks\n"
		<< setw(64) << '*' << endl << endl;

	cout << "Blocks have their own variable scope.\n"
		<< "If variables are declared with the same name, they\n"
		<< "will have different values in their respective blocks.\n"
		<< "Otherwise, the variables will keep their values\n"
		<< "between blocks' scopes\n\n"
		<< "Examples:\n\n";

	// Outer Block:
	{
		cout << "Entering outer block...\n\n";

		// "test" will test variables declared 
		// with the same name but in different scopes:
		int test = 25;
		int outerVar = 0;

		cout << "outer variable: " << outerVar << endl
			<< "locally declared test variable: " << test << "\n\n";

		// Inner Block:
		{
			cout << "Entering inner block...\n\n";

			int innerVar = 1;
			int test = 30;
			
			cout << "inner variable: " << innerVar << "\n"
				<< "outer variable: " << outerVar << " (still the same value)\n"
			       	<< "locally declared test variable: "
				<< test << " (different than outer block)\n\n";
			
			// Loop Block:
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

	// Investigation 3:
	cout << setw(64) << '*'
		<< "\n\t\tInvestigation 3: |A|r|r|a|y|s|\n"
		<< setw(64) << '*' << endl << endl;

	int arr[5] = {1,2,3,4,5};

	cout << "value of arr[0] before testByRef: " << arr[0] << endl;

	testByRef(arr);

	cout << "value of arr[0] after testByRef was called: " << arr[0] << endl << endl;

	cout << "Therefore, this array in C++ was passed by reference.\n"
		<< "\"arr\" was passed as a parameter for testByRef(),\n"
		<< "and once testByRef() modified a value in \"arr,\" it\n"
		<< "kept the modified value when it returned from testByRef()\n"
		<< "and was back at main's scope." << endl << endl;

	cout << "Passing by reference is the default in C++ because when you pass\n"
		<< "an array as a parameter, you pass it's address. Pass by value is\n"
		<< "a different story. You can pass literal numerical values as parameters\n"
		<< "and it would be passed by value, but array parameters stand for its address."
		<< endl << endl;

	cout << "There is, however, a non-traditional way of passing arrays by value.\n"
	       << "By defining a struct for the array, you can use a pointer to assign\n"
	       << "values for the array wrapped in that specific scope. Therefore, this\n"
	       << "is a way of passing by value, as shown by the following example (idea\n"
	       << "from geeksforgeeks.org):"
	       << endl << endl;

	struct valueWrap arrByVal; // struct will wrap the array to pass it by value with a pointer

	cout << "value of arrByVal[1] before testByVal is called: " << arrByVal.arrWrap[1] << endl;

	testByVal(arrByVal);

	cout << "value of arrByVal[1] after testByVal was called: " << arrByVal.arrWrap[1] << endl << endl;

	cout << "It's interesting to point out the addresses of what we just worked with here.\n"
	       << "We worked with *ptr = arrByVal.arrWrap inside the function.\n"
	       << "We also worked with arrByVal.arrWrap by itself outside the function.\n"
	       << "ptr and arrByVal.arrWrap have different addresses."
       	       << endl << endl;

	return 0;
}
