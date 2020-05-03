def minFallingPathSum(A):
    # Recurrence Relation dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
    row, col =  len(A), len(A[0])
    for i in range(1, row):
        for j in range(col):
            a = float('inf') if j-1<0 else A[i-1][j-1]
            b = float('inf') if j+1>=col else A[i-1][j+1]
            A[i][j] += min(a, A[i-1][j], b)
    return min(A[-1])

print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
