# approach is to first take mini as ith index and check for the smallest value index after ith index
# and at last swap the indexes.
# O(n2) time complexity

def selectionSort(arr, n):
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if (arr[j] < arr[mini]):
                mini = j
        arr[mini], arr[i] = arr[i], arr[mini]
    return arr
