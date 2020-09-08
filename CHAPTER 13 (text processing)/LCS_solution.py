def LCS_solution(X, Y, L):
	"""Return the longest substring of X and Y, given LCS table L"""
	solution = []
	j,k = lne(X), len(Y)
	while L[j][k] > 0:					# common characters remain
		if X[j-1] == Y[k-1]:
			solution.append(X[j-1])
			j -= 1
			k -= 1
		elif L[j-1][k] >= l[j][k-1]:
			j -= 1
		else:
			k -= 1
	return "".join(reversed(solution))	# return left-to-right version

	