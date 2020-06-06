from stack_class import *

def is_matched(exp):
    """Return True if all delimeters matched correctly, False otherwise"""
    
    lefty = "({["
    righty = ")}]"
    
    s=ArrayStack()
    
    for c in exp:
        if c in lefty:
            s.push(c)               # push left delimeter
        elif c in righty:
            if s.is_empty():
                return False        # noting to match with
            if righty.index(c) != lefty.index(s.pop()):
                return False        # mismatched
            
    return s.is_empty()             # the stack must be empty if all symbles matched.
