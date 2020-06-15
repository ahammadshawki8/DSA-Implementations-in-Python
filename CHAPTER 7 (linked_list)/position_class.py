class Position:
    """An abstraction representing the location of a single element."""

    def __init__(self,container,node):
        """Constructor should not be invoked by the user."""
        self._container = container
        self._node = node

    def element(self):
        """Return the element stored at this position."""
        return self._node._element

    def __eq__(self,other):
        """Return True if other is a Position representing the same location."""
        return ((type(other) is type(self)) and (other._node is self._node))

    def __ne__(self,other):
        """Return True if other does not represent the same location."""
        return not(self == other)           # opposite of __eq__
