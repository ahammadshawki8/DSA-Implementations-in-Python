from priority_queue_base_class import *
from empty_exception import *
from positional_list import *

class UnsortedPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with a unsorted list"""

    def _find_min(self):            # non-public utility
        """Return Position of item with minimum key."""
        if self.is_empty():         # is_em[ty inherited from base class
            raise Empty("Priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self,key,value):
        """Add a key value pair"""
        self._data.add_last(self._Item(key,value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
