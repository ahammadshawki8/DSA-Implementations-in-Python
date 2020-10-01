# the functions of this code belong to BinaryTree class
from binary_tree_abc import *

class TreeTraversals(BinaryTree):
    def inorder(self):
        """Generate a inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def  _subtree_inorder(self,p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:        # if left child exists, traverse its subtree.
            for other in self._subtree_inorder(self.left(p):
                yield other
        yield p                             # visit p between its subtrees
        if self.right(p) is not None:       # if right child exists, traverse its subtree.
            for other in self._subtree_inorder(self.right(p):
                yield other
