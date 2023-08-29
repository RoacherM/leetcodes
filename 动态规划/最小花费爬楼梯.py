"""
Author: ByronVon
Date: 2023-08-15 22:04:47
FilePath: /leetcode/动态规划/最小花费爬楼梯.py
Description: 
"""


def minCostClimbingStairs(cost):
    # cost表示整数数组，cost[i]为从楼梯第i个台阶向上爬需要支付的费用
    # 可以向上爬1到2个台阶
    # 可以从下标0或者1开始
    # 返回达到楼梯顶部的最低花费
    ## 动态规划问题，核心是定义状态和转移方程
    # 设 状态 dp[i]为到达i台阶时的最小费用，则有
    # 设 方程 dp[i] = cost[i]+min(dp[i-1], dp[i-2])
    # 边界条件为dp[0]=cost[0], dp[1]=cost[1]
    n = len(cost)
    if n == 1:
        return cost[0]
    if n == 2:
        return min(cost[0], cost[1])
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]
    # 计算每个状态
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[n - 1], dp[n - 2])


if __name__ == "__main__":
    print(minCostClimbingStairs([10, 15, 20]))
    print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
