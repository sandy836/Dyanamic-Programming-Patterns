def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    #Recurrence Relation dp[i] = min(dp[i-1]+cost_1_days_ticket, dp[i-7]+cost_7_days_ticket, dp[i-30]+cost_30_days_ticket
        lastDay = days[-1]
        dp = [0]*(lastDay+1)
        days_to_travel = set(days)
        for i in range(1, lastDay+1):
            if i not in days_to_travel:
                dp[i] = dp[i-1]
                continue
            dp[i] = min(dp[i-1]+costs[0], dp[max(0, i-7)]+costs[1], dp[max(0, i-30)]+costs[2])
        return dp[-1]