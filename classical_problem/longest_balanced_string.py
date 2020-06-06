class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, s):
        open_bracket = ['(', '{', '[']
        close_bracket = [')', '}', ']']
        s = "*"+s
        dp = [0]*len(s) 
        _max_len = 0
        for i in range(1, len(s)):
            if s[i] in close_bracket and s[i-1] == open_bracket[close_bracket.index(s[i])]:
                dp[i] = dp[i-1]+ 2 + dp[i-2]
            elif s[i] in close_bracket and s[i-1] not in open_bracket and \
                s[i-dp[i-1]-1] == open_bracket[close_bracket.index(s[i])]:
                dp[i] = dp[i-1]+ 2 + dp[i-dp[i-1]-2]
            _max_len = max(_max_len, dp[i])
        return _max_len