def max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        if len(arr) == 2:
            if arr[0] > arr[1]:
                return arr[0]
            else:
                return arr[1]
        else:
            start = 0
            end = len(arr)
            mid =(start+end)//2
            if max(arr[start:mid])> max(arr[mid:end]):
                return max(arr[start:mid])
            else:
                return max(arr[mid:end])

if __name__=="__main__":
    print(max([1,23,4,33,44,67,10,109,30002,42,3,5]))
    print(max([1,23,4,33,44,67,10,10,0,42,3,5]))
    print(max([1,23,4,33,40,67,10,109,34,42,3,50000]))
    print(max([34521,23,4,33,44,67,10,109,1,42,3,5]))
    print(max([0,4]))
    print(max([0]))
