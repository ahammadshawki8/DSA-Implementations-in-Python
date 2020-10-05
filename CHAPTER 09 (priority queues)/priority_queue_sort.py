from heap_priority_queue import *
from positional_list import *

def pq_sort(C): # assuming C is a positional_list
    """Sort a collection of elements stored in a positional list."""
    n = len(C)
    P = HeapPriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element,element)          # use element as keu and value
    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v)                   # store smallest remaining element in C
        
