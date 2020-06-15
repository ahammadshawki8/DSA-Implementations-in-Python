from eular_tour_class import *
class BinaryEularTour(EularTour):
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
