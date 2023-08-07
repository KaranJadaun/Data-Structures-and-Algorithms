# approach is to make two partition sorted and unsorted
# take the ith element. till ith the array is sorted
# iterate from ith to 0 and check its correct position and place it

def insertionSort(arr, n):
    for i in range(n):
        j = i
        while (j > 0 and arr[j - 1] > arr[j]):
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr
