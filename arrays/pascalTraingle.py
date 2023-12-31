# approach is to first create a matrix where each row as i + 1 elements
# and then simply loop in rows and for element in row it is
# dp[i][j] is sum of previous row previous element + previous row same element

def generate(self, n: int) -> List[List[int]]:
    dp = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp
