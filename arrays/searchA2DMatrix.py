# we have to figure out how to make this 2d into 1d array and how to access the indices efficiently.
# after that we will simply apply the binary search and access using mod and division operator.

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    low = 0
    high = m * n - 1
    while (low != high):
        mid = (low + high - 1) >> 1
        if (matrix[mid // m][mid % m] < target):
            low = mid + 1
        else:
            high = mid
    return (matrix[high // m][high % m] == target)
