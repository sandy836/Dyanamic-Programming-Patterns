def maximalSquare(matrix):
    if not matrix:
        return 0
    row, col, max_area = len(matrix), len(matrix[0]), 0
    dp = [[0]*(col+1) for _ in range(row+1)]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '0':
                continue
            dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j])+1
            max_area = max(max_area, dp[i+1][j+1])
    return max_area*max_area

print(maximalSquare([["1","0","1","0","0"],
                     ["1","0","1","1","1"],
                     ["1","1","1","1","1"],
                     ["1","0","0","1","0"]]))