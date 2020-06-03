"""
Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.
"""

def countMinSquares(self, A):
    dp = [float('inf')]*(A+1)
    dp[0] = 0
    for i in range(0, A+1):
        j = 0
        while j*j<=i:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j+=1
    return dp[-1]