# firstly swap all elements of the matrix to i j position to j i position
# and then simply reverse the whole array so that i will rotate the image 
# 1 2 3    1 4 7    7 4 1
# 4 5 6 -> 2 5 8 -> 8 5 2
# 7 8 9    3 6 9    9 6 3

def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
