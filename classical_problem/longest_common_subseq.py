#with memoization
def max_lca(str_1, str_2, state_max):
    res = 0
    if str_1+"_"+str_2 in state_max:
        return state_max[str_1+"_"+str_2]
    if not str_1 or not str_2:
        return res
    if str_1[0] == str_2[0]:
        res = max_lca(str_1[1:], str_2[1:], state_max)+1
    else:
        res = max(max_lca(str_1, str_2[1:], state_max), max_lca(str_1[1:], str_2, state_max))
    state_max[str_1+"_"+str_2] = res
    return res
state_max = dict()
print(max_lca("aaaaaa", "ababab", state_max))

#dp state calculation
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
print(max_lca_2("aaaaaa", "ababab"))


