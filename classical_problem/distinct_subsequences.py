def count_distinct_subsequences_rec(word, target):
    if not target:
        return 1
    if not word:
        return 0
    if word[0] == target[0]:
        return count_distinct_subsequences_rec(word[1:], target[1:])+\
            count_distinct_subsequences_rec(word[1:], target)
    else:
        return count_distinct_subsequences_rec(word[1:], target)

print(count_distinct_subsequences_rec("abc", "abc"))

def count_distinct_subsequences(word, target):
    n = len(word)
    m = len(target)
    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(0, n+1):
        dp[0][i] = 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word[j-1] == target[i-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]

print(count_distinct_subsequences("rabbbit", "rabbit"))


