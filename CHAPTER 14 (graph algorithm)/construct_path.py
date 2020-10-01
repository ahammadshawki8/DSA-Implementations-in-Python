from basic_dfs import *

def construct_path(u,v,discoverd):
	path = [] 							# empty path by default
	if v in discovered:
		# we build list from v to u and then reverse it at the end
		path.append(v)
		walk = v
		while walk is not u:
			e = discovered[walk]		# find edge leading to walk
			parent = e.opposite(walk)
			path.append(parent)
			walk = parent
		path.reverse()					# reorient path from u to v
	return path