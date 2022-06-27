def bubbleSort(arr):
    ''' This function takes list as input and sort them
    using bubble sorting.''' 
    size = len(arr)
    swap = False
    for i in range(size):
        for j in range(0,size - i -1):
            if arr[j] > arr[j + 1] :
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap = True
        if not swap :
            break
    return arr
                
print(bubbleSort([3,4,5,2,6,3,32,7,1]))           