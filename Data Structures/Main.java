/**
 * Name: Breno Yamada Riquieri
 * Date: 12/18/18
 * Description: Circular Linked List & Dynamic Array
 */

/** Our List Abstract Data Type */
interface IList_ADT {
  /** Adds the given value to the end of the list */
  void append(char value);
  
  /** Adds the given value to the beginning of the list */
  void prepend(char value);
  
  /** Deletes the given container from our list (a container holds a value).
    * Correct usage of this function will call search first to find the given
    * value, then (if null is not returned) will use the returned object as 
    * an argument to the delete method. This separates the responsibility of
    * searching from the responsibility of deleting.
    * If container is somehow invalid or if null is passed in, no action is taken.
    */
  void delete(Object container);
    
  /** Returns the number of values currently in our list */
  int size();

  /** Searches for the FIRST occurence of a given value in our list.
    * If found, it returns the container that contains the value.
    * If not found, it returns null */
  Object search(char value);
  
  /** Performs full traversal over all values in our list concatenating each one
    * as they are visited. The full concatenated string is then returned. 
    * Traversal should visit the values in the order that they are stored in the
    * list from first to last.
    * It is important that you do not put any space or other characters in between
    * each value. Simply concatenate them, as is, with nothing in between nor a newline
    * at the end */
  String toString();
}


/** Array implementation of our List */
class Array implements IList_ADT {
  // Initializing array to a size of 10 elements.
  // This will require resizing solution to be implemented.
  private int capacity = 10;
  private char[] array = new char[capacity];
  private int end = 0;
  
  /** Appends by setting new value to the first empty element. 	*/
  public void append(char value)
  {
	  // If array is full: create a new one twice its old size,
	  // transcribe values from old array to the new array.
	  if (end >= capacity)
	  {
		  capacity *= 2;
		  char[] newArray = new char[capacity];
		  
		  for (int i = 0; i < end; i++)
			  newArray[i] = array[i];
		  array = newArray;
	  }
	  
	  array[end] = value;
	  end += 1;
  }
  
  /** Prepends by shifting all current values up the array,
	  and setting new value as the first value in the array.	*/
  public void prepend(char value)
  {
	  // If array is full: create a new one twice its old size,
	  // transcribe values from old array to the new array.
	  if (end >= capacity)
	  {
		  capacity *= 2;
		  char[] newArray = new char[capacity];
		  
		  for (int i = 0; i < end; i++)
			  newArray[i] = array[i];
		  array = newArray;
	  }
	  
	  for (int i = end; i > 0; i--)
	  {
		  array[i] = array[i - 1]; 
	  }
	  array[0] = value;
	  end += 1;
  }
  
  /** Deletes the target by covering it up and shifting 
	  other values down the array.								*/
  public void delete(Object container)
  {
	  int index = ((int) container);
	  
	  if (index >= 0)
	  {
		  for (int i = index; i < (size() - 1); i++)
			  array[i] = array[i + 1];
		  end -= 1;
	  }
  }
  
  /** Returns end, the variable incremented everytime
	  a new value was appendend or prepended. 					*/  
  public int size()
  {
	  return end;
  }
  
  /** Linear search through the array.
	  Returns the first match, or null if not found.			*/
  public Object search(char value)
  {
	  for (int i = 0; i < end; i++)
	  {
		  if (value == array[i])
			  return i;
	  }
	  
	  return null;
  }
  
  /** Creates an empty string and append values held by
	  every index to it.										*/
  public String toString()
  {
	  String result = "";
	  
	  for (int i = 0; i < size(); i++)
		  result += array[i];
	  
	  return result;
  }
}


/** Doubly Linked List implementation of our List */
class LinkedList implements IList_ADT {
  private Node head;
  private Node tail;
  private int count;
  
  public LinkedList()
  {
	  head = null;
	  tail = null;
	  count = 0;
  }
  
  /** Appends a new node to the end of the linked list by making
	  it the new tail, and back pointing to the previous tail.	*/
  public void append(char value)
  {
	  Node node = new Node(value);
	  
	  if (head == null)
	  {
		  head = node;
		  tail = node;
	  }
	  else
	  {
		  tail.setNext(node);
		  node.setPrev(tail);
		  
		  // Wrapping it:
		  node.setNext(head);
		  head.setPrev(node);
	  }
	  tail = node;
	  count++;
  }
  
  /** Prepends a new node to the beginning of the linked list
	  by making it the head, and pointing to previous head.		*/
  public void prepend(char value)
  {
	  Node node = new Node(value);
	  
	  if (head == null)
	  {
		  head = node;
		  tail = node;
	  }
	  else
	  {
		  node.setNext(head);
		  head.setPrev(node);
		  
		  // Wrapping it:
		  node.setPrev(tail);
		  tail.setNext(node);
	  }
	  head = node;
	  count++;
  }
  
  /** Deletes target by making previous node point to next,
	  and next point back to previous.							*/
  public void delete(Object container)
  {
	  Node target = ((Node)container);
	  target.getNext().setPrev(target.getPrev());
	  target.getPrev().setNext(target.getNext());
	  
	  if (target.getNext() == tail)
		  target.getNext().setPrev(head);
	  
	  if (target.getPrev() == head)
		  target.getPrev().setPrev(tail);
  }
  
  /** Returns count, the variable incremented everytime
	  a new node was appendend or prepended. 					*/
  public int size()
  {
	  return count;
  }
  
  /** Goes through every node checking if value is found.
	  If not found, returns null.								*/
  public Object search(char value)
  {
	  Node cur = head;
	  
	  while (cur != null)
	  {
		  if (cur.getData() == value)
			  return cur;
		  else
			  cur = cur.getNext();
	  }
	  return null;
  }
  
  /** Creates an empty string and append values of every
	  node to it.												*/
  public String toString()
  {
	  String result = "";
	  Node cur = head;
	  
	  // First one is added manually because we will know when
	  // to stop whenever it comes full circle back to head.
	  // Therefore,  the while loop will check if we reached head
	  // again, meaning we can't enter the loop if cur = head.
	  result += cur.getData();
	  cur = cur.getNext();
	  
	  while (cur != head)
	  {
		  char value = cur.getData();
		  result += value;
		  cur = cur.getNext();
	  }
	  return result;
  }}


/** A doubly linked list node for our doubly linked list */
class Node {
  /** the value held in this node */
  private char data;
  
  /** points to the next node */
  private Node next;
  
  /** points to the previous node */
  private Node prev;
  
  /** constructor */
  public Node(char data) {
    this.data = data;
    next = prev = null;
  }
  
  /** returns the pointer to the next node */
  public Node getNext() {
    return next;
  }
  
  /** returns the pointer to the previous node */
  public Node getPrev() {
    return prev;
  }
  
  /** returns the value held inside this node */
  public char getData() {
    return data;
  }
  
  /** sets the pointer to the next node */
  public void setNext(Node next) {
    this.next = next;
  }
  
  /** sets the pointer to the previous node */
  public void setPrev(Node prev) {
    this.prev = prev;
  }}


/** contains our entry point */
public class Main {
  /** entry point - DO NOT CHANGE the pre-existing code below */
  public static void main(String[] args) {
    int[] numbers = {105,116,112,115,65,58,47,47,116,105,110,121,88,117,114,108,46,99,111,109,47};
    int[] numbers2 = {97,59,111,53,33,111,106,42,50};
    int[] numbers3 = {116,104,32,111,116,32,111,71};
    
    
    /// List as an Array
    IList_ADT array = new Array();
    
    // add values
    for(int num : numbers) {
      array.append((char)num);
    }
    for(int num : numbers3) {
      array.prepend((char)num);
    }
	
    // delete some values
    Object container;
    container = array.search((char)105);
    array.delete(container);
    container = array.search((char)65);
    array.delete(container);
    container = array.search((char)88);
    array.delete(container);
   
    // print em
    System.out.print(array);
    
    
    /// List as a Linked List
    // add values
    IList_ADT linkedList = new LinkedList();
    
    for(int num : numbers2) {
      linkedList.append((char)num);
    }
    linkedList.prepend((char)55);
    linkedList.prepend((char)121);

    // delete some values
    container = linkedList.search((char)59);
    linkedList.delete(container);
    container = linkedList.search((char)33);
    linkedList.delete(container);
    container = linkedList.search((char)42);
    linkedList.delete(container);
    
    // print em
    System.out.print(linkedList);
    
    System.out.println();
    
    // ???
	System.out.println("Secret Number = 0");
  }}
