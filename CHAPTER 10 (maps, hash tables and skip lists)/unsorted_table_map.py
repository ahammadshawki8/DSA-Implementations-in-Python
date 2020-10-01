from map_base_class import *

class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""
    
    def __init__(self):
        """Create an empty map."""
        self._table = []            # list of _Items

    def __getitem__(self,k):
        """Return value associated with key.

        Raise KeyError if not found.
        """
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error: "+ repr(k))

    def __setitem__(self,k,v):
        """Assign value to key k, overwiting existing value if present."""
        for item in self._table:
            if k == item._key:          # Found a match
                item._value = v         # reassign value
                return                  # and quit
        # did not find a match for key
        self._table._append(self._Item(k,v))

    def __delitem__(self,k):
        """Remove item associated with key k.

        Raise KeyError if not found.
        """
        for j in range(len(self._table)):
            if k == self._table[j]._key:        # Found a match
                self._table.pop(j)              # remove item
                return                          # and quit
        raise KeyError("Key Error: "+ repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of map's key."""
        for item in self._table:
            yield item._key                     # yield the key
