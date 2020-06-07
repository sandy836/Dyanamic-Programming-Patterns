def longest_common_subStr(str_1, str_2):
    max_len = 0
    row = len(str_1)+1
    col = len(str_2)+1
    dp = [[0]*col for i in range(row)]

    for i in range(1, row):
        for j in range(1, col):
            if str_1[i-1] == str_2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0
    return max_len

print(longest_common_subStr("abcd", "xyzabcd"))
    


