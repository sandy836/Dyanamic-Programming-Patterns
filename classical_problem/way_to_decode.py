"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total 
number of ways to decode it.
"""
class Solution:
	# @param A : string
	# @return an integer
	def numDecodings(self, s):
	    if not s:
            return 0
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, n+1):
            #taking one char at a time
            num_1 = int(s[i-1:i])
            #taking two char at a time
            num_2 = int(s[i-2:i])
            if num_1>=1 and num_1<=9:
                dp[i] += dp[i-1]
            if num_2>=10 and num_2<=26:
                dp[i] += dp[i-2]
        
        return dp[-1]