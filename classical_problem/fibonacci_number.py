"""
Given a positive integer A, write a program to find the Ath Fibonacci number.

In a Fibonacci series, each term is the sum of the previous two terms and the first two terms of the 
series are 0 and 1. i.e. f(0) = 0 and f(1) = 1. Hence, f(2) = 1, f(3) = 2, f(4) = 3 and so on.
NOTE: 0th term is 0. 1th term is 1 and so on.
"""
def main():
    n = int(input())
    dp = [0]*n
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        dp[0] = dp[1] = 1
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp[-1])

if __name__ == '__main__':
    main()