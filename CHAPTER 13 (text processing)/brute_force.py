def find_brute(T,P):
	"""Return the lowest index of T at which substring P begins (or else -1)"""
	n,m = len(T), len(P) 		# introduce convenient notions
	for i in range(n-m+1):		# start every potential starting index withinh T
		k = 0					# an nindex into pattern P
		while k < m and T[i+k] == P[k]:		# kth character of P matches
			k += 1
		if k == m:				# if we reached the end of the pattern.
			return i 			# substring T[i:i+m] matches P
	return -1					# failed to find a match starting with any i

print(find_brute("dhakawwe","wwe"))