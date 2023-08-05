# take first row and first columm as the value to check if there is a zero in that row and column or not
# but matrix[0][0] is in both so we take col0 as -1 to remove that conflit
# and then check using O(n2) that if there is 0 or not if there is 0 then mark it row and column as 0 and just check one condition
# and then mark the zeroes using the first row and column if any of them is 0 then mark it 0
# then for exception make the rows and columns as zeroes using two loops in the end

def setZeroes(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    m = len(matrix[0])
    col0 = -1
    for i in range(n):
        for j in range(m):
            if (matrix[i][j] == 0):
                matrix[i][0] = 0
                if (j == 0): 
                    col0 = 0
                else:
                    matrix[0][j] = 0
    for i in range(1, n):
        for j in range(1, m):
            if (matrix[i][0] == 0 or matrix[0][j] == 0):
                matrix[i][j] = 0

    if (matrix[0][0] == 0):
        for j in range(m):
            matrix[0][j] = 0
    if (col0 == 0):
        for i in range(n):
            matrix[i][0] = 0
