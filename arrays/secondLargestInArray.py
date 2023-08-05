# appraoch is to take small and second small
# whenever a number is smaller than small make the small second small and small to arr[i]
# else if number is smaller than small and greater than second small make it second small

def secondSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    return second_small
