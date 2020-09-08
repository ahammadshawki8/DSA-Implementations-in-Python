
# Creating Queue class with circular linked list
class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        self._tail = None                   # will represent tail of the queue
        self._size = 0                      # number of queue elements

    def __len__(self):
        """Return the number if the elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return (self._size == 0)

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e.,FIFO)

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        oldhead = self._tail._next
        if self._size == 1:                 # removing only element
            self._tail = None               # queue becomes empty
        else:
            self._tail._next=oldhead._next  # bypass the old head
        self.size -= 1
        return oldhead

    def enqueue(self,e):
        """Add element to the back of the queue"""
        newest = self._Node(e,None)         # node will be the new tail node
        if self.is_empty():
            newest._next = newest           # initialize circularity
        else:
            newest._next = self._tail._next # new node pionts the head
            self._tail._next = newest       # old tail points the new node
        self._tail = newest                 # new node becomes the tail
        self._size +=1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next  # old head becomes new tail


# Extra Utilities
# creating empty class
class Empty(Exception):
    pass

# simple implementation of Node class.
class _Node:
    """Lightweight, non-public class for storing a singly linked list"""
    __slots__ = "_element", "_next"         # streamline memory usage.

    def __init__(self,element,next):
        self._element = element             # reference to user's element
        self._next = next                   # reference to next node