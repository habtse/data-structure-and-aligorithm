def sellectionSort(arr: [int]) -> [int]:
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(1 + i ,size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
    return arr

