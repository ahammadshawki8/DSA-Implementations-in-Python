def bubble_sort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]  
    return array
if __name__ == "__main__":
    array = [3,4,7,2,6,1,0,11,13,8]    
    print(bubble_sort(array))    