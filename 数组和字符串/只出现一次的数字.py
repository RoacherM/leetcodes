"""
Author: ByronVon
Date: 2023-08-10 14:44:05
FilePath: /leetcode/其他/只出现一次的数字.py
Description: 
"""


def singleNumber(nums):
    # 寻找一个非空整数数组
    # 你必须设计并实现线性时间复杂度的算法来解决此问题，
    # 且该算法只使用常量额外空间。
    nums = sorted(nums)
    if len(nums) == 1:
        return nums[0]
    # nums不可能等于2
    # 每个元素和左右比较，如果都不一样则pass
    # 先检查左段元素
    if nums[0] != nums[1]:
        return nums[0]
    if nums[-1] != nums[-2]:
        return nums[-1]

    for i in range(1, len(nums) - 1):
        if nums[i - 1] != nums[i] and nums[i] != nums[i + 1]:
            return nums[i]


if __name__ == "__main__":
    print(singleNumber([3, 3, 1, 2, 2]))
