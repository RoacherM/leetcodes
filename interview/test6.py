"""
Author: ByronVon
Date: 2023-08-25 16:29:10
FilePath: /leetcode/interview/test6.py
Description: 
"""
# n个台阶, 每次走一步或者两步，


def func(n):
    # dp[i] = dp[i-1] + dp[i-2]
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    print(func(1))
    print(func(2))
    print(func(3))
