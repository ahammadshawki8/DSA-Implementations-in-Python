# Extra Utilities

# creating empty class
class Empty(Exception):
    pass

class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer              # trailer is after header
        self._trailer._prev = self._header              # header is before trailer
        self._size = 0                                  # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self,e,predecessor,successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e,predecessor,successor)    # linked to neighbours
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self,node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -=1
        element = node._element                         # record deleted element
        node._prev = node._next = node._element = None  # deprecate node for garbage collection
        return element                                  # return deleted element


# simple implementation of Node class.
class _Node:
    """Lightweight, non-public class for storing a doubly linked list"""
    __slots__ = "_element", "_prev", "_next"    # streamline memory usage.

    def __init__(self,element,prev,next):
        self._element = element                 # reference to user's element
        self._prev = prev                       # reference to previous node
        self._next = next                       # reference to next node




# Main Code
class LinkedDeque(_DoublyLinkedBase):           # note the use of inheritance
    """Double-ended queue implementation based ona doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element      # real item just before trailer

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._perv._element     # real item just before trailer

    def insert_first(self,e):
        """Add an element to the front of the deque."""
        self._insert_between(e,self._header,self._header._next)     # after header

    def insert_last(self,e):
        """Add an element to the back of the deque."""
        self._insert_between(e,self._trailer._prev,self._trailer)   # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)        # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)        # use inherited method
