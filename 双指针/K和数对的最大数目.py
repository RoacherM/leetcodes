"""
Author: ByronVon
Date: 2023-08-08 20:55:45
FilePath: /leetcode/双指针/K和数对的最大数目.py
Description: https://leetcode.cn/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
"""


def maxOperation(nums, k):
    # 返回数组中选出和为k的两个整数，并将其移出数组，返回最大操作数
    # nums = sorted(nums)
    nums = sorted(nums)

    op = 0
    i, j = 0, len(nums) - 1
    while i < j:
        print(nums[i : j + 1])
        if nums[i] + nums[j] == k:
            op += 1
            i += 1
            j -= 1
        elif nums[i] + nums[j] > k:
            j -= 1
        else:
            i += 1
    return op


if __name__ == "__main__":
    print(maxOperation(nums=[1, 2, 3, 4], k=5))
    print(maxOperation(nums=[3, 1, 3, 4, 3], k=6))
