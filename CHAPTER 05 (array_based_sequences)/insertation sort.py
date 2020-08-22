# insertation sort
def insertation_sort(arr):
    for k in range(1,len(arr)):
        cur=arr[k]
        j=k
        while j>0 and arr[j-1]>cur:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=cur
    return arr

# testing
if __name__=="__main__":
    print(insertation_sort([2,3,4,1,7,9,8,5,6,0]))
