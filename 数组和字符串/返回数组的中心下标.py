"""
Author: ByronVon
Date: 2023-08-08 21:56:25
FilePath: /leetcode/数组和字符串/返回数组的中心下标.py
Description: https://leetcode.cn/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75
"""


from calendar import c


def pivotIndex(nums):
    """
    给你一个整数数组 nums ，请计算数组的 中心下标 。

    数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

    如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
    """
    #     # 记录前缀和与后缀和
    #     L, R = [0] * len(nums), [0] * len(nums)
    #     # 前缀和
    #     L[0] = 0
    #     for i in range(1, len(nums)):
    #         L[i] = L[i - 1] + nums[i - 1]
    #     R[len(nums) - 1] = 0
    #     for i in reversed(range(len(nums) - 1)):
    #         R[i] = R[i + 1] + nums[i + 1]
    #     print(nums)
    #     print(L, R)
    for i in range(len(nums)):
        l = sum(nums[:i])
        r = sum(nums[i + 1 :])
        if l == r:
            return i
    return -1


if __name__ == "__main__":
    print(pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
    print(pivotIndex(nums=[1, 2, 3]))
    print(pivotIndex(nums=[2, 1, -1]))
