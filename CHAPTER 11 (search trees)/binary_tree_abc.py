from tree_abc import *

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
        
    
