# Extra Utilities

# creating linked queue class
class LinkedQueue:
    """FIFO queue implementation using a sigly linked list for storage."""

    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0                  # number of sequence elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return (self._size == 0)

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element      # front alligned with the head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():             # special case as queue is empty
            self._tail=None             # removed head had been the tail
        return answer

    def enqueue(self,e):
        """Add an element to the back of the queue."""
        newest = self._Node(e,None)     # node will be new tail node
        if self.is_empty():             # special case: previously empty
            self._head = newest
        else:
            self._tail._next = newest
        self.tail = newest              # update reference to tail node
        self._size += 1







# Main Code
def inplace_quick_sort(S,a,b):
    """Sort the list from S[a] to S[b] inclusive using the quick sort algorithm."""
    if a >= b:
        return                  # range is trivially sorted
    pivot = S[b]                # last element of the range is pivot
    left = a                    # will scan rightward
    right = b-1                 # will scan leftward

    while left <= right:
        # scan until reaching value equal or larger than pivot (or right maker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left maker)
        while left <= right and S[right] > pivot:
            right -= 1

    if left <= right:           # scans did not strictly cross
        S[left], S[right] = S[right], S[left]   # swap values
        left, right = left+1, right-1           # shrink range

    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_Sort(S, a, left-1)
    inplace_quick_sort(S, left+1, b)

if __name__ == "__main__":
    S = LinkedQueue()
    S.enqueue(20)
    S.enqueue(1)
    S.enqueue(0)
    S.enqueue(2)
    S.enqueue(19)
    inplace_quick_sort(S,0,4)