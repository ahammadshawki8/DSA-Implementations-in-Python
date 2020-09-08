# Extra Utilities
class Tree:
    """Abstract base class for representing a tree structure."""

    #---------------------------nested Position class----------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self,other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("Must be implemented by subclass")

        def __ne__(self,other):
            """Return True if other does not represents the same location."""
            return not(self == other)           # opposite of __eq__

    #-----------abstract methods that contrete subclass bust support-----------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self,p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self,p):
        """Return the number of children the Position p has."""
        raise NotImplementedError("Must be implemented by subclass")

    def children(self,p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("Must be implemented by subclass")

    #--------------concrete methods implemented in this class------------------
    def is_root(self,p):
        """Return True if Position p representing the root of  the tree."""
        return (self.root() == p)

    def is_leaf(self,p):
        "Return True if Position p does not have any children"""
        return (self.num_children(p) == 0)

    def is_empty(self):
        """Return True id the tree is empty."""
        return len(self) == 0

    #-----------------------------new methods----------------------------------
    def depth(self,p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):             # works, but O(n**2) worst-case
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() is self.is_leaf(p))

    def _height2(self,p):           # time is linear in size of sub-tree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return max(self._height2(c) for c in self.children(p))

    def height(self,p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)         # start _height2 recursion


# creating linked queue class
class LinkedQueue:
    """FIFO queue implementation using a sigly linked list for storage."""

    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0                  # number of sequence elements

    def __len__(self):
        """Return the number of elements in the queue."""
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
        return self._head._element      # front alligned with the head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():             # special case as queue is empty
            self._tail=None             # removed head had been the tail
        return answer

    def enqueue(self,e):
        """Add an element to the back of the queue."""
        newest = self._Node(e,None)     # node will be new tail node
        if self.is_empty():             # special case: previously empty
            self._head = newest
        else:
            self._tail._next = newest
        self.tail = newest              # update reference to tail node
        self._size += 1

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






# Main Code

class TreeTraversals(Tree):
    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not sself.is_empty():
            fringe = LinkedQueue()          # known positions not yet yeilded
            fringe.enqueue(self.root())     # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue()        # remove the front of the queue
                yield p                     # report this position
                for c in self.children(p):
                    fringe.enqueue(c)       # add children to the back of the queue


