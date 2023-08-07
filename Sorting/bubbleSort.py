# approach is to iterate array n2 times and after each iteration place the maximum value to the end
# so the array will get sorted

def bubbleSort(arr, n):
    for i in range(n - 1, -1, -1):
        for j in range(0, i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
