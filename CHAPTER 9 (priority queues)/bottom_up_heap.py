from heap_priority_queue import *

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
