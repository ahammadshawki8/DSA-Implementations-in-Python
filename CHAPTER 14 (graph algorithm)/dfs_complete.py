from basic_dfs import *

def DFS_complete(g):
	"""Perform DFS for entire graph and return forest as a dictionary.

	Result maps each vertex v to the edge that was used to discover it.
	(Vertices that are roots of s DFS tree are mapped to None)
	"""
	forest = {}
	for u in g.vertices():
		if u not in forest:
			forest[u] = None		# u will be root of a tree
			DFS(g,u,forest)
	return forest