from heap_priority_queue import *

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    #-------------------------nested Locator class--------------------------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = "_index"        # add index as additional feild

        def __init__(self,k,v,j):
            super().__init__(k,v)
            self._index = j


    #--------------------------non public behaviours------------------------------
    # overide swap to record new indices
    def _swap(self,i,j):
        super._swap(i,j)                # perform the swap
        self._data[i]._index = i        # reset locator index(post swap)
        self._data[j]._index = j        # reset locator index(post swap)

    def _bubble(self,j):
        if j > 0  and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self,key,value):
        """Add a key-value pair"""
        token = self.Locator(key,value,len(self._data))     # initialize locator index
        self._data.append(token)
        self._upheap(len(self._data)-1)
        return token

    def update(self,loc,newkey,newval):
        """Update the key and the value for entry identified by the locator loc."""
        j = loc._index
        if not (0 <= j <= len(self) and self._data[j] in loc):
            raise ValueError("Invalid locator")
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """Remove and return the(k,v) pair identified by locator loc."""
        j = loc._index
        if not (0 <= j <= len(self) and self._data[j] in loc):
            raise ValueError("Invalid locator")
        if j == len(self) - 1:              # item at last position
            self._data.pop()                # just remove it
        else:
            self._swap(j,len(self)-1)       # swap item to the last position
            self._data.pop()                # remove it from list
            self._bubble(j)                 # fix the displaced by the swap
        return (loc._key,loc._value)
            
                
