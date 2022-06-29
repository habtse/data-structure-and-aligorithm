
def partision(arr, lower_index, higher_index):
    """ function that define the partision"""
    pivot = arr[higher_index]
    i = lower_index -1
    for j in range(lower_index, higher_index):
        if arr[j] <= pivot:
            i +=1
            (arr[i], arr[j]) = (arr[j], arr[i])
    arr[i + 1], arr[higher_index] = arr[higher_index], arr[i + 1]
    return i + 1

def quick_sort(arr, lower_index, upper_index):
    """function that sort recursively"""
    if lower_index < upper_index:
        partision_index = partision(arr, lower_index, upper_index )
        quick_sort(arr, lower_index, partision_index- 1 )
        quick_sort(arr, partision_index + 1, upper_index)
    return arr


data = [8, 7, 2, 1, 0, 9, 6]
print(quick_sort(data, 0, len(data) -1))