# Extra Utilities

class EulerTour:
    """Abstract base class for performing Euler tour of a tree.

    _hook_previsit ans _hook_postvisit may be overriden by subclasses.
    """
    def __init__(self,tree):
        """Prepare an Euler tour template for given tree."""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(),0,[])   # start the recursion

    def _tour(self,p,d,path):
        """Perform tour of subtree rooted at Position p.

        p      Position of current node being visited
        d      depth of p in the tree
        path   list of indices of children on path from root to p
        """
        self._hook._previsit(p,d,path)                  # pre-visit p
        result = []
        path.append(0)                  # add new index to the end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c,d+1,path))      # recur on child's subtree
            path[-1] += 1           # increment index
        path.pop()                  # remove extraneous index from the end of the path
        answer = self._hook._postvisit(p,d,path,results)    # post-visit p
        return answer

    def _hook_previsit(self,p,d,path):          # can be overriden
        pass
    def _hook_postvisit(self,p,d,path,results): # can be overriden
        pass

class BinaryEularTour(EulerTour):
    """Abstract base class for performing Eular tour of a binary tree.

    This version includes an additional _hook_invisit that is called after the tour
    of the left subtree (if any), yet before the tour of right subtree (if any).

    NOTE: Right child is always assigned index 1 in path, even if no left sibling.
    """
    def _tour(self,p,d,path):
        results = [None,None]               # will update the results of recursions
        self._hook_previsit(p,d,path)       # pre visit for p
        if self._tree.left(p) is not None:  # consider the left child
            path.append(0)
            result[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p,d,path)        # in visit for p
        if self._tree.right(p) is not None: # consider the right child
            path.append(1)
            result[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p,d,path,results) # post visit of p

    def _hook_invisit(self,p,d,path):       # can be overriden
        pass
        return answer





# Main Code

class BinaryLayout(BinaryEularTour):
    """Class for computing (x,y) coordinates for each node of a binary tree."""
    def __init__(self,tree):
        super().__init__(tree)          # must call the parent constructor
        self._count = 0                 # initialize count of processed nodes

    def _hook_invisit(self,p,d,path):
        p.element().setX(self._count)   # x-coordinate serialized by count
        p.element().setY(self,d)        # y-coordinate is depth
        self._count +=1                 # advaced count for processed nodes
