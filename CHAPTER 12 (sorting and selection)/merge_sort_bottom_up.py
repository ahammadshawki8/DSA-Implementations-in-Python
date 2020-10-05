def merge(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."""
    end1 = start+inc                    # boundary for run1
    end2 = min(start+2*inc, len(src))   # boundary for run2
    x,y,z = start, start+inc, start     # index into run1, run2, result
    while x < end1 and y < end2:
        if src[x] > src[y]:
            result[z] = src[x]
            x += 1                      # copy from run1 and incriment x
        else:
            result[z] = src[y]
            y += 1                      # copy from run2 and incriment y
        z += 1                          # incriment z to reflect new result
    if x < end1:
        result[z:end2] = src[x:end1]    # copy reminder of run1 to output
    if y < end2:
        result[z:end2] = src[y:end2]    # copy reminder of run2 to output

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    import math
    logn = math.ceil(math.log(n,2))
    src, dest = S, [None]*n                 # make temporary storage for dest
    for i in (2**k for k in range(logn)):   # pass i creates all runs of length 2i
        for j in range(0, n, 2*i):              # each pass merges two length i runs
            merge(src,dest,j,i)
        src, dest = dest, src       # reverse roles of lists
    if S is not src:
        S[0:n] = src[0:n]       # additonal copy to get results to S

    return S



# testing
if __name__ == "__main__":
    print(merge_sort([23,1,456,22,0,34,34,45,67,2,4,3,11]))
