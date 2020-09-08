def LCS(X,Y):
	"""Return table such that L[i][j] is length of LCS for X[0:j] and Y[0:k]."""
	n,m = len(X), len(Y)				 	# introduce convenient notations
	L = [[0]*(m+1) for k in range (n+1)] 	# (n+1) X (m+1) table
	for j in range(n):
		for k in range(m):
			if X[j] == Y[k]: 				# align this match 
				L[j+1][k+1] = L[j][k] + 1
			else:							# choose to ignore one character
				L[j+1][k+1] = max(L[j][K+1], L[j+1][k])
	return L
