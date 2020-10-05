from linked_binary_tree import *
from collections import Counter
from sorted_priority_queue import *

def huffman(string):
	f = Counter()
	f.update(string)
	f = dict(f)

	Q = SortedPriorityQueue()

	for s in string:
		T =  LinkedBinaryTree()
		root = T._add_root(s)
		Q.add(f[s],T)

	while len(Q) > 1:
		(f1,T1) = Q.remove_min()
		(f2,T2) = Q.remove_min()

		T =  LinkedBinaryTree()
		root = T._add_root(f1 + f2)
		T._attach(root, T1, T2)

		Q.add(f1+f2,T)
	(f,T) = Q.remove_min()

	return T
