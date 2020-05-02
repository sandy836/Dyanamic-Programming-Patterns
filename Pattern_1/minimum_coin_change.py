class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Recurrence Relation dp[i] = min(dp[i],dp[i-coin[0], dp[i-coin[1], dp[i-coin[2]],. . .dp[i-coin[k]])
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(0, amount+1):
            for coin in coins:
                if i-coin<0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]