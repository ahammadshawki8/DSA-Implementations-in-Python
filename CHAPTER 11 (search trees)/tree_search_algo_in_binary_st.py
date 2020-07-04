# this is a part of binary search tree class.
# The right, left and parent functions can be found in the binary search tree implementation.

def TreeSearch(T,p,k):
    if k == p.key():
        return p                                # successful search
    elif k < p.key() and T.left(p) is not None:
        return TreeSearch(T,T.left(p),k)        # recur on the left subtree
    elif k > p.key() and T.right(p) is not None:
        return TreeSearch(T,T.right(p),k)       # recur on the right subtree
    return p                                    # unsuccessful search
