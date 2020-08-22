# simple implementation of Node class.
class Node:
    """Lightweight, non-public class for storing a singly linked list"""
    __slots__ = "_element", "_next"         # streamline memory usage.

    def __init__(self,element,next):
        self._element = element             # reference to user's element
        self._next = next                   # reference to next node
