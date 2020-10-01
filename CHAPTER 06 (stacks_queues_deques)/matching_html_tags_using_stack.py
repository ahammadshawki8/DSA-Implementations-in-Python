from stack_class import *

def is_metched_html(raw):
    """Return True if all the HTML tags properly matched, False otherwise."""
    s = ArrayStack()
    j = raw.find("<")               # find first "<" character (if any)
    while j != -1:
        k = raw.find(">",j+1)       # find next ">" chracter
        if k == -1:
            return False            # invalid tag because there is only one tag
        tag = raw[j+1:k]            # strip away < >
        if not tag.startswith("/"): # this is opening tag
            s.push(tag)
        else:                       # this is closing tag
            if s.is_empty():
                return False        # nothing to match with
            if tag[1:] != s.pop():
                return False        # mismatched delimeter
        j = raw.find("<",k+1)       # find next "<" character (if any)
    return s.is_empty()             # were all opening tags matched?

