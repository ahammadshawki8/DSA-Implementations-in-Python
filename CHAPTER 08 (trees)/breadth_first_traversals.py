# the functions of this code belong to Tree class of tree_abc

from tree_abc import *
from linked_queue_class import *

class TreeTraversals(Tree):
    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not sself.is_empty():
            fringe = LinkedQueue()          # known positions not yet yeilded
            fringe.enqueue(self.root())     # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue()        # remove the front of the queue
                yield p                     # report this position
                for c in self.children(p):
                    fringe.enqueue(c)       # add children to the back of the queue


