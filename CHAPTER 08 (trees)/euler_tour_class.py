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
