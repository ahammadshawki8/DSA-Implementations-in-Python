def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j== len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]      # copy ith element S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]      # copy jth element S2 as next item of S
            j += 1


def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n= len(S)
    if n < 2:
        return S        # list is already sorted

    # devide
    mid = n//2
    S1 = S[0:mid]       # copy of first half
    S2 = S[mid:n]       # copy of second half

    # conquer (with recursion)
    merge_sort(S1)      # sort copy of first half
    merge_sort(S2)      # sort copy of second half

    # merge results
    merge(S1,S2,S)      # merge sorted halves back to S

    return S

if __name__ == "__main__":
    print(merge_sort([23,1,456,22,0,34,34,45,67,2,4,3,11]))
