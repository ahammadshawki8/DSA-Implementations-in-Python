def find_kmp(T,P):
    """Return the lowest index of T at which the substring P begins (or else -1)."""
    n, m = len(T), len(P)       # introduce convenient notrations
    if m == 0:
        return 0                # trivial search for empty string
    fail = compute_kmp_fail(P)  # rely on utility to precompute
    j = 0                       # index into text
    k = 0                       # index into pattern
    while j < n:
        if T[j] == P[k]:        # P[0:1+k] matches thus
            if k == m -1:       # match is complete
                return j-m+1
            j += 1              # try to extend match
            k += 1
        elif k > 0:
            k = fail[k-1]       # reuse suffix of P[0:k]
        else:
            j += 1
    return -1


def compute_kmp_fail(P):
    "Utility that computes and return KMP 'fail' list"
    m = len(P)
    fail = [0] * m          # by default, presume overlap of 0 everywhere 
    j = 1
    k = 0
    while j < m:            # compute f(j) during the pass, if non-zero
        if P[j] == P[k]:    # k + 1 character matches thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:         # k follows a matching prefix
            k = fail[k-1]
        else:
            j += 1          # no match found starting at j
    return fail
