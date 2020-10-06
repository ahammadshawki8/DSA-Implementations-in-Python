from graph_class import *


def shortest_path_tree(g,s,d):
	"""Reconstruct shortest-path tree rooted at vertex s, given distance map d.

	Return tree as a map from each reachable vertex v (other than s) to the
	edge e=(u,v) that is used to reach v fromits parent u in the tree.
	"""

	tree = {}
	for v in d:
		if v is not s:
			for e in g.incident_edges(v, False): 	# consider incoming edges
				u = e.opposite(v)
				wgt = e.element()
				if d[v] == d[u] + wgt:
					tree[v] = e 					# edge e is used to reach v
	return tree