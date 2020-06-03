"""
In Danceland, one person can party either alone or can pair up with another person.
Can you find in how many ways they can party if there are A people in Danceland?
Note: Return your answer modulo 10003, as the answer can be large.
"""
def solve(self, A):
    if A == 0:
        return 0
    if A == 1:
        return 1
        
    dp = [0]*(A+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, A+1):
        dp[i] = (dp[i-1] + dp[i-2]*(i-1))%10003
    
    return dp[-1]