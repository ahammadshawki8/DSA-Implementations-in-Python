from map_base_class import *
class SortedTableMap(MapBase):
    """Map implemetation using a sorted table."""

    #----------------------------nonpulic behavious-----------------------------
    def _find_index(self,k,low,high):
        """Return index of the leftmost item with key greater than or equal to k.

        Return high+1 if no such item qualifies.

        That is, j will be returned such that:
            all items of slice table[low:j] have key < k
            all items of slice table[j:high+1] have key >= k
        """
        if high < low:
            return high + 1                 # no item qualifies
        else:
            mid = (low + high)//2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k,low,mid-1)    # may return mid
            else:
                return k > self._table[mid]._key        # answer is right of mid

    #---------------------------public behaviours----------------------------
    def __init__(self):
        """Create an empty map"""
        self._table = []

    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)

    def __getitem__(self,k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = self._find_index(k,0,len(self._table)-1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError("Key Error: " + repr(k))
        return self._table[j]._value

    def __setitem__(self,k,v):
        """Assign value v to key k, overwriting existing value if present."""
        j = self._find_index(k,0,len(self._table)-1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v                           # reassign value
        else:
            self._table.insert(j, self._Item(k,v))              # adds new item

    def __delitem__(self,k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self._find_index(k,0,len(self._table)-1)
        if j == len(self._table) or self._table[j]._key !=  k:
            raise KeyError("Key Error: " + repr(k))
        self._table.pop(j)                                      # delete item

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum."""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate keys of the map ordered from maximum to minimum."""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if len(self._table) > 0:
            ans = self._table[0]
            return (ans._key, ans._value)
        else:
            return None

    def find_max(self):
        """Return (key,value) pair with maximum key (or None if empty)."""
        if len(self._table) > 0:
            ans = self._table[-1]
            return (ans._key, ans._value)
        else:
            return None

    def find_ge(self,k):
        """Return (key,value) pair with least key greater than or equal to k."""
        j = self._find_index(k,0,len(self._table) -1)           # j's key >= k
        if j < len(self._table):
            ans = self._table[j]
            return (ans._key, ans._value)
        else:
            return None

    def find_lt(self,k):
        """Return (key,value) pair with greatest key strictly less than k."""
        j = self._find_index(k,0,len(self._table) -1)           # j's key >= k
        if j > 0:
            ans = self._table[j-1]
            return (ans._key, ans._value)
        else:
            return None

    def find_gt(self,k):
        """Return (key,value) pair with least key strictly greater than k."""
        j = self._find_index(k,0,len(self._table) -1)           # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            j += 1                                              # advanced past match
        if j < len(self._table):
            ans = self._table[j]
            return (ans._key, ans._value)
        else:
            return None

    def find_range(self,start=None,stop=None):
        """Iterate all (key,value) pairs such that start <= key < stop.

        if start is None, iteration begins with minimum key of map.
        if stop is None, iteration continues through the maximum key of the map.
        """
        if start is None:
            j = 0
        else:
            j = self._find_index(start,0,len(self._table)-1)    # find first result
        while j < len(self._table) and (stop is None or self.table[j]._key < stop):
            ans = self._table[j]
            yield (ans._key, ans._value)
            j += 1
