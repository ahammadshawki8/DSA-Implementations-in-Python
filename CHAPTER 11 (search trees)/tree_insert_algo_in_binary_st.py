# this is a part of binary search tree class.
# The right, left and parent functions can be found in the binary search tree implementation.

def TreeInsert(T,k,v):
    p = TreeSearch(T,T.root(),k)
    if k == p.key():
        T[p] = v
    elif k < p.key():
        T[T.left(p)] = v
    else:
        T[T.right(p)] = v
