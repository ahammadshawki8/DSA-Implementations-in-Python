# this function will be part of Tree class from tree_abc
from tree_abc import *

class Representation(Tree):
    def parenthesize(T,p):
        """Print parenthesized representation of subtree of T rooted at p."""
        print(p.element(),end="")           # use of ed avoiding trailing newline
        if not T.is_leaf(p):
            first_time = True
            for c in T.children(p):
                sep = " (" if first_time else ", "  # determine proper separator
                print(sep,end="")
                first_time = False      # any feature passes will not be the first
                parenthesize(T,c)       # recur on children
            print(")",end="")           #  include closing parenthesis  
