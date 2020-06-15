import sys
space = sys.getsizeof

def disk_space(T,p):
    """Return total disk_Space for subtree of T rooted at p"""
    subtotal = p.element().space()          # space used at the position p
    for c in T.children(p):
        subtotal += disk_space(T,c)         # add child's space to subtotal
    return subtotal
    
