from linked_queue_class import *
from merge_sort_linked import *


def decorated_merge_sort(data,key=None):
    """Demonstration of the decorate-sort-undercorate pattern."""
    if key is not None:
        for j in range(len(data)):
            data[j] = _Item(key(data[j]), data[j])  # decorate each element
    merge_sort(data)                                # sort with existing algorithm
    if key is not None:
        for j in range(len(data)):
            data[j] = data[j]._value                # undercoat each element