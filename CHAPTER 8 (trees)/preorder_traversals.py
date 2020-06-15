# the functions of this code belongs to Tree class of tree_abc

from tree_abc import *

class TreeTraversals(Tree):
    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):  # start the recursion
                yield p

    def _subtre_preorder(self,p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p                     # visit p before its subtree
        for c in self.children(p):  # for each child of c
            for other in self._subtree_preorder(c):  # do preorder of c's children
                yield other         # yeilding each to our caller
