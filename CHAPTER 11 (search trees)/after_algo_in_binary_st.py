# this is a part of binary search tree class.
# The right, left and parent functions can be found in the binary search tree implementation.

def after(p):
    if right(p) is not None:    # successor is leftmost position in p's right subtree
        walk = right(p)
        while left(walk) is not None:
            walk = left(walk)
        return walk
    else:                   # successor is nearest ancestor having p in its left subtree
        walk = p
        ancestor = parent(walk)
        while ancestor is not None and walk == right(ancestor):
            walk = ancestor
            ancestor = parent(walk)
        return ancestor
