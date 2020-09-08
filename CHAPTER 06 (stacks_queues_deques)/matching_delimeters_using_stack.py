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




# Extra Utilities
# Stack class
class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack"""
        self._data=[]                   # nonpublic list instance

    def __len__(self):
        """Return the numbers of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if stack is empty"""
        return len(self._data)==0

    def push(self,e): # e for element
        """Add element e to the top of the stack"""
        self._data.append(e)            # new item stored at the end of the list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is currently empty")
        return self._data[-1]           # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e, LIFO)

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is currently empty")
        return self._data.pop()          # remove last item from the list

    def __str__(self):
        """Printing a representation of the stack"""
        print("< ")
        for e in self._data[-1::-1]:
            print(" ",e)
        print(">")
        return "REPRESENTATION OF STACK"
                 
# creating empty class
class Empty(Exception):
    pass