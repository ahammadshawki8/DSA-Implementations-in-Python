from empty_exception import *
from node_class import *

# creating linked stack class
class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty stack."""
        self._head = None                   # referebce to the head node
        self._size = 0                      # number of stack elements

    def __len__(self):
        """Return number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return (self._size == 0)

    def push(self,e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e,self._head)
        self.size +=1
        
    def top(self,e):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack (i.e,LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty.")
        answer = self._head._element
        self._head=self._head._next         # bypass the former top node
        self._size -= 1
        return answer
    
    
