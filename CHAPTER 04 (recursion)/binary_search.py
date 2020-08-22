# Sample list
arr = [3,4,10,6,1,2,5,11,67,83,20,0,7,8,9,33,42,18,55,37,73,28,100,1101]

# sort the list
arr.sort()

# binary search function
def binary_search(data,target,low=None,high=None):
    # managing the default param
    if low == None:
        low = 0
    if high == None:
        high = len(data)-1
        
    if low > high:
        print("Invalid Entry")
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            print("Found -->",mid)
            return True
        else:
            if target > data[mid]:
                return binary_search(data,target,mid+1,high)
            else:
                return binary_search(data,target,low,mid-1)

# binary search function
    # in a different point of view (without recursion)
def binary_search2(data,target,low=None,high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(data)-1

    while low < high:
        mid = (low+high)//2
        if target == data[mid]:
            print("Found -->",mid)
            return True
        else:
            if target > data[mid]:
                return binary_search(data,target,mid+1,high)
            else:
                return binary_search(data,target,low,mid-1)
    print("Invalid Entry")
    return False


# testing our first function
if __name__ == "__main__":
    print(binary_search(arr,20))
    print(binary_search(arr,1101))
    print(binary_search(arr,0))
    print(binary_search(arr,83,0,23))
    print(binary_search(arr,83,5,21))
    print(binary_search(arr,83,0,21))
    print(binary_search(arr,83,5,23))
    print(binary_search(arr,83,20,5))

print("\n\n")

# testing our second function
if __name__ == "__main__":
    print(binary_search2(arr,20))
    print(binary_search2(arr,1101))
    print(binary_search2(arr,0))
    print(binary_search2(arr,83,0,23))
    print(binary_search2(arr,83,5,21))
    print(binary_search2(arr,83,0,21))
    print(binary_search2(arr,83,5,23))
    print(binary_search2(arr,83,20,5))

