

//******************************************************************
// SPECIFICATION FILE (SortedList.h)
// This file gives the specification of a list abstract data type.
// The list components are assumed to be in ascending order by value.
// The implementation uses a linked structure.
//******************************************************************

#pragma once

#include "License.h"

typedef License ItemType;         // Type of each component
struct NodeType;              // Forward declaration

class SortedList
{
public:
  // Constructor
  // Post: Empty list has been created
  SortedList();


  // Destructor
  // Post: All nodes are returned to the heap
  ~SortedList();


  // Copy constructor
  // Post:  A deep copy of otherList is created and dataPtr is the
  //        external pointer to this copy
  SortedList(const SortedList& otherList);


  // Action respnsibilities


  // Pre:  List is not full and item is not in the list
  // Post: item is in the list and length has been incremented
  void Insert(ItemType item);


  // Post: item is not in the list
  void Delete(ItemType item);


  // The current position is reset to access the first item in the list
  void ResetList();


  // Assumptions:  No transformers are called during the iteration.
  // There is an item to be returned; that is, HasNext is true when
  // this method is invoked
  // Pre:  ResetList has been called before beginning the iteration
  // Post: Returns item at the current position.
  ItemType GetNextItem();


  // Knowledge responsibility


  // Post: Returns the length of the list
  int GetLength() const;


  // Post: Returns true if list is empty; false otherwise
  bool IsEmpty() const;


  // Post: Returns true if list if full; false otherwise
  bool IsFull() const;


  // Post: Returns true if item is in the list and false otherwise
  bool IsThere  (ItemType item ) const;


  // Returns true if there is another item to be returned; false
  // otherwise
  bool HasNext() const;


  private:
    NodeType* dataPtr;     // External pointer to the first node in the list
    int length;
    NodeType* currentPos;   // Pointer to the current position in a traversal
    NodeType* lastPtr;
};
