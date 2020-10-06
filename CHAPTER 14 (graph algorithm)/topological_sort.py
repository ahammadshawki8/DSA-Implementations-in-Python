from graph_class import *

def topological_sort(g):
	"""Reurn a list of vertices of directed acyclic graph g in topological order.

	If graph g has a cycle, the result will be incomplete.
	"""

	topo = [] 			# a list of vertices placed in topological order.
	ready = [] 			# list of vertices that have no remaining constraints.
	incount = {}		# keep track of in-degree for each vertex.

	for u in g.vertices():
		incount[g] = g.degree(u, False)			# parameter requests incoming degree
		if incount[u] == 0:						# if u have no incoming edges
			ready.append(u)						# it is free of contraints

	while len(ready) > 0 :
		u = ready.pop()							# u is free of contraints
		topo.append(u)							# add u to topological order
		for e in g.incident_edges(u):			# consider all outgoing neighbours of u
			v = e.opposite(u)
			incount[v] -= 1						# v has one less constraint without u
			if incount[v] == 0:
				ready.append(v)
	return topo