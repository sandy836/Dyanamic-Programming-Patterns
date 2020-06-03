"""
You are climbing a stair case and it takes A steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def climbStairs(self, A):
    if A == 1:
        return 1
    dp = [0]*(A+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, A+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]