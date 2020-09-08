# Extra Utilities
# creating empty class
class Empty(Exception):
    pass

class PriorityQueueBase:
    """Abstract base class for a priority queue."""
    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__="_key","_value"

        def __init__(self,k,v):
            self._key = k
            self._value = v

        def __lt__(self,other):
            return self._key < other._key           # compare items based on their keys

    def is_empty(self):                 # concrete method assuming abstract len
        """Return True if the priority queue is empty"""
        return len(self) == 0

class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""
    #---------------------------non-public behaviours-----------------------------
    def _parent(self,j):
        return (j-1)//2

    def _left(self,j):
        return 2*j+1

    def _right(self,j):
        return 2*j+2

    def _has_left(self,j):
        return self._left(j) < len(self._data)      # index beyond end of the list

    def _has_right(self,j):
        return self._right(j) < len(self._data)     # index beyond end of the list

    def _swap(self,i,j):
        """Swap the elements at indices i and j of array."""
        self._data[i],self._data[j] = self._data[j],self._data[i]

    def _upheap(self,j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j,parent)
            self._upheap(parent)        # recur at position of parent

    def _downheap(self,j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left          # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self.data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self.swap(j,small_child)
                self._downheap(small_child)     # recur at the position of small child

    # ----------------------------public behaviours------------------------------

    def __init__(self):
        """Create a new priority queue."""
        self._data =[]

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self,key,value):
        """Add a key-value pair to the priority queue."""
        self._data.apapend(self.Item(key,value))
        self._upheap(len(self._data)-1)             # upheap newly added position.

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data[0]
        return (item._key,item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with the minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        self._swap(0,len(self._data)-1)     # put minimum item at the end
        item =self.data.pop()               # and remove it from the list
        self._downheap(0)                   # then fix new root
        return (item._key, item._value)





# Main Code       

class BottomUPHeap(HeapPriorityQueue):
    def __init__(self,contents=()):
        """Create a new priority queue.

        By default, queue will be empty. If contents is given, it should be as
        an iterable sequence of (k,v) tuples specifying the initial contents.
        """
        self._data = [self._Item(k,v) for k,v in contents]  # empty by default
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self)-1)   # start of parent of last leaf
        for j in range(start,-1,-1):        # going to and including the root
            self._downheap(j)
