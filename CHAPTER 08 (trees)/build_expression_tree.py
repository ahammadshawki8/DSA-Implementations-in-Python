# Extra Utilities

# Extra Utility
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

class ExpressionTree(LinkedBinaryTree):
    """An arithmatic expression tree."""

    def __init__(self,token,left=None,right=None):
        """Create an expression tree

        In a single parameter form, token should be a leaf value (e.g., "42")
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator,
        and left and right should be existing ExpressionTree instances
        that become the operands for the binary tree.
        """
        super().__init__()          # LinkedBinaryTree initialization
        if not isinstance(token,str):
            raise TypeError("Token must be a string")
        self._add_root(token)       # use inherited, _nonpublic method.
        if left is not None:
            if token not in "+=*/x":
                raise ValueError("Token must be a valid operator")
            self._attach(self.root(),left,right)    # use inherited, non public method

    def __str__(self):
        """Return string representation of a expression."""
        pieces = []             #sequence of piecewise strings to compose
        self._parenthesize_recur(self,root(),pices)
        return " ".join(pieces)

    def _parenthesize_recur(self,p,result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))         # leaf value as a string
        else:
            result.append("(")                              # opening parenthesis
            self._parenthesize_recur(self.left(p),result)   # left subtree
            self.append(p.element())                        # operator
            self._parenthesize_recur(self.right(p),result)  # right subtree
            result.append(")")                              # closing parenthesis

    def evaluate(self):
        """Return the numeric result of the expresion."""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self,p):
        """Return the numeric results of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())       # we assume element is numeric
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op=="+":
                return left_val + right_val
            elif op=="-":
                return left_val - right_val
            elif op=="/":
                if right_val == 0:
                    raise ZeroDivisionError
                return left_val / right_val
            else:
                return left_val * right_val     # treat "x" or "*" as multiplication
            
            

# Main Code

def build_expression_tree(tokens):
    """Return an Expression Tree based opon by a tokenized expression."""
    S = []                      # we use python list as stacks
    for t in tokens:            
        if t in "+-x*/":        # t is an operator symbol
            S.append(t)         # push the operator symbol
        elif t not in "()":     # consider t to be a literal
            S.append(ExpressionTree(t)) # push trivial tree storing value
        elif t==")":        # compose a new tree from theree constituent parts
            right = S.pop()     # right subtree as per LIFO
            op = S.pop()        # operator symbol
            left = S.pop()      # left subtree
            S.append(ExpressionTree(op,left,right)) # repush tree
        # we ignore the left parenthesis
        return S.pop()
