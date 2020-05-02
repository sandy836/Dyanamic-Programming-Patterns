def minPathSum(grid):
    # Recurrence Relation dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + cost[i][j]
    row, col = len(grid), len(grid[0])
    dp = [[0]*col for _ in range(row)]
    dp[0][0] = grid[0][0]
    for i in range(1, col):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1, row):
        dp[i][0] =  dp[i-1][0] + grid[i][0]
    
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
    return dp[-1][-1]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
