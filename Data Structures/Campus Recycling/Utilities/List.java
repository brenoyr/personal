package Utilities;

public class List<Type>
{
    // We don't actually have to set a max size with linked lists
    // But it is a good idea.
    // Just picture an infinite loop adding to the list! :O
    public static final int MAX_SIZE = 50;

    private Node<Type> head;
    private Node<Type> tail;
    private Node<Type> curr;
    private int num_items;

    // constructor
    // remember that an empty list has a "size" of -1 and its "position" is at -1
    public List()
    {
        num_items = 0;
        head = new Node<Type>();
        tail = new Node<Type>();
        curr = new Node<Type>();
    }

    // copy constructor
    // clones the list l and sets the last element as the current
    public List(List<Type> l)
    {
        Node<Type> n = new Node<Type>();
		n.setNext(l.head.getNext());

        this.head = new Node<Type>();
        this.tail = new Node<Type>();
        this.curr = new Node<Type>();
        this.num_items = 0;

        while (n.getNext() != null)
        {
            this.InsertAfter(n.getNext().getData());
            n.setNext(n.getNext().getNext());
        }
    }

    // navigates to the beginning of the list
    public void First()
    {
        curr.setNext(head.getNext());
    }

    // navigates to the end of the list
    // the end of the list is at the last valid item in the list
    public void Last()
    {
        curr.setNext(tail.getNext());
    }

    // navigates to the specified element (0-index)
    // this should not be possible for an empty list
    // this should not be possible for invalid positions
    public void SetPos(int pos)
    {
		if(!(pos >= num_items))
		{
			First();
        	for(int j = 0; j < pos; j++)
            	Next();
		}
    }

    // navigates to the previous element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Prev()
    {
        if((curr.getNext() != head.getNext()) && (head.getNext() != null))
            curr.setNext(curr.getNext().getPrev());
    }


    // navigates to the next element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Next()
    {
        if((head.getNext() != null) && (curr.getNext() != tail.getNext()))
            curr.setNext(curr.getNext().getNext());
    }

    // returns the location of the current element (or -1)
    public int GetPos()
    {
        Node temp = new Node();
        temp.setNext(head.getNext());
        for(int j = 0; j < num_items; j++)
        {
			if(curr.getNext() == temp.getNext())
                return j;
            temp.setNext(temp.getNext().getNext());
        }
        return -1;
    }

    // returns the value of the current element (or null)
    public Type GetValue()
    {
        if(curr.getNext() != null)
            return curr.getNext().getData();
        else
            return null;
    }

    // returns the size of the list
    // size does not imply capacity
    public int GetSize()
    {
        return num_items;
    }

    // inserts an item before the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertBefore(Type data)
    {
        Node toInsert = new Node();
        toInsert.setData(data);
        if(num_items == 0)
        {
            tail.setNext(toInsert);
            head.setNext(toInsert);
            curr.setNext(toInsert);
            num_items++;
        }
		else if(curr.getNext() == head.getNext())
		{
			toInsert.setNext(curr.getNext());
			curr.getNext().setPrev(toInsert);
			head.setNext(toInsert);
			curr.setNext(toInsert);
			num_items++;
		}
        else if(!this.IsFull())
        {
            Prev();
            toInsert.setNext(curr.getNext().getNext());
			toInsert.setPrev(curr.getNext());
            curr.getNext().setNext(toInsert);
			toInsert.getNext().setPrev(toInsert);
            curr.setNext(toInsert);
            num_items++;
        }
    }

    // inserts an item after the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertAfter(Type data)
    {
        Node toInsert = new Node();
        toInsert.setData(data);
        if(num_items == 0)
        {
            head.setNext(toInsert);
            curr.setNext(toInsert);
            tail.setNext(toInsert);
            num_items++;
        }
        else if(!this.IsFull())
        {
            toInsert.setNext(curr.getNext().getNext());
			toInsert.setPrev(curr.getNext());
            curr.getNext().setNext(toInsert);
			if(curr.getNext() == tail.getNext())
				tail.setNext(toInsert);
			else
				toInsert.getNext().setPrev(toInsert);
            curr.setNext(toInsert);
            num_items++;
        }
    }

    // removes the current element
    // this should not be possible for an empty list
    public void Remove()
    {
		if(num_items == 1)
		{
			head.setNext(null);
			tail.setNext(null);
			curr.setNext(null);
			num_items--;
		}
		else if((curr.getNext() == tail.getNext()) && (curr.getNext() != null))
		{
			Prev();
			curr.getNext().setNext(null);
			tail.setNext(curr.getNext());
			num_items--;
		}
		else if((curr.getNext() == head.getNext()) && (curr.getNext() != null))
		{
			head.setNext(curr.getNext().getNext());
			curr.setNext(curr.getNext().getNext());
			curr.getNext().setPrev(null);
			num_items--;
		}
        else if(num_items != 0)
        {
            Prev();
            curr.getNext().setNext(curr.getNext().getNext().getNext());
			curr.getNext().getNext().setPrev(curr.getNext());
			Next();
            num_items--;
        }
    }

    // replaces the value of the current element with the specified value
    // this should not be possible for an empty list
    public void Replace(Type data)
    {
		if(this.GetSize() != 0)
			curr.getNext().setData(data);
    }

    // returns if the list is empty
    public boolean IsEmpty()
    {
		if(num_items == 0)
			return true;
		else
			return false;
    }

    // returns if the list is full
    public boolean IsFull()
    {
		if(num_items == MAX_SIZE)
			return true;
		else
			return false;
    }

    // returns if two lists are equal (by value)
    public boolean Equals(List<Type> l)
    {
		Node thisTemp = new Node();
		Node lTemp = new Node();

		thisTemp.setNext(this.head.getNext());
		lTemp.setNext(l.head.getNext());

		if(this.GetSize() != l.GetSize())
			return false;

		for(int j = 0; (j < this.GetSize()) && (j < l.GetSize()); j++)
		{
			if(thisTemp.getNext().getData() != lTemp.getNext().getData())
				return false;
			thisTemp.setNext(thisTemp.getNext().getNext());
			lTemp.setNext(lTemp.getNext().getNext());
		}
		return true;
    }

    // returns the concatenation of two lists
    // l should not be modified
    // l should be concatenated to the end of *this
    // the returned list should not exceed MAX_SIZE elements
    // the last element of the new list is the current
    public List<Type> Add(List<Type> l)
    {
		List toReturn = new List(this);

		l.First();
		for(int j = 0; j < l.GetSize(); j++)
		{
			toReturn.InsertAfter(l.curr.getNext().getData());
			l.Next();
		}

		return toReturn;
    }

    // returns a string representation of the entire list (e.g., 1 2 3 4 5)
    // the string "NULL" should be returned for an empty list
    public String toString()
    {
		Node temp = new Node();

		if(GetSize() == 0)
			return null;

		String fullList = "";

		temp.setNext(head.getNext());
		for(int j = 0; j < GetSize(); j++)
		{
			fullList = fullList + temp.getNext().getData() + " ";
		    temp.setNext(temp.getNext().getNext());
		}

		return fullList;
    }
}
