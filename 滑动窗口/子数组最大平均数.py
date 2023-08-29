"""
Author: ByronVon
Date: 2023-08-10 11:45:04
FilePath: /leetcode/数组和字符串/子数组最大平均数.py
Description: https://leetcode.cn/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
"""

# 找出平均数最大的长度为K的连续子数组


def findMaxAverage(nums, k):
    # 直接遍历,注意-10000<=nums[i]<=10000, k<=n
    max_average = -10000
    for i in range(0, len(nums) - k + 1):
        average = sum(nums[i : i + k]) / k
        # print(nums[i : i + k], average)
        if average > max_average:
            max_average = average
    print(max_average)
    return max_average


def findMaxAverage2(nums, k):
    # 每次都sum太慢，可以通过滑窗的方式快速计算每个子数组的和
    ans = [sum(nums[:k])]
    print("initia:", ans)
    for i in range(1, len(nums) - k + 1):
        ans.append(ans[-1] - nums[i - 1] + nums[i + k - 1])

    print(max(ans) / k)
    return max(ans) / k


if __name__ == "__main__":
    findMaxAverage2(range(10), 6)
    findMaxAverage2([1, 12, -5, -6, 50, 3], 4)
    findMaxAverage2([5], 1)
    findMaxAverage2([4, 2], 2)
    findMaxAverage2([0, 1, 1, 3, 3], 4)
    findMaxAverage2([0, 4, 0, 3, 2], 1)
