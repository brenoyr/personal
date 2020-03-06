package Utilities;

public class Stack<Type> extends List
{
	public Stack()
	{
		super();
	}

	public void push(Type data)
	{
		super.InsertAfter(data);
	}

	public Type pop()
	{
		Type returnVal = peek();
		super.Remove();
		return returnVal;
	}

	public Type peek()
	{
		return (Type)super.GetValue();
	}
}
