package Utilities;

public class Node<Type>
{
	private Type data;
	private Node<Type> next;
	private Node<Type> prev;

	// constructor
	public Node()
	{
		this.data = null;
		this.next = null;
		this.prev = null;
	}

	// accessor and mutator for the data component
	public Type getData()
	{
		return this.data;
	}

	public void setData(Type data)
	{
		this.data = data;
	}

	// accessor and mutator for next link component
	public Node<Type> getNext()
	{
		return this.next;
	}

	public void setNext(Node<Type> link)
	{
		this.next = link;
	}

	// accessor and mutator for prev link component
	public Node<Type> getPrev()
	{
		return this.prev;
	}

	public void setPrev(Node<Type> link)
	{
		this.prev = link;
	}
}
