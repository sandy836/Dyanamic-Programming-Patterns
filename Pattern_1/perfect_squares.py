def numSquares(n):
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for i in range(1, n+1):
        j = 1
        while i-j*j>=0:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1
    return dp[-1]
print(numSquares(300))
