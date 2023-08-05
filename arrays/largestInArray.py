# approach is to simply initialize a maxi and simply iterate over the array 


def findLargestElement(arr, n):
    maxi = arr[0]
    for i in range(0, n):
        if (maxi < arr[i]):
            maxi = arr[i]
    return maxi
