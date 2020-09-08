# Extra Utilities
from collections import MutableMapping

class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class."""
    #---------------------------nested _Item class------------------------------
    class _Item:
        """Lightweight composit to store key-value pairs as map items."""
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self,other):
            return self._key == other,_key      # compare items based on their keys

        def __ne__(self,other):
            return not(self == other)           # opposite of __eq__

        def __lt__(self,other):
            return self._key < other,_key       # compare items based on their keys

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

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    #-------------------------addtional abstract mathods---------------------------
    def left(self,p):
        """Return the Position representing p's left child.

        Return None if p does note have a left child.
        """
        raise NotImplementedError("Must be implemented by subclass.")

    def right(self,p):
        """Return the Position representing p's right child.

        Return None if p does note have a right child.
        """
        raise NotImplementedError("Must be implemented by subclass.")

    #---------------concrete methods implemented in this class-------------------
    def sibling(self,p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:              # p must be the root
            return None                 # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)   # possibly None
            else:
                return self.left(parent)    # possibly None

    def children(self,p):
        """Generate an iteration of Position representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.rightt(p) is not None:
            yield self.right(p)
        
class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node:            # Lightweight, non-public clss for storing a node.
        __slots__ = ("_element","_parent","_left","_right")
        def __init__(self,element,parent=None,left=None,right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self,container,node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self,other):
            """Return True if other is a Position representing the same location."""
            return ((type(other) is type(other)) and (other._node is self._node))

        def __ne__(self,other):
            """Return True if other is a Position not representing the same location."""
            return (self == other)              # opposite of __eq__

    def _validate(self,p):
        """Return associated node, if position is valid."""
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:      # cconvention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node
        
    def _make_position(self,node):
        """Return Position instance for given node (or None if no node)"""
        return self.Position(self,node) if node is not None else None

    #------------------------binary tree comstructor-----------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    #---------------------------public accessors----------------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)"""
        return self._make_position(self._root)

    def parent(self):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self,p):
        """Return the Position of p's left child (or None if no left child)"""
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self,p):
        """Return the Position of p's right child (or None if no right child)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self,p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:          # left child exists
            count += 1
        if node._right is not None:         # right child exists
            count += 1
        return count

    def _add_root(self,e):
        """Place element e at the root of an empty tree and return new position.

        Raise ValueError if tree is non empty.
        """
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self,p,e):
        """Create a new left child child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists")
        node._left=self._Node(e,node)               # node is e's parent
        self._size += 1
        return _make_position(node._left)

    def _add_right(self,p,e):
        """Create a new right child child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        node._right=self._Node(e,node)               # node is e's parent
        self._size += 1
        return _make_position(node._right)

    def _delete(self,p):
        """Delete the node at Position p, and replace it with its child,if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid of p has two children.
        """
        node = self._validate(p)
        if self._num_children(p) == 2:
            raise ValueError("p has two children")
        child = node._left if node._left else node._right       # might be None
        if child is not None:
            child._parent = node._parent        # child grandparent becomes parent
        if node is self._root:
            self._root == child                 # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node                     # convention for deprecated node.
        return node._element

    def _attach(self,p,t1,t2):
        """Attach trees t1 and t2 as left and right subtees of external p."""
        node = self._validate(p)
        if not self.is_leaf:
            raise ValueError("Position must be a leaf")
        if not type(self) is type(t1) is type(t2): # all three trees must be same type.
            raise TypeError("Tree types must match")
        self.size += len(t1) + len(t2)
        if not t1.is_empty():               # attach t1 as the left subtree of node.
            t1._root._parent = node
            node._left = t1._root
            t1._root = None                 # set t1 instance to empty.
            t1._size = 0
        if not t2.is_empty():               # attach t2 as the right subtree of node.
            t2._node._parent = _node
            node._right = t2._root
            t2._root = None                 # set t2 instance to empty.
            t2._size = 0
   
class TreeMap(LinkedBinaryTree,MapBase):
    """Sorted map implementation using binary search tree."""
    
    #----------------------------override Position class------------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of map's key-value pair."""
            return self.element()._key

        def value(self):
            """Return value of map's key-value pair."""
            return self.element()._value

    #------------------------------non-public utilities--------------------------
    def _subtree_search(self,p,k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key():                    # found match
            return p
        elif k < p.key():                   # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p),k)
        else:
            if self.right(p) is not None:   # search right subtree
                return self._subtree_search(self.right(p),k)
        return p                            # unsuccessful search

    def _subtree_first_position(self,p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None: # keep walking left
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self,p):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None: # keep walking right
            walk = self.eright(walk)
        return walk

    #--------------------------public utilities---------------------------------
    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self,p):
        """Return the Position just before p in the natural order.

        Return None if p is the first position.
        """
        self._validate(p)               # inherited from LinkedBinaryTee
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self,p):
        """Return the Position just after p in the natural order.

        Return None if p is the last position.
        """
        self._validate(p)               # inherited from LinkedBinaryTee
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above
        

    def find_position(self,k):
        """Return position with key k, or else neighbour (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(),k)
            self._rebalance_access(p)       # hook for balance tree subclasses
            return p

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self,k):
        """Return (key,value) pair with least key greater then or equal to k.

        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)           # may not find exact match
            if p.key() < k:                     # p's key is too small
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self,start=None,stop=None):
        """Iterate all (key,value) pairs such that start <= key <= stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through maximum key of map.
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # we initialize p with logic simmilar to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(),p.value())
                p = self.after(p)

    def __getitem__(self,k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError("KeyError: "+ repr(k))
        else:
            p = self._subtree_search(self.root(),k)
            self._rebalance_access(p)           # hook for banalced tree subclasses
            if k != p.key():
                raise KeyError("KeyError: " + repr(k))
            return p.value()

    def __setitem__(self,k,v):
        """Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            leaf = self._add_root(self._Item(k,v))  # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(),k)
            if p.key() == k:
                p.element()._value = v              # replace existing item's value
                self._rebalance_access(p)           # hook for balanced tree subclasses
                return
            else:
                item = self._Item(k,v)
                if p.key() < k:
                    leaf = self._add_right(p,item)  # inherited from LinkedBinaryTree
                else:
                    leaf = self._add_left(p,item)   # inherited from LinkedBinaryTree
            self._rebalance_insert(leaf)            # hook for balanced tree subclasses
            return

    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self,p):
        """Remove the item at given Position."""
        self._validate(p)                   # inherited from LinkedBinaryTree
        if self.left(p) and self.right(p):  # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self.replace(p,replacement.element())   # from LinkedBinaryTree
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)                     # inherited from LinkedBinaryTree
        self._rebalance_delete(parent)      # if root deleted, parent is None

    def __delitem__(self,k):
        """Remove item associated with key k (raise KeyError is not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(),k)
            if k == p.key():
                self.delete(p)          # rely on positional version
                return                  # successful deletion complete
            self._rebalance_access(p)   # hook for balanced tree subclasses
        raise KeyError("Key Error: " + repr(k))

    def _rebalance_insert(self,p):
        pass
    
    def _rebalance_delete(self,p):
        pass
    
    def _rebalance_access(self,p):
        pass

    def _relink(self,parent,child,make_left_child):
        """Relink parent node with child node (we allow child to be None)"""
        if make_left_child:             # make it a left child
            parent._left = child
        else:                           # make it a right child
            parent._right = child       
        if child is not None:
            child._parent = parent      # make child point to parent

    def _rotate(self,p):
        """Rotate Position p above its parent."""
        x = p._node
        y = x._parent                   # we assume this exists
        z = y._parent                   # grandparent (possibly None)
        if z is none:
            self._root = x              # x becomes root
            x._parent = None
        else:
            self._relink(z,x,y==z._left)    # x becomes the direct child of z
        # now rotate x and y, including transfer of the middle subtree
        if x == y._left:
            self._relink(y,x._right,True)   # x._right becomes left child of y
            self._relink(x,y,False)         # y becomes the right child of x
        else:
            self._relink(y,x.left,False)    # x._left becomes right child of y
            self._relink(x,y,True)          # y becoms the left child of x

    def _restructure(self,x):
        """Perform trinode restructure of Position x with parent/grandparent."""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(x)):    # matching allignment
            self.rotate(y)                                  # single rotation (of y)
            return y                                        # y is new subtree root
        else:                                               # opposite allignment
            self._rotate(x)                                 # double rotation of x
            self._rotate(x)
            return x                                        # x is new subtree root






# Main Code
class AVLTreeMap(TreeMap):
    """Sorted MAp implementation using AVL tree."""
    #-------------------nested _Node class---------------------------------------
    __slots__ = "_height"           # additional data member to store height

    def __init__(self,element,parent = None,left=None,right=None):
        super().__init__(element,parent,left,right)
        self._height = 0        # will be recomputed during balancing

    def left_height(self):
        return self._left._height if self._left is not None else 0

    def right_height(self):
        return self._right._height if self._right is not None else 0

    #--------------------------positional based utility methods----------------
    def _recompute_hieght(self,p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalance(self,p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1

    def _tall_child(self,p,favorleft=False): # parameter controls tiebreaker
        if p._node.left_height() + (1 if favorleft else 0) > p._node.left_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self,p):
        child = self._tall_child(p)
        # if child is on left, favour left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child,alignment)

    def _rebalance(self,p):
        while p is not None:
            old_height = p._node._height        # trivially 0 if new node
            if not self._isbalance(p):          # imbalance detected!
                # perform trinode resturturing, setting p to resulting root
                # and recompute new local heights after the restructuring'
                p = self._restucture(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)           # adjust for recent changes
            if p._node._height == old_height:   # has height changed?
                p = None                        # no further changes needed
            else:
                p = self.parent(p)              # repeat with parent

    #------------------------- override balancing hooks------------------------
    def _rebalance_insert(self,p):
        self._rebalance(p)

    def _rebalance_delete(self,p):
        self._rebalance(p)
