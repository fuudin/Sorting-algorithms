def partition(array, low, high):
    pivot = array[high]
 
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
 
 
def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
 
 
arr = [1, 7, 4, 1, 10, 9, -2, 50]
 
size = len(arr) - 1

quickSort(arr, 0, size)
print(arr) 
