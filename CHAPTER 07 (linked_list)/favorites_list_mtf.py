# Extra Utilities

class FavouritesList:
    """List of elements orderred from most frequently accessed to least."""

    #---------------------------nested _Item class----------------------------
    class _Item:
        __slots__ = "_value", "_count"          # streamline memory usage
        def __init__(self,e):
            self._value = e                     # the user's element
            self.count = 0                      # access count initially zero

    #---------------------------nonpublic utilities---------------------------
    def _find_position(self,e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while ((walk is not None) and (walk.element()._value != e)):
            walk = self._data.after(walk)
        return walk

    def _move_up(self,p):
        if p != self._data.first():             # consider moving
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:     # must shift forward
                while ((walk != self._data.first()) and 
                       (cnt > self._data.before(walk).element()._count)):
                            walk = self._data.before(walk)
                self._data.add_before(walk,self._data.delete(p))  # delete/reinsert

    #-----------------------------public methods------------------------------
    def  __init__(self):
        """Create an empty list of favourites."""
        self._data = PositionalList()           # will be list of _Item instances.

    def __len__(self):
        """Return nub=mber of entries on favourites list."""
        return len(self._data)

    def is_empty(self):
        """Return True if list is empty."""
        return (len(self._data) == 0)

    def access(self,e):
        """Accesss element e, thereby increasing its access count."""
        p = self._find_position(e)              # try to locate existing element
        if p is None:
            p. self._data.add_last(self._Item(e))   # if new, place at end
        p.element()._count += 1                     # always increment count
        self._move_up(p)                            # consider moving forward

    def remove(self,e):
        """Remove element e from list of favourites."""
        p = self._find_position(e)              # try to locate existing element
        if p is not None:
            self._data.delete(p)                # delete it, if found

    def top(self,k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()               # element of list is _Item
            yield item._value                   # report user's element    
            walk = self._data.after(walk)
            
    
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




class PositinalList(_DoublyLinkedBase):
    """A sequent container of elements allowing positional access."""
    #-----------------------nested position class----------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self,container,node):
            """Constructor should not be invoked by the user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this position."""
            return self._node._element

        def __eq__(self,other):
            """Return True if other is a Position representing the same location."""
            return ((type(other) is type(self)) and (other._node is self._node))

        def __ne__(self,other):
            """Return True if other does not represent the same location."""
            return not(self == other)           # opposite of __eq__

    #---------------------------utility methods-------------------------------
    def _validate(self,p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("P is no loger valid")
        return p._node
    
    def _make_position(self,node):
        """Return Position instance for given node (or None if sentinel)."""
        if (node is self._header) or (node is self._trailer):
            return None                     # boundary violation
        else:
            return self.Position(self,node) # legitimate position

    #-------------------------------accessors----------------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self,p):
        """Return the Position just before Position p (or None if p is first)"""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def sfter(self,p):
        """Return the Position just after Position p (or None if p is last)"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #-------------------------------mutators-----------------------------------
    # override inherited version to return Position, rather than Node.
    def _insert_between(self,e,predecessor,successor):
        """Add element between exiting nodes and return new Position."""
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)

    def add_first(self,e):
        """Insert element e at the front of the list and return a new Position."""
        return self._insert_between(e,self._header,self._header._next)

    def add_last(self,e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e,self._trailer._prev,self._trailer)

    def add_before(self,p,e):
        """Insert element e into the list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e,original._prev,original)

    def add_after(self,p,e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e,original,original._next)

    def delete(self,p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self,p,e):
        """Replace the element at Position p with with e.

        Return the element formaly at Position p.
        """
        original = self._validate(p)
        old_value = original._element       # temporarily store old element
        original._element = e               # replace the new element
        return old_value
    




# Main Code

class FavouritesListMTF(FavouritesList):
    """List of elements odered with move-to-front heuristic."""

    # we override _move_up provide move to front semantics.
    def _move_up(self,p):
        """Move accesses item at Position p to frony of the list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))  # delete/insert

    # we overide top because list is no longer sorted
    def top(self,k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1<=k<=len(self):
            raise ValueError("Illegal value for k")

        # we begin to make a copy of original list
        temp = PositionList()
        for item in self._data:             # positional list supports iteration
            temp.add_last(item)

        # we repeatedly find, report and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have found the element with highest count
            yield highPos.element()._value  # report element to user
            temp.delete(highPos)            # remove form temp list

