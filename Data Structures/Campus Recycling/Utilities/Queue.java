package Utilities;

public class Queue<Type> extends List
{
	public Queue()
	{
		super();
	}

	public void enqueue(Type data)
	{
		super.Last();
		super.InsertAfter(data);
	}

	public Type dequeue()
	{
		Type returnVal = peek();
		super.First();
		super.Remove();
		return returnVal;
	}

	public Type peek()
	{
		super.First();
		return (Type)super.GetValue();
	}
}
