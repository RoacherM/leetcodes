"""
Author: ByronVon
Date: 2023-08-08 20:10:24
FilePath: /leetcode/双指针/移动零.py
Description: https://leetcode.cn/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-7
"""


def moveZeros(nums):
    # 将所有的零移动到数组的末尾，并保持非零元素的相对顺序
    # 不能复制数组
    ## 类似冒泡的思路，每次移动交换一个0和后续的元素
    if sum(nums) == 0:
        return nums
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == 0:
                # 交换相邻元素
                nums[i], nums[j] = nums[j], nums[i]
        print(nums)


def moveZeros2(nums):
    left = 0
    for right in range(len(nums)):
        print(nums, left, right)
        if nums[right] != 0:
            # 当left和right指向不同的位置时，进行交换
            if left != right:
                nums[left], nums[right] = nums[right], nums[left]
            # left指针移动到下一个位置
            left += 1
    return nums


if __name__ == "__main__":
    print(moveZeros2([0, 1, 0, 3, 12]))
    print(moveZeros2([0, 0, 1]))
    print(moveZeros([0]))
    print(moveZeros2([0, 1, 0, 3, 4, 12, 0]))
