"""
Author: ByronVon
Date: 2023-08-23 18:31:59
FilePath: /leetcode/数组和字符串/删除有序数组种的重复项.py
Description: 
"""


def removeDuplicates(nums):
    # 修改原数组，返回最短的不重复的nums
    # nums按照升序进行排列, 且len(nums)>=1
    # 先记录下第一个点的位置
    l = 0
    for r in range(1, len(nums)):
        # 发生变化
        if nums[r] > nums[r - 1]:
            # if nums[r] != nums[l]:
            l += 1
            nums[l] = nums[r]
    print(nums, l + 1)
    return l + 1


if __name__ == "__main__":
    removeDuplicates([1, 1, 2])
    removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    removeDuplicates([1, 1, 1, 2, 2, 3, 3])
    removeDuplicates([1])
    removeDuplicates([1, 2, 3])
