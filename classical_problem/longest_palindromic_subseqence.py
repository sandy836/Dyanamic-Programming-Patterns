def max_lca_2(str_1, str_2):
    col = len(str_1)+1
    row = len(str_2)+1
    dp = [[0]*(col) for i in range(row)]
    
    for i in range(1, row):
        for j in range(1, col):
            if str_1[j-1] == str_2[i-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]
print(max_lca_2("aedsead", "daesdea"))