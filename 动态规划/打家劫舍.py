"""
Author: ByronVon
Date: 2023-08-15 23:16:56
FilePath: /leetcode/动态规划/打家劫舍.py
Description: 
"""


def rob(nums):
    # 不能偷窃相邻房价的东西
    # 设当前最大的值，即状态为：dp[i]
    # 则状态的转移方程为：dp[i] = max(dp[i-2]+cost[i], dp[i-1])
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    dp = [0] * len(nums)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    # print(dp)
    return dp[-1]


def rob2(nums):
    # 不能偷窃相邻房价的东西
    # 设当前最大的值，即状态为：dp[i]
    # 则状态的转移方程为：dp[i] = max(dp[i-2]+cost[i], dp[i-1])
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    # 优化下内存占用
    dp_2, dp_1 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp = max(dp_2 + nums[i], dp_1)
        dp_2, dp_1 = dp_1, dp
    print(dp_1)
    return dp_1


if __name__ == "__main__":
    rob2([1, 2, 3, 1])
    rob2([2, 7, 9, 3, 1])
