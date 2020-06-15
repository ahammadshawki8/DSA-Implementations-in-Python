from expression_tree import *

def build_expression_tree(tokens):
    """Return an Expression Tree based opon by a tokenized expression."""
    S = []                      # we use python list as stacks
    for t in tokens:            
        if t in "+-x*/":        # t is an operator symbol
            S.append(t)         # push the operator symbol
        elif t not in "()":     # consider t to be a literal
            S.append(ExpressionTree(t)) # push trivial tree storing value
        elif t==")":        # compose a new tree from theree constituent parts
            right = S.pop()     # right subtree as per LIFO
            op = S.pop()        # operator symbol
            left = S.pop()      # left subtree
            S.append(ExpressionTree(op,left,right)) # repush tree
        # we ignore the left parenthesis
        return S.pop()
