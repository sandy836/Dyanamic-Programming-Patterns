def minCostClimbingStairs(cost):
    # Recurrence Relation dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    dp = [0]*len(cost)
    
    #Base condition
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    return min(dp[-1], dp[-2])

print(minCostClimbingStairs([10, 15, 20]))
